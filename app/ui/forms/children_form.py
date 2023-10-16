import tkinter as tk
from typing import Any, Dict, List, Optional, Tuple, Union

import ttkbootstrap as ttk

from app import constants
from app.database.entities import ChildEntity
from app.ui.components import AddressField, DropdownField, ListField, TextField
from app.ui.forms import BaseForm
from app.utils.images import image_tk


class ChildrenForm(BaseForm):
    """
    A form for managing children's information.

    This form is used to create, edit, or view information about children in the application.
    """

    child_entity: Optional[ChildEntity] = None

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the ChildrenForm widget.

        :param master: The parent widget.
        """
        super().__init__(master)
        self.save_img = image_tk(constants.ICONS_DIR / 'save.png', (32, 32))
        self.children_img = image_tk(constants.ICONS_DIR / 'children.png', (52, 52))

        self.title('Formulário')
        self.header_title.config(text='Formulário para Crianças')
        self.header_title.config(image=self.children_img, compound=tk.TOP)

        # child details.
        child_container = ttk.Labelframe(self.container)
        child_container.config(text='Detalhes da Criança')
        child_container.config(padding=10)
        child_container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        ttk.Frame(self.container).pack(side=tk.TOP, fill=tk.X, pady=50)

        self.child_name_field = TextField(child_container)
        self.child_name_field.label.config(text='Nome')
        self.child_name_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(child_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.child_gender_field = DropdownField(child_container)
        self.child_gender_field.label.config(text='Gênero')
        self.child_gender_field.set_options(('Masculino', 'Feminino'))
        self.child_gender_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(child_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.child_birthdate_field = TextField(child_container)
        self.child_birthdate_field.label.config(text='Data de nascimento')
        self.child_birthdate_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(child_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.child_cpf_field = TextField(child_container)
        self.child_cpf_field.label.config(text='CPF')
        self.child_cpf_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(child_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.child_rg_field = TextField(child_container)
        self.child_rg_field.label.config(text='RG')
        self.child_rg_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(child_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.child_activities_field = ListField(child_container)
        self.child_activities_field.config(text='Atividades pretendidas no Prossan')
        self.child_activities_field.pack(side=tk.TOP, fill=tk.X)

        # parent details.
        parent_container = ttk.Labelframe(self.container)
        parent_container.config(text='Detalhes do Responsável')
        parent_container.config(padding=10)
        parent_container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        ttk.Frame(self.container).pack(side=tk.TOP, fill=tk.X, pady=50)

        self.parent_name_field = TextField(parent_container)
        self.parent_name_field.label.config(text='Nome')
        self.parent_name_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(parent_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.parent_gender_field = DropdownField(parent_container)
        self.parent_gender_field.label.config(text='Gênero')
        self.parent_gender_field.set_options(('Masculino', 'Feminino'))
        self.parent_gender_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(parent_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.parent_birthdate_field = TextField(parent_container)
        self.parent_birthdate_field.label.config(text='Data de nascimento')
        self.parent_birthdate_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(parent_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.parent_cpf_field = TextField(parent_container)
        self.parent_cpf_field.label.config(text='CPF')
        self.parent_cpf_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(parent_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.parent_rg_field = TextField(parent_container)
        self.parent_rg_field.label.config(text='RG')
        self.parent_rg_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(parent_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.parent_address_field = AddressField(parent_container)
        self.parent_address_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(parent_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.parent_contacts_field = ListField(parent_container)
        self.parent_contacts_field.config(text='Lista de contatos')
        self.parent_contacts_field.pack(side=tk.TOP, fill=tk.X)

        # actions.
        actions_container = ttk.Frame(self.container)
        actions_container.pack(side=tk.TOP, fill=tk.X)

        self.confirm_button = ttk.Button(actions_container)
        self.confirm_button.config(image=self.save_img, compound=tk.RIGHT)
        self.confirm_button.config(cursor='hand2')
        self.confirm_button.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)

        # noinspection PyArgumentList
        child_container.config(bootstyle='info')

        # noinspection PyArgumentList
        parent_container.config(bootstyle='info')

        # noinspection PyArgumentList
        self.confirm_button.config(bootstyle='default-link')

    def get_child_name(self) -> str:
        """
        Retrieve the current value in the child name field.

        :return: A string representing the current value in the child name field.
        """
        return self.child_name_field.get_value()

    def get_child_gender(self) -> str:
        """
        Retrieve the current in value the child gender field.

        :return: A string representing the current value in the child gender field.
        """
        return self.child_gender_field.get_value()

    def get_child_birthdate(self) -> str:
        """
        Retrieve the current in value the child birthdate field.

        :return: A string representing the current value in the child birthdate field.
        """
        return self.child_birthdate_field.get_value()

    def get_child_cpf(self) -> str:
        """
        Retrieve the current value in the child cpf field.

        :return: A string representing the current value in the child cpf field.
        """
        return self.child_cpf_field.get_value()

    def get_child_rg(self) -> str:
        """
        Retrieve the current value in the child rg field.

        :return: A string representing the current value in the child rg field.
        """
        return self.child_rg_field.get_value()

    def get_child_activities(self) -> List[str]:
        """
        Retrieve the current value in the child activities field.

        :return: A list containing strings representing the current values in the child activities field.
        """
        return self.child_activities_field.get_value()

    def get_parent_name(self) -> str:
        """
        Retrieve the current value in the parent name field.

        :return: A string representing the current value in the parent name field.
        """
        return self.parent_name_field.get_value()

    def get_parent_gender(self) -> str:
        """
        Retrieve the current value in the parent gender field.

        :return: A string representing the current value in the parent gender field.
        """
        return self.parent_gender_field.get_value()

    def get_parent_birthdate(self) -> str:
        """
        Retrieve the current value in the parent birthdate field.

        :return: A string representing the current value in the parent birthdate field.
        """
        return self.parent_birthdate_field.get_value()

    def get_parent_cpf(self) -> str:
        """
        Retrieve the current value in the parent cpf field.

        :return: A string representing the current value in the parent cpf field.
        """
        return self.parent_cpf_field.get_value()

    def get_parent_rg(self) -> str:
        """
        Retrieve the current value in the parent rg field.

        :return: A string representing the current value in the parent rg field.
        """
        return self.parent_rg_field.get_value()

    def get_parent_address(self) -> Tuple[str, str, str, str]:
        """
        Retrieve the current value in the parent address field.

        :return: A tuple representing the current value in the parent address field.
        """
        return self.parent_address_field.get_value()

    def get_parent_contacts(self) -> List[str]:
        """
        Retrieve the current value in the parent contacts field.

        :return: A list containing strings representing the current values in the parent contacts field.
        """
        return self.parent_contacts_field.get_value()

    def set_child_name(self, child_name: str) -> None:
        """
        Define the value of the child name field.

        :param child_name: A string representing the new value for the child name.

        :return: None
        """
        self.child_name_field.set_value(child_name)

    def set_child_gender(self, child_gender: str) -> None:
        """
        Define the value of the child gender field.

        :param child_gender: A string representing the new value for the child gender.

        :return: None
        """
        self.child_gender_field.set_value(child_gender)

    def set_child_birthdate(self, child_birthdate: str) -> None:
        """
        Define the value of the child birthdate field.

        :param child_birthdate: A string representing the new value for the child birthdate.

        :return: None
        """
        self.child_birthdate_field.set_value(child_birthdate)

    def set_child_cpf(self, child_cpf: str) -> None:
        """
        Define the value of the child cpf field.

        :param child_cpf: A string representing the new value for the child cpf.

        :return: None
        """
        self.child_cpf_field.set_value(child_cpf)

    def set_child_rg(self, child_rg: str) -> None:
        """
        Define the value of the child rg field.

        :param child_rg: A string representing the new value for the child rg.

        :return: None
        """
        self.child_rg_field.set_value(child_rg)

    def set_child_activities(self, child_activities: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Define the value of the child activities field.

        :param child_activities: A list or tuple containing strings representing the new values for the child
        activities.

        :return: None
        """
        self.child_activities_field.set_value(child_activities)

    def set_parent_name(self, parent_name: str) -> None:
        """
        Define the value of the parent name field.

        :param parent_name: A string representing the new value for the parent name.

        :return: None
        """
        self.parent_name_field.set_value(parent_name)

    def set_parent_gender(self, parent_gender: str) -> None:
        """
        Define the value of the parent gender field.

        :param parent_gender: A string representing the new value for the parent gender.

        :return: None
        """
        self.parent_gender_field.set_value(parent_gender)

    def set_parent_birthdate(self, parent_birthdate: str) -> None:
        """
        Define the value of the parent birthdate field.

        :param parent_birthdate: A string representing the new value for the parent birthdate.

        :return: None
        """
        self.parent_birthdate_field.set_value(parent_birthdate)

    def set_parent_cpf(self, parent_cpf: str) -> None:
        """
        Define the value of the parent cpf field.

        :param parent_cpf: A string representing the new value for the parent cpf.

        :return: None
        """
        self.parent_cpf_field.set_value(parent_cpf)

    def set_parent_rg(self, parent_rg: str) -> None:
        """
        Define the value of the parent rg field.

        :param parent_rg: A string representing the new value for the parent rg.

        :return: None
        """
        self.parent_rg_field.set_value(parent_rg)

    def set_parent_address(self, parent_address: Tuple[str, str, str, str]) -> None:
        """
        Define the value of the parent address field.

        :param parent_address: A tuple containing four strings representing the new address value in the order: (
        Street, District, City, State).

        :return: None
        """
        self.parent_address_field.set_value(parent_address)

    def set_parent_contacts(self, parent_contacts: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Define the value of the parent contacts field.

        :param parent_contacts: A list or tuple containing strings representing the new values for the parent contacts.

        :return: None
        """
        self.parent_contacts_field.set_value(parent_contacts)

    def get_values(self) -> Dict[str, Any]:
        """
        Retrieve the current values in the entire form.

        :return: A dict representing the current values in the entire form.
        """
        return {
            'child_name': self.get_child_name(),
            'child_gender': self.get_child_gender(),
            'child_birthdate': self.get_child_birthdate(),
            'child_cpf': self.get_child_cpf(),
            'child_rg': self.get_child_rg(),
            'child_activities': self.get_child_activities(),
            'parent_name': self.get_parent_name(),
            'parent_gender': self.get_parent_gender(),
            'parent_birthdate': self.get_parent_birthdate(),
            'parent_cpf': self.get_parent_cpf(),
            'parent_rg': self.get_parent_rg(),
            'parent_address': self.get_parent_address(),
            'parent_contacts': self.get_parent_contacts(),
        }

    def set_child_entity(self, child_entity: ChildEntity) -> None:
        """
        Set the child entity and populate the associated fields with their values.

        :param child_entity: An instance of the ChildEntity class containing the data to be set in the fields.

        :return: None
        """
        self.child_entity = child_entity

        self.set_child_name(self.child_entity.child_name)
        self.set_child_gender(self.child_entity.child_gender)
        self.set_child_birthdate(self.child_entity.child_birthdate)
        self.set_child_cpf(self.child_entity.child_cpf)
        self.set_child_rg(self.child_entity.child_rg)
        self.set_child_activities(self.child_entity.child_activities)

        self.set_parent_name(self.child_entity.parent_name)
        self.set_parent_gender(self.child_entity.parent_gender)
        self.set_parent_birthdate(self.child_entity.parent_birthdate)
        self.set_parent_cpf(self.child_entity.parent_cpf)
        self.set_parent_rg(self.child_entity.parent_rg)
        self.set_parent_address(self.child_entity.parent_address)
        self.set_parent_contacts(self.child_entity.parent_contacts)
