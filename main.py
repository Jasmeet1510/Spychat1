from spy_details import spy_name,spy_age,spy_rating
print "Hello World!!"
print "let's get started"


def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    while show_menu:
        menu_choice = input("What would you like to do ? \n 1. Add a status \n 2. Add a Friend \n 0. Exit \n ")
        if menu_choice == 1:
            status = raw_input("Write your status: ")
            print "Your status is " + status
        elif menu_choice == 2:
            print "Will add a friend"
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice!!"

question = raw_input("Are you an new user? Y or N :")
if question.upper() == "N":
    print "Your details are already submitted"
    start_chat(spy_name,spy_age,spy_rating)


elif question.upper() == "Y":
    spy_name = raw_input("What is your name?")
    if len(spy_name)>3:
        print "Welcome " +  spy_name + "Nice to have you here!!"
        spy_salutation = raw_input("How may I call you ? Mr. or Ms. ")
        spy_name = spy_salutation + " " +spy_name
        print "Alright " + spy_name + "I'd like to have some more details about you before we proceed.."
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_age = input("What is your age? ")
        if spy_age>18 and spy_age<50:
            print "Great , Your age is pefect Spy!"
            spy_rating = input("May i know your rating?")
            if spy_rating>=5.0:
                print "Great Spy"
            elif spy_rating<5.0:
                print "Nice Spy"
            elif spy_rating<4.5 and spy_rating<=3.5:
                print "Fine Spy"
            else:
                print "Useless Spy"
            spy_is_online = True
            print  "Authentication Complete. Thank you " + str(spy_name) + "  " + "age: " + " " + str(spy_age) + " " + "and rating of: " + str(spy_rating) + "Welcome on board."
            start_chat(spy_name, spy_age, spy_rating)
        else:
            print"Spy, your age is not valid"
    else:
        print "Please enter a valid name of atleast 4 letters"

else:
    print "Invalid Entry"

