
def display(input, data_in_list):
    for each_row in data_in_list:
        if input in each_row:
            print(each_row)

# if __name__ == "display":

data_list = [["1","jonsen","gaire"],["2", "herum", "k hunxa"]]
input_value = input("Enter anything")
display(input_value, data_list)