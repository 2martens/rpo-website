from django.db import models
from django.utils.translation import ugettext_lazy as _


class SupportGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    total_amount = models.IntegerField(_('Total amount'))
    stretch_goals = models.CommaSeparatedIntegerField(_('Stretch goals'), max_length=255)

    def __str__(self):
        return self.name


class Supporter(models.Model):
    user = models.OneToOneField('auth.User')
    statement = models.TextField(_('Support statement'), null=True)
    support_group = models.ForeignKey(SupportGroup, on_delete=models.PROTECT, null=True)
    support_anonymous = models.BooleanField(_('Support anonymously'), default=False)
    additional_information = models.CharField(_('Additional information'), max_length=50, blank=True)
    UNIVERSITIES = (
        ('UHH', 'Universität Hamburg'),
        ('TUHH', 'Technische Universität Hamburg'),
        ('HAW', 'Hochschule für Angewandte Wissenschaften Hamburg'),
        ('Other', 'Andere Universität oder Hochschule')
    )
    university = models.CharField(_('University'), choices=UNIVERSITIES, max_length=30, null=True)
