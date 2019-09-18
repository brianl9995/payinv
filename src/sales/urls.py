from django.conf.urls import url
from . import views

urlpatterns = [
    # sale
    url(r'^add/$', views.SaleEditView.as_view(),
        name='sale_add'),
    url(r'^$', views.SaleListView.as_view(), name='sale_list'),
    url(r'^pending/invoice/$', views.SaleListPendingInvoice.as_view(),
        name='sale_list_pending_invoice'),
    url(r'^pending/payment/$', views.SaleListPendingPayment.as_view(),
        name='sale_list_pending_payment'),
    url(r'^$', views.SaleListView.as_view(), name='index'),  # homeme
    url(r'^(?P<pk>[\w-]+)/$', views.sale, name='sale'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.SaleEditView.as_view(),
        name='sale_edit'),


]
