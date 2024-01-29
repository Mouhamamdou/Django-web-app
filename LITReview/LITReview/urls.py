"""
URL configuration for LITReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import authentication.views
import ticket.views
import review.views
import userfollows.views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', ticket.views.Home.as_view(), name='home'),
    path('signup/', authentication.views.SignupPageView.as_view(), name='signup'),

    path('tickets/create/', ticket.views.TicketCreateView.as_view(), name='ticket-create'),
    path('tickets/<int:pk>/', ticket.views.TicketDetailView.as_view(), name='ticket-detail'),
    path('tickets/', ticket.views.TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/update/', ticket.views.TicketUpdateView.as_view(), name='ticket-update'),
    path('tickets/<int:pk>/delete/', ticket.views.TicketDeleteView.as_view(), name='ticket-delete'),
    path('create-ticket-review/', ticket.views.TicketAndReviewCreateView.as_view(), name='create-ticket-review'),

    path('reviews/create/', review.views.ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', review.views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/', review.views.ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/update/', review.views.ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', review.views.ReviewDeleteView.as_view(), name='review-delete'),
    path('reviews/create/<int:ticket_id>/', review.views.ReviewCreateView.as_view(), name='review-create-specific'),

    path('follow-users/', userfollows.views.UserFollowCreateView.as_view(), name='follow-users'),
    path('follow-users/list/', userfollows.views.UserFollowListView.as_view(), name='user-follows-list'),
    path('follow-users/<int:pk>/delete/', userfollows.views.UserFollowDeleteView.as_view(), name='user-follows-delete'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
