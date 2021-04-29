from django.urls import path

from . import views

app_name = 'buah'

urlpatterns = [
    path('tambah/', views.TambahBuah.as_view(), name='tambah'),
    path('edit/<pk>/', views.UpdateBuah.as_view(), name='ubah'),
    path('detail/<pk>/', views.DetailBuah.as_view(), name='detail'),
    path('hapus/<pk>/', views.HapusBuah.as_view(), name='hapus'),
    path('', views.IndexBuah.as_view(), name='index'),
]