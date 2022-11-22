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
from profiles.views import AthleteSignUpView, CoachSignUpView, SignUpView
from django.conf.urls import handler404, handler500
from home import views as error_views

urlpatterns = [
    path('', include('home.urls')), #home page
    path('blog/', include('blog.urls')),
    path('athletes/', include('athletes.urls')),
    path('profiles/', include('profiles.urls')),
    #path('uploader', include('uploader.urls')),
    path('demo/', include('demo.urls')),
    #path('vbox/', include('vbox.urls')),
    path('forum/', include('forum.urls')),

    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='profiles/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="profiles/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='profiles/password/password_reset_complete.html'), name='password_reset_complete'),

    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/athlete/', AthleteSignUpView.as_view(), name='athlete_signup'),
    path('accounts/signup/coach/', CoachSignUpView.as_view(), name='coach_signup'),

    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),

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
handler404 = error_views.error_404
handler500 = error_views.error_500

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

