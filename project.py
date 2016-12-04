def __init__():
    # just for test
    dfa1 = [[0, 1, 2, 3], [0, 1], None, [0], [2]]
    dfa2 = [[4, 5, 6], [0, 1], None, [4], [6]]

    dfa = cross_product(dfa1, dfa2)

    print("states: ", dfa[0])
    print("alphabets: ", dfa[1])
    print("transitions: : ", dfa[2])
    print("initial state: ", dfa[3])
    print("accept state: ", dfa[4])


# TODO: transition
def cross_product(first_dfa, second_dfa):
    # states, alphabets, transitions, initial state, accept state

    dfa1 = (first_dfa[0], first_dfa[1], first_dfa[2], first_dfa[3], first_dfa[4])
    dfa2 = (second_dfa[0], second_dfa[1], second_dfa[2], second_dfa[3], second_dfa[4])

    dfa = []
    states = []
    alphabets = []
    transitions = []
    accept_state = []
    initial_state = (dfa1[3], dfa2[3])

    for s1 in dfa1[0]:
        for s2 in dfa2[0]:
            states.append((s1, s2))

    for i in dfa1[1]:
        if i not in alphabets:
            alphabets.append(i)

    for i in dfa2[1]:
        if i not in alphabets:
            alphabets.append(i)

    for i in states:
        if i[0] in dfa1[4] or i[1] in dfa2[4]:
            accept_state.append((i[0], i[1]))

    dfa.append(states)
    dfa.append(alphabets)
    dfa.append(transitions)
    dfa.append(initial_state)
    dfa.append(accept_state)

    return dfa


def intersect_dfa(first_dfa, second_dfa):
    int_dfa = [[], [], [], [], []]
    for i in first_dfa[0]:
        for y in second_dfa[0]:
            int_dfa[0].append((i, y))

    for i in first_dfa[1]:
        for y in second_dfa[1]:
            int_dfa[1].append(i)
            if (i == j):
                continue
            int_dfa[1].append(j)
    int_dfa[3].append((first_dfa[3], second_dfa[3]))
    int_dfa[4].append((first_dfa[4], second_dfa[4]))

    return int_dfa


def complement(dfa):
    for i in dfa[0]:
        for y in dfa[4]:
            if (i == y):
                continue
            dfa[4].append(i)
    return dfa


def checkEmpty(dfa):
    if dfa[4] == None:
        return True

    if dfa[3] == dfa[4]:
        return False

    list = []
    visited_states = []
    list.append(dfa[3])

    while (list != None):
        for i in dfa[2]:
            if i[0][0] == list[0]:
                if i[1] not in visited_states and i[1] not in list:
                    for j in dfa[4]:
                        if i[1] == dfa[4]:
                            return False
                        list.append(i[1])
        visited_states.append(list[0])
        list.pop(0)
    return True


def union(first_dfa, second_dfa):
    int_dfa = [[], [], [], [], []]
    for i in first_dfa[0]:
        for y in second_dfa[0]:
            int_dfa[0].append((i, y))

    for i in first_dfa[1]:
        for j in second_dfa[1]:
            int_dfa[1].append(i)
            if (i == j):
                continue
            int_dfa[1].append(j)
    int_dfa[3].append((first_dfa[3], second_dfa[3]))

    for i in first_dfa[4]:
        int_dfa[4].append(i)
    for i in second_dfa[4]:
        int_dfa[4].append(i)

    return int_dfa


if __name__ == "__main__":
    __init__()