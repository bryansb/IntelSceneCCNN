# existing imports
from django.urls import path
from django.conf.urls import url
from apiCNN import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('image_upload', views.UploadImage.image_view, name = 'image_upload'), 
    path('scene_predict', views.Classification.predictScene, name = 'scene_predict'),
    url(r'^$', views.Autenticacion.singIn),
    url(r'^postsign/', views.Autenticacion.postsign),
    url(r'^scene/$', views.Classification.determineScene),
    url(r'^scene_predict/$', views.Classification.predictScene),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
