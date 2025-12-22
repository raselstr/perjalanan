from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models.role import Role
from .models.menu import Menu, SubMenu
from .models.access import RoleMenuAccess
from .models.profile import UserProfile

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_no', 'is_active')
    ordering = ('order_no',)


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'order_no', 'is_active')
    ordering = ('menu', 'order_no')


@admin.register(RoleMenuAccess)
class RoleMenuAccessAdmin(admin.ModelAdmin):
    list_display = ('role', 'menu', 'sub_menu')
    list_filter = ('role', 'menu')

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Role User'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)