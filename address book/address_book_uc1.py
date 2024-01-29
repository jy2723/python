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

    def display_contact_info(self):
        print("Contact Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"ZIP Code: {self.zip_code}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")

john_doe = Contact("xyz", "abc", "123 Main St", "Anytown", "CA", "603525", "962541234", "xyz@example.com")
john_doe.display_contact_info()
