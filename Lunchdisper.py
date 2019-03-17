from os import system
from datetime import datetime
months = {
    'jan': NotImplemented,
    'feb': NotImplemented,
    'mar': NotImplemented,
    'apr': NotImplemented,
    'may': NotImplemented,
    'jun': NotImplemented,
    'jul': NotImplemented,
    'aug': NotImplemented,
    'sep': r'~/Desktop/School/Greenhills\ September\ 18\ Lunch.pdf',
    'oct': r'~/Desktop/School/october\ lunch\ menu.jpg',
    'nov': r'~/Desktop/School/November\ Menu\ Final.jpg',
    'dec': r'~/Desktop/School/December\ Lunch\ Menu.jpg'
}
thefile = NotImplemented
while thefile is NotImplemented:
    month = input('Which month? ')
    month = month.lower()[:3]
    if month == '':
        month = datetime.now().strftime('%h').lower()
    thefile = months[month]
    if thefile is NotImplemented:
        print("This month's schedule has not yet been released")
print('Opening...')
system("open "+thefile)
