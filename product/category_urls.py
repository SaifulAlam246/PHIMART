from django.urls import path
from product import views

urlpatterns = [
 path('',views.ViewCategories.as_view(),name='category-list'),
 path('<int:pk>/', views.view_specific_category,name='view-specific-category')
]