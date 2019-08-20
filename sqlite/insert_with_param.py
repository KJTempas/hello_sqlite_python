import sqlite3

conn = sqlite3.connect('my_first_db.db')  # Creates or opens database file

# Create a table if not exists...
conn.execute('create table if not exists phones (brand text, version int)')

# Ask user for information for a new phone
brand = input('Enter brand of phone: ')
version = int(input('Enter version of phone (as an integer): '))

# Parameters. Use a ? as a placeholder for data that will be filled in
# Provide data as a second argument to .execute, as a tuple of values
conn.execute('insert into phones values (?, ?)', (brand, version))

conn.commit()  # Ask the database to save changes

# Fetch and display all data. Results stored in the cursor object
cur = conn.execute('select * from phones')

for row in cur:
    print(row)

conn.close()

# TODO error handling!
