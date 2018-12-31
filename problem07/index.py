def split_str_by_one(string):
    char_list = []
    for char in string:
        char_list.append(char)
    return char_list

def decode_msg(msg_list, left_index, right_index):
    case_1 = 0
    case_2 = 0
    if left_index >= right_index: #最后一个字符为0有两种情况，一种是采用了两种字符编码，此时应该return 1 另外一种情况是这个字符为单独的0，此时应该返回0
        if msg_list[right_index] == '0' and left_index == right_index: #如果采用的是单个字符的编码的话数组不会越界
            return 0
        return 1
    if 9 < int(msg_list[left_index] + msg_list[left_index + 1]) < 27:
        case_1 += 1
        case_1 *= decode_msg(msg_list, left_index + 2, right_index)
    if msg_list[left_index] != '0':
        case_2 += 1
        case_2 *= decode_msg(msg_list, left_index + 1, right_index)
    count = case_1 + case_2
    return count

def count_decoded_ways(encoded_msg):
    char_list = split_str_by_one(encoded_msg)
    return decode_msg(char_list, 0, len(char_list) - 1)
    