from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('GUI_test/', views.GUI_test, name='GUI_test'),
    path('GUI_test/GUI_test', views.GUI_test),
    path('login/GUI_test/GUI_test', views.GUI_test),
    path('GUI_test/login/', views.login),

    path('GUI_test/Save_canvas/', views.Save_canvas),
    path('logout/GUI_test/Save_canvas/', views.Save_canvas),

    path('GUI_test/userpage/', views.userpage, name='userpage'),

    path('login/GUI_test/', views.GUI_test),
    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),
    path('logout/GUI_test/', views.GUI_test),
    path('logout/GUI_test/login', views.login),

    path('register/', views.register, name='register'),
    path('register/GUI_test/', views.GUI_test),
    path('register/login/', views.login),

    path('product/', views.product_page, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_product/GUI_test/', views.GUI_test),
    path('login/GUI_test/Save_canvas/', views.Save_canvas),

    path('GUI_test/adv_page/', views.adv_page, name='adv_page'),

    path('product/<slug:url_product_code>', views.product_delta)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)