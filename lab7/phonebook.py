import psycopg2
import csv

from config import *

def print_help():
    print(r"add {name: string} {phone_number: integer} - add")
    print(r"edit {choice: (name: string) or (phone_num: integer)} {new_valuer} - edit")
    print(r"get {choice: (name: string) or (phone_num: integer) - get}")
    print(r"delete {choice: (name: string) or (phone_num: integer) - delete")
    print(r"importcsv {file_path} - inserts .csv file to PhoneBook")

def create_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS contacts (name VARCHAR(50) NOT NULL, phone_number INTEGER UNIQUE NOT NULL);")

def delete_table(cur):
    cur.execute("DROP TABLE IF EXISTS contacts;")


def add_contact(cur, name, phone_number):
    cmd = f"INSERT INTO contacts (name, phone_number) VALUES ('{name}', {phone_number});"
    cur.execute(cmd)

def edit_contact(cur, type, change, value):
    cmd = "UPDATE contacts SET"
    if type == 0:
        cmd += f"phone_number = {int(value)} WHERE name = '{change}';"
    elif type == 1:
        cmd += f"name = '{value}' WHERE phone_number = {int(change)};"
    cur.execute(cmd)

def get_contact(cur, x):
    cmd = f"SELECT * FROM contacts WHERE name = '{x}' OR CAST(phone_number AS TEXT) = '{x}';"
    cur.execute(cmd)
    return cur.fetchall()

def delete_contact(cur, x):
    cmd = f"DELETE FROM contacts WHERE name = '{x}' OR CAST(phone_number AS TEXT) = '{x}';"
    cur.execute(cmd)

def add_csv_file(cur, path):
    with open(path, newline='', encoding='utf-8') as f:
        data = csv.DictReader(f)
        for r in data:
            cur.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s);", (r['name'], r['phone_number']))

def main():
    # connect to the database
    cfg = load_config() # note: this function returns object
    conn = psycopg2.connect(**cfg)
    print("Connected to the database")
    cur = conn.cursor()

    # main code

    run = True

    print(r"Type '?' or 'help' to print help inforamtion")
    
    while run:
        cmd = input()

        if cmd == "":
            continue
        cmds = list(cmd.split())

        match cmds[0]:
            case "quit":
                run = False
            case "q":
                run = False
            case "exit":
                run = False

            case "?":
                print_help()
            case "help":
                print_help()

            case "add":
                if len(cmds) >= 2:
                    if get_contact(cur, cmds[2]):
                        print("Phone number already exsists")
                    else:
                        add_contact(cur, cmds[1], cmds[2])
                else:
                    print("Syntax error")
            case "edit":
                pass
            case "get":
                found = get_contact(cur, cmds[1])

                if len(cmds) == 1:
                    print("Syntax error")
                    continue
                
                if len(found) == 0:
                    print("Not found")
                else:
                    print(f"Name: {found[0][0]}")
                    print(f"Phone number: {found[0][1]}")
            case "delete":
                if len(cmds) == 1:
                    print("Syntax error")
                    continue
                delete_contact(cur, cmds[1])
            case "importcsv":
                add_csv_file(cur, cmds[1])
            
        conn.commit()
    # save and close connection
    conn.commit()
    print("Commands saved")

    cur.close()
    conn.close()
    print("Connection closed")


try:
    main()
except (psycopg2.DatabaseError, Exception) as error:
    print(error)