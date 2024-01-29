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
            


if __name__ == "__main__":
        address_book = AddressBook()

        print("Enter person details:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("address:")
        city = input("city:")
        state = input("state:")
        zip_code = input("zip_code:")
        phone_number = input("Phone Number: ")
        email = input("Email: ")

        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)

        address_book.add_contact(new_contact)
        print("\nAddress Book Contents:")
        address_book.display_contacts()
