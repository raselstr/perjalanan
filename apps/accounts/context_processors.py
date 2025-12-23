from apps.accounts.models.menu import Menu, SubMenu
from apps.accounts.models.access import RoleMenuAccess


def sidebar_menu(request):
    if not request.user.is_authenticated:
        return {}

    menus = []

    if request.user.is_superuser:
        all_menus = Menu.objects.filter(is_active=True).prefetch_related('submenus')

        for menu in all_menus:
            submenus = menu.submenus.filter(is_active=True)

            is_open = request.path.startswith(menu.url_prefix or '')
            menus.append({
                'menu': menu,
                'submenus': submenus,
                'is_open': is_open,
            })

        return {'sidebar_menus': menus}
