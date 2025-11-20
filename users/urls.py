from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import add_alumni, approve_alumni_request,claim_alumni_id
from .views import transac_search
urlpatterns = [
    path('',views.home, name="home"),
    path('id_request/',views.idRequest, name="idRequest"),

    path('graduatetracer/',views.graduateTracer, name="graduateTracer"),
    path('reunionandevents/',views.alumni_events, name="alumni_events"),
    path('jobfairs/',views.jobfairs, name="jobfairs"),
    path('yearbook/',views.yearbook, name="yearbook"),
    path('transaction_alumni.html/',views.transaction_alumni, name="transaction_alumni"),

    path('graduateTracer_submit', views.graduateTracer_submit,name='graduateTracer_submit'),

    path('search_id/', views.search_id, name='search_id'),
    
    path('search_id2/', views.search_id2, name='search_id2'),
    
    path('search_yearbook/', views.search_yearbook, name='search_yearbook'),

    path('add_alumni/', views.add_alumni, name="add_alumni"),

    # admin side
    path('admin_id_request/', views.admin_id_request, name='admin_idRequest'),
    path('admin_grad_tracer/', views.admin_gradTracer, name='admin_gradTracer'),
    path('admin_events/', views.admin_events, name='admin_events'),
    path('admin_jobfairs',views.admin_jobfairs, name="admin_jobfairs"),
    path('admin_yearbook',views.admin_yearbook, name="admin_yearbook"),


    path('approve_alumni_request/<int:alumni_id>/', approve_alumni_request, name='approve_alumni_request'),
    path('claim_alumni_id/<int:alumni_id>/', claim_alumni_id, name='claim_alumni_id'),
    path('transac_search', transac_search, name='transac_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)