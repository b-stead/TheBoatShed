"""TheBoatShed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from django.contrib.auth import views as auth_views
from django.views.static import serve
from coach.pages import athletes, coaches, squads

urlpatterns = [
    path('home/', include('home.urls')), #home page
    path('blog/', include('blog.urls')),
    path('coach/', include('coach.urls')),
    path('vbox/', include('vbox.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    path('accounts/signup/', squads.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', athletes.AthleteSignUpView.as_view(), name='athlete_signup'),
    path('accounts/signup/coach/', coaches.CoachSignUpView.as_view(), name='coach_signup'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #line used to link up document upload urls

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]


# Switch to social login if it is configured - Keep for later

"""
try:
    from . import github_settings
    social_login = 'registration/login.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
"""

