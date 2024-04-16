from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Images
from .forms import AlbumForm
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from users.decorators import user_not_authenticated



def gallery(request):
    if request.user.is_authenticated:
        gallery = Album.objects.all()
        return render(request, 'album/gallery.html', {'gallery': gallery})
    return redirect('home')

# create main content
class createAlbumView(CreateView):
    template_name = 'album/add_images.html'
    form_class = AlbumForm
    success_url = reverse_lazy('gallery')

class CustomDeleteView(DeleteView):
    model = Album
    template_name = 'album/delete.html'
    success_url = reverse_lazy('message')

#def CustomDeleteView(request, pk):
#    album = get_object_or_404(Album, pk=pk)
#    if request.method == "POST":
#        album.delete()
#        messages.success(request, f"Successfully deleted")
#        return redirect('message')
#    return render(request, 'album/delete.html', {'album': album})
    

def deletedMessage(request):
    return render(request, 'album/message.html')