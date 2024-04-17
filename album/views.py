from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Images
from .forms import AlbumForm
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404



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
                    album = album,
                    images = image
                )
            return redirect('gallery')
        except Exception as e:
            print(e)

class AlbumEditView(LoginRequiredMixin, UpdateView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.status != 'author':
           
            return redirect('login')  
        return super().dispatch(request, *args, **kwargs)

    model = Album
    form_class = AlbumForm
    template_name = 'album/albumedit.html'
    success_url = reverse_lazy('gallery')