from django.conf.urls import url
from mezzanine.accounts.urls import SIGNUP_URL, _slash

from rpocore import views

urlpatterns = []

urlpatterns += [
    url("^%s%s$" % (SIGNUP_URL.strip("/"), _slash),
        views.signup, name="signup"),
]
