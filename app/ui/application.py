import tkinter as tk
from datetime import datetime
from typing import Callable, List, Optional, Tuple

import ttkbootstrap as ttk

from app import constants
from app.database.entities import AdultEntity, ChildEntity
from app.ui.components import Footer, Menubar, NavBar, Toolbar
from app.ui.dialogs import ConfirmCancelDialog, DangerDialog, InfoDialog
from app.ui.forms import AdultsForm, ChildrenForm, DocumentForm
from app.ui.pages import AdultsPage, ChildrenPage, HomePage
from app.utils.images import image_tk


class Application(ttk.Window):
    """
    Graphical User Interface for Managing Adult and Child Records.

    The `Application` class is responsible for building the graphical user interface (GUI) of the application.
    It provides the main structure and components for managing adult and child records. This includes navigation,
    forms, tables, and other UI elements.
    """

    def __init__(self) -> None:
        super().__init__()
        # internal settings.
        self.protocol('WM_DELETE_WINDOW', self.stop)

        # images.
        self.logo_img = image_tk(constants.IMAGES_DIR / 'logo.jpg')

        # style.
        self.font_family = None
        self.font_size = 14
        self.font_weight = tk.NORMAL
        self.font = (self.font_family, self.font_size, self.font_weight)

        self.light_theme = 'cosmo'
        self.dark_theme = 'darkly'

        # menubar.
        self.menubar = Menubar(self)
        self.config(menu=self.menubar)

        # toolbar.
        self.toolbar = Toolbar(self)
        self.toolbar.pack(side=ttk.TOP, fill=ttk.X)

        # body.
        body = ttk.PanedWindow(self, orient=ttk.HORIZONTAL)
        body.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES, pady=10)

        self.navbar = NavBar(body)
        body.add(self.navbar, weight=1)

        self.pages_container = ttk.Frame(body)
        self.pages_container.config(padding=10)
        body.add(self.pages_container, weight=10)

        # footer.
        self.footer = Footer(self)
        self.footer.pack(side=ttk.TOP, fill=ttk.X)

        # pages.
        self.children_page = ChildrenPage(self.pages_container)
        self.adults_page = AdultsPage(self.pages_container)
        self.home_page = HomePage(self.pages_container)

        # initial state.
        self.theme = self.dark_theme
        self.title('Escritório do Prossan')
        self.iconphoto(True, self.logo_img)
        self.update_date_time()
        self.go_to_home_page()
        self.apply_style()

    def apply_style(self) -> None:
        """
        Apply the selected style and font settings to the GUI elements.

        This method applies the chosen style and font settings to various GUI elements within the application,

        :return: None
        """

        def direct_change(widget: tk.Misc) -> None:
            """
            Recursively change the font configuration for Tkinter widgets.

            This function is used to traverse the widget hierarchy and apply font configuration to specific widgets.
            It detects the specific widget and sets their font to the defined font (self.font).

            :param widget: The widget to process.
            """
            if isinstance(widget, ttk.Entry) or isinstance(widget, ttk.Menu):
                widget.config(font=self.font)
            for children in widget.winfo_children():
                direct_change(children)

        style = ttk.Style()
        style.theme_use(self.theme)
        style.configure('.', font=self.font)
        style.configure('Treeview', rowheight=self.font_size * 2)
        style.configure('TCombobox', arrowsize=self.font_size + 10)
        style.configure('TSpinbox', arrowsize=self.font_size + 10)
        self.option_add('*TCombobox*Listbox.font', self.font)
        direct_change(self)

    def dark_mode(self) -> None:
        """Activate dark mode, changing the application's theme to a dark style."""
        self.theme = self.dark_theme
        self.apply_style()

    def light_mode(self) -> None:
        """Activate light mode, changing the application's theme to a light style."""
        self.theme = self.light_theme
        self.apply_style()

    def zoom_in(self) -> None:
        """Increase the font size of the application."""
        self.font_size += 2
        self.font = (self.font_family, self.font_size, self.font_weight)
        self.apply_style()

    def zoom_out(self) -> None:
        """Decrease the font size of the application."""
        self.font_size -= 2
        self.font = (self.font_family, self.font_size, self.font_weight)
        self.apply_style()

    def clear_pages_container(self) -> None:
        """Remove all child widgets from the pages container."""
        for children in self.pages_container.winfo_children():
            children.pack_forget()

    def go_to_children_page(self) -> None:
        """Display the Children Page, replacing the current page."""
        self.clear_pages_container()
        self.children_page.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.navbar.reset_bootstyle()
        self.navbar.focus_children_button()

    def go_to_adults_page(self) -> None:
        """Display the Adults Page, replacing the current page."""
        self.clear_pages_container()
        self.adults_page.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.navbar.reset_bootstyle()
        self.navbar.focus_adults_button()

    def go_to_home_page(self) -> None:
        """Display the Home Page, replacing the current page."""
        self.clear_pages_container()
        self.home_page.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.navbar.reset_bootstyle()
        self.navbar.focus_home_button()

    def update_date_time(self) -> None:
        """
        Update the date and time label in the footer with the current system date and time.

        The date and time are updated every second to reflect the current system time.
        """
        date_time = datetime.now().strftime('%d/%B/%Y %H:%M:%S')
        self.footer.date_time_label.config(text=date_time)
        self.after(1000, self.update_date_time)

    def stop_date_time_update(self) -> None:
        """Stop Application.update_date_time callback."""
        self.after_cancel(self.update_date_time)

    def open_confirm_cancel_dialog(self, title: str, message: str, command: Callable) -> None:
        """
        Open a confirmation and cancellation dialog box.

        :param title: The title of the dialog.
        :param message: The message or question displayed in the dialog.
        :param command: A callback function to execute when the user confirms.

        Example:
            open_confirm_cancel_dialog("Confirmation", "Are you sure you want to proceed?", some_function_to_execute)
        """
        dialog = ConfirmCancelDialog(self, title, message, command)
        dialog.place_window_center()
        dialog.grab_set()

    def open_info_dialog(self, title: str, message: str) -> None:
        """
        Open an information dialog.

        :param title: A string representing the title of the information dialog.
        :param message: A string containing the message to be displayed.
        """
        dialog = InfoDialog(self, title, message)
        dialog.place_window_center()
        dialog.grab_set()

    def open_danger_dialog(self, title: str, message: str) -> None:
        """
        Open a danger dialog.

        :param title: A string representing the title of the information dialog.
        :param message: A string containing the message to be displayed.
        """
        dialog = DangerDialog(self, title, message)
        dialog.place_window_center()
        dialog.grab_set()

    def open_create_children_form(self) -> ChildrenForm:
        """
        Open a form for creating a new child record.

        This method creates and displays a form for inputting information to create a new child record.

        :return: The form for creating a new child record.
        """
        form = ChildrenForm(self)
        form.confirm_button.config(text='Confirmar registro')
        form.child_name_field.entry.focus()
        form.grab_set()
        self.apply_style()
        return form

    def open_details_children_form(self, child_entity: ChildEntity) -> ChildrenForm:
        """
        Open a form for viewing and editing details of a child record.

        This method opens a form that displays and allows editing of the details of a specific child record.
        The form is pre-filled with the information from the provided ChildEntity, and you can make changes as needed.

        :param child_entity: The child record to display and edit.

        :return: The form for viewing and editing child record details.
        """
        form = ChildrenForm(self)
        form.set_child_entity(child_entity)
        form.confirm_button.config(text='Confirmar alterações')
        form.child_name_field.entry.focus()
        form.grab_set()
        self.apply_style()
        return form

    def open_create_adults_form(self) -> AdultsForm:
        """
        Open a form for creating a new adult record.

        This method creates and displays a form for inputting information to create a new adult record.

        :return: The form for creating a new adult record.
        """
        form = AdultsForm(self)
        form.confirm_button.config(text='Confirmar registro')
        form.adult_name_field.entry.focus()
        form.grab_set()
        self.apply_style()
        return form

    def open_details_adults_form(self, adult_entity: AdultEntity) -> AdultsForm:
        """
        Open a form for viewing and editing details of an adult record.

        This method opens a form that displays and allows editing of the details of a specific adult record.
        The form is pre-filled with the information from the provided AdultEntity, and you can make changes as needed.

        :param adult_entity: The adult record to display and edit.

        :return: The form for viewing and editing adult record details.
        """
        form = AdultsForm(self)
        form.set_adult_entity(adult_entity)
        form.confirm_button.config(text='Confirmar alterações')
        form.adult_name_field.entry.focus()
        form.grab_set()
        self.apply_style()
        return form

    def open_document_form(
        self,
        initialfile: Optional[str] = None,
        initialdir: Optional[str] = None,
        filetypes: Tuple[Tuple[str, str], ...] = None,
    ) -> DocumentForm:
        """
        Open a document form for generating documents.

        :param initialfile: The initial file name to be displayed in the form.
        :param initialdir: The initial directory path to open in the file dialog.
        :param filetypes: The filetypes.

        :return: An instance of the PdfForm for user interaction.
        """
        form = DocumentForm(self, initialfile, initialdir, filetypes)
        form.place_window_center()
        form.grab_set()
        self.apply_style()
        return form

    def focus_search_children_entry(self) -> None:
        """
        Focus search children entry.

        :return: None.
        """
        self.children_page.search_entry.focus()

    def focus_search_adults_entry(self) -> None:
        """
        Focus search adults entry.

        :return: None.
        """
        self.adults_page.search_entry.focus()

    def get_children_table_selection(self) -> Optional[Tuple[str, ...]]:
        """
        Get the currently selected child record from the children table.

        :return: A tuple representing the selected child's data, or None if nothing is selected.
        """
        return self.children_page.table.get_selection()

    def get_adults_table_selection(self) -> Optional[Tuple[str, ...]]:
        """
        Get the currently selected adult record from the adults table.

        :return: A tuple representing the selected adult's data, or None if nothing is selected.
        """
        return self.adults_page.table.get_selection()

    def get_searched_children(self) -> str:
        """
        Get the currently searched children.

        :return: A string representing the currently searched children.
        """
        return self.children_page.search_entry.get().strip()

    def get_searched_adults(self) -> str:
        """
        Get the currently searched adults.

        :return: A string representing the currently searched adults.
        """
        return self.adults_page.search_entry.get().strip()

    def set_children(self, children: List[ChildEntity]) -> None:
        """
        Set values in the children table with data from a list of ChildEntity objects.

        :param children: A list of ChildEntity objects to display in the table.
        """
        table = self.children_page.table
        table.clear_rows()

        for child in children:
            row = (child.child_id, child.child_name, child.child_cpf, child.child_rg)
            table.insert_row(row)

    def set_adults(self, adults: List[AdultEntity]) -> None:
        """
        Set values in the adults table with data from a list of AdultEntity objects.

        :param adults: A list of AdultEntity objects to display in the table.
        """
        table = self.adults_page.table
        table.clear_rows()

        for adult in adults:
            row = (adult.adult_id, adult.adult_name, adult.adult_cpf, adult.adult_rg)
            table.insert_row(row)

    def start(self) -> None:
        """
        Start the application main loop, displaying the graphical user interface.

        This method initializes the application window, centers it on the screen, and enters the main event loop.

        :return: None
        """
        self.geometry('1000x550')
        self.place_window_center()
        self.mainloop()

    def stop(self) -> None:
        """Stop the application."""
        self.stop_date_time_update()
        self.destroy()
