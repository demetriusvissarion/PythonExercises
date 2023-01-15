######### Calculate standard deviation
def calculate_standard_deviation(data):
    count = len(data)
    if count == 0:
        raise ValueError
    else:
        mean = sum(data) / count
        sum_of_differences = 0
        for num in data:
            sum_of_differences += (num - mean)**2
        variance = sum_of_differences / len(data)
        std_dev = variance**(1/2)
        return std_dev

data = [1, 2, 3]

print(calculate_standard_deviation(data))
