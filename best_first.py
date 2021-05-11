import copy


def find_index_of_0(t_state):
    for i in range(3):
        for j in range(3):
            if t_state[i][j] == 0:
                ind = [i, j]
                return ind


def goal_test(curr_state):
    if curr_state == goal_state[0]:
        print('Goal state found!')
        open_list.pop(0)
        close_list.append(curr_state)
        return True
    return False


def move_up(this_state, i, j):
    if 0 < i <= 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i-1][j]
        my_state[i-1][j] = temp
        # print(my_state)
        if my_state not in close_list:
            # open_list.insert(0, my_state)
            return my_state


def move_down(this_state, i, j):
    if 0 <= i < 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i+1][j]
        my_state[i+1][j] = temp
        # return [i+1, j]
        if my_state not in close_list:
            # open_list.insert(0, my_state)
            return my_state


def move_left(this_state, i, j):
    if 0 < j <= 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i][j-1]
        my_state[i][j-1] = temp
        if my_state not in close_list:
            # open_list.insert(0, my_state)
            return my_state


def move_right(this_state, i, j):
    if 0 <= j < 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i][j+1]
        my_state[i][j+1] = temp
        if my_state not in close_list:
            # open_list.insert(0, my_state)
            return my_state


def heuristic(st):
    count = 0
    for i in range(3):
        for j in range(3):
            if st[i][j] != goal_state[0][i][j]:
                count = count + 1
    return count, st


def comp(e):
    return e[0]


initial_state = [[[2, 0, 3], [1, 8, 4], [7, 6, 5]]]
goal_state = [[[1, 2, 3], [8, 0, 4], [7, 6, 5]]]

open_list = [initial_state[0]]
close_list = []

while len(open_list) > 0 and not goal_test(open_list[0]):
    curr_state = open_list[0]
    open_list.pop(0)
    index = find_index_of_0(curr_state)
    a = move_up(curr_state, index[0], index[1])
    b = move_right(curr_state, index[0], index[1])
    c = move_down(curr_state, index[0], index[1])
    d = move_left(curr_state, index[0], index[1])
    compare = []
    if a:
        compare.append(heuristic(a))
    if b:
        compare.append(heuristic(b))
    if c:
        compare.append(heuristic(c))
    if d:
        compare.append(heuristic(d))
    compare.sort(key=comp, reverse=True)
    for x in compare:
        open_list.insert(0, x[1])
    compare.clear()
    close_list.append(curr_state)

print("Open list:\n",open_list)
print("Closed List:\n",close_list)
print("Goal State found after examining {} states!".format(len(close_list)))
