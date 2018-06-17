from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (CreateUserView, OpenAccountView,
                    UserDetailView, AccountDetailView)

urlpatterns = {
    url(r'^api/create/$', CreateUserView.as_view(), name="createuser"),
    url(r'^api/openaccount/$', OpenAccountView.as_view(), name="openaccount"),

    url(r'^api/profile/(?P<pk>[0-9]+)/$',
                    UserDetailView.as_view(),
                    name="profile"
    ),

    url(r'^api/account/(?P<pk>[0-9]+)/$',
                    AccountDetailView.as_view(),
                    name="account"
    ),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
