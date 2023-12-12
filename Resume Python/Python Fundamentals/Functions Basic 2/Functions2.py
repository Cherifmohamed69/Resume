# function 1
for x in range(5, 0, -1):
    print(x)

print ("......................................")

# function 2

def print_and_return(hh):
    print(hh[0])
    return hh[1]
result = print_and_return([1,2])
print(result)

print ("......................................")
# function 3

def first_plus_length(lst):
    return lst[0] + len(lst)
result = first_plus_length([1, 2, 3, 4, 5])
print(result)

print ("......................................")

# function 4

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False

    second_value = lst[1]
    new_list = [num for num in lst if num > second_value]

    print(len(new_list))
    return new_list
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

print ("......................................")

# function 5

def length_and_value(size, value):
    return [value] * size

print(length_and_value(4, 7))

print(length_and_value(6, 2))