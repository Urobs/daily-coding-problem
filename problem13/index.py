def generate_alp_dict():
    d = []
    for key in range(ord('a'), ord('z')+1):
        d.append(0)
    return d

def is_valid(k, count):
    val = 0
    for element in count:
        if element > 0:
            val += 1
    return (val <= k)

def convert_to_index(char):
    return ord(char) - 97

def get_len_of_substr(k, s):
    current_start = 0
    current_end = 0
    max_length = 0
    count = generate_alp_dict()
    for char in s:
        current_char_index = convert_to_index(char)
        count[current_char_index] += 1
        current_end += 1
        while is_valid(k, count) == False:
            count[convert_to_index(s[current_start])] -= 1
            current_start += 1
        if current_end - current_start > max_length:
            max_length = current_end - current_start
    return max_length