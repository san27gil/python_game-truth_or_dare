import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

headers = {'user-agent': 'Mozilla/5.0'}

url = 'https://psicologiaymente.com/social/preguntas-jugar-verdad-o-reto'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

url2 = 'https://www.mundodeportivo.com/uncomo/ocio/articulo/retos-para-amigos-divertidos-50883.html'
response2 = requests.get(url2, headers=headers)
soup2 = BeautifulSoup(response2.text, 'html.parser')

# Create empty lists
questions_list = []
challenge_list = []

# Extracting data from websites
questions = soup.find('body').find_all('h3')
challenges = soup2.find('body').find_all('li')

# Add all questions to an empty list
questions = questions[:135]
for question in questions:
    question = question.text.strip()
    question = question[question.find('¿'):]
    questions_list.append(question)

challenges = challenges[10:40]
for challenge in challenges:
    challenge = challenge.text.strip()
    challenge_list.append(challenge)

# Create a DataFrame for each
df = pd.Series(questions_list)
pd.options.display.max_colwidth = None

df2 = pd.Series(challenge_list)
pd.options.display.max_colwidth = None


# Welcome:
print('''
*---------------------------------------------------------*
|            BIENVENIDO A VERDAD O ATREVIMIENTO           |
*---------------------------------------------------------*
''')

# Instructions
time.sleep(1)
def instuctions():
    print('Hola! ¿Quieres que te explique cómo jugar? Y/N')
    how_to =input('> ')
    how_to = how_to.title()
    instuctions = how_to.startswith('Y')

    if instuctions == True:
        time.sleep(1)
        print('''
    1. Los jugadores deben ir respondiendo uno por uno a las preguntas.
    2. Cuando un jugador no quiera responder a una, deberá realizar un reto.
    3. Para mostrar una pregunta simplemente pulsa enter.
    4. Para proponer un reto introduce "r" y pulsa enter.
    
        ''')
        print('\nEmpezamos. Pulsa enter para mostrar la primera pregunta:')
    else:
        time.sleep(1)
        print('Empezamos. Pulsa enter para mostrar la primera pregunta:')

instuctions()

# Loop to show the questions
while True:
    pregunta = input('> ')
    if pregunta == '':
        time.sleep(0.5)
        print('Pregunta:')
        print(df.sample().to_string(header=None, index=None))
    elif pregunta == 'r':
        time.sleep(0.5)
        print('Reto:')
        print(df2.sample().to_string(header=None, index=None))
