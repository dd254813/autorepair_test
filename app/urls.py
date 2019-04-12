from django.conf.urls import url
from django.urls import path
from app.views import BaseView, sing_up_for_diagnostic, get_holded_time

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('sing_up_for_diagnostic/', sing_up_for_diagnostic, name='sing_up_for_diagnostic'),
    path('get_holded_time/', get_holded_time, name='get_holded_time'),
]
