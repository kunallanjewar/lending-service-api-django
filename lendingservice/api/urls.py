from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from .views import( ProfileView, AccountView,
                    ProfileView, AccountView,
                    RegisterUserView, TransactionView
                )

urlpatterns = {
    url(r'^register/$',
                    RegisterUserView.as_view(),
                    name="createuser"
    ),

    url(r'^account/$',
                    AccountView.as_view(),
                    name="account"
    ),

    url(r'^profile/$',
                    ProfileView.as_view(),
                    name="profile"
    ),

    url(r'^transaction/$',
                    TransactionView.as_view(),
                    name="transaction"
    ),

    url(r'^account/$',
                    AccountView.as_view(),
                    name="account"
    ),

    url(r'^auth/', include('rest_framework.urls',
                    namespace='rest_framework')
    ),

    url(r'^get-token/', views.obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
