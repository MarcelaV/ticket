from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ticket.views import TicketListView, TicketCreate, TicketDetail

urlpatterns = [
    url(r'^lista', login_required(TicketListView.as_view()), name='ticket_list'),
    url(r'^crear', login_required(TicketCreate.as_view()), name='ticket_create'),
    url(r'^detail/(?P<pk>[0-9]+)$', TicketDetail.as_view(), name="ticket_detail")
]

