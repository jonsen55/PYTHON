from read_file import read_file
from write_file import *
from operation import return_land

def display_land_details():
    '''
    Method read data in file and returns list[str]
    input: none
    return: list[str]
    '''

    details = ["-------------------------------------------------------------------","|Kittaa|Place       |Direction|Aanaa |Price     |Status           |","-------------------------------------------------------------------"]

    # extracting the data read from the .txt file and assigning them to respective variables
    for items in read_file():
        kittaa = items[0]
        place = items[1]
        direction = items[2]
        aanaa = items[3]
        price = items[4]
        availability = items[5]

        list_of_status.append(availability)
        list_of_kittaa.append(kittaa)
        list_of_chosen_price.append(price)
        list_of_chosen_aanaa.append(aanaa)
        list_of_place.append(place)
        details.append(f'''|{kittaa:<6}|{place:<12}|{direction:<9}|{aanaa:<6}|{price:<10}|{availability:<17}|''')
    details.append("-------------------------------------------------------------------")
    return details

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
        # only valid option is accepted
        if input_rent_more == str(1) or input_rent_more.lower() == "yes":
            returning_value = rent_land()
            break
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

def rent_land():
    '''
    Method asks for valid land details available and returns String
    input: none
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
                    index_chosen_kittaa.append(i)
                    # keeping records of renting lands and updating it in main file
                    if chosen_status.lower() == "available" and ask_kittaa not in list_of_chosen_kittaa:
                        list_of_chosen_kittaa.append(ask_kittaa)
                        list_of_chosen_place.append(list_of_place[index_chosen_kittaa])
                        update_land_details(ask_kittaa)
                        break
                    else:
                        print(f"The chosen Kittaa {ask_kittaa:<4} is not available!!")
                        break
            rent_more_output = rent_more()
            if rent_more_output != None:
                print(rent_more_output)
            else:
                break
                
            # return generate_bill(kittaa_list, place_list, price_list, aanaa_list)
            return generate_bill(list_of_chosen_kittaa, list_of_chosen_place, list_of_chosen_price, list_of_chosen_aanaa)
        else:
            print('''
                !Entered Kittaa doesnot exist!
                *Please enter a valid Kittaa*''')
            continue

# initializing lists
list_of_kittaa = []
list_of_chosen_kittaa = []
list_of_status = []
list_of_place = []
list_of_chosen_price = []
list_of_chosen_place = []
list_of_chosen_aanaa = []
index_chosen_kittaa = []
kittaa_list = []
place_list = []
price_list = []
aanaa_list = []

# asking user for their choice from menu option
while True:
    print('''
          -------------------------------------------------------------------------
          ||                                                                     ||
          ||                        TECHNO PROPERTY NEPAL                        ||
          ||                                                                     ||
          ||                  'Rent the property you can't own'                  ||
          ||                                                                     ||
          -------------------------------------------------------------------------
          |  B.P Marg - 14, Pokhara                                  061-5390001  |
          -------------------------------------------------------------------------
          |  Do you want to:                                                      |
          |                         1. Display all details                        |
          |                         2. Rent Land                                  |
          |                         3. Return Land                                |
          |                         4. Exit                                       |
          -------------------------------------------------------------------------
          ''')
    user_choose = input("Enter your choice >>>")
    if user_choose == str(1) or user_choose.lower() == "display":
        for rows in display_land_details():
            print(rows)
        
    elif user_choose == str(2) or user_choose.lower() == "rent":
        display_land_details()
        rent_land_output = rent_land()
        if rent_land_output != None:
            print(rent_land_output)

    elif user_choose == str(3) or user_choose.lower() == "return":
        display_land_details()
        print(return_land(list_of_kittaa, list_of_place, list_of_chosen_price, list_of_chosen_aanaa))

    elif user_choose == str(4) or user_choose.lower() == "close":
        print('''
              Thank you for your reachout to our Company.
              Have a nice day!''')
        break
    # for any misinput
    else:
        print("\n*Please enter valid option*\n")
