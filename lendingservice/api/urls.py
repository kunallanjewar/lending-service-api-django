from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^api/create_user/$', CreateUserView.as_view(), name="create"),
    url(r'^api/open_account/$', OpenAccountView.as_view(), name="openaccount"),
    url(r'^api-auth/', include('rest_framework.urls',
                    namespace='rest_framework')
        ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
