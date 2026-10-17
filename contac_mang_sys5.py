# # ========== CONTACT MANAGER ==========

# # 1. Add Contact
# # 2. View Contacts
# # 3. Search Contact
# # 4. Update Contact
# # 5. Delete Contact
# # 6. Exit

# Name
# Phone
# Email
# City
contacts = []

def add_cont():
    name = input("Please enter name: ")
    phone = int(input("Please enter Phone number: " ))
    email = input("Please enter email: ")
    city = input("Please enter city name: ")

    for cont in contacts:
        if cont['fphon'] == phone:
             print(f"Number Already Available with Name {cont['fnam']}")
             return

    cont_list = {
        "fnam" : name,
        "fphon" :phone,
        "emai" : email,
        "cit": city
        
        }

    contacts.append(cont_list)
def view_cont():
     for i, no in enumerate(contacts, start=1):
          print(f" *{i}* \n Name : {no['fnam']} \n Phone Number : {no['fphon']} \n Email : {no['emai']} \n City : {no['cit']}")

while True:
    choice = int(input("Please choose a valid option: "))

    if choice == 1:
        add_cont()
    if choice == 2:
            view_cont()
