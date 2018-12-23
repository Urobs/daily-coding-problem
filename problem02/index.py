def product_expect_current_index_with_division(num_list):
    
    total_product_execpt_zero = 1
    count_zero = 0
    length = len(num_list)

    for num in num_list:
        if num == 0:
            count_zero += 1
        else:
            total_product_execpt_zero *= num

    result = []
    if count_zero == 1:
        for index in range(length):
            if num_list[index] == 0:
                result.append(total_product_execpt_zero)
            else:
                result.append(0)
    elif count_zero == 2:
        result =  [0 for num in range(length)]
    else:
        result = [total_product_execpt_zero / num for num in num_list]

    return result

def product_expect_current_index_without_division(num_list):
    p = 1
    count_zero = 0
    zero_key = None
    length = len(num_list)
    product_result = []
    for num in num_list:
        product_result.append(p)
        if num != 0:
            p *= num
        else:
            count_zero += 1
    p = 1

    if count_zero == 2:
        return [0 for num in range(length)]
    else:
        for num in reversed(num_list):
            product_result[length - 1] *= p
            if num != 0:
                p *= num 
            else:
                zero_key = length - 1
            length -= 1

    if count_zero == 1:
        temp = [0 for num in product_result] 
        temp[zero_key] = product_result[zero_key]
        return temp
    else:
        return  product_result