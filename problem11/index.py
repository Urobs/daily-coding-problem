#常规方法，这种方法的时间复杂度为O(n*python内置str.find()的复杂度)
def find_element_have(query_str, str_list):
    res = []
    for str in str_list:
        if query_str in str:
            res.append(str)
    return res 