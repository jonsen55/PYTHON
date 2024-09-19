from read_file import read_file
from datetime import datetime, timedelta

def update_land_details(chosen_kittaa):
    '''
    Method accepts an int and returns None
    input: int
    return: None
    '''
    each_row = read_file()
    
    # updating the availability of the chosen land
    for i in range(len(each_row)):
        for j in range(len(each_row[i])):
            if each_row[i][0] == str(chosen_kittaa):
                if each_row[i][5] == "Available":
                    each_row[i][5] = "Not Available"
                    break
                else:
                    each_row[i][5] = "Available"
                    break
    
    # writing updated details to the .txt file
    land_details = open("CourseWork\land_details.txt","w")
    for i in range(len(each_row)):
        for j in range(len(each_row[i])):
            if j < 5:
                land_details.write(each_row[i][j]+',')
            else:
                land_details.write(each_row[i][j]+'\n')
        
    land_details.close()


def item_details(items_details_row):
    '''
    Method accepts a list and returns String
    input: List
    return: String
    '''

    each_row = ""
    for item in items_details_row:
        i = 0
        # adding details for the bill
        each_row += f'''{item[i]}\n\t\t'''
        i += 1
    return each_row

        
def generate_bill(kittaa, place, price, aanaa, process = "rent"):
    '''
    Method accepts lists of kittaa, place, price and aanaa, ask for user details, writes the Bill in a new file and returns the Bill.
    input: kittaa, place, price, aanaa --> List
    return: String
    '''

    # opening file on the basis of requirement
    if process == "rent":
        land_data = open("CourseWork\Bill_details.txt","w")
    else:
        land_data = open("CourseWork\Return_Bill_details.txt","w")
    grand_total = 0
    final_price = 0.0
    list_of_months = []
    returning_date = []

    # asking user credentials and validating them
    while True:
        name = input("Enter your name>>> ")
        if name.isalpha() or ' ' in name:
            break
        else:
            print("Please enter your valid name!")
    address = input("Enter your address>>> ")

    # validating phone number
    while True:
        try:
            phone = int(input("Enter your phone number>>>"))
            if str(phone).isdigit() and len(str(phone)) == 10:
                break
            else:
                print("Please enter valid phone number!")
                continue
        except Exception:
            print("Please enter numbers only!")

    if process.lower() == "rent":
        # validating number of months
        while True:
            try:
                duration_input = int(input("For how many months do you want to rent your first land?>>>"))
            except Exception:
                print("Please enter numbers only!")
                continue
            if duration_input < 6:
                print("Duration should exceed 6 months")
                continue
            else:
                list_of_months.append(duration_input)
                if len(kittaa) > 1:
                    while True:
                        try:
                            confirm_another_month = int(input("How many lands did you rent?>>> "))
                            break
                        except:
                            print("Please enter numbers only!")
                    for i in range(confirm_another_month-1):
                        try:
                            duration_input = int(input("For how many months do you want to rent the another land?>>>"))
                        except Exception:
                            print("Please enter numbers only!")
                            continue
                        if duration_input < 6:
                            print("Duration should exceed 6 months")
                            continue
                        else:
                            list_of_months.append(duration_input)

            # calculating total cost and returning time
            total_cost = []
            for i in range(len(list_of_months)):
                for price_a_month in price:                
                    total_cost.append(((list_of_months[i]) * int(price_a_month)))
                    returning_date.append(datetime.now().date() + timedelta(list_of_months[i] * 30))
            break
    else:
        # validating number of months
        while True:
            try:
                duration_input = int(input("For how many months did you rent your first land?>>>"))
            except Exception:
                print("Please enter numbers only!")
                continue
            if duration_input < 6:
                print("Duration should exceed 6 months")
                continue
            else:
                # only valid number of months are accepted
                list_of_months.append(duration_input)
                if len(kittaa) > 1:
                    while True:
                        try:
                            confirm_another_month = int(input("How many lands do you want to return?>>> "))
                            break
                        except:
                            print("Please enter numbers only!")
                    # further inquiry for more lands
                    for i in range(confirm_another_month-1):
                        try:
                            duration_input = int(input("For how many months did you rent the another land?>>>"))
                        except Exception:
                            print("Please enter numbers only!")
                            continue
                        if duration_input < 6:
                            print("Duration should exceed 6 months")
                            continue
                        else:
                            list_of_months.append(duration_input)
                    total_cost = []
                    for i in range(len(list_of_months)):
                        for price_a_month in price:                
                            total_cost.append(((list_of_months[i]) * int(price_a_month)))
                            returning_date.append(datetime.now().date())
                    break
                else:
                    total_cost = []                
                    total_cost.append(((list_of_months[0]) * int(price_a_month)))
                    returning_date.append(datetime.now().date())
                    break


    item_details_row = []
    # aading formated data
    if process.lower() == "rent":
        j = 0
        for i in range(len(kittaa)):
            item_details_row.append(f'''|{j:<3}|{kittaa[i]:<7}|{place[i]:<20}|{list_of_months[i]:<3}months  |{returning_date[i]}    |{aanaa[i]:<6}|{total_cost[i]:<12}|\n'''.strip().split(','))
            j += 1
            grand_total += total_cost[i]
            final_price += grand_total * 0.13
    else:
        # adding details to a list
        j = 0
        for i in range(len(price)):
            item_details_row.append(f'''|{j:<3}|{kittaa[i]:<7}|{place[i]:<20}|{list_of_months[i]:<3}months  |{returning_date[i]}    |{aanaa[i]:<6}|{total_cost[i]:<12}|\n'''.strip().split(','))
            j += 1
            grand_total += total_cost[i]
            final_price += grand_total * 0.13
    bill = f'''-----------------------------------------------------------------------------------------------------------------
|                                           Techno Property Nepal                                               |
|                                        B.P Marg - 14, Pokhara, Nepal                                          |
|                              VAT: 874527                   Ph. No: 9802373729                                 |
|                                                                                                               |
-----------------------------------------------------------------------------------------------------------------                
                  Name: {name.title():<20}                           Date:{datetime.now().date()}
                  Address: {address.title()}
                  Phone: {phone}
 
                ---------------------------------------------------------------------------------
                |SN |Kittaa |Place               |Duration   |Returning Date|Aanaa |Total       |
                ---------------------------------------------------------------------------------
                {item_details(item_details_row)}
                ---------------------------------------------------------------------------------
                                                                            Total:{grand_total}
                                                                            Vat  :13%
                                                                      Grand Total:{final_price}
------------------------------------------------------------------------------------------------------------------
                                                            
'''
    
    land_data.write(bill)
    land_data.close()
    print(bill)