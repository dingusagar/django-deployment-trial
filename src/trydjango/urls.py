"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from pages.views import home_view, contact_view, about_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('products/', include('products.urls')),
    path('', home_view, name='home'),
    path('about/<int:id>/', about_view, name='product-detail'),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
