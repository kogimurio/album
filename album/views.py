from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Images, Picha
from .forms import AlbumForm
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404, FileResponse
import os
from django.contrib.messages.views import SuccessMessageMixin



def gallery(request):
    if request.user.is_authenticated:
        if request.user.status == 'author':
            gallery = Album.objects.all()
            return render(request, 'album/gallery.html', {'gallery': gallery})
        else:
            return HttpResponse("You don't have permission to view this page.")
    return redirect('home')

# create main content
class createAlbumView(LoginRequiredMixin, CreateView):
    template_name = 'album/add_images.html'
    form_class = AlbumForm
    success_url = reverse_lazy('gallery')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.status != 'author':
           
            return redirect('login')  
        return super().dispatch(request, *args, **kwargs)


#delete View
class CustomDeleteView(LoginRequiredMixin, DeleteView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.status != 'author':
           
            return redirect('login')  
        return super().dispatch(request, *args, **kwargs)

    model = Album
    template_name = 'album/delete.html'
    success_url = reverse_lazy('message')

#successful delete message
def deletedMessage(request):
    if request.user.is_authenticated:
        if request.user.status == 'author':
            return render(request, 'album/message.html')
        else:
            return HttpResponse("You don't have permission to view this page.")
    return redirect('home')

#ablum detail view
class AlbumDetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'album/gallerydetail.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.status != 'author':
           
            return redirect('login')  
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = Album.objects.get(id=self.kwargs['pk'])
        if album.author != self.request.user:
            raise Http404("You are not authorized to view this album.")
        context['galleryobj'] = album
        return context

#add images view
class GalleryAddView(LoginRequiredMixin, TemplateView):
    template_name = 'album/galleryaddimage.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.status != 'author':
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        try:
            images = self.request.FILES.getlist('images')
            album = Album.objects.get(id=self.kwargs['pk'])

            for image in images:
                product_image = Images.objects.create(
                    album=album,
                    images=image
                )

            messages.success(self.request, 'Images added successfully.')
            return redirect('gallery')
        except Exception as e:
            print(e)
class AlbumEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/albumedit.html'
    success_url = reverse_lazy('gallery')
    success_message = "Album updated successfully"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.status != 'author':
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


def download_image(request, image_id):
    try:
        image = Images.objects.get(id=image_id)
        image_path = image.images.path
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                response = FileResponse(f)
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(image_path))
                return response
        else:
            return HttpResponse("File not found")
    except Images.DoesNotExist:
        return HttpResponse("Image does not exist")
