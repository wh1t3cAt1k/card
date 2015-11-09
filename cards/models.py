from django.db import models

# Create your models here.

class Card(models.Model):
    STATUS_EXPIRED = "EX"
    STATUS_ACTIVE = "AC"
    STATUS_DEACTIVATED = "DE"
    STATUS_CHOICES = (
            (STATUS_ACTIVE, "Active"),
            (STATUS_EXPIRED, "Expired"),
            (STATUS_DEACTIVATED, "Deactivated")
    )

    id = models.AutoField(primary_key = True)
    series = models.CharField(verbose_name="Series", max_length=8, null=False, blank=False)
    number = models.CharField(verbose_name="Number", max_length=16, null=False, blank=False)
    issue_date = models.DateTimeField(verbose_name="Issue Date", auto_now=False, null=False, blank=False)
    expire_date = models.DateTimeField(verbose_name="Expiry Date", auto_now=False, null=False, blank=False)
    status = models.CharField(
        verbose_name="Status", 
        max_length=2, 
        null=False, 
        blank=False, 
        default=STATUS_ACTIVE,
        choices=STATUS_CHOICES)

class Purchase(models.Model):
    id = models.AutoField(primary_key = True)
    card = models.ForeignKey(Card, verbose_name="Card used to purchase", null=False)
    purchase_date = models.DateTimeField(verbose_name="Purchase Date", null=False, blank=False)
    item = models.CharField(verbose_name="Item name", max_length=255, null=False, blank=False)
    price = models.DecimalField(verbose_name="Item price", max_digits=10, decimal_places=2, null=False, blank=False)


