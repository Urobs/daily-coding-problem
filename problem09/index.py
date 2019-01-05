def count_non_ajacent_sum(num_list):
    incl = num_list[0]
    excl = 0
    for i in range(1, len(num_list)):
        temp_incl = incl
        #当前一轮循环的累加值
        incl = num_list[i] + excl #累加上当前的元素之后是增是减呢，在下一轮循环判断
        excl = excl if excl > temp_incl else temp_incl #判断上一轮循环的累加值

    return excl if excl > incl else incl