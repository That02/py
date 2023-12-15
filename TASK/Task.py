import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def view_contacts(contacts):
    if len(contacts) == 0:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for contact in contacts:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")
        print()

def add_contact(contacts):
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    email = input("Введите email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Контакт добавлен.\n")

def search_contact(contacts):
    query = input("Введите имя для поиска: ")
    found_contacts = []
    for contact in contacts:
        if query.lower() in contact['name'].lower():
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print("Контакты не найдены.")
    else:
        print("Результаты поиска:")
        for contact in found_contacts:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")
    print()

def delete_contact(contacts):
    query = input("Введите имя контакта для удаления: ")
    deleted = False
    for contact in contacts:
        if query.lower() == contact['name'].lower():
            contacts.remove(contact)
            deleted = True
    if deleted:
        save_contacts(contacts)
        print("Контакт удален.\n")
    else:
        print("Контакт не найден.\n")

def edit_contact(contacts):
    query = input("Введите имя контакта для редактирования: ")
    for contact in contacts:
        if query.lower() == contact['name'].lower():
            print(f"Текущие данные контакта: Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")
            name = input("Введите новое имя (или оставьте пустым): ")
            if name:
                contact['name'] = name
            phone = input("Введите новый телефон (или оставьте пустым): ")
            if phone:
                contact['phone'] = phone
            email = input("Введите новый email (или оставьте пустым): ")
            if email:
                contact['email'] = email
            save_contacts(contacts)
            print("Контакт отредактирован.\n")
            return
    print("Контакт не найден.\n")

def main():
    contacts = load_contacts()
    while True:
        print("Меню Телефонного справочника:")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Удалить контакт")
        print("5. Редактировать контакт")
        print("0. Выход")
        choice = input("Выберите пункт меню (цифра): ")
        
        if choice == "0":
            break
        elif choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main() 
1