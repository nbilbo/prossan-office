# Ok, is really complicate create pdf files.

from datetime import datetime
from typing import List, Tuple

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Image, ListFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

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

HEADER_PARAGRAPH_STYLE = ParagraphStyle(name='HeaderParagraph', fontSize=7, spaceAfter=6)

TITLE_PARAGRAPH_STYLE = ParagraphStyle(name='TitleParagraph', alignment=1, fontSize=20)

BIG_PARAGRAPH_STYLE = ParagraphStyle(name='BigParagraph', alignment=1, fontSize=16, spaceAfter=6)

NORMAL_PARAGRAPH_STYLE = ParagraphStyle(name='NormalParagraph', alignment=1, fontSize=14, spaceAfter=6)

SMALL_PARAGRAPH_STYLE = ParagraphStyle(name='SmallParagraph', alignment=1, fontSize=12, spaceAfter=6)

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
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
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


def format_housing(housing: Tuple[str, str]) -> str:
    """
    Formats a housing tuple into a string.

    :param housing: A tuple containing housing info.
    :return: A formatted string containing housing info.
    """
    type_housing = f'Tipo: {housing[0]}'
    paid_monthly = f'Mensalidade: R$ {housing[1] if len(housing[1]) else "000.00"}'
    return '\n'.join((type_housing, paid_monthly))


def format_address(address: Tuple[str, str, str, str]) -> str:
    """
    Formats an address tuple into a string.

    :param address: A tuple containing address info.
    :return: A formatted string containing address info.
    """
    street = f'Rua: {address[0]}'
    district = f'Bairro: {address[1]}'
    city = f'Cidade: {address[2]}'
    state = f'Estado: {address[3]}'
    return '\n'.join((street, district, city, state))


def generate_header_table() -> Table:
    """
    Generate a header table for a PDF document using predefined constants.

    :return: A `Table` object representing the generated header table.
    """
    header_table_data = [[HEADER_IMAGE, HEADER_DESC_FLOWABLE]]
    header_table = generate_table(header_table_data, (150, 350), HEADER_TABLE_STYLE)
    return header_table


def generate_table(data: List[List], col_widths: Tuple[int, int], table_style: TableStyle) -> Table:
    """
    Generate a table within a PDF document.

    This function creates a table to be included in a PDF document using ReportLab.

    :param data: The data to be displayed in the table. Each inner list represents a row.
    :param col_widths: The list of column widths in points for the table.
    :param table_style:The style settings for the table.

    :return: A `Table` object representing the generated table.
    """
    table = Table(data, colWidths=col_widths, repeatRows=1)
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


def generate_child_data(child_entity: ChildEntity) -> List[List]:
    return [
        ['Informações'],
        ['Nome', child_entity.child_name],
        ['Gênero', child_entity.child_gender],
        ['Data de nascimento', child_entity.child_birthdate],
        ['CPF', child_entity.child_cpf],
        ['RG', child_entity.child_rg],
        ['Etinia (Raça)', child_entity.child_ethnicity],
        ['Religião', child_entity.child_religion],
        ['Número da roupa', child_entity.child_clothing_number],
        ['Número do calçado', child_entity.child_shoe_number],
        ['Nome da escola', child_entity.child_school_name],
        ['Escolaridade', child_entity.child_school_degree],
        ['Periodo esoolar', child_entity.child_school_period],
        ['Atividades pretendidas no Prossan', '\n'.join(child_entity.child_activities)],
    ]


def generate_parent_data(child_entity: ChildEntity) -> List[List]:
    return [
        ['Informações do responsável'],
        ['Nome', child_entity.parent_name],
        ['Gênero', child_entity.parent_gender],
        ['Data de nascimento:', child_entity.parent_birthdate],
        ['CPF', child_entity.parent_cpf],
        ['RG', child_entity.parent_rg],
        ['Renda familiar', child_entity.parent_household_income],
        ['Moradia', format_housing(child_entity.parent_housing)],
        ['Endereço', format_address(child_entity.parent_address)],
        ['Contatos', '\n'.join(child_entity.parent_contacts)],
        ['Autorizaçao p/ pratica de exercicios', child_entity.parent_authorization],
    ]


def generate_signature_section(elements: List, text: str, show_date: bool = False) -> None:
    elements.append(Paragraph('_ _' * 20, style=NORMAL_PARAGRAPH_STYLE))
    elements.append(Paragraph(text, style=NORMAL_PARAGRAPH_STYLE))

    if show_date:
        elements.append(Paragraph(datetime.now().strftime('%d/%B/%Y'), style=NORMAL_PARAGRAPH_STYLE))
        elements.append(Spacer(1, 0.4 * inch))


def generate_observation_section(elements: List) -> None:
    observation_title = 'Observação'
    observation_text = 'O Prossan não se responsabiliza pelo fornecimento do material nem guarda dos mesmos.'
    elements.append(Paragraph(observation_title, style=BIG_PARAGRAPH_STYLE))
    elements.append(Paragraph(observation_text, style=NORMAL_PARAGRAPH_STYLE))


def generate_social_validation_section(elements: List) -> None:
    text = (
        'Confome Estatuto Social do Prossan, que visa atender as pessoas de baixa renda, '
        'concluo que o requerente acima enquadra (Sim) ou (Não) no critério de avaliação social.'
    )

    elements.append(Paragraph('Avaliação Social', BIG_PARAGRAPH_STYLE))
    elements.append(Paragraph(text, NORMAL_PARAGRAPH_STYLE))
    elements.append(Paragraph('Admito ( ) Não Admito( )', NORMAL_PARAGRAPH_STYLE))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(generate_signature_section(elements, 'Assinatura Assistente Social', False))


def generate_child_entity_pdf(child_entity: ChildEntity, file_path: str, title: str) -> None:
    """
    Generate a PDF document for a ChildEntity.

    :param child_entity: The ChildEntity object to be represented in the PDF.
    :param file_path: The path where the generated PDF file will be saved.
    :param title: Document title.

    :return: None
    """
    elements = []
    doc = generate_simple_document(file_path, title)

    elements.append(generate_header_table())
    elements.append(Spacer(1, 0.4 * inch))

    elements.append(Paragraph('Ficha de matricula de crianças e adolecentes', style=TITLE_PARAGRAPH_STYLE))
    elements.append(Spacer(1, 0.4 * inch))

    elements.append(generate_table(generate_child_data(child_entity), (250, 250), INFO_TABLE_STYLE))
    elements.append(Spacer(1, 0.4 * inch))

    elements.append(generate_table(generate_parent_data(child_entity), (250, 250), INFO_TABLE_STYLE))
    elements.append(Spacer(1, 0.4 * inch))

    generate_observation_section(elements)
    elements.append(Spacer(1, 0.4 * inch))

    generate_signature_section(elements, 'Assinatura do responsável', True)
    elements.append(Spacer(1, 0.4 * inch))

    generate_social_validation_section(elements)
    elements.append(Spacer(1, 0.4 * inch))

    # Build the PDF document.
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
    elements.append(header_table)
    elements.append(Spacer(1, 0.4 * inch))

    # Create a data list for the adult's table.
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

    # Create the parent's table and set styles.
    adult_table = generate_table(adult_data, (250, 250), INFO_TABLE_STYLE)
    elements.append(adult_table)

    # Build the PDF document.
    doc.build(elements)
