from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    order_no = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    url_prefix = models.CharField(
        max_length=100,
        blank=True,
        help_text="contoh: /account_settings/"
    )


class SubMenu(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='submenus',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order_no = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
