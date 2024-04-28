from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path(r'api/text_to_image',views.GenrateImageAPIView.as_view(),name="generate_image"),
]
