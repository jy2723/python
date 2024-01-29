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
        return f"Name: {self.first_name} {self.last_name}\naddress: {self.address}\ncity: {self.city}\nstate: {self.state}\nzip_code: {self.zip_code}\nPhone: {self.phone_number}\nEmail: {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

    def find_contact_index_by_name(self, first_name, last_name):
        for i in range(len(self.contacts)):
            contact = self.contacts[i]
            if contact.first_name == first_name and contact.last_name == last_name:
                return i
        return -1
    def delete_contact(self, first_name, last_name):
        index = self.find_contact_index_by_name(first_name, last_name)
        if index != -1:
            del self.contacts[index]
            print(f"\nContact for {first_name} {last_name} has been deleted.")
        else:
            print(f"\nContact for {first_name} {last_name} not found in the address book.")



    
if __name__ == "__main__":
    address_book = AddressBook()
    print("Enter person details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    address = input("Address:")
    city = input("City:")
    state = input("State:")
    zip_code = input("Zip Code:")
    phone_number = input("Phone Number: ")
    email = input("Email: ")

    new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)

    address_book.add_contact(new_contact)

    print("\nAddress Book Contents:")
    address_book.display_contacts()

    delete_first_name = input("\nEnter the first name of the contact you want to delete: ")
    delete_last_name = input("Enter the last name of the contact you want to delete: ")

    address_book.delete_contact(delete_first_name, delete_last_name)


    print("\nUpdated Address Book Contents:")
    address_book.display_contacts()
