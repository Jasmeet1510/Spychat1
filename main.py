# Importing spy_details
from spy_details import spy,friends

# Importing steganography library for encoding and decoding
from steganography.steganography import Steganography

#importing date and time
from datetime import datetime

# Importing classes(Spy, ChatMessage) and list(friends) from spy_details
from spy_details import Spy, ChatMessages

# Importing csv file
import csv
# Importing termcolor to get a colourful output
from termcolor import colored


#Starting message
print "Hello!!"
print(colored("***** << Welcome to Spychat >> *****","magenta"))

# Using escape sequence
print ("Let\'s get started...\n")
#=======================================================================================================================
# Defining  load friends function to load the friends when application starts
def load_friends():
    with open('friends.csv','rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            if row:
                name = row[0]
                salutation = row[1]
                rating = row[2]
                age = row[3]
                spy = Spy(name,salutation,age,rating)
                friends.append(spy)

load_friends()
#=======================================================================================================================

# Defining  load chats function to load the chats when application starts
def load_chats():
    with open('chats.csv','rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[1:]:
            if row:
                chat_message = row[0]
                time = row[1]
                sent_by_me = row[2]
                print "Chats are :" + chat_message + time + sent_by_me

load_chats()
#=======================================================================================================================

# List used for storing old status messages
STATUS_MESSAGES = ['Cant talk Spychat only', 'Available', 'Busy', 'Sleeping', 'At the movie', 'At the work','Urgent Calls Only']
user = Spy("jass","Ms.",23,5.6)
#=======================================================================================================================

# Declaring function for adding status
def add_status(C_S_M):
    # Checking whether any old status is set
    if C_S_M != None:
        print "Your current status is: "+C_S_M
    else:
        # When no old status is set
        print "You do not have any status currently "
        # Asking whether we want to select any old status or not
    user_choice = raw_input("Do you want to select from old status? Y or N: ")
    # upper() function converts from any case to upper case
    if user_choice.upper() == "Y":
        serial_number = 1
        # Displaying old statuses from list
        for old_status in STATUS_MESSAGES:
            # Concatenating serial number with old status
            print str(serial_number) + " " + old_status
            # Incrementing serial number each time to display all statuses
            serial_number = serial_number + 1
            # Asking the user to select one of the displayed statuses
        user_status_selection = input(colored("Select your status from these: ","blue"))
        new_status = STATUS_MESSAGES[user_status_selection - 1]

    elif user_choice.upper() == "N":
        new_status = raw_input(colored("Enter your status: ","blue"))
        STATUS_MESSAGES.append(new_status)
    else:
        # If user presses enter rather than message
        print(colored("Invalid Entry Please Try Again!!","red"))
        # Returning the status
    return new_status
#=======================================================================================================================
# Declaring function for adding friend
def add_friend():
    frnd_name = raw_input("Enter your friend name: ")
    frnd_salutation = raw_input("Mr. or Ms. : ")
    frnd_name = frnd_salutation + " " + frnd_name
    frnd_age = input("Enter the age of your friend : ")
    frnd_rating = input("Enter the rating of your friend : ")
    frnd_is_online = True
    if len(frnd_name)>2 and 50>=frnd_age>=12 and frnd_rating >= spy.rating :
        f = Spy(frnd_name,frnd_age,frnd_rating,frnd_is_online)
        # Appending new friend to list
        friends.append(f)
        t = datetime.now()
        print"Your friend has been Successfully added on :" + t.strftime("%d/%m/%y")
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([f.name, f.rating, f.age, f.is_online])
            # If validation fails
    else:
        # If validation fails
        print(colored("Alert! Friends with these values cant be added ","red"))
        # Returning the number of friends
    return len(friends)
#=======================================================================================================================
# Declaring function for selecting the friend to whom message will be sent
def select_frnd():
    serial_no = 1
    # friend is a local variable of "for" loop
    for frnd in friends:
        # Concatenating serial number and name
        print str(serial_no) + " " + frnd.name
        serial_no = serial_no + 1
        # Asking user to select one of the friends
    user_selected_frnd = input("Select the friend from whom you want to send or read the message.")
    user_index = user_selected_frnd - 1
    # Returning the index of selected friend
    return user_index
#=======================================================================================================================
# Declaring function for sending message
def send_message():
    # Selecting a friend to send message
    selected_frnd = select_frnd()
    # Asking for the secret message
    user_message = raw_input("Enter your secret message: ")
    # Asking for name of image to be encoded with secret message
    original_image = raw_input("Enter the name of your image: ")
    output_path = "output.jpg"
    # Using encode() funtion from Steganography library to encrypt the message
    Steganography.encode(original_image,output_path,user_message)
    time = datetime.now()
    sent_by_me = True
    new_chat = ChatMessages(user_message,time,sent_by_me)
    # The message will be appended in ChatMessage class
    friends[selected_frnd].chats.append(new_chat)
    print "Message has successfully Encrypted at : " + time.strftime("%a,%d %Y %H:%M:%S")

#=======================================================================================================================
# Declaring funtion for reading the secret message
def read_message():
    # Selecting the friend
    chosen_frnd = select_frnd()
    # Asking the name of image from where secret message is to be decoded
    output_path = raw_input("Enter the name of the image to be decoded: ")


        # Using decode() funtion with file name of encrypted message as parameter
    secret_text = Steganography.decode(output_path)
    print (colored("Your secret message is:", "cyan"))
    print (colored(secret_text, "blue"))
        # Converting secret_text to uppercase
    new_text = (secret_text.upper()).split()

        # Checking emergency templates for help
    if 'SOS' in new_text or 'SAVE ME' in new_text or 'HELP ME' in new_text or 'ALERT' in new_text or 'RESCUE' in new_text or 'ACCIDENT' in new_text:
            # Emergency alert
        print(colored("Plzzz help !!!!","red"))

    else:
        time = datetime.now()
        new_chat = ChatMessages(chosen_frnd,secret_text,time)
        friends[chosen_frnd].chats.append(new_chat)
        with open('chats.csv','a') as chats_data:
            writer = csv.writer(chats_data)
            writer.writerow([friends[chosen_frnd],secret_text,time])


#======================================================================================================================
def remove_friend():
    chosen_frnd = select_frnd()
    del friends[chosen_frnd]
    print "Friend has been removed !"
    return len(friends)
#=======================================================================================================================
## Declaring function for starting chat
def start_chat(spy):
    # Initializing current status message with None
    current_status_message = None
    # Initializing show_menu variable with true value
    show_menu = True
    while show_menu:
        # Displaying options to select different features of application
        menu_choice = input("What would you like to do ? \n 1. Add a status \n 2. Add a Friend \n 3.Send a message \n 4.Read a message \n 5.Remove a friend \n 0.Exit \n ")             #getting choice from spy
        if menu_choice == 1:
           current_status_message = add_status(current_status_message)
           print "Your new status is updated to " + current_status_message
        elif menu_choice == 2:
            number_of_frnds = add_friend()
            print "Your friend list contains: " + str(number_of_frnds) + " " + "friends."# Calling the add_friend() function for adding friend
        elif menu_choice == 3:
            send_message()              # Calling the send_message() function for sending the secret message
        elif menu_choice == 4:
            read_message()   # Calling the read_message() function for reading the secret message
        elif menu_choice == 5:
            number_of_frnds = remove_friend()
        elif menu_choice == 0:
            show_menu = False                # For exitting from menu
        else:
            print "Invalid choice!!"

#=======================================================================================================================

#Getting login selection

login_selection = input("1.Press 1 to Login \n2.Press 2 to Signup " )
if login_selection == 1:
    user_name = raw_input("Enter your username:")
    password = input("Enter your password:")
    if user_name == "jass" and password == 12345 :                       #login id is jass and pass is 12345
        start_chat(user)


elif login_selection == 2:
    spy_name = raw_input("What is your name?")
    if len(spy_name)>3:
        print "Welcome " +  spy_name + "Nice to have you here!!"
        spy_salutation = raw_input("How may I call you ? Mr. or Ms. ")
        spy_name = spy_salutation + " " +spy_name
        print "Alright " + spy_name + " I'd like to have some more details about you before we proceed.."

        spy_age = input("What is your age? ")
        if spy_age>11 and spy_age<50:
            print "Great , Your age is perfect Spy!"
            spy_rating = input("May i know your rating?")
            if spy_rating>=5.0:
                print "Great Spy"
            elif spy_rating <5.0:
                print "Nice Spy"
            elif spy_rating<4.5 and spy_rating<=3.5:
                print "Fine Spy"
            else:
                print "Useless Spy"
            spy_is_online = True
            print "Authentication Complete. Thank you " + str(spy.name) + "  " + "age: " + " " + str(spy.age) + " " + "and rating of: " + str(spy.rating) + " " + "Welcome on board."
            spy = Spy(spy_name,spy_salutation,spy_age,spy_rating)
            start_chat(spy)
        else:
            print(colored("Spy, your age is not valid","red"))
    else:
        print(colored("Please enter a valid name of atleast 4 letters","red"))

else:
    print(colored("Invalid Entry" ,"red"))









































