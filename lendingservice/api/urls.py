from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from .views import (CreateUserView, OpenAccountView,
                    UserDetailView, AccountDetailView)

urlpatterns = {
    url(r'^register/$', CreateUserView.as_view(), name="create-user"),
    url(r'^api/openaccount/$', OpenAccountView.as_view(), name="open-account"),

    url(r'^api/profile/(?P<pk>[0-9]+)/$',
                    UserDetailView.as_view(),
                    name="profile"
    ),

    url(r'^api/account/(?P<pk>[0-9]+)/$',
                    AccountDetailView.as_view(),
                    name="account"
    ),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-token/', views.obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
