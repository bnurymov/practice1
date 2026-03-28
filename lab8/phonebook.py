"""
Practice 8 — PhoneBook with PostgreSQL Functions & Stored Procedures
"""

import psycopg2
from connect import get_connection


# ──────────────────────────────────────────────
# Helper
# ──────────────────────────────────────────────

def _print_rows(rows, headers=("ID", "Name", "Phone")):
    if not rows:
        print("  (no records found)")
        return
    col_w = [max(len(str(h)), max(len(str(r[i])) for r in rows))
             for i, h in enumerate(headers)]
    fmt = "  " + "  ".join(f"{{:<{w}}}" for w in col_w)
    sep = "  " + "  ".join("-" * w for w in col_w)
    print(fmt.format(*headers))
    print(sep)
    for row in rows:
        print(fmt.format(*row))


# ──────────────────────────────────────────────
# 1. Search contacts by pattern  (uses FUNCTION)
# ──────────────────────────────────────────────

def search_contacts(pattern: str):
    """Call PostgreSQL function get_contacts_by_pattern()."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
            rows = cur.fetchall()
        print(f"\n🔍 Search results for '{pattern}':")
        _print_rows(rows)
    finally:
        conn.close()


# ──────────────────────────────────────────────
# 2. Get contacts with pagination  (uses FUNCTION)
# ──────────────────────────────────────────────

def get_contacts_page(limit: int = 10, offset: int = 0):
    """Call PostgreSQL function get_contacts_paginated()."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM get_contacts_paginated(%s, %s);",
                (limit, offset)
            )
            rows = cur.fetchall()
        print(f"\n📄 Contacts (limit={limit}, offset={offset}):")
        _print_rows(rows)
    finally:
        conn.close()


# ──────────────────────────────────────────────
# 3. Upsert one contact  (uses PROCEDURE)
# ──────────────────────────────────────────────

def upsert_contact(name: str, phone: str):
    """
    Call stored procedure upsert_contact().
    Inserts a new contact or updates the phone if the name already exists.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
        conn.commit()
        print(f"✅ upsert_contact('{name}', '{phone}') executed.")
    finally:
        conn.close()


# ──────────────────────────────────────────────
# 4. Insert many contacts  (uses PROCEDURE)
# ──────────────────────────────────────────────

def insert_many(names: list[str], phones: list[str]):
    """
    Call stored procedure insert_many_contacts().
    Uses a loop + IF inside the procedure to validate phone format.
    After the call, fetches any invalid rows from the temp table.
    """
    if len(names) != len(phones):
        print("❌ names and phones lists must have the same length.")
        return

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "CALL insert_many_contacts(%s::VARCHAR[], %s::VARCHAR[]);",
                (names, phones)
            )
            # Read invalid contacts collected by the procedure
            try:
                cur.execute("SELECT name, phone, reason FROM invalid_contacts;")
                invalid = cur.fetchall()
            except psycopg2.Error:
                invalid = []

        conn.commit()
        print(f"✅ insert_many_contacts executed for {len(names)} entries.")
        if invalid:
            print("⚠️  Invalid contacts (skipped):")
            _print_rows(invalid, headers=("Name", "Phone", "Reason"))
        else:
            print("   All entries were valid.")
    finally:
        conn.close()


# ──────────────────────────────────────────────
# 5. Delete contact by name or phone  (uses PROCEDURE)
# ──────────────────────────────────────────────

def delete_contact(name: str = None, phone: str = None):
    """
    Call stored procedure delete_contact().
    Pass name, phone, or both.
    """
    if name is None and phone is None:
        print("❌ Provide at least a name or phone.")
        return

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s, %s);", (name, phone))
        conn.commit()
        print(f"🗑️  delete_contact(name={name!r}, phone={phone!r}) executed.")
    finally:
        conn.close()


# ──────────────────────────────────────────────
# Simple CLI menu
# ──────────────────────────────────────────────

def menu():
    actions = {
        "1": ("Search contacts by pattern",          _menu_search),
        "2": ("Show contacts (paginated)",            _menu_paginate),
        "3": ("Add / update one contact",             _menu_upsert),
        "4": ("Insert many contacts from a list",     _menu_insert_many),
        "5": ("Delete contact by name or phone",      _menu_delete),
        "0": ("Exit",                                  None),
    }

    while True:
        print("\n" + "=" * 40)
        print("       📞 PhoneBook — Practice 8")
        print("=" * 40)
        for key, (label, _) in actions.items():
            print(f"  {key}. {label}")
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Bye!")
            break
        if choice in actions and actions[choice][1]:
            try:
                actions[choice][1]()
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print("Invalid choice.")


def _menu_search():
    pattern = input("Enter pattern (name / phone): ").strip()
    search_contacts(pattern)


def _menu_paginate():
    try:
        limit  = int(input("Limit  (default 10): ").strip() or 10)
        offset = int(input("Offset (default  0): ").strip() or 0)
    except ValueError:
        limit, offset = 10, 0
    get_contacts_page(limit, offset)


def _menu_upsert():
    name  = input("Name:  ").strip()
    phone = input("Phone: ").strip()
    upsert_contact(name, phone)


def _menu_insert_many():
    print("Enter contacts one per line as  name,phone  (empty line to finish):")
    names, phones = [], []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        parts = line.split(",", 1)
        if len(parts) != 2:
            print("  Format: name,phone — skipping this line.")
            continue
        names.append(parts[0].strip())
        phones.append(parts[1].strip())
    if names:
        insert_many(names, phones)
    else:
        print("No contacts entered.")


def _menu_delete():
    print("Leave blank to skip a field.")
    name  = input("Name:  ").strip() or None
    phone = input("Phone: ").strip() or None
    delete_contact(name, phone)


# ──────────────────────────────────────────────

if __name__ == "__main__":
    menu()
