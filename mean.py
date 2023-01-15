######## Calculate the mean of an array of variable length 
def calculate_mean(array):
    if len(array) == 0:
        raise ValueError
    else:
        sum = 0
        for i in array:
            sum = sum + i
        return (sum / len(array))


data = [5, 10, 45, 20, 20]

print(calculate_mean(data))