from django.urls import path
from . import views
from users import views as usersview

urlpatterns = [
    path('', views.products, name="products"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('update_item', views.updateItem, name="update_item"),
    path('product_details', views.productDetails, name="product_details"),
    path('process_order',views.processOrder, name="process_order"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('category',views.products, name="category"),

    path('addProductView', views.addProductView, name="addProductView"),
    path('editProductView', views.editProductview, name="editProductView"),

    path('addProduct',views.addProduct, name="addProduct"),

    path('profile',views.profile, name="profile"),
    path('faqs',views.faqs, name="faqs"),

    path('updateProfile',views.updateProfile, name="updateProfile"),

    path('update_wishlist', views.UpdateWishList, name="update_wishlist"),
    path('wishlist', views.ViewWishList, name="wishlist"),

    path('add_review/<int:id>', views.add_review, name='add_review'),
]