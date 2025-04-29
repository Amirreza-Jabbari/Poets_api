from django.urls import path
from .views import GolestanHikayatView, HafezView, KhayyamView, MoulaviView

urlpatterns = [
    # Golestan
    path('saadi/golestan/', GolestanHikayatView.as_view()),
    path('saadi/golestan/<int:bab>/', GolestanHikayatView.as_view()),
    path('saadi/golestan/<int:bab>/<int:hekayat>/',
         GolestanHikayatView.as_view()),

    # Hafez
    path('hafez/', HafezView.as_view()),
    path('hafez/<str:cat>/', HafezView.as_view()),
    path('hafez/<str:cat>/<int:num>/', HafezView.as_view()),

    # Khayyam
    path('khayyam/', KhayyamView.as_view()),
    path('khayyam/<str:cat>/', KhayyamView.as_view()),
    path('khayyam/<str:cat>/<int:num>/', KhayyamView.as_view()),

    # Moulavi
    path('moulavi/', MoulaviView.as_view()),
    path('moulavi/<str:cat>/', MoulaviView.as_view()),
    path('moulavi/<str:cat>/<int:num>/', MoulaviView.as_view()),

]
