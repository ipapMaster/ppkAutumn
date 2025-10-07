# Дополнительно устанавливаемые модули
# Модули документов
# PIP - Python Installation Package
# pip install docxtpl
# Работа с Word-документом, как с шаблоном
from docxtpl import DocxTemplate
import datetime as dt

document = DocxTemplate('word/tpl.docx')

content = {
    'name': 'Семён Семёнович',
    'event': 'увеселительное мероприятие',
    'place': 'ДК Газа',
    'date': dt.date.today().strftime('%d.%m.%Y'),
    'time': dt.datetime.now().strftime('%H:%M'),
    'items': ['паспорт', 'приглашение']
}

document.render(content)
document.save('word/invitation.docx')
