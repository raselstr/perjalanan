from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=150, blank=True)
    order_no = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order_no']

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='submenus'
    )
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    order_no = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order_no']

    def __str__(self):
        return f"{self.menu.name} → {self.name}"
