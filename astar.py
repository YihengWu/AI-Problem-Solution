import heapq

repeated_states = []
heap = [(6,0,(3,3,1),[(3,3,1)],[])]
boat_action = [(1,0),(2,0),(0,1),(0,2),(1,1)]

#my heuristic function is simple, just choose the state that makes the sum
#of cat and dog on the left side of river as small as possible

def astar_search():
    k = 0
    while True:
        a_state = heapq.heappop(heap)
        state = a_state[2]
        if state[0]==0 and state[1]==0 and state[2]==0:
            return a_state

        for x in boat_action:
            if boat_action_legal(state, x):
                if state[2] == 1:
                    a,b,c = state[0]-x[0], state[1]-x[1],0
                else:
                    a,b,c = state[0]+x[0], state[1]+x[1],1
                k += 1
                new_state_seq = list(a_state[3])
                new_state_seq.append((a,b,c))
                new_boat_seq = list(a_state[4])
                new_boat_seq.append(x)

                new_heap_element = (a+b, k, (a,b,c), new_state_seq, new_boat_seq)
                if (a,b,c) in repeated_states:
                    continue
                else:
                    repeated_states.append((a,b,c))
                    heapq.heappush(heap, new_heap_element)

def boat_action_legal(state, x):
    cat1, dog1 = state[0],state[1]
    cat0, dog0 = 3-cat1, 3-dog1
    if state[2] == 1:
        cat_left1, dog_left1 = cat1-x[0], dog1-x[1]
        cat_left0, dog_left0 = cat0+x[0], dog0+x[1]
    else:
        cat_left1, dog_left1 = cat1+x[0], dog1+x[1]
        cat_left0, dog_left0 = cat0-x[0], dog0-x[1]
    if cat_left1>=0 and dog_left1>=0 and cat_left0>=0 and dog_left0>=0:
        if (cat_left1 == 0 or cat_left1>=dog_left1) and (cat_left0 == 0 or cat_left0>=dog_left0):
            return True
        else:
            return False
    else:
        return False



if __name__ == '__main__':
    result = astar_search()
    states = result[3]
    boat_states = result[4]
    print("A state tuple (a,b,c) means a cats and b dogs are on the left side of the river. \nIf c = 1, the boat is on the left side. Otherwise, the boat is on the right side.\n")
    for i in range(len(states)-1):
        if i == 0:
            print("initial state: ", states[0])
            print("action0: %d Cats on board and %d dogs on board" %(boat_states[0][0], boat_states[0][1]))
        else:
            print("state%d: " %(i), states[i])
            print("action%d: %d Cats on board and %d dogs on board" %(i, boat_states[i][0], boat_states[i][1]))
    print("goal:", states[len(states)-1])
