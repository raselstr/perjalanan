from apps.accounts.models.menu import Menu
from apps.accounts.models.access import RoleMenuAccess

def sidebar_menu(request):
    if not request.user.is_authenticated or not request.user.role:
        return {}

    menus = (
        Menu.objects
        .filter(
            rolemenuaccess__role=request.user.role,
            is_active=True
        )
        .distinct()
        .prefetch_related('submenus')
    )

    return {'menus': menus}
