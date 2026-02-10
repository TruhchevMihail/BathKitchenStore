from django.urls import path
from . import views

urlpatterns = [
    path("bath/", views.bath_home, name="bath_home"),
    path("bath/<slug:category_slug>/", views.category_products, {"section": "bath"}, name="bath_category"),

    path("kitchen/", views.kitchen_home, name="kitchen_home"),
    path("kitchen/<slug:category_slug>/", views.category_products, {"section": "kitchen"}, name="kitchen_category"),

    path("brands/", views.brand_list, name="brand_list"),
    path("brands/<slug:brand_slug>/", views.brand_detail, name="brand_detail"),
]
