from django.db import models
from .role import Role
from .menu import Menu, SubMenu

class RoleMenuAccess(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    sub_menu = models.ForeignKey(
        SubMenu,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('role', 'menu', 'sub_menu')

    def __str__(self):
        return f"{self.role} → {self.menu} → {self.sub_menu or 'ALL'}"
