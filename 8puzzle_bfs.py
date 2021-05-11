import copy


# find index of 0 from the current state
def find_index_of_0(t_state):
    for i in range(3):
        for j in range(3):
            if t_state[i][j] == 0:
                ind = [i, j]
                return ind


# check if current state is the goal state
def goal_test(curr_state):
    if curr_state == goal_state[0]:
        print('Goal state found!')
        open_list.pop(0)
        close_list.append(curr_state)
        return True
    return False


# move the 0 up by one step if possible
def move_up(this_state, i, j):
    if 0 < i <= 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i-1][j]
        my_state[i-1][j] = temp
        # print(my_state)
        if my_state not in close_list:
            open_list.append(my_state)


# move the 0 down by one step if possible
def move_down(this_state, i, j):
    if 0 <= i < 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i+1][j]
        my_state[i+1][j] = temp
        # return [i+1, j]
        if my_state not in close_list:
            open_list.append(my_state)


# move the 0 left by one step if possible
def move_left(this_state, i, j):
    if 0 < j <= 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i][j-1]
        my_state[i][j-1] = temp
        if my_state not in close_list:
            open_list.append(my_state)


# # move the 0 right by one step if possible
def move_right(this_state, i, j):
    if 0 <= j < 2:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i][j+1]
        my_state[i][j+1] = temp
        if my_state not in close_list:
            open_list.append(my_state)


initial_state = [[[1, 2, 3], [8, 0, 4], [7, 6, 5]]]
goal_state = [[[2, 8, 1], [0, 4, 3], [7, 6, 5]]]


open_list = [initial_state[0]]
close_list = []

#continue to process various states until either goal state
# is found or all states are exhausted
while len(open_list) > 0 and not goal_test(open_list[0]):
    check_currstate = open_list[0]
    print("Currently Processing State: {}".format(check_currstate))
    open_list.pop(0)
    index = find_index_of_0(check_currstate)
    move_up(check_currstate, index[0], index[1])
    move_right(check_currstate, index[0], index[1])
    move_down(check_currstate, index[0], index[1])
    move_left(check_currstate, index[0], index[1])
    close_list.append(check_currstate)

# print Number of states processed to find the goal state
print('Goal state found after examining {} states!'.format(len(close_list)))
# print the states present in the open list that would have been processed
# next in case if goal state was not found
print('Open list:')
for item in open_list:
    print(item)
