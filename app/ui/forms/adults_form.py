import tkinter as tk
from typing import Any, Dict, List, Optional, Tuple, Union

import ttkbootstrap as ttk

from app import constants
from app.database.entities import AdultEntity
from app.ui.components import AddressField, DropdownField, ListField, TextField
from app.ui.forms import BaseForm
from app.utils.images import image_tk


class AdultsForm(BaseForm):
    """
    A form for managing adult's information.

    This form is used to create, edit, or view information about adults in the application.
    """

    adult_entity: Optional[AdultEntity] = None

    def __init__(self, master: tk.Misc) -> None:
        """
        Initialize the AdultsForm widget.

        :param master: The parent widget.
        """
        super().__init__(master)
        self.save_img = image_tk(constants.ICONS_DIR / 'save.png', (32, 32))
        self.adults_img = image_tk(constants.ICONS_DIR / 'adults.png', (52, 52))

        self.title('Escritório do Prossan - Formulário para adultos')
        self.header_title.config(text='Formulário para Adultos')
        self.header_title.config(image=self.adults_img, compound=tk.TOP)

        # details.
        adult_container = ttk.Labelframe(self.container)
        adult_container.config(text='Detalhes')
        adult_container.config(padding=10)
        adult_container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        ttk.Frame(self.container).pack(side=tk.TOP, fill=tk.X, pady=50)

        self.adult_name_field = TextField(adult_container)
        self.adult_name_field.label.config(text='Nome')
        self.adult_name_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.adult_gender_field = DropdownField(adult_container)
        self.adult_gender_field.label.config(text='Gênero')
        self.adult_gender_field.set_options(('Masculino', 'Feminino'))
        self.adult_gender_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.adult_birthdate_field = TextField(adult_container)
        self.adult_birthdate_field.label.config(text='Data de nacimento')
        self.adult_birthdate_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.adult_cpf_field = TextField(adult_container)
        self.adult_cpf_field.label.config(text='CPF')
        self.adult_cpf_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.adult_rg_field = TextField(adult_container)
        self.adult_rg_field.label.config(text='RG')
        self.adult_rg_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.adult_address_field = AddressField(adult_container)
        self.adult_address_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.adult_contacts_field = ListField(adult_container)
        self.adult_contacts_field.config(text='Lista de contatos')
        self.adult_contacts_field.pack(side=tk.TOP, fill=tk.X)
        ttk.Frame(adult_container).pack(side=tk.TOP, fill=tk.X, pady=25)

        self.adult_activities_field = ListField(adult_container)
        self.adult_activities_field.config(text='Atividades pretendidas no Prossan')
        self.adult_activities_field.pack(side=tk.TOP, fill=tk.X)

        # actions.
        actions_container = ttk.Frame(self.container)
        actions_container.pack(side=tk.TOP, fill=tk.X)

        self.confirm_button = ttk.Button(actions_container)
        self.confirm_button.config(image=self.save_img, compound=tk.RIGHT)
        self.confirm_button.config(cursor='hand2')
        self.confirm_button.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)

        # noinspection PyArgumentList
        adult_container.config(bootstyle='info')

        # noinspection PyArgumentList
        self.confirm_button.config(bootstyle='default-link')

    def get_adult_name(self) -> str:
        """
        Retrieve the current value in the adult name field.

        :return: A string representing the current value in the adult name field.
        """
        return self.adult_name_field.get_value()

    def get_adult_gender(self) -> str:
        """
        Retrieve the current value in the adult gender field.

        :return: A string representing the current value in the adult gender field.
        """
        return self.adult_gender_field.get_value()

    def get_adult_birthdate(self) -> str:
        """
        Retrieve the current in value the adult birthdate field.

        :return: A string representing the current value in the adult birthdate field.
        """
        return self.adult_birthdate_field.get_value()

    def get_adult_cpf(self) -> str:
        """
        Retrieve the current value in the adult cpf field.

        :return: A string representing the current value in the adult cpf field.
        """
        return self.adult_cpf_field.get_value()

    def get_adult_rg(self) -> str:
        """
        Retrieve the current value in the adult rg field.

        :return: A string representing the current value in the adult rg field.
        """
        return self.adult_rg_field.get_value()

    def get_adult_activities(self) -> List[str]:
        """
        Retrieve the current value in the adult activities field.

        :return: A list containing strings representing the current values in the adult activities field.
        """
        return self.adult_activities_field.get_value()

    def get_adult_address(self) -> Tuple[str, str, str, str]:
        """
        Retrieve the current value in the adult address field.

        :return: A tuple representing the current value in the adult address field.
        """
        return self.adult_address_field.get_value()

    def get_adult_contacts(self) -> List[str]:
        """
        Retrieve the current value in the adult contacts field.

        :return: A list containing strings representing the current values in the adult contacts field.
        """
        return self.adult_contacts_field.get_value()

    def set_adult_name(self, adult_name: str) -> None:
        """
        Define the value of the adult name field.

        :param adult_name: A string representing the new value for the adult name.

        :return: None
        """
        self.adult_name_field.set_value(adult_name)

    def set_adult_gender(self, adult_gender: str) -> None:
        """
        Define the value of the adult gender field.

        :param adult_gender: A string representing the new value for the adult gender.

        :return: None
        """
        self.adult_gender_field.set_value(adult_gender)

    def set_adult_birthdate(self, adult_birthdate: str) -> None:
        """
        Define the value of the adult birthdate field.

        :param adult_birthdate: A string representing the new value for the adult birthdate.

        :return: None
        """
        self.adult_birthdate_field.set_value(adult_birthdate)

    def set_adult_cpf(self, adult_cpf: str) -> None:
        """
        Define the value of the adult cpf field.

        :param adult_cpf: A string representing the new value for the adult cpf.

        :return: None
        """
        self.adult_cpf_field.set_value(adult_cpf)

    def set_adult_rg(self, adult_rg: str) -> None:
        """
        Define the value of the adult rg field.

        :param adult_rg: A string representing the new value for the adult rg.

        :return: None
        """
        self.adult_rg_field.set_value(adult_rg)

    def set_adult_address(self, adult_address: Tuple[str, str, str, str]) -> None:
        """
        Define the value of the adult address field.

        :param adult_address: A tuple containing four strings representing the new address value in the order:
        (Street, District, City, State).

        :return: None
        """
        self.adult_address_field.set_value(adult_address)

    def set_adult_activities(self, adult_activities: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Define the value of the adult activities field.

        :param adult_activities: A list or tuple containing strings representing the new values for
        the adult activities.

        :return: None
        """
        self.adult_activities_field.set_value(adult_activities)

    def set_adult_contacts(self, adult_contacts: Union[List[str], Tuple[str, ...]]) -> None:
        """
        Define the value of the adult contacts field.

        :param adult_contacts: A list or tuple containing strings representing the new values for
        the adult contacts.

        :return: None
        """
        self.adult_contacts_field.set_value(adult_contacts)

    def get_values(self) -> Dict[str, Any]:
        """
        Retrieve the current values in the entire form.

        :return: A dict representing the current values in the entire form.
        """
        return {
            'adult_name': self.get_adult_name(),
            'adult_gender': self.get_adult_gender(),
            'adult_birthdate': self.get_adult_birthdate(),
            'adult_cpf': self.get_adult_cpf(),
            'adult_rg': self.get_adult_rg(),
            'adult_address': self.get_adult_address(),
            'adult_contacts': self.get_adult_contacts(),
            'adult_activities': self.get_adult_activities(),
        }

    def set_adult_entity(self, adult_entity: AdultEntity) -> None:
        """
        Set the adult entity and populate the associated fields with their values.

        :param adult_entity: An instance of the AdultEntity class containing the data to be set in the fields.

        :return: None
        """
        self.adult_entity = adult_entity
        self.set_adult_name(self.adult_entity.adult_name)
        self.set_adult_gender(self.adult_entity.adult_gender)
        self.set_adult_birthdate(self.adult_entity.adult_birthdate)
        self.set_adult_cpf(self.adult_entity.adult_cpf)
        self.set_adult_rg(self.adult_entity.adult_rg)
        self.set_adult_address(self.adult_entity.adult_address)
        self.set_adult_activities(self.adult_entity.adult_activities)
        self.set_adult_contacts(self.adult_entity.adult_contacts)
