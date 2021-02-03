import sqlite3

# Connects to the SQLite Database with the jokes.
connection = sqlite3.connect('jokes.sqlite')
cursor = connection.cursor()

# Grabs the "Jokes" table, ordered by their ID.
cursor.execute('SELECT * FROM Jokes ORDER BY id')

# Holds the IDs of the jokes we need to delete.
jokes_with_errors = list()

# Checks if the setup have any errors.
for row in cursor:

    id = row[0]
    setup = row[1]

    print('CHECKING: ' + setup)

    # Checks if the setup is more than 80 characters.
    if len(setup) >= 50:
        print('LENGTH ERROR in joke #' + str(id))
        jokes_with_errors.append(id)

    # Checks if the setup has any quotation marks.
    if setup.find('"') > 0:
        print('QUOTATION MARK ERROR in joke #' + str(id))
        jokes_with_errors.append(id)
    
    # Checks if the setup has any newline characters.
    if "\n" in setup:
        print('NEWLINE CHARACTER ERROR in joke #' + str(id))
        jokes_with_errors.append(id)

# Connects to the SQLite Database with the jokes.
connection = sqlite3.connect('jokes.sqlite')
cursor = connection.cursor()

# Grabs the "Jokes" table, ordered by their ID.
cursor.execute('SELECT * FROM Jokes ORDER BY id')

# Checks if the punchline have any errors.
for row in cursor:

    id = row[0]
    punchline = row[2]

    print('CHECKING: ' + punchline)

    if len(punchline) >= 30:
        print('LENGTH ERROR in joke #' + str(id))
        jokes_with_errors.append(id)

    # Checks if the setup has any quotation marks.
    if punchline.find('"') > 0:
        print('QUOTATION MARK ERROR in joke #' + str(id))
        jokes_with_errors.append(id)
    
    # Checks if the setup has any newline characters.
    if "\n" in punchline:
        print('NEWLINE CHARACTER ERROR in joke #' + str(id))
        jokes_with_errors.append(id)

# Deletes jokes which are in the "t" list.
for joke in jokes_with_errors:
    print('Deleting joke #' + str(joke) + ".")
    cursor.execute('DELETE FROM Jokes WHERE id = ' + str(joke))

connection.commit()