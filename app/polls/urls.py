from django.urls import path

from polls.views import PollPublicView, PollAdminView


app_name = 'polls'

urlpatterns = [
    path('polls/', PollPublicView.as_view(), name='submit-poll'),
    path('polls-admin/', PollAdminView.as_view(), name='get-polls'),
    path('polls-admin/<int:id>/', PollAdminView.as_view()),
]
