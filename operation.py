from write_file import generate_bill, update_land_details
from datetime import datetime
from read_file import read_file


def rent_land(list_of_kittaa, list_of_status, list_of_chosen_price, list_of_chosen_aanaa, list_of_place):
    '''
    Method asks for valid land details available and returns String
    input: lists
    return: String
    '''

    # validating data
    while True:
        try:
            ask_kittaa = int(input("Enter kittaa>>> "))
        except Exception:
            print("\nPlease enter a valid kittaa\n")
            continue

        # checking if the land is valid and available
        if str(ask_kittaa) in list_of_kittaa:
            for i in range(len(list_of_kittaa)):
                if str(ask_kittaa) == list_of_kittaa[i]:
                    chosen_status = list_of_status[i]
                    index_chosen_kittaa = i
                    if chosen_status.lower() == "available":
                        
                        break
                    else:
                        print(f"The chosen Kittaa {ask_kittaa:<4} is not available!!")
                        break
            print(rent_more())
            # while True:
            #     ask_bill = input("Do you want invoice bill?\n1. Yes\n2. No")
            #     if ask_bill == str(1) or ask_bill.lower() == "yes":
            
                    # break
                # elif ask_bill == str(2) or ask_bill.lower() == "no":
                #     returning_value = "Thank you for your purchase :)"
                #     break
                # else:
                #     print("Please enter a valid option!")
                #     continue
            return generate_bill(list_of_kittaa[index_chosen_kittaa], list_of_place[index_chosen_kittaa], list_of_chosen_price[index_chosen_kittaa], list_of_chosen_aanaa[index_chosen_kittaa])
        else:
            print('''
                !Entered Kittaa doesnot exist!
                *Please enter a valid Kittaa*''')
            continue

 
def rent_more():
    '''
    Method confirms additional rents and returns String Literal
    input: none
    return: String Literal
    '''

    # run until one of the options is chosen
    while True:
        print("Do you want to rent more?\n1. Yes\n2. No")
        input_rent_more = input("Enter your choice >>> ")
        if input_rent_more == str(1) or input_rent_more.lower() == "yes":
            rent_land()
        elif input_rent_more == str(2) or input_rent_more.lower() == "no":
            returning_value = '''
            PUCHASE SUCCESSFUL!
            THANK YOU FOR YOUR PURCHASE'''
            break
        # for any misinput
        else:
            print("Please enter a valid option!")
            continue
    return returning_value


def return_land(kittaa, place, price, aanaa):
    '''
    Method asks for kittaa number of returning land and returns String Literal
    input: lists
    return: String Literal
    '''
    total_fine = 0
    status = []
    index = []
    date_of_return = []
    return_kittaa_list = []
    rented_kittaa = []
    price_list = []

    for items in read_file():
        status.append(items[5])
        if items[5] == "Not Available":
            rented_kittaa.append(items[0])
            price_list.append(items[4])

    # validating kittaa
    while True:
        try:
            returning_kittaa = int(input("Enter the kittaa number of the land you want to return >>> "))
            return_kittaa_list.append(returning_kittaa)
            update_land_details(str(returning_kittaa))
        except Exception:
            print("Please enter numbers only")
            continue
        user_choice = input("Do you have lands to return more?\n1. Yes\n2. No\n>>> ")
        # only valid option is accepted
        if user_choice == str(1) or user_choice.lower() == "yes":
            continue
        elif user_choice == str(2) or user_choice.lower() == "no":
            break
        else:
            print("Please enter a valid option!")
            continue



    # checking if the land is valid and rented
    for i in range(len(return_kittaa_list)):
        if str(return_kittaa_list[i]) in rented_kittaa:
            count = 0
            for each_kittaa in kittaa:
                if str(return_kittaa_list[i]) == each_kittaa:
                    index.append(count)
                    count += 1
                

            # name = input("Enter your name >>> ")
            print("By when you should have returned the land?")

            # asking user for returning date, and validating them
            while True:
                try:
                    year = int(input("Year >>> "))
                    if year <= 0 or year < 2020:
                        print("Please enter a valid year!")
                        continue
                    month = int(input("Month >>>"))
                    if month <= 0 or month > 12:
                        print("Please enter a valid month!")
                        continue
                    day = int(input("Day >>> "))
                    if day <= 0 or day > 31:
                        print("Please enter a valid day!")
                        continue
                    break
                except Exception:
                    print("Please enter numbers only!")
                    continue

            date_of_return.append(datetime(year, month, day))
            process = "return"
            # adding fine if the returning date is exceeded
            if date_of_return[i] > datetime.now():
                generate_bill(kittaa, place, price_list, aanaa, process)
                total_fine = 0
            else:
                year_exceeded = datetime.now().year - year
                month_exceeded = datetime.now().month - month
                day_exceeded = datetime.now().day - day

                if day_exceeded > 15 and day_exceeded < 30:
                    total_fine = 5000 + (month_exceeded * 10000) + int(year_exceeded / 12) * 10000
                else:
                    total_fine = (month_exceeded * 10000) + int(year_exceeded / 12) * 10000
                
                # generate a bill for returning lands
                generate_bill(kittaa, place, price_list, aanaa, process)
            returning_value = f"Your additional fine will be Rs.{total_fine} only"
            break
        else:
            returning_value = '''
                Entered Kittaa number of land is available for rent!
                Please enter valid kittaa number of the land'''
    return returning_value
