import sqlite3

def query_data():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        person_id = input("Enter a person's ID number (-1 to exit): ")
        if person_id == '-1':
            break

        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id=?", (person_id,))
        person = cursor.fetchone()

        if person:
            first_name, last_name, age = person
            print(f"{first_name} {last_name}, {age} years old")

            cursor.execute("""
                SELECT p.name, p.breed, p.age
                FROM pet AS p
                JOIN person_pet AS pp ON p.id = pp.pet_id
                WHERE pp.person_id=?
            """, (person_id,))
            pets = cursor.fetchall()

            if pets:
                for pet in pets:
                    pet_name, breed, pet_age = pet
                    print(f"{first_name} {last_name} owned {pet_name}, a {breed}, that was {pet_age} years old")
            else:
                print(f"{first_name} {last_name} has no pets.")
        else:
            print("Error: Person not found.")

    conn.close()

if __name__ == "__main__":
    print("Running query_pets.py")
    query_data()