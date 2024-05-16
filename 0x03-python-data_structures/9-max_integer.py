#1/usr/bin/python3
def def max_integer(my_list=[]):
    new_list = []
    if my_list:
        my_list.sort(reverse = True)
        return (my_list[0])
    return None
