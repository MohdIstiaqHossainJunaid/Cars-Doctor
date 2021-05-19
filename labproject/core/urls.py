from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/profile/', HomeView.as_view(), name='home'),
    path('findus/', Findus.as_view(), name='findus'),
    path('contact/', Contact.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('profile/', user_profile, name='profile'),
    path('search/', searchposts, name='searchposts'),

    path('payment/cash-on-delivery/', PaymentViewcod.as_view(), name='paymentcod'),
    path('payment/bkash/', PaymentViewbkash.as_view(), name='paymentbkash'),
]
