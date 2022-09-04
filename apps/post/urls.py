from django.urls import path

from . import views

urlpatterns = [
    path('',views.post,name="post"),
    path('admincat/',views.admincategorias,name='admincat'),
    path('detalle/<int:pk>', views.post_detail, name='post_detail'),
    path('edit/<int:pk>', views.post_edit, name='post_edit'),
    path('nuevo', views.post_new, name='post_new'),
    path('delete/<int:pk>', views.post_delete, name='post_delete'),
    path('vistaspost/', views.vistasPost, name='vista_post'),
]

