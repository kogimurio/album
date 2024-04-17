from django.urls import path
from .import views
from .views import createAlbumView, CustomDeleteView, AlbumDetailsView, GalleryAddView, AlbumEditView

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('addimages/', createAlbumView.as_view(), name='addimages'),
    path('delete/<int:pk>/delete/', CustomDeleteView.as_view(), name='delete'),
    path('message/', views.deletedMessage, name='message'),
    path('gallerydetail/<int:pk>/', AlbumDetailsView.as_view(), name='gallerydetail'),
    path('galleryadd/<int:pk>/', GalleryAddView.as_view(), name='galleryadd'), 
    path('albumedit/<int:pk>/', AlbumEditView.as_view(), name='albumedit'), 

]