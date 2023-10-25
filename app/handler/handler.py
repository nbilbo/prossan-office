import traceback
from functools import partial

from app import constants
from app.database.repositories import AdultRepository, ChildRepository
from app.ui import Application
from app.ui.forms import AdultsForm, ChildrenForm, DocumentForm
from app.utils.pdf import generate_adult_entity_pdf, generate_child_entity_pdf


class Handler:
    """
    Class to configure application widgets events.
    This class provides methods to handle events related to application widgets.
    """

    def __init__(self, application: Application) -> None:
        """
        Initialize the Handler with the given Application instance and configure widget events.

        :param application: An instance of the Application class.
        """
        self.application = application
        self.bind_menubar()
        self.bind_navbar()
        self.bind_toolbar()
        self.bind_children_page()
        self.bind_adults_page()

    def bind_menubar(self) -> None:
        """
        Bind actions to the menubar buttons.

        :return: None
        """
        help_menu = self.application.menubar.help_menu
        file_menu = self.application.menubar.file_menu

        help_menu.add_command(label='Sobre', command=self.handle_about)
        file_menu.add_command(label='Exportar crianças', command=self.handle_export_children)
        file_menu.add_command(label='Exportar adultos', command=self.handle_export_adults)

        file_menu.add_separator()
        file_menu.add_command(label='Sair', command=self.handle_exit)

    def bind_navbar(self) -> None:
        """
        Bind actions to the navigation bar buttons.

        :return: None
        """
        navbar = self.application.navbar
        navbar.home_button.config(command=self.handle_home_navbar)
        navbar.children_button.config(command=self.handle_children_navbar)
        navbar.adults_button.config(command=self.handle_adults_navbar)

    def bind_toolbar(self) -> None:
        """
        Bind actions to the toolbar buttons.

        :return: None
        """
        toolbar = self.application.toolbar
        toolbar.dark_theme_button.config(command=self.handle_dark_mode)
        toolbar.light_theme_button.config(command=self.handle_light_mode)
        toolbar.zoom_in_button.config(command=self.handle_zoom_in)
        toolbar.zoom_out_button.config(command=self.handle_zoom_out)

    def bind_children_page(self) -> None:
        """
        Bind actions to the children page buttons.

        :return: None
        """
        create_button = self.application.children_page.create_button
        details_button = self.application.children_page.details_button
        delete_button = self.application.children_page.delete_button
        pdf_button = self.application.children_page.pdf_button

        create_button.config(command=self.handle_open_create_children_form)
        details_button.config(command=self.handle_open_details_children_form)
        delete_button.config(command=self.handle_open_delete_children_dialog)
        pdf_button.config(command=self.handle_children_pdf)

    def bind_adults_page(self) -> None:
        """
        Bind actions to the adults page buttons.

        :return: None
        """
        create_button = self.application.adults_page.create_button
        details_button = self.application.adults_page.details_button
        delete_button = self.application.adults_page.delete_button
        pdf_button = self.application.adults_page.pdf_button

        create_button.config(command=self.handle_open_create_adults_form)
        details_button.config(command=self.handle_open_details_adults_form)
        delete_button.config(command=self.handle_open_delete_adults_dialog)
        pdf_button.config(command=self.handle_adults_pdf)

    def bind_create_children_form(self, form: ChildrenForm) -> None:
        """
        Bind actions to the create children form.

        :param form: An instance of ChildrenForm representing the form for creating children.

        :return: None
        """
        confirm_command = partial(self.handle_confirm_create_children, form)
        form.confirm_button.config(command=confirm_command)

    def bind_details_children_form(self, form: ChildrenForm) -> None:
        """
        Bind actions to the update children form.

        :param form: An instance of ChildrenForm representing the form for updating children.

        :return: None
        """
        update_command = partial(self.handle_confirm_update_children, form)
        form.confirm_button.config(command=update_command)

    def bind_pdf_children_form(self, form: DocumentForm) -> None:
        """
        Bind a PdfForm instance to confirm the generation of a PDF document for a child entity.

        This method binds the specified PdfForm to the action of confirming the generation of a PDF document
        for a child entity.

        :param form: The PdfForm instance used for specifying the file location and name of the PDF document.

        :return: None
        """
        command = partial(self.handle_confirm_children_pdf, form)
        form.confirm_button.config(command=command)

    def bind_create_adults_form(self, form: AdultsForm) -> None:
        """
        Bind actions to the create adults form.

        :param form: An instance of AdultsForm representing the form for creating adults.

        :return: None
        """
        create_command = partial(self.handle_confirm_create_adults, form)
        form.confirm_button.config(command=create_command)

    def bind_details_adults_form(self, form: AdultsForm) -> None:
        """
        Bind actions to the details adults form.

        :param form: An instance of AdultsForm representing the form for updating adults.

        :return: None
        """
        update_command = partial(self.handle_confirm_update_adults, form)
        form.confirm_button.config(command=update_command)

    def bind_pdf_adults_form(self, form: DocumentForm) -> None:
        """
        Bind a PdfForm instance to confirm the generation of a PDF document for an adult entity.

        This method binds the specified PdfForm to the action of confirming the generation of a PDF document
        for an adult entity.

        :param form: The PdfForm instance used for specifying the file location and name of the PDF document.

        :return: None
        """
        command = partial(self.handle_confirm_adults_pdf, form)
        form.confirm_button.config(command=command)

    def bind_export_children_form(self, form: DocumentForm) -> None:
        """
        Bind the export action for children to the provided document form.

        :param form: A DocumentForm to which the export action for children is bound.

        :return: None
        """
        command = partial(self.handle_confirm_export_children, form)
        form.confirm_button.config(command=command)

    def bind_export_adults_form(self, form: DocumentForm) -> None:
        """
        Bind the export action for adults to the provided document form.

        :param form: A DocumentForm to which the export action for adults is bound.

        :return: None
        """
        command = partial(self.handle_confirm_export_adults, form)
        form.confirm_button.config(command=command)

    def handle_about(self) -> None:
        self.application.open_info_dialog('Sobre', 'Função em desenvolvimento')

    def handle_export_children(self) -> None:
        """
        Handle the export action for children.

        This method handles the export action for children. It opens a document form for exporting child data.

        :return: None
        """
        initialfile = 'criancas.xlsx'
        initialdir = constants.HOME_DIR
        form = self.application.open_document_form(initialfile, initialdir)
        self.bind_export_children_form(form)

    def handle_export_adults(self) -> None:
        """
        Handle the export action for adults.

        This method handles the export action for adults. It opens a document form for exporting adult data.

        :return: None
        """
        initialfile = 'adultos.xlsx'
        initialdir = constants.HOME_DIR
        form = self.application.open_document_form(initialfile, initialdir)
        self.bind_export_adults_form(form)

    def handle_confirm_export_children(self, form: DocumentForm) -> None:
        self.application.open_info_dialog('Atenção', 'Função em desenvolvimento')
        form.destroy()

    def handle_confirm_export_adults(self, form: DocumentForm) -> None:
        self.application.open_info_dialog('Atenção', 'Função em desenvolvimento')
        form.destroy()

    def handle_exit(self) -> None:
        self.application.stop()

    def handle_home_navbar(self) -> None:
        """
        Navigate to the application's home page.

        This method triggers a navigation action to take the user to the home page of the application.

        :return: None
        """
        self.application.go_to_home_page()

    def handle_children_navbar(self) -> None:
        """
        Navigate to the application's children page.

        This method triggers a navigation action to take the user to the children page of the application.

        :return: None
        """
        self.application.go_to_children_page()
        self.refresh_children_page()

    def handle_adults_navbar(self) -> None:
        """
        Navigate to the application's adults page.

        This method triggers a navigation action to take the user to the adults page of the application.

        :return: None
        """
        self.application.go_to_adults_page()
        self.refresh_adults_page()

    def handle_zoom_in(self) -> None:
        """
        Zoom in the application's view.

        This method triggers an action to zoom in on the application's content, making it appear larger.

        :return: None
        """
        self.application.zoom_in()

    def handle_zoom_out(self) -> None:
        """
        Zoom out the application's view.

        This method triggers an action to zoom out on the application's content, making it appear smaller.

        :return: None
        """
        self.application.zoom_out()

    def handle_dark_mode(self) -> None:
        """
        Activate dark mode for the application.

        This method triggers an action to enable dark mode, which changes the appearance of the application
        to a dark color scheme.

        :return: None
        """
        self.application.dark_mode()

    def handle_light_mode(self) -> None:
        """
        Activate light mode for the application.

        This method triggers an action to enable light mode, which changes the appearance of the application
        to a light color scheme.

        :return: None
        """
        self.application.light_mode()

    def handle_open_create_children_form(self) -> None:
        """
        Open the create children form and configure its widget events.

        This method opens the form for creating children and sets up the event handlers for its widgets.

        :return: None
        """
        form = self.application.open_create_children_form()
        self.bind_create_children_form(form)

    def handle_open_details_children_form(self) -> None:
        """
        Open the details children form and configure its widget events.

        This method opens the form for viewing details of a selected child and sets up event handlers for its widgets.

        :return: None
        """
        selection = self.application.get_children_table_selection()
        if selection is not None:
            child_id = int(selection[0])
            child_entity = ChildRepository.select_one(child_id)
            if child_entity is not None:
                form = self.application.open_details_children_form(child_entity)
                self.bind_details_children_form(form)

    def handle_open_delete_children_dialog(self) -> None:
        """
        Open a confirmation dialog for child deletion.

        This method opens a confirmation dialog to prompt the user for confirmation before deleting
        a selected child record.

        :return: None
        """
        if self.application.get_children_table_selection() is not None:
            title = 'Confirmação'
            message = 'Tem certeza que deseja deletar?'
            command = self.handle_confirm_delete_children
            self.application.open_confirm_cancel_dialog(title, message, command)

    def handle_confirm_create_children(self, form: ChildrenForm) -> None:
        """
        Create a new child record using the values from a ChildrenForm.

        This method extracts the values from the provided ChildrenForm and attempts to create a new child
        record using those values. If successful, the form is closed, and the children page is refreshed.

        :param form: An instance of ChildrenForm containing the data for the new child record.

        :return: None
        """
        try:
            values = form.get_values()
            ChildRepository.insert_one(values)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            self.refresh_children_page()
            form.destroy()

    def handle_confirm_update_children(self, form: ChildrenForm) -> None:
        """
        Update a child record using the values from a ChildrenForm.

        This method extracts the values from the provided ChildrenForm and attempts to update an existing child
        record with those values. If successful, the form is closed, and the children page is refreshed.

        :param form: An instance of ChildrenForm containing the updated data for the child record.

        :return: None
        """
        try:
            values = form.get_values()
            child_id = form.child_entity.child_id
            ChildRepository.update_one(child_id, values)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'informação'
            message = 'operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            self.refresh_children_page()
            form.destroy()

    def handle_confirm_delete_children(self) -> None:
        """
        Delete the currently selected child record in the children table.

        This method attempts to delete the child record that is currently selected in the children table.
        If a selection is made, the corresponding child record is deleted, and the children page is refreshed.

        :return: None
        """
        try:
            selection = self.application.get_children_table_selection()
            if selection is not None:
                child_id = int(selection[0])
                ChildRepository.delete_one(child_id)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            self.refresh_children_page()

    def handle_children_pdf(self) -> None:
        """
        Handle the request to generate a PDF document for a selected child.

        This method retrieves the selected child from the application's children table and opens a PdfForm
        for specifying the file location and name of the PDF document.

        :return: None
        """
        selection = self.application.get_children_table_selection()
        if selection is not None:
            child_id = int(selection[0])
            child_entity = ChildRepository.select_one(child_id)
            if child_entity is not None:
                initialfile = child_entity.child_first_name + '.pdf'
                initialdir = constants.HOME_DIR
                form = self.application.open_document_form(initialfile, initialdir)
                self.bind_pdf_children_form(form)

    def handle_confirm_children_pdf(self, form: DocumentForm) -> None:
        """
        Handle the confirmation of generating a PDF document for a selected child.

        This method generates a PDF document for the selected child using the child's data and the specified
        file location from the PdfForm.

        :param form: The PdfForm instance containing the selected file location for the PDF document.

        :return: None
        """
        try:
            selection = self.application.get_children_table_selection()
            if selection is not None:
                child_id = int(selection[0])
                child_entity = ChildRepository.select_one(child_id)
                if child_entity is not None:
                    pdf_path = form.get_value()
                    pdf_title = 'Formulário do Prossan'
                    generate_child_entity_pdf(child_entity, pdf_path, pdf_title)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            form.destroy()

    def handle_open_create_adults_form(self) -> None:
        """
        Open the create adults form and configure its widget events.

        This method opens the form for creating adults and sets up the event handlers for its widgets.

        :return: None
        """
        form = self.application.open_create_adults_form()
        self.bind_create_adults_form(form)

    def handle_open_details_adults_form(self) -> None:
        """
        Open the details adults form and configure its widget events.

        This method opens the form for viewing details of a selected adult and sets up event handlers for its widgets.

        :return: None
        """
        selection = self.application.get_adults_table_selection()
        if selection is not None:
            adult_id = int(selection[0])
            adult_entity = AdultRepository.select_one(adult_id)
            if adult_entity is not None:
                form = self.application.open_details_adults_form(adult_entity)
                self.bind_details_adults_form(form)

    def handle_open_delete_adults_dialog(self) -> None:
        """
        Open a confirmation dialog for adult deletion.

        This method opens a confirmation dialog to prompt the user for confirmation before deleting
        a selected adult record.

        :return: None
        """
        if self.application.get_adults_table_selection() is not None:
            title = 'Confirmação'
            message = 'Tem certeza que deseja deletar?'
            command = self.handle_confirm_delete_adults
            self.application.open_confirm_cancel_dialog(title, message, command)

    def handle_confirm_create_adults(self, form: AdultsForm) -> None:
        """
        Create a new adult record using the values from a AdultsForm.

        This method extracts the values from the provided AdultsForm and attempts to create a new adult
        record using those values. If successful, the form is closed, and the adults page is refreshed.

        :param form: An instance of AdultsForm containing the data for the new adult record.

        :return: None
        """
        try:
            values = form.get_values()
            AdultRepository.insert_one(values)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            self.refresh_adults_page()
            form.destroy()

    def handle_confirm_update_adults(self, form: AdultsForm) -> None:
        """
        Update an adult record using the values from a AdultsForm.

        This method extracts the values from the provided AdultsForm and attempts to update an existing adult
        record with those values. If successful, the form is closed, and the adults page is refreshed.

        :param form: An instance of AdultsForm containing the updated data for the adult record.

        :return: None
        """
        try:
            values = form.get_values()
            adult_id = form.adult_entity.adult_id
            AdultRepository.update_one(adult_id, values)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            self.refresh_adults_page()
            form.destroy()

    def handle_confirm_delete_adults(self) -> None:
        """
        Delete the currently selected adult record in the adults table.

        This method attempts to delete the child record that is currently selected in the adults table.
        If a selection is made, the corresponding adult record is deleted, and the adults page is refreshed.

        :return: None
        """
        try:
            selection = self.application.get_adults_table_selection()
            if selection is not None:
                adult_id = int(selection[0])
                AdultRepository.delete_one(adult_id)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            self.refresh_adults_page()

    def handle_adults_pdf(self) -> None:
        """
        Handle the request to generate a PDF document for a selected adult.

        This method retrieves the selected adult from the application's adults table and opens a PdfForm
        for specifying the file location and name of the PDF document.

        :return: None
        """
        selection = self.application.get_adults_table_selection()
        if selection is not None:
            adult_id = int(selection[0])
            adult_entity = AdultRepository.select_one(adult_id)
            if adult_entity is not None:
                initialfile = adult_entity.adult_first_name + '.pdf'
                initialdir = constants.HOME_DIR
                form = self.application.open_document_form(initialfile, initialdir)
                self.bind_pdf_adults_form(form)

    def handle_confirm_adults_pdf(self, form: DocumentForm) -> None:
        """
        Handle the confirmation of generating a PDF document for a selected adult.

        This method generates a PDF document for the selected adult using the adult's data and the specified
        file location from the PdfForm.

        :param form: The PdfForm instance containing the selected file location for the PDF document.

        :return: None
        """
        try:
            selection = self.application.get_adults_table_selection()
            if selection is not None:
                adult_id = int(selection[0])
                adult_entity = AdultRepository.select_one(adult_id)
                if adult_entity is not None:
                    pdf_path = form.get_value()
                    pdf_title = 'Formulário do Prossan'
                    generate_adult_entity_pdf(adult_entity, pdf_path, pdf_title)

        except Exception as error:
            self.application.open_danger_dialog('Atenção', str(error))
            print(traceback.format_exc())

        else:
            title = 'Informação'
            message = 'Operação realizada com sucesso.'
            self.application.open_info_dialog(title, message)
            form.destroy()

    def refresh_children_page(self) -> None:
        """
        Refresh application children table.

        :return: None
        """
        registers = ChildRepository.select_many()
        self.application.set_children(registers)

    def refresh_adults_page(self) -> None:
        """
        Refresh application adults table.

        :return: None
        """
        registers = AdultRepository.select_many()
        self.application.set_adults(registers)
