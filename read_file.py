def read_file(file_path="CourseWork\land_details.txt"):
    '''
    Method read data in file and returns 2D list
    input: file path, i.e. str
    return: list[list]
    '''
    
    
    read_file = open(file_path)
    data_in_list = read_file.readlines()
    each_data = []
    # taking data line-wise, striping and splitting it to different elements
    for i in range(len(data_in_list)):
        each_data.append(data_in_list[i].strip().split(','))
    read_file.close()

    return each_data