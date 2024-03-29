from django.urls import path, include
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('about/', views.about, name='about_us'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name ="update_item"),
	path('process_order/', views.processOrder, name ="process_order"),
	path("__reload__/", include("django_browser_reload.urls")),

]