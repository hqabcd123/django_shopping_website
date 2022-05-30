from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('GUI_test/', views.GUI_test, name='GUI_test'),
    path('GUI_test/Save_canvas/', views.Save_canvas),
    path('login/GUI_test/', views.GUI_test),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logout/GUI_test/', views.GUI_test),
    path('register/', views.register, name='register'),
    path('register/GUI_test/', views.GUI_test),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)