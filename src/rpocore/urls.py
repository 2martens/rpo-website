from django.conf.urls import url
from mezzanine.accounts.urls import SIGNUP_URL, _slash, SIGNUP_VERIFY_URL, _verify_pattern

from rpocore import views

urlpatterns = []

urlpatterns += [
    url("^%s%s$" % (SIGNUP_URL.strip("/"), _slash),
        views.signup, name="signup"),
    url("^%s%s%s$" % (SIGNUP_VERIFY_URL.strip("/"), _verify_pattern, _slash),
        views.signup_verify, name="signup_verify"),
]
