from django.urls import path
from .import views
from .views import createAlbumView, CustomDeleteView

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('addimages/', createAlbumView.as_view(), name='addimages'),
    path('delete/<int:pk>/delete/', CustomDeleteView.as_view(), name='delete'),
    path('message/', views.deletedMessage, name='message'),
    #path('delete/<int:pk>/', views.CustomDeleteView, name='delete'),
]