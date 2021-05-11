import copy


# find index of 0 from the current state
def find_index_of_0(t_state):
    for i in range(4):
        for j in range(4):
            if t_state[i][j] == 0:
                ind = [i, j]
                return ind


# check if current state is goal state
def goal_test(curr_state):
    if curr_state == goal_state[0]:
        print('Goal state found!')
        # print Number of states processed to find the goal state
        print('Goal state found after examining {} states!'.format(len(close_list)))
        open_list.pop(0)
        close_list.append(curr_state)
        return True
    return False


#move the 0 up by one step if possible
def move_up(this_state, i, j):
    if 0 < i <= 3:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i-1][j]
        my_state[i-1][j] = temp
        if my_state not in close_list:
            open_list.insert(0, my_state)


# move the 0 down by one step if possible
def move_down(this_state, i, j):
    if 0 <= i < 3:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i+1][j]
        my_state[i+1][j] = temp
        if my_state not in close_list:
            open_list.insert(0, my_state)


# move the 0 left by one step if possible
def move_left(this_state, i, j):
    if 0 < j <= 3:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i][j-1]
        my_state[i][j-1] = temp
        if my_state not in close_list:
            open_list.insert(0, my_state)


# move the 0 right by one step if possible
def move_right(this_state, i, j):
    if 0 <= j < 3:
        my_state = copy.deepcopy(this_state)
        temp = my_state[i][j]
        my_state[i][j] = my_state[i][j+1]
        my_state[i][j+1] = temp
        if my_state not in close_list:
            open_list.insert(0, my_state)

#list containing initial state
initial_state = [[[1, 2, 6, 9], [4, 8, 10, 13], [11, 3, 7, 15], [14, 5, 12, 0]]]
#list containing goal state
goal_state = [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]]]


open_list = [initial_state[0]]
close_list = []

i = 1
#continue to process various states until either goal state
# is found or all states are exhausted
while len(open_list) > 0 and not goal_test(open_list[0]):
    check_currstate = open_list[0]
    print("Processing state {}: {}".format(i,check_currstate))
    i = i + 1
    open_list.pop(0)
    index = find_index_of_0(check_currstate)

    move_up(check_currstate, index[0], index[1])
    move_left(check_currstate, index[0], index[1])
    move_down(check_currstate, index[0], index[1])
    move_right(check_currstate, index[0], index[1])

    close_list.append(check_currstate)


# print the states present in the open list that would have been processed
# next in case if goal state was not found
print('Open list:')
for item in open_list:
    print(item)
