from datetime import datetime

spy = {
    'name':'Mr. Bond',
    'age': 24,
    'rating': 2.5,
    'is_online': True
}

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy("jasmeet","Ms.",21,0.5)

friend_one = Spy('Raman','Mr.',23,4.9)
friend_two = Spy('Rupinder','Ms.',25,5.0)
friend_three = Spy('komal','Ms.',26,6.4)
friend_four = Spy('Aman','Mr.',20,9.4)
friend_five = Spy('Sidak','Mr.',30,8.5)

friends= [friend_one,friend_two,friend_three,friend_four,friend_five]


class ChatMessages:
    def __init__(self,chat_message,time,sent_by_me):
        self.chat_message = chat_message
        self.time = time
        self.sent_by_me = sent_by_me
