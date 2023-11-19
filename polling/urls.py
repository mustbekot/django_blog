from django.urls import path
from polling.views import last_view, detail_view

urlpatterns = [
    path('', last_view, name="poll_index"),
    path("<int:poll_id>", detail_view, name='poll_detail')
]
