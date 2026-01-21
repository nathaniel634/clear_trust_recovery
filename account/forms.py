from django import forms
from django.core.exceptions import ValidationError
from datetime import date

from .models import Complaint


class ComplaintForm(forms.ModelForm):

    # ✅ Override select fields to add placeholder option
    currency = forms.ChoiceField(
        choices=[("", "Select Currency Used")] + list(Complaint.CURRENCY_CHOICES),
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

    transfer_method = forms.ChoiceField(
        choices=[("", "Select Transfer Method Used")] + list(Complaint.TRANSFER_METHOD_CHOICES),
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

    case_type = forms.ChoiceField(
        choices=[("", "Select Case Type")] + list(Complaint.CASE_TYPE_CHOICES),
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

    # ✅ Date field (already correct)
    last_transaction_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Last Transaction Date",
                "onfocus": "this.type='date'",
                "onblur": "this.type='text'"
            }
        )
    )

    class Meta:
        model = Complaint
        fields = [
            "full_name",
            "email",
            "country",
            "phone",
            "case_type",
            "scam_company_name",
            "amount_lost",
            "currency",
            "transfer_method",
            "last_transaction_date",
            "story",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Your Full Name",
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email Address",
                "class": "form-control"
            }),
            "country": forms.Select(attrs={
                "class": "form-control"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Phone Number",
                "class": "form-control"
            }),
            "scam_company_name": forms.TextInput(attrs={
                "placeholder": "Scam Company / Person Name",
                "class": "form-control"
            }),
            "amount_lost": forms.NumberInput(attrs={
                "placeholder": "Amount Lost",
                "class": "form-control"
            }),
            "story": forms.Textarea(attrs={
                "placeholder": "Tell us exactly what happened...",
                "rows": 5,
                "class": "form-control"
            }),
        }

    def clean_amount_lost(self):
        amount = self.cleaned_data.get("amount_lost")
        if amount is not None and amount <= 0:
            raise forms.ValidationError("Amount lost must be greater than zero.")
        return amount
    
    def clean_last_transaction_date(self):
        tx_date = self.cleaned_data.get("last_transaction_date")
        if tx_date and tx_date > date.today():
            raise ValidationError("Transaction date cannot be in the future.")
        return tx_date
