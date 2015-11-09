from django.contrib import admin
from django import forms
from django.utils import timezone
from .models import Card

# Register your models here.

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

    def clean(self):
        issue_date = self.cleaned_data.get("issue_date")
        expire_date = self.cleaned_data.get("expire_date")
        if expire_date < issue_date:
            raise forms.ValidationError("Expiry date should not be earlier than issue date!")
        
        status = self.cleaned_data.get("status")
        if timezone.now() > expire_date and status == Card.STATUS_ACTIVE:
            raise forms.ValidationError("The card has expired, cannot set status to active.")
        
        return self.cleaned_data

class CardAdmin(admin.ModelAdmin):
    form = CardForm

admin.site.register(Card, CardAdmin)
