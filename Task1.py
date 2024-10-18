info = {}

def add(name, phone, email, address):
    info[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Info '{name}' successfully added.")

def display():
    if info:
        print('\nList of info:\n')
        for name, info in info.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
    else:
        print("\nNo info available.\n")

def search(name):
    if name in info:
        info = info[name]
        print(f"\nInfo found:\nName: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
    else:
        print(f"\nInfo '{name}' not found.")

def update(name, phone=None, email=None, address=None):
    if name in info:
        if phone:
            info[name]['phone'] = phone
        if email:
            info[name]['email'] = email
        if address:
            info[name]['address'] = address
        print(f"Info '{name}' updated successfully.")
    else:
        print(f"Info '{name}' not found.")

def delete(name):
    if name in info:
        del info[name]
        print(f"Info '{name}' deleted successfully.")
    else:
        print(f"Info '{name}' not found.")

def main():
    while True:
        print("-------MENU-------")
        print("1. ADD Info")
        print("2. VIEW ALL Info")
        print("3. SEARCH Info")
        print("4. UPDATE Info")
        print("5. DELETE Info")
        print("6. EXIT\n")

        c = int(input("Enter your choice: "))
        if c == 1:
            n = input("Enter name: ")
            p = input("Enter phone number: ")
            e = input("Enter email: ")
            a = input("Enter address: ")
            add(n, p, e, a)
        elif c == 2:
            display()
        elif c == 3:
            ele = input("Enter name: ")
            search(ele)
        elif c == 4:
            name = input("Enter the name: ")
            phone = input("Enter phone (press enter): ")
            email = input("Enter email (press enter): ")
            address = input("Enter address (press enter): ")
            update(name, phone if phone else None, email if email else None, address if address else None)
        elif c == 5:
            name = input("Enter name: ")
            delete(name)
        elif c == 6:
            print("EXITING")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
