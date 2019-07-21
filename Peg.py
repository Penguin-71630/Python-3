board = [input() for i in range(7)]


def check_if_o_surround(i_list, i_str, l_id, s_id):
    if 0 <= l_id + 2 * i_list <= 6 and 0 <= s_id + 2 * i_str <= 6:
        if board[l_id + i_list][s_id + i_str] == 'o' \
                and board[l_id + 2 * i_list][s_id + 2 * i_str] == 'o':
            return True
        else:
            return False
    else:
        return False


def find_steps(list_id, str_id):
    step = 0

    step += int(check_if_o_surround(0, 1, list_id, str_id))
    step += int(check_if_o_surround(0, -1, list_id, str_id))
    step += int(check_if_o_surround(1, 0, list_id, str_id))
    step += int(check_if_o_surround(-1, 0, list_id, str_id))

    return step


total = 0
for item in range(7):
    for char in range(7):
        if board[item][char] == '.':
            total += find_steps(item, char)

print(total)
