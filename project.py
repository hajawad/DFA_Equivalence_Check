#!/usr/bin/python

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


if __name__ == "__main__":
    __init__()
