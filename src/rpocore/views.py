from django.contrib.auth import (login as auth_login, authenticate)
from django.contrib.messages import *
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from mezzanine.accounts import get_profile_form
from mezzanine.conf import settings
from mezzanine.utils.email import send_approve_mail, send_verification_mail
from mezzanine.utils.urls import next_url, login_redirect

from rpocore.util import update_supporter_svg


def signup(request, template="accounts/account_signup.html",
           extra_context=None):
    """
    Signup form.
    """
    profile_form = get_profile_form()
    form = profile_form(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        new_user = form.save()
        if not new_user.is_active:
            if settings.ACCOUNTS_APPROVAL_REQUIRED:
                send_approve_mail(request, new_user)
                info(request, _("Thanks for supporting this campaign! You'll receive "
                                "an email when your support is counted."))
            else:
                send_verification_mail(request, new_user, "signup_verify")
                info(request, _("A verification email has been sent with "
                                "a link to verify your support."))
            return redirect(next_url(request) or "/")
        else:
            success(request, _("Successfully supported the campaign"))
            auth_login(request, new_user)
            return login_redirect(request)
    context = {"form": form, "title": _("Support RPO 2016")}
    context.update(extra_context or {})
    return TemplateResponse(request, template, context)


def signup_verify(request, uidb36=None, token=None):
    """
    View for the link in the verification email sent to a new user
    when they create an account and ``ACCOUNTS_VERIFICATION_REQUIRED``
    is set to ``True``. Activates the user, logs them in and redirects
    them to the get into action page.
    """
    user = authenticate(uidb36=uidb36, token=token, is_active=False)
    if user is not None:
        become_active_url = getattr(
            settings, "BECOME_ACTIVE_URL", "/become-active/"
        )
        user.is_active = True
        user.save()
        auth_login(request, user)
        success(request, _("Successfully supported the campaign"))
        return redirect(become_active_url)
    else:
        error(request, _("The link you clicked is no longer valid."))
        return redirect("/")
