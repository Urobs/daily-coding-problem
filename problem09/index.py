def count_non_ajacent_sum(num_list):
    #分为两种累加值，包含上一个元素的最大累加值，以及不包含上一个元素的最大累加值
    #每一次循环比较上一次循环的累加值大小
    #关键思路其实在于每一轮循环累加的时候，当前元素添加的是距离为1的所有符合要求规则的元素的最大累加值，而我们一般的思路只是加上那个值
    incl = num_list[0]
    excl = 0
    for i in range(1, len(num_list)):
        temp_incl = incl
        #当前一轮循环的累加值
        incl = num_list[i] + excl #累加上当前的元素之后是增是减呢，在下一轮循环判断
        excl = excl if excl > temp_incl else temp_incl #判断上一轮循环的累加值

    return excl if excl > incl else incl