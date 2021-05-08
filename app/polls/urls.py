from django.urls import path

from polls.views import PollPublicView, PollAdminView


urlpatterns = [
    path('polls/', PollPublicView.as_view()),
    path('polls-admin/', PollAdminView.as_view()),
]
