# forms.py
from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    last_transaction_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
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
                "placeholder": "Scam Company / Platform Name",
                "class": "form-control"
            }),
            "amount_lost": forms.NumberInput(attrs={
                "placeholder": "Amount Lost",
                "class": "form-control"
            }),
            "currency": forms.Select(attrs={
                "class": "form-control"
            }),
            "transfer_method": forms.Select(attrs={
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
        if amount <= 0:
            raise forms.ValidationError("Amount lost must be greater than zero.")
        return amount
