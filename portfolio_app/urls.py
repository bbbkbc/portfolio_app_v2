from django.contrib import admin
from django.urls import path, include
from portfolio_app.core import views
from portfolio_app.stockdata import views as views_data

urlpatterns = [
    path('', views.home, name='home'),
    path('secret/', views.secret_page, name='secret'),
    path('secret_2/', views.SecretPage.as_view(), name='secret_2'),
    path('data_download/', views_data.export, name='export'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
