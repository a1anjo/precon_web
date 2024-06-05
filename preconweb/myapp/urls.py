from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('warema',views.warema, name='warema'),
    path('overlap',views.overlap, name='overlap'),
    path('serge',views.serge, name='serge'),
    path('origin',views.origin, name='origin'),
    path('thankyou',views.thankyou, name='thankyou'),
    path('contact',views.contact, name='contact'),
    path('brouchere',views.brouchere, name='brouchere'),
    path('other_products',views.other_products, name='other_products'),
    path('send-message/', views.send_message, name='send_message'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)