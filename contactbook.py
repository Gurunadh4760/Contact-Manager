class Contact:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
    def update_contact(self,name=None,phone=None,email=None,address=None):
        if name:
            self.name=name
        if phone:
            self.phone=phone
        if email:
            self.email=email
        if address:
            self.address=address
    def __str__(self):
        return "Name: " + self.name + ", Phone: " + self.phone + ", Email: " + self.email + ", Address: " + self.address
class ContactManager:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,contact):
        self.contacts.append(contact)
        print("contact added")
    def view_contact(self):
        if self.contacts is None:
            print("no contacts")
        else:
            for idx,contact in enumerate(self.contacts,1):
                message = f"{idx}. {contact.name} - {contact.phone}"
                print(message)
    def Search_contact(self,query):
        result=[contact for contact in self.contacts if query.lower()in contact.name.lower()or query in contact.phone]
        if result is None:
            print("No contact found")
        else:
            for contact in result:
                print(contact)
    def update_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                new_name=input("enter new name:")
                new_phone=input("enter new phone:")
                new_email=input("enter new email:")
                new_address=input("enter new email:")
                print("Contact updated")
                return
        print("Contact not found")
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted ")
                return
        print("Contact not found.")   
def menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")   
def main():
    manager=ContactManager()
    while True:
        menu()
        choice=input("enter your choice:")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
        elif choice =='2':
            manager.view_contact()
        elif choice=='3':
            query = input("Enter name or phone to search: ")
            manager.Search_contact(query)
        elif choice=='4':
            name=input("enter name of contact to update")
            manager.update_contact(name)
        elif choice == '5':
            name = input("Enter  name of contact to delete: ")
            manager.delete_contact(name)    
        elif choice=='6':
            print("exit")
            break
        else:
            print("please try again it is invalid")
if __name__ == "__main__":
    main()            
                
                
            
                
            
                
        
              
            
                            
                    
            
                    
                
                  
                
                
                    
                    