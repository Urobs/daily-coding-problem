def find_out_if_sum_equal_k(list, k) :
    if len(list) < 2 :
        return False
    list = sorted(list)
    j = len(list) - 1
    i = 0
    while i != j :
        l_sum = list[i] + list[j]
        if l_sum > k :
            j -= 1
        elif l_sum < k :
            i += 1
        else :
            return True
    return False