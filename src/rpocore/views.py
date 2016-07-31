from django.contrib.auth import (login as auth_login)
from django.contrib.messages import *
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from mezzanine.accounts import get_profile_form
from mezzanine.conf import settings
from mezzanine.utils.email import send_approve_mail, send_verification_mail
from mezzanine.utils.urls import next_url, login_redirect


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
