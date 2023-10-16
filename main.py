import locale

from app.handler import Handler
from app.ui import Application

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
app = Application()
handler = Handler(app)
app.start()
