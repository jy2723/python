import json
class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nAddress: {self.address}\nCity: {self.city}\nState: {self.state}\nZip Code: {self.zip_code}\nPhone: {self.phone_number}\nEmail: {self.email}\n"


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        def sort_key(contact):
            return contact.first_name, contact.last_name

        sorted_contacts = sorted(self.contacts, key=sort_key)

        print(f"\nContacts in Address Book '{self.name}':")
        for contact in sorted_contacts:
            print(contact)
    



    def find_contact_index_by_name(self, first_name, last_name):
        for i, contact in enumerate(self.contacts):
            if contact.first_name == first_name and contact.last_name == last_name:
                return i
        return -1
    
    def edit_contact(self, first_name, last_name):
        index = self.find_contact_index_by_name(first_name, last_name)
        if index != -1:
            new_address = input("Enter new address: ")
            new_city = input("Enter new city: ")
            new_state = input("Enter new state: ")
            new_zip_code = input("Enter new zip code: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")

            self.contacts[index].address = new_address
            self.contacts[index].city = new_city
            self.contacts[index].state = new_state
            self.contacts[index].zip_code = new_zip_code
            self.contacts[index].phone_number = new_phone_number
            self.contacts[index].email = new_email

            print(f"\nContact for {first_name} {last_name} has been updated.")
        else:
            print(f"\nContact for {first_name} {last_name} not found in the address book.")

    def delete_contact(self, first_name, last_name):
        index = self.find_contact_index_by_name(first_name, last_name)
        if index != -1:
            del self.contacts[index]
            print(f"\nContact of {first_name} {last_name} has been deleted from Address Book '{self.name}'.")
        else:
            print(f"\nContact of {first_name} {last_name} not found in Address Book '{self.name}'.")

    def contact_exists(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return True
        return False

    def add_contactt(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        if self.contact_exists(first_name, last_name):
            print(f"\nContact of {first_name} {last_name} already exists in Address Book '{self.name}'.")
        else:
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")

            new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            self.add_contact(new_contact)
            print(f"\nContact of {first_name} {last_name} has been added to Address Book '{self.name}'.")

    

    def run(self):
        while True:
            print(f"\nEnter 1 to add a new contact to Address Book '{self.name}', 2 to delete a contact, 3 to edit contacts, 4 to display contacts, 5 to exit: ")

            choice = input("Your choice: ")

            if choice == '1':
                self.add_contactt()
            elif choice == '2':
                delete_first_name = input("Enter the first name of the contact you want to delete: ")
                delete_last_name = input("Enter the last name of the contact you want to delete: ")
                self.delete_contact(delete_first_name, delete_last_name)
            elif choice == '3':
                first_name_to_edit = input("Enter the first name of the contact you want to edit: ")
                last_name_to_edit = input("Enter the last name of the contact you want to edit: ")
                self.edit_contact(first_name_to_edit, last_name_to_edit)
            elif choice == '4':
                self.display_contacts()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")



class MultipleAddressBook:
    def __init__(self):
        self.address_books = {}

    def create_address_book(self):
        name = input("Enter the name of the new Address Book: ")
        self.address_books[name] = AddressBook(name)
    
    def search_person(self):
        search_city = input("Enter the city to search for a person: ")
        search_state = input("Enter the state to search for a person: ")

        found_contacts = []

        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                if contact.city == search_city and contact.state == search_state:
                    found_contacts.append(contact)

        if found_contacts:
            print(f"\nSearch results in {search_city}, {search_state}:")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"No contacts found in {search_city}, {search_state}.")

    def run(self):
        while True:
            print("\nEnter 1 to create a new Address Book, 2 to work with an existing Address Book, 3 to search for a person, or 4 to exit.")
            choice = input("Your choice: ")

            if choice == '1':
                self.create_address_book()
            elif choice == '2':
                self.manage_address_books()
            elif choice == '3':
                self.search_person()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_address_books(self):
        print("\nExisting Address Books:")
        for name in self.address_books:
            print(name)

        selected_name = input("Enter the name of the Address Book you want to work with: ")

        if selected_name in self.address_books:
            selected_address_book = self.address_books[selected_name]
            selected_address_book.run()
        else:
            print(f"Address Book '{selected_name}' not found.")
    def save_all_to_json(self, filename):
        all_contacts = {}
        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                contact_dict = {
                    'Address Book': address_book.name,
                    'First Name': contact.first_name,
                    'Last Name': contact.last_name,
                    'Address': contact.address,
                    'City': contact.city,
                    'State': contact.state,
                    'Zip Code': contact.zip_code,
                    'Phone Number': contact.phone_number,
                    'Email': contact.email
                }
                all_contacts.append(contact_dict)

        with open(filename, 'w') as json_file:
            json.dump(all_contacts, json_file, indent=2)

        print(f"All contacts saved to {filename} in JSON format.")

if __name__ == "__main__":
    address_book_system = MultipleAddressBook()
    address_book_system.run()
    address_book_system.save_all_to_json("all_contacts.json")



    
