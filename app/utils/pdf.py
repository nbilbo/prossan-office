from typing import List, Tuple

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    ListFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from app import constants
from app.database.entities import AdultEntity, ChildEntity

HEADER_IMAGE = Image(constants.IMAGES_DIR / 'logo.jpg', width=150, height=130)

HEADER_DESC = [
    'PROJETO SOCIAL SANTO ANTÔNIO (PROSSAN)CNPJ 05.369.990/0001-53',
    'RECONHECIDA DE UTILIDADE PÚBLICA MUNICIPAL - LEI N. 4.195/2011',
    'RECONHECIDA DE UTILIDADE PÚBLICA ESTADUAL- LEI N. 21298/2014',
    'UTILIDADE PÚBLICA FEDERAL - LEI N. 1.351/2015',
    'CONSELHO MUNICIPAL DOS DIREITOS DA CRIANÇA E DO ADOLESCENTE - CMDCA N. 15/2021',
    'CONSELHO SOCIAL DE ASSISTÊNCIA SOCIAL - CMAS N. 15/2021',
    'CEBAS - ASSISTÊNCIA SOCIAL - 30/07/2018',
    'PRAÇA VER. JOSÉ CUSTÓDIO FERREIRA N. 01 BAIRRO SANTO ANTÔNIO POUSO ALEGRE MG',
]

HEADER_PARAGRAPH_STYLE = ParagraphStyle('HeaderParagraph', fontSize=7, spaceAfter=6)

HEADER_DESC_FLOWABLE = ListFlowable(
    [Paragraph(desc, HEADER_PARAGRAPH_STYLE) for desc in HEADER_DESC],
    bulletFontSize=0,
)

HEADER_TABLE_STYLE = TableStyle(
    [
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (0, 0), 12),
        ('GRID', (-1, -1), (-1, -1), (-1, -1), colors.white),
    ]
)

INFO_TABLE_STYLE = TableStyle(
    [
        # header.
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        # content.
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        # general.
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
)


def generate_table(data: List[List], col_widths: Tuple[int, int], table_style: TableStyle) -> Table:
    """
    Generate a table within a PDF document.

    This function creates a table to be included in a PDF document using ReportLab.

    :param data: The data to be displayed in the table. Each inner list represents a row.
    :param col_widths: The list of column widths in points for the table.
    :param table_style:The style settings for the table.

    :return: A `Table` object representing the generated table.
    """
    table = Table(data, colWidths=col_widths)
    table.setStyle(table_style)
    return table


def generate_simple_document(file_path: str, title: str) -> SimpleDocTemplate:
    """
    Generate a SimpleDocTemplate for creating a PDF document.

    This function generates a SimpleDocTemplate object for creating a PDF document.
    It configures the document with specified file path, title, and margins.

    :param file_path: The path where the generated PDF file will be saved.
    :param title: The document title.

    :return: A SimpleDocTemplate object configured for creating a PDF document.
    """
    return SimpleDocTemplate(
        file_path,
        pagesize=A4,
        title=title,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
    )


def generate_child_entity_pdf(child_entity: ChildEntity, file_path: str, title: str) -> None:
    """
    Generate a PDF document for a ChildEntity.

    :param child_entity: The ChildEntity object to be represented in the PDF.
    :param file_path: The path where the generated PDF file will be saved.
    :param title: Document title.

    :return: None
    """
    doc = generate_simple_document(file_path, title)
    elements = []

    # Header table.
    header_table_data = [[HEADER_IMAGE, HEADER_DESC_FLOWABLE]]
    header_table = generate_table(header_table_data, (150, 350), HEADER_TABLE_STYLE)

    # Add the header table to the elements list
    elements.append(header_table)

    # Add a spacer to create space below the header
    elements.append(Spacer(1, 0.4 * inch))

    # Create a data list for the child's table
    child_data = [
        ['Informações da criança'],
        ['Nome', child_entity.child_name],
        ['Gênero', child_entity.child_gender],
        ['Data de nascimento', child_entity.child_birthdate],
        ['CPF', child_entity.child_cpf],
        ['RG', child_entity.child_rg],
        ['Atividades pretendidas no Prossan', '\n'.join(child_entity.child_activities)],
    ]

    # Create the child's table and set styles
    child_table = generate_table(child_data, (250, 250), INFO_TABLE_STYLE)

    # Add the child's table to the elements list
    elements.append(child_table)

    # Add a spacer to create a margin between the child and parent tables
    elements.append(Spacer(1, 0.4 * inch))

    # Create a data list for the parent's table
    parent_data = [
        ['Informações do responsável'],
        ['Nome', child_entity.parent_name],
        ['Gênero', child_entity.parent_gender],
        ['Data de nascimento:', child_entity.parent_birthdate],
        ['CPF', child_entity.parent_cpf],
        ['RG', child_entity.parent_rg],
        ['Endereço', '\n'.join(child_entity.parent_address)],
        ['Contatos', '\n'.join(child_entity.parent_contacts)],
    ]

    # Create the parent's table and set styles
    parent_table = generate_table(parent_data, (250, 250), INFO_TABLE_STYLE)

    # Add the parent's table to the elements list
    elements.append(parent_table)

    # Build the PDF document
    doc.build(elements)


def generate_adult_entity_pdf(adult_entity: AdultEntity, file_path: str, title: str) -> None:
    """
    Generate a PDF document for a AdultEntity.

    :param adult_entity: The ADultEntity object to be represented in the PDF.
    :param file_path: The path where the generated PDF file will be saved.
    :param title: Document title.

    :return: None
    """
    doc = generate_simple_document(file_path, title)
    elements = []

    # Header table.
    header_table_data = [[HEADER_IMAGE, HEADER_DESC_FLOWABLE]]
    header_table = generate_table(header_table_data, (150, 350), HEADER_TABLE_STYLE)

    # Add the header table to the elements list
    elements.append(header_table)

    # Add a spacer to create space below the header
    elements.append(Spacer(1, 0.4 * inch))

    # Create a data list for the adult's table
    adult_data = [
        ['Informações'],
        ['Nome', adult_entity.adult_name],
        ['Gênero', adult_entity.adult_gender],
        ['Data de nascimento:', adult_entity.adult_birthdate],
        ['CPF', adult_entity.adult_cpf],
        ['RG', adult_entity.adult_rg],
        ['Atividades pretendidas no Prossan', '\n'.join(adult_entity.adult_activities)],
        ['Endereço', '\n'.join(adult_entity.adult_address)],
        ['Contatos', '\n'.join(adult_entity.adult_contacts)],
    ]

    # Create the parent's table and set styles
    adult_table = generate_table(adult_data, (250, 250), INFO_TABLE_STYLE)

    # Add the parent's table to the elements list
    elements.append(adult_table)

    # Build the PDF document
    doc.build(elements)
