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




print(christmas_day_air_quality("AirQuality.csv", True))
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]

print(christmas_day_air_quality("AirQuality.csv", False))
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]