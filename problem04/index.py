def find_first_missing_integer(num_list):

    num_list = sorted(num_list)

    for i in range(len(num_list)):
        if i + 1 == len(num_list):
            if num_list[-1] < 0:
                return 0
            return num_list[-1] + 1
        elif num_list[i] >= 0 and num_list[i + 1] - num_list[i] > 1:
            return num_list[i] + 1
        elif num_list[i] <= 0 and num_list[i + 1] > 0 and num_list[i + 1] != 1:
            return 1