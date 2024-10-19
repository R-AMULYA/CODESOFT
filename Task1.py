
import re

info = {}

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 7

def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def add(name, phone, email, address):
    if name and is_valid_phone(phone) and is_valid_email(email) and address:
        info[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Info '{name}' successfully added.")
    else:
        print("Invalid input. Please ensure that all fields are filled and valid.")

def display():
    if info:
        print('\nList of info:\n')
        for name, details in info.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("\nNo info available.\n")

def search(name):
    if name in info:
        found_info = info[name]
        print(f"\nInfo found:\nName: {name}, Phone: {found_info['phone']}, Email: {found_info['email']}, Address: {found_info['address']}")
    else:
        print(f"\nInfo '{name}' not found.")

def update(name, phone=None, email=None, address=None):
    if name in info:
        if phone and is_valid_phone(phone):
            info[name]['phone'] = phone
        if email and is_valid_email(email):
            info[name]['email'] = email
        if address:
            info[name]['address'] = address
        print(f"Info '{name}' updated successfully.")
    else:
        print(f"Info '{name}' not found.")

def delete(name):
    if name in info:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del info[name]
            print(f"Info '{name}' deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Info '{name}' not found.")

def main():
    while True:
        print("\n-------MENU-------")
        print("1. ADD Info")
        print("2. VIEW ALL Info")
        print("3. SEARCH Info")
        print("4. UPDATE Info")
        print("5. DELETE Info")
        print("6. EXIT\n")

        try:
            c = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if c == 1:
            n = input("Enter name: ").strip()
            p = input("Enter phone number: ").strip()
            e = input("Enter email: ").strip()
            a = input("Enter address: ").strip()
            add(n, p, e, a)
        elif c == 2:
            display()
        elif c == 3:
            ele = input("Enter name: ").strip()
            search(ele)
        elif c == 4:
            name = input("Enter the name: ").strip()
            phone = input("Enter phone (press enter if no change): ").strip()
            email = input("Enter email (press enter if no change): ").strip()
            address = input("Enter address (press enter if no change): ").strip()
            update(name, phone if phone else None, email if email else None, address if address else None)
        elif c == 5:
            name = input("Enter name: ").strip()
            delete(name)
        elif c == 6:
            print("EXITING")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
