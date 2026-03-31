import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="nurymoff2",
    password="ktoto2008"
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        name VARCHAR(100),
        number VARCHAR(100) PRIMARY KEY
    )
""")
conn.commit()

def create():
    name = input("Name: ")
    number = input("Number: ")
    try:
        cur.execute(
            "INSERT INTO contacts (name, number) VALUES (%s, %s)",
            (name, number)
        )
        conn.commit()
        print("Contact was added")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Error: {e}")

def read():
    aors = input("All or specific contact: ")
    if(aors == "specific"):
        norn = input("Name or number: ")
        if(norn.isdigit() or "+" in norn):
            cur.execute("SELECT * FROM contacts WHERE number=%s", (norn,))
            row = cur.fetchall()
            if not row:
                print("No contact")
            else:
                print(f"Name: {row[0][0]} | Number: {row[0][1]}")
        else:
            cur.execute("SELECT * FROM contacts WHERE name=%s", (norn,))
            row = cur.fetchall()
            if not row:
                print("No contact")
            else:
                print(f"Name: {row[0][0]} | Number: {row[0][1]}")
    elif(aors == "all"):
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        if not rows:
            print("No contact")
        for row in rows:
            print(f"Name: {row[0]} | Number: {row[1]}")

def update():
    norn = input("Name or number: ")
    if(norn.isdigit() or "+" in norn):
        new_name = input("New name: ")
        new_number = input("new number: ")
        cur.execute(
            "UPDATE contacts SET name=%s, number=%s WHERE number=%s",
            (new_name, new_number, number)
        )
    else:
        new_name = input("New name: ")
        new_number = input("new number: ")
        cur.execute(
            "UPDATE contacts SET name=%s, number=%s WHERE name=%s",
            (new_name, new_number, name)
        )
    conn.commit()
    print("Contact updated")

def delete():
    norn = input("Name or number: ")
    if(norn.isdigit() or "+" in norn):
        cur.execute("DELETE FROM contacts WHERE number=%s", (norn,))
    else:
        cur.execute("DELETE FROM contacts WHERE name=%s", (norn,))
    conn.commit()
    print("Contact deleted")

with open("contacts.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    count = 0
    for row in reader:
        try:
            cur.execute(
                "INSERT INTO contacts (name, number) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (row[0], row[1])
            )
            count += 1
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error{row}: {e}")
    conn.commit()

while True:
    word = input()
    if(word == "w"):
        create()
    elif(word == "r"):
        read()
    elif(word == "u"):
        update()
    elif(word == "d"):
        delete()
    elif(word == "q"):
        break


