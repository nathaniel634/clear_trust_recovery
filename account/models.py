from django.db import models
from django_countries.fields import CountryField


class Complaint(models.Model):
    TRANSFER_METHOD_CHOICES = [
         ("", "Select Transfer Method Used"),
        ('crypto', 'Cryptocurrency'),
        ('bank', 'Bank Transfer'),
        ('card', 'Credit/Debit Card'),
        ('wire', 'Wire Transfer'),
        ('cash', 'Cash'),
        ('other', 'Other'),
    ]

    CURRENCY_CHOICES = [
        ("", "Select Currency"),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        ('USDT', 'USDT'),
        ('OTHER', 'Other'),
    ]

    CASE_TYPE_CHOICES = [
        ("romance_scam", "Romance Scam"),
        ("crypto_scam", "Cryptocurrency Scam"),
        ("investment_scam", "Investment Scam"),
        ("bitcoin_scam", "Bitcoin Scam"),
        ("forex_scam", "Forex Scam"),
        ("online_shopping_scam", "Online Shopping Scam"),
        ("identity_theft", "Identity Theft"),
        ("impersonation_scam", "Impersonation Scam"),
        ("other", "Other"),
    ]

    # Personal Information
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    country = CountryField(blank_label="Select your country")
    phone = models.CharField(max_length=30)

    # Scam Details
    case_type = models.CharField(max_length=50, choices=CASE_TYPE_CHOICES,
        verbose_name="Case Type")
    scam_company_name = models.CharField(max_length=255)
    amount_lost = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    transfer_method = models.CharField(
        max_length=20, choices=TRANSFER_METHOD_CHOICES
    )
    last_transaction_date = models.DateField()

    # Case Description
    story = models.TextField(help_text="Describe how the scam occurred")

    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.scam_company_name}"
