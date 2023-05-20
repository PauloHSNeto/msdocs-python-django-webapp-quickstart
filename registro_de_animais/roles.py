from rolepermissions.roles import AbstractUserRole


class Sindico(AbstractUserRole):
    available_permissions = {
        'can_add_animal': True,
        'can_update_animal': True,
        'can_delete_animal': True,
        'can_see_animal': True,
        'can_see_all_animals': True
    }

class Morador(AbstractUserRole):
    available_permissions = {
        'can_add_animal': True,
        'can_update_animal': True,
        'can_delete_animal': True,
        'can_see_animal': True,
        'can_see_all_animals': False
    }