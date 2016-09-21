from datetime import date

from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page


class SupportGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    total_amount = models.IntegerField(_('Total amount'))
    stretch_goals = models.CharField(
        _('Stretch goals'),
        max_length=255,
        validators=[validate_comma_separated_integer_list]
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Support group')
        verbose_name_plural = _('Support groups')


class Supporter(models.Model):
    user = models.OneToOneField('auth.User')
    statement = models.TextField(
        _('Support statement'),
        null=True,
        help_text=_('This statement will appear on the list of supporters together with your name.')
    )
    support_group = models.ForeignKey(SupportGroup, on_delete=models.PROTECT, null=True)
    support_anonymous = models.BooleanField(
        _('Support anonymously'),
        help_text=_('If checked your name will not appear on the list of supporters.'),
        default=False
    )
    additional_information = models.CharField(
        _('Additional information'),
        max_length=50,
        blank=True,
        help_text=_('Here you can specify additional information about your activities, organizations, etc. It appears'
                    ' next to your name in the list of supporters.')
    )
    UNIVERSITIES = (
        ('UHH', 'Universität Hamburg'),
        ('TUHH', 'Technische Universität Hamburg'),
        ('HAW', 'Hochschule für Angewandte Wissenschaften Hamburg'),
        ('HCU', 'HafenCity Universität Hamburg'),
        ('HFBK', 'Hochschule für bildende Künste Hamburg'),
        ('HfMT', 'Hochschule für Musik und Theater Hamburg'),
        ('HSU', 'Helmut-Schmidt-Universität Hamburg'),
        ('Other', 'Andere Universität oder Hochschule')
    )
    university = models.CharField(_('University'), choices=UNIVERSITIES, max_length=30, null=True)
    
    class Meta:
        verbose_name = _('Supporter')
        verbose_name_plural = _('Supporters')


class NotableSupporter(Orderable):
    supporter_page = models.ForeignKey('rpocore.SupporterPage', related_name='notable_supporters', null=True)
    name = models.CharField(max_length=30)
    position = models.CharField(_('Position'), max_length=50)
    FACULTIES = (
        ('MIN', 'MIN'),
        ('WiSo', 'WiSo'),
        ('BWL', 'BWL'),
        ('Recht', 'Recht'),
        ('Medizin', 'Medizin'),
        ('Erzwiss', 'Erzwiss'),
        ('GeiWi', 'GeiWi'),
        ('PB', 'Psychologie und Bewegungswissenschaften')
    )
    faculty = models.CharField(_('Faculty'), choices=FACULTIES, max_length=30)
    image = models.ImageField(_('Image'), upload_to='supporters/', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('First signatory')
        verbose_name_plural = _('First signatories')


class SupporterPage(Page):
    class Meta:
        verbose_name = _('Supporter page')
        verbose_name_plural = _('Supporter pages')


class FormalStatement(models.Model):
    organization = models.CharField(_('Organization'), max_length=255)
    file = models.FileField(_('File'), help_text=_('Only PDF files allowed'), upload_to='statements', blank=True)

    def __str__(self):
        return self.organization
    
    class Meta:
        verbose_name = _('Formal statement')
        verbose_name_plural = _('Formal statements')


class InformalStatement(models.Model):
    organization = models.CharField(_('Organization'), max_length=255)
    file = models.FileField(_('File'), help_text=_('Only PDF files allowed'), upload_to='statements')

    def __str__(self):
        return self.organization
    
    class Meta:
        verbose_name = _('Informal statement')
        verbose_name_plural = _('Informal statements')


class StatementPage(Page):
    formal_statements = models.ManyToManyField(FormalStatement, blank=True)
    informal_statements = models.ManyToManyField(InformalStatement, blank=True)
    
    class Meta:
        verbose_name = _('Statement page')
        verbose_name_plural = _('Statement pages')


class Phase(Orderable):
    name = models.CharField(max_length=255)
    description = models.CharField(_('Description'), max_length=255)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    process = models.ForeignKey('rpocore.Process', on_delete=models.CASCADE)
    active = models.BooleanField(_('Active'), default=False)
    
    class Meta:
        verbose_name = _('Phase')
        verbose_name_plural = _('Phases')

    def __str__(self):
        return self.name

    @property
    def in_past(self):
        if self.start_date < date.today() and self.end_date < date.today():
            return True
        else:
            return False


class Process(models.Model):
    RESULTS = (
        ('inprogress', 'Am Laufen'),
        ('success', 'Erfolg'),
        ('failure', 'Versagen'),
    )
    result = models.CharField(_('Result'), choices=RESULTS, blank=True, max_length=30)
    
    class Meta:
        verbose_name = _('Process')
        verbose_name_plural = _('Processes')


class HomepagePage(Page):
    process = models.ForeignKey(Process, on_delete=models.SET_NULL, null=True)
    campaign_positions = RichTextField(
        _('Campaign positions block'),
        blank=True,
        help_text=_('Please enter the markup for this block.')
    )
    supporter_statistics = RichTextField(
        _('Become supporter block'),
        blank=True,
        help_text=_('Please enter the markup for this block.')
    )
    get_active = RichTextField(
        _('Get active block'),
        blank=True,
        help_text=_('Please enter the markup for this block.')
    )
    
    class Meta:
        verbose_name = _('Homepage page')
        verbose_name_plural = _('Homepage pages')


class CarouselItem(Orderable):
    homepage = models.ForeignKey(HomepagePage, related_name='carousel_items')
    url = models.CharField(_('URL'), max_length=200)
    caption = models.CharField(_('Caption'), max_length=100)
    background_image = models.ImageField(
        _('Background image'),
        help_text=_("If you don't upload an image the background HTML will be used."),
        blank=True
    )
    background_html = RichTextField(
        _('Background HTML'),
        help_text=_("This field will be used if you don't upload an image."),
        blank=True
    )

    def __str__(self):
        return self.caption
    
    class Meta:
        verbose_name = _('Carousel item')
        verbose_name_plural = _('Carousel items')
