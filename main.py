from spy_details import spy,friends                     #importing details from another file
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Spy, ChatMessages
import csv

print "Hello World!!"
print "Welcome to Spychat.let's get started!"

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

STATUS_MESSAGES = ['Cant talk Spychat only', 'Available', 'Busy', 'Sleeping', 'At the movie', 'At the work'] #list declared
user = Spy("jass","Ms.",23,5.6)


def add_status(C_S_M):                                              #function to add a status
    if C_S_M != None:
        print "Your current status is: "+C_S_M
    else:
        print "You do not have any status currently "

    user_choice = raw_input("Do you want to select from old status? Y or N: ")
    if user_choice.upper() == "Y":
        serial_number = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_number) + " " + old_status
            serial_number = serial_number + 1
        user_status_selection = input("Select your status from these: ")
        new_status = STATUS_MESSAGES[user_status_selection - 1]

    elif user_choice.upper() == "N":
        new_status = raw_input("Enter your status: ")
        STATUS_MESSAGES.append(new_status)
    else:
        print "Invalid Entry Please Try Again!!"
    return new_status

def add_friend():                                                       #function to add a friend111
    frnd_name = raw_input("Enter your friend name: ")
    frnd_salutation = raw_input("Mr. or Ms. : ")
    frnd_name = frnd_salutation + " " + frnd_name
    frnd_age = input("Enter the age of your friend : ")
    frnd_rating = input("Enter the rating of your friend : ")
    frnd_is_online = True
    if len(frnd_name)>2 and 50>=frnd_age>=12 and frnd_rating >= spy.rating :
        f = Spy(frnd_name,frnd_age,frnd_rating,frnd_is_online)
        friends.append(f)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([f.name, f.rating, f.age, f.is_online])
    else:
        print "Alert! Friends with these values cant be added"
    return len(friends)

def select_frnd():                                                      #function to select a friend
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " + frnd.name
        serial_no = serial_no + 1
    user_selected_frnd = input("Select the friend from whom you want to send or read the message.")
    user_index = user_selected_frnd - 1
    return user_index

def send_message():                                                     #function to send message
    selected_frnd = select_frnd()
    user_message = raw_input("Enter your secret message: ")
    original_image = raw_input("Enter the name of your image: ")
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,user_message)
    time = datetime.now()
    sent_by_me = True
    new_chat = ChatMessages(user_message,time,sent_by_me)
    friends[selected_frnd].chats.append(new_chat)
    print "Message has successfully Encrypted at : " + time.strftime("%a,%d %Y %H:%M:%S")


def read_message():                                                     #function to read message
    chosen_frnd = select_frnd()
    output_path = raw_input("Enter the name of the image to be decoded: ")
    secret_text = Steganography.decode(output_path)
    time = datetime.now()
    new_chat = ChatMessages(chosen_frnd,secret_text,time)
    friends[chosen_frnd].chats.append(new_chat)
    with open('chats.csv','a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([friends[chosen_frnd],secret_text,time])
    print "Your secret message is " + secret_text + "."

def start_chat(spy):                            #function to start a chat
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input("What would you like to do ? \n 1. Add a status \n 2. Add a Friend \n 3.Send a message \n 4.Read a message \n 0.Exit \n ")             #getting choice from spy
        if menu_choice == 1:
           current_status_message = add_status(current_status_message)
           print "Your new status is updated to " + current_status_message
        elif menu_choice == 2:
            number_of_frnds = add_friend()
            t = datetime.now()
            print"Your friend has been Successfully added on :" + t.strftime("%d/%m/%y")
            print "Your friend list contains: " + " " + str(number_of_frnds) + "friends."
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice!!"

login_selection = input("1.Press 1 to Login \n2.Press 2 to Signup " )
if login_selection == 1:
    user_name = raw_input("Enter your username:")
    password = input("Enter your password:")
    if user_name == "jass" and password == 12345:                        #login id is jass and pass is 12345
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
            print "Spy, your age is not valid"
    else:
        print "Please enter a valid name of atleast 4 letters"

else:
    print "Invalid Entry"

