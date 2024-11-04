import sqlite3

def create_database():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE pet (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER,
            dead INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE person_pet (
            person_id INTEGER,
            pet_id INTEGER,
            FOREIGN KEY (person_id) REFERENCES person(id),
            FOREIGN KEY (pet_id) REFERENCES pet(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
