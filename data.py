import sqlite3

# Connects to the SQLite Database with the jokes.
connection = sqlite3.connect('jokes.sqlite')
cursor = connection.cursor()

# Opens the JavaScript file, allows us to edit the file.
handle = open('data.js', 'w')

# Grabs the "Jokes" table, ordered by random.
cursor.execute('SELECT * FROM Jokes ORDER BY random()')

# Begins the JSON file.
handle.write('jokes={"joke":[\n')
jokes = list()

for row in cursor:

    id = row[0]
    setup = row[1].replace("�", "'")
    punchline = row[2].replace("�", "'")

    # Writes a JavaScript Object in the JSON file.
    if setup.find('�') < 0 and punchline.find('�') < 0: 
        handle.write('{"id":' + str(id) + ', "setup":"' + setup.replace("�", "'") + '", "punchline":"' + punchline.replace("�", "'") + '"' "},\n")

# Ends the JSON file.
handle.write(']};')