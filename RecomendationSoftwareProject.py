from Restaurant import Restaurant
from RestaurantData import restaurant_arry

order1 = Restaurant(restaurant_arry)
def get_order():
    various_key = order1.get_key()
    print("Hi, what whould you like to order?")
    question1 = input("y for Yes | n for No")
    if question1 == 'y':
        print(f"What would you like to order? We have {order1.get_key()}.") 
        print("Let me recommend you some fantastic foods! But first, are you in rush?")
        question2 = input("y for Yes | n for No")
        if question2.lower() == "y":
            print(f"Alrighttt, since you are in rush, we recommend you the {various_key[0]} and {various_key[3]} in term of food categoris! Don't worry, they won't take too much of time!")
            question3 = input("Which one do you like to order?")
            if question3 == various_key[0]:
                print("Here is our recommendation for you:")
                order1.arranged_menu(question3)
            elif question3 == various_key[3]:
                print("Here is our recommendation for you:")
                order1.arranged_menu(question3)
            else:
                print("Pls enter the valid type of restaurant")
        elif question2.lower() == "n":
            print("Nice! Are you eating with your family?")
            question4 = input("y for Yes | n for No")
            if question4.lower() == "y":
                print(f"What a sweet family! We recommend you our {various_key[2]} set!")
                print("Here is our recommendation for you:")
                order1.arranged_menu(question4)
            elif question4.lower() == "n":
                nofamily = [i for i in various_key if i not in 'Family Dining']
                print(f"Alrighttt, here we have {nofamily}!")
                question5 = input("Which one do you prefer?")
                if question5.lower() in nofamily:
                    print("Here is our recommendation for you:")
                    order1.arranged_menu(question5)
                else:
                    print("Please make a valid order")
        else:
            print("Sorry, please make a valid insertion based on the above menu type")
    else:
        print("Alright, we wish to see you again")

test1 = get_order()