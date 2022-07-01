from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms import widgets

from .models import Bezoekreden, WinkelBezoek


theWidget = forms.TextInput(attrs={'size': '10'})
wdgSmall = forms.TextInput(attrs={'size': '6'})
wdgTextA = forms.Textarea(attrs={'rows': 2, 'cols': 60})

class ContactForm(forms.ModelForm):
    cnt_TussenVgsl = forms.CharField(widget=theWidget, label='Tussenvoegsels', required=False)
    cnt_VoorLtrs = forms.CharField(widget=theWidget, label='Voorletters', required=False)
    cnt_Notities = forms.CharField(widget=wdgTextA, label='Notities', required=False)


class AdresForm(forms.ModelForm):
    adr_HuisNr = forms.CharField(widget=wdgSmall, label='Huisnummer', required=False)
    adr_HuisNrToev = forms.CharField(widget=theWidget, label='Toevoeging', required=False)
    #adr_Land = CountryField(multiple=False)
    adr_PostCd = forms.CharField(widget=theWidget, label='Postcode', required=False)
    adr_Notities = forms.CharField(widget=wdgTextA, label='Notities', required=False)


class AdresGrForm(forms.ModelForm):
    adg_HuisNr = forms.CharField(widget=wdgSmall, label='Huisnummer', required=False)
    adg_HuisNrToev = forms.CharField(widget=theWidget, label='Toevoeging', required=False)
    #adr_Land = CountryField(multiple=False)
    adg_PostCd = forms.CharField(widget=theWidget, label='Postcode', required=False)
    adg_Notities = forms.CharField(widget=wdgTextA, label='Notities', required=False)


class NummerForm(forms.ModelForm):
    nmb_Notities = forms.CharField(widget=wdgTextA, label='Notities', required=False, help_text='Kanttekening bij dit nummer (bijv: meest recent)')


class NummerGrForm(forms.ModelForm):
    nmg_Notities = forms.CharField(widget=wdgTextA, label='Notities', required=False, help_text='Kanttekening bij dit nummer (bijv: meest recent)')


class WinkelBezoekForm(forms.ModelForm):
    wbz_TijdStip = forms.SplitDateTimeField(widget=AdminSplitDateTime, label='Tijdstip van bezoek')
    wbz_Bezoeken = forms.ModelMultipleChoiceField(
        queryset=Bezoekreden.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'style': 'list-style-type:none;'}),
        label='Bezoekreden(en)'
    )
    wbz_Notities = forms.CharField(widget=wdgTextA, label='Notities')

    class Meta:
        model = WinkelBezoek
        fields = ('wbz_TijdStip', 'wbz_Bezoeken', 'wbz_Notities')


