from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='us'),
    path('contacto/', views.contact, name='contact'),
    path('<int:publicacion_id>/', views.detail, name='detail'),
    path('crear/',views.createPost, name='create'),
    path('<int:publicacion_id>/editar/', views.editPost, name='edit'),
    path('<int:publicacion_id>/borrar/', views.deletePost, name='delete'),

    path('login/', auth_views.LoginView.as_view(template_name='src/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='src/logout.html'), name='logout'),


    path('publicaciones/', views.posts, name='publicaciones')

    # url(r'^publicaciones/(?P<pk>[0-9]+)/$', views.publicacionesDetail, name='publicacionesDetail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)