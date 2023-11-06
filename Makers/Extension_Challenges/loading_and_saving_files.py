import os

def does_file_exist(filename):
    file_path = 'Makers/Extension_Challenges/' + filename

    if os.path.exists(file_path):
        return True
    else:
        return False

# # current_directory = os.getcwd()
# # print(current_directory)

# #   Returns: False
# print(does_file_exist("nonsense"))
# #   Returns: True
# print(does_file_exist("AirQuality.csv"))



def get_file_contents(filename):
    file_path = 'Makers/Extension_Challenges/' + filename

    if does_file_exist(filename):
        with open(file_path) as my_file:
            lines = []
            for line in my_file:
                if line[0] != ';':
                    lines.append(line)
            return lines
    else:
        return "This file cannot be found!"
    


#   Returns: "This file cannot be found!"
# print(get_file_contents("nonsense"))
#   Returns:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
# [...]
# print(get_file_contents("AirQuality.csv"))


def christmas_day_air_quality(filename, include_header_row):
    result = []
    my_list = get_file_contents(filename)
    if include_header_row:
        result.append(my_list[0])
    for line in my_list:
        if line[0:10] == '25/12/2004':
            result.append(line)
    return result




# print(christmas_day_air_quality("AirQuality.csv", True))
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]

# print(christmas_day_air_quality("AirQuality.csv", False))
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]



def christmas_day_average_air_quality(filename):
    my_list = christmas_day_air_quality(filename, True)
    # split lines into list of strings by ";"
    list_of_lists = []
    counter = 0
    while counter < len(my_list):
        row_split = my_list[counter].split(';')
        list_of_lists.append(row_split)
        counter += 1

    # take every 4th item in each line list and put it into new list
    ave_list = []
    counter_2 = 1
    while counter_2 < len(list_of_lists):
        ave_list.append(list_of_lists[counter_2][3])
        counter_2 += 1
    # return average of the new list
    result = [eval(i) for i in ave_list]
    print(result)
    return round(sum(result) / len(result), 2)


# print(christmas_day_average_air_quality("AirQuality.csv"))




def get_averages_for_month(filename):
    if does_file_exist(filename):
        my_list = get_file_contents(filename)

        # split string lines into list of lists by ";"
        list_of_lists = []
        counter = 1
        while counter < len(my_list):
            row_split = my_list[counter].split(';')
            list_of_lists.append(row_split)
            counter += 1

        # filter data for each month
        result = {key: [] for key in range(1, 13)}
        for key in result:
            for line in list_of_lists:
                if int(line[0][3:5]) == key:
                        result[key].append(int(line[3]))

        # calculate the average for each month
        for key, value in result.items():
            if len(value) > 0:
                average = round(sum(value) / len(value), 2)
            result[key] = average
    
    return result




# print(get_averages_for_month("AirQuality.csv"))
#   Returns: {1: 1003.47, [...], 12: 948.71}



import shutil
def create_march_data(filename):
    if does_file_exist('AirQuality.csv'):
        # my_list = get_file_contents(filename)
        march_path = 'Makers/Extension_Challenges/AirQualityMarch.csv'
    
        # while WIP delete "AirQualityMarch.csv" so I can create it again
        if does_file_exist(march_path):
            os.remove(march_path)

        # create copy of "AirQuality.csv" and call it "AirQualityMarch.csv"
        src = filename
        dst = march_path
        shutil.copy(src,dst)

        # In "AirQualityMarch.csv," delete all rows except for March
        with open(march_path, 'r') as file_handle:
            example_file_content = file_handle.readlines()

        with open(march_path, 'w') as march_file:
            # Write the header row
            march_file.write(example_file_content[0])

            # Write only the data rows for March
            for line in example_file_content[1:]:
                if "/03/" in line:
                    march_file.write(line)


print(create_march_data("Makers/Extension_Challenges/AirQuality.csv"))