import os

FOLDER = 'contacts/'
FILE_EXTENSION = '.txt'


#Directory application
def App():
    Create_Directory()
    
    while True:
        Show_Menu()
        option = input("    Choose an option: ")
        option = check_user_input(option)
        
        while(isinstance(option, str) or option not in [1,2,3,4,5,6]):
            option = input("    Invalid option. Try again: ")
            option = check_user_input(option)    
        
        match option:
            case 1:
                Add_Contact()


            case 2:
                Edit_Contact()
                

            case 3:
                Search_Contact()


            case 4:
                Delete_Contact()


            case 5:
                See_Directory()


            case 6: 
                print('\r\n \n \n~~~~~~~~~~~    OFF    ~~~~~~~~~~~~')
                break














########################################################################################################################
##########################################  UTILITY FUNCTIONS AND CLASSES  #############################################
########################################################################################################################

# Class for contacts
class Contact:
    def __init__ (self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email


# Function to create the directory
def Create_Directory():
    if not os.path.exists('Contacts/'):   #Checking if a directory folder exists.
        os.makedirs('Contacts/')      #creating the folder


#Funtion to display the main menu
def Show_Menu():
    print("""
    Tell me, what do you want to do?
    
    1) Add a new contact.
    2) Edit a contact.
    3) Search for a contact.
    4) Delete a contact.
    5) View contact list.
    6) Close contact directory.
    """)
    
    
# Function to convert the "input" into numbers
def check_user_input(x):
    try:
        # Convert it into integer
        val = int(x)
    except ValueError:
        try:
            # Convert it into float
            val = float(x)
        except ValueError:
            val = x

    return (val)


# Function to add contacts to the directory
def Add_Contact():
    while True:
        name_contact = input('\n    Enter the Name for your new contact: ')
    
        Exists = os.path.isfile(FOLDER + name_contact + FILE_EXTENSION)
    
        if Exists == False:
            with open(FOLDER + name_contact + FILE_EXTENSION, 'w') as file:
        
                phone_contact = input('    Enter the phone number of ' + name_contact + ': ')
                email_contact = input('    Enter the e-mail of ' + name_contact + ': ')
                contact = Contact(name_contact, phone_contact, email_contact)
        
                file.write('Name: ' + contact.name + '\n' )
                file.write('Phone Number: ' + contact.phone_number + '\n')
                file.write('Mail Address : ' + contact.email + '\n')

                print('\r\n    CONTACT CREATED SUCCESSFULLY\n')
            
            Contin = input('''\n    Do you want to create another contact?            
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
            Contin = check_user_input(Contin)
            while(isinstance(Contin, str) or Contin not in [1,2]):
                Contin = input("    Invalid option. Try again: ")
                Contin = check_user_input(Contin)
                    
            if Contin == 2:
                break

                break
    
        else:
            Overwrite_Contact = input ('''\n    That contact already exists, do you want to overwrite it?          
    Yes (Enter 1)
    No (Enter 2)
               
    ''')
            Overwrite_Contact = check_user_input(Overwrite_Contact)
            while(isinstance(Overwrite_Contact, str) or Overwrite_Contact not in [1,2]):
                Overwrite_Contact = input("    Invalid option. Try again: ")
                Overwrite_Contact = check_user_input(Overwrite_Contact)
                    
            if Overwrite_Contact == 1:
                with open(FOLDER + name_contact + FILE_EXTENSION, 'w') as file:
        
                    phone_contact = input('    Enter the phone number of ' + name_contact + ': ')
                    email_contact = input('    Enter the e-mail of ' + name_contact + ': ')
                    contact = Contact(name_contact, phone_contact, email_contact)
        
                    file.write('Name: ' + contact.name + '\n' )
                    file.write('Phone Number: ' + contact.phone_number + '\n')
                    file.write('Mail Address : ' + contact.email + '\n')

                    print('\r\n    CONTACT OVERWRITTEN SUCCESSFULLY\n')
                    break
            
            else:
                back = input('''\n    Do you want to go back to the main menu?            
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
                back = check_user_input(back)
                while(isinstance(back, str) or back not in [1,2]):
                    back = input("    Invalid option. Try again: ")
                    back = check_user_input(back)
                    
                if back == 1:
                    break


# Function to edit directory contacts
def Edit_Contact():
    
    while True:
        previous_name = input('\n    Enter the name of the contact to edit: ')
        Exists = os.path.isfile(FOLDER + previous_name+ FILE_EXTENSION)
    
        if Exists:
            
            change_name = input('''    Do you want to change the name?
    Yes (Enter 1)
    No (Enter 2)
            
    ''')
        
            change_name = check_user_input(change_name)
            while(isinstance(change_name, str) or change_name not in [1,2]):
                change_name = input("    Invalid option. Try again: ")
                change_name = check_user_input(change_name)
        
            if change_name == 1:
                with open(FOLDER + previous_name + FILE_EXTENSION, 'w') as file:
                    new_name = input('\r\n    Enter new name: ')

                    phone_contact = input('    Enter the phone number of ' + new_name + ': ')
                    email_contact = input('    Enter the e-mail of ' + new_name + ': ')
                    contact = Contact(new_name, phone_contact, email_contact)
        
                    file.write('Name: ' + contact.name + '\n')
                    file.write('Phone Number: ' + contact.phone_number + '\n')
                    file.write('Mail Address : ' + contact.email + '\n')

                os.rename(FOLDER + previous_name + FILE_EXTENSION, FOLDER + new_name + FILE_EXTENSION)

                print('\r\n    CONTACT RENAMED AND EDITED SUCCESSFULLY\n')
                break

            else:
                with open(FOLDER + previous_name + FILE_EXTENSION, 'w') as file:
                    new_phonecontact = input('    Enter the new phone number of ' + previous_name + ': ')
                    new_emailcontact = input('    Enter the new e-mail of ' + previous_name + ': ')
                    contact = Contact(previous_name, new_phonecontact, new_emailcontact)
        
                    file.write('Name: ' + contact.name + '\n' )
                    file.write('Phone Number: ' + contact.phone_number + '\n')
                    file.write('Mail Address : ' + contact.email + '\n')

                print('\r\n    CONTACT EDITED SUCCESSFULLY\n')
                break
            
            
            
        else:
            edit = input('''\n    There is no contact with that name, do you want to edit any other contact?
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
            edit = check_user_input(edit)
            while(isinstance(edit, str) or edit not in [1,2]):
                edit = input("    Invalid option. Try again: ")
                edit = check_user_input(edit)
        
            if edit == 2:
                    break
                    
                
# Function to search contacts in the directory
def Search_Contact():

    while True:
        SearchName = input('\n    Enter the name of the contact you want to search for: ')
        try:
            with open(FOLDER + SearchName + FILE_EXTENSION) as contact:
                print('\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
                for line in contact:
                    print('    ' + line.rstrip())
            
                print('    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n ')

            Contin = input('''Do you want to look another contact?            
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
            Contin = check_user_input(Contin)
            while(isinstance(Contin, str) or Contin not in [1,2]):
                Contin = input("    Invalid option. Try again: ")
                Contin = check_user_input(Contin)
                    
            if Contin == 2:
                break


        except IOError:
            print('\n    There is no contact with that name.')
            back = input('''    Do you want to go back to the main menu?            
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
            back = check_user_input(back)
            while(isinstance(back, str) or back not in [1,2]):
                back = input("    Invalid option. Try again: ")
                back = check_user_input(back)
                    
            if back == 1:
                break


# Function to delete contacts from the directory
def Delete_Contact():
    while True:
        DeleteName = input('\n    Enter the name of the contact you want to delete: ')
        try:
            os.remove(FOLDER + DeleteName + FILE_EXTENSION)
            print('    CONTACT DELETED SUCCESSFULLY')

            Contin = input('''\n    Do you want to delete any other contact?            
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
            Contin = check_user_input(Contin)
            while(isinstance(Contin, str) or Contin not in [1,2]):
                Contin = input("    Invalid option. Try again: ")
                Contin = check_user_input(Contin)
                    
            if Contin == 2:
                break


        except IOError:
            print('\n    There is no contact with that name.')
            back = input('''    Do you want to go back to the main menu?            
    Yes (Enter 1)
    No (Enter 2)
    
    ''')
            back = check_user_input(back)
            while(isinstance(back, str) or back not in [1,2]):
                back = input("    Invalid option. Try again: ")
                back = check_user_input(back)
                    
            if back == 1:
                break

# Function to see the directory
def See_Directory():

    ''' All files are listed'''
    files = os.listdir(FOLDER)   

    ''' Only files ending in ".txt" are listed'''
    files_txt = [i for i in files if i.endswith(FILE_EXTENSION)]
    print('\r\n \n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for file in files_txt:
        with open(FOLDER + file) as contact:

            for line in contact:
                print('    ' + line.rstrip())
            
            print('\n ')

    print('    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n \n')

    




#Invoking the application directory function
App()