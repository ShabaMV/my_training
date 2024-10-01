# import this
# import datetime
# year = datetime.date.today().year
# print(year-1976)

import datetime

current_year = datetime.date.today().year
me = {'name': 'Mike',
       'sex': 'male',
       'age': current_year - 1976,
       'expirience': current_year - 2024,
       'mood': 'keep calm & go to code'}
print(me)
# name = input('Please enter your name:')
# print(f'Hello, {name}! Welcome.')
