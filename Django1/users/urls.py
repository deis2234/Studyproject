from django.urls import path, include

from Django1 import settings
from users.views import SignUpView, LoginUser
from django.contrib.auth.views import LogoutView
from Djangoapp import views

urlpatterns = [
    path('registration/', SignUpView.as_view(), name='registrations'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('nachal', views.nachal, name='nachal')
]
