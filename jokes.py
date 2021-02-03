import ssl
import json
import sqlite3
import urllib.request
import urllib.parse
import urllib.error

# Bypasses SSL Certificate Errors.
certification = ssl.create_default_context()
certification.check_hostname = False
certification.verify_mode = ssl.CERT_NONE

# Prompts the user for how many jokes they would like to store.
amount_of_jokes = int(input('How many jokes would you like?'))

# Connects to the SQLite Database with the jokes.
connection = sqlite3.connect('jokes.sqlite')
cursor = connection.cursor()

# Creates the table, if not already initialized.
cursor.execute('CREATE TABLE IF NOT EXISTS Jokes (id INTEGER PRIMARY KEY, setup TEXT UNIQUE, punchline TEXT UNIQUE)')

for count in range(0, amount_of_jokes):

    # Grabs a joke from an API.
    service_url = 'https://official-joke-api.appspot.com/random_joke'
    handle = urllib.request.urlopen(service_url, context = certification)
    data = json.load(handle)

    # Grabs the joke information from the JSON.
    setup = data['setup'].strip()
    punchline = data['punchline'].strip()

    # Adds the joke into the SQLite Database. 
    print('Adding joke #' + str(count) + ':')
    print(setup)
    print(punchline)
    cursor.execute('INSERT OR IGNORE INTO Jokes (setup, punchline) VALUES (?, ?)', (setup, punchline))

connection.commit()
