from pathlib import Path

HOME_DIR = Path.home()
BASE_DIR = Path().parent
ASSETS_DIR = BASE_DIR / 'assets'
ICONS_DIR = ASSETS_DIR / 'icons'
IMAGES_DIR = ASSETS_DIR / 'images'
DATABASE_PATH = BASE_DIR / 'database.json'

GENDER_OPTIONS = ('Masculino', 'Feminino')
ETHNICITY_OPTIONS = ('Negra', 'Branca', 'Parda', 'Amarela', 'Indigena')
RELIGION_OPTIONS = ('Católica', 'Evangélica', 'Espírita')
SCHOOL_DEGREE_OPTIONS = ('Educação infantil', 'Ensino fundamental', 'Ensino médio')
SCHOOL_PERIOD_OPTIONS = ('Manhã', 'Tarde', 'Noite')
HOUSEHOLD_OPTIONS = ('Sem renda', 'Um salário mínimo', 'Dois salários mínimos', 'Três ou mais salários mínimos')
TYPE_HOUSING = ('Própia', 'Alugada', 'Financiada', 'Cedida')
