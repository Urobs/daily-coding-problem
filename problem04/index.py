def find_first_missing_integer(num_list):

    num_list = sorted(num_list)

    for i in range(len(num_list)):
        if i + 1 == len(num_list): #只有一个数时，或者数组的查找元素在数组之外时
            if num_list[-1] <= 0: 
                return 1
            elif i == 0:
                return 2 if num_list[-1] == 1 else 1
            return num_list[i] + 1
        elif num_list[i] >= 0 and num_list[i + 1] - num_list[i] > 1:
            return num_list[i] + 1
        elif num_list[i] <= 0 and num_list[i + 1] > 0 and num_list[i + 1] != 1:
            return 1

def find_first_missing_integer_beta(num_list):
    max_num = max(num_list) #找到最大的值

    if max_num < 1: #如果数列都是非正数,返回1
        return 1

    if len(num_list) == 1: #如果数列只有一个元素，那么返回2或者1，数列非1就返回1
        return 1 if num_list[0] == 2 else 1
    
    tag_list = [0] * max_num

    for num in num_list:
        if num > 0 and tag_list[num - 1] == 0:
            tag_list[num - 1] = 1
    
    
    for index in range(len(tag_list)):
        if tag_list[index] == 0:
            return index + 1
    return index + 2 