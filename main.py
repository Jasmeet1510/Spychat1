from spy_details import spy                         #importing details from another file
print "Hello World!!"
print "let's get started"

STATUS_MESSAGES = ['Cant talk Spychat only', 'Available', 'Busy', 'Sleeping', 'At the movie', 'At the work']            #list declared
friends = [{'name':'komal','age':25,'rating':5.8,'is_online':True},{'name': 'yash','age':26,'rating':5.9,'is_online':True}]     #dictionary declared

def add_status(C_S_M):                              #function declared to add a status
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

def add_friend():                                   #function to add a friend
    frnd = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    frnd['name'] = raw_input("Enter your friend name: ")
    frnd_salutation = raw_input("Mr. or Ms. : ")
    frnd['name'] = frnd_salutation + " " + frnd['name']
    frnd['age']= input("Enter the age of your friend : ")
    frnd['rating'] = input("Enter the rating of your friend : ")
    if len(frnd['name'])>2 and 50>=frnd['age']>=12 and frnd['rating'] >= spy['rating']:
        friends.append(frnd)
    else:
        print "Alert! Friends with these values cant be added"
    return len(friends)

def select_frnd():                                                      #function to select a friend
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " + frnd['name']
        serial_no = serial_no + 1
    user_selected_frnd = input("Select the friend to whom you want to send the message.")
    user_index = user_selected_frnd - 1
    return user_index

def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input("What would you like to do ? \n 1. Add a status \n 2. Add a Friend \n 3.Send a message \n 0.Exit \n ")             #getting choice from spy
        if menu_choice == 1:
           current_status_message = add_status(current_status_message)
           print "Your new status is updated to " + current_status_message
        elif menu_choice == 2:
            number_of_frnds = add_friend()
            print"Your friend has been added."
            print "Your friend list contains" + str(number_of_frnds)
        elif menu_choice == 3:
            selected_frnd = select_frnd()
            message = friends[selected_frnd]
            print "We are going to send message to " + message['name']
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice!!"

question = raw_input("Are you a new user? Y or N :")
if question.upper() == "N" :
    print "Your details are already registered"
    start_chat(spy['name'],spy['age'],spy['rating'])

elif question.upper() == "Y":
    spy = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    spy['name'] = raw_input("What is your name?")
    if len(spy['name'])>3:
        print "Welcome " +  spy['name'] + "Nice to have you here!!"
        spy_salutation = raw_input("How may I call you ? Mr. or Ms. ")
        spy['name'] = spy_salutation + " " +spy['name']
        print "Alright " + spy['name'] + " I'd like to have some more details about you before we proceed.."

        spy['age'] = input("What is your age? ")
        if spy['age']>11 and spy['age']<50:
            print "Great , Your age is pefect Spy!"
            spy['rating'] = input("May i know your rating?")
            if spy['rating']>=5.0:
                print "Great Spy"
            elif spy['rating']<5.0:
                print "Nice Spy"
            elif spy['rating']<4.5 and spy['rating']<=3.5:
                print "Fine Spy"
            else:
                print "Useless Spy"
            spy_is_online = True
            print "Authentication Complete. Thank you " + str(spy['name']) + "  " + "age: " + " " + str(spy['age']) + " " + "and rating of: " + str(spy['rating']) + "Welcome on board."
            start_chat(spy['name'], spy['age'], spy['rating'])
        else:
            print "Spy, your age is not valid"
    else:
        print "Please enter a valid name of atleast 4 letters"

else:
    print "Invalid Entry"

