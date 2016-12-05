# Authors: Hashim Al Jawad, Ibrahim Al Mubarak
# Course: CS357
# Date: 12/05/2016
# Description: a program to check whether two DFAs have the same language or not.

#!/usr/bin/python


##############################################################
# DFA
# This class represents a determinstic finite automaton.
class DFA(object):
    states = []
    alphabets = []
    transitions = []
    initialState = None
    acceptState = []
    ##############################################################
    # __init__(self,s,a,t,i,accept)
    # This function creates an instance of the DFA class.
    # inputs: s - a list of states (e.g. ['q1','q2','q3'])
    #         a - a list of the alphabets (e.g. ['a','b'])
    #         t - a list of transitions (e.g. [['q1',a],'q2']
    #         i - initial state (list) (e.g. ['q0'])
    #         accept - a list of all the accept states (e.g. ['q2','q3'])
    def __init__(self,s,a,t,i,accept):
        self.states = s
        self.alphabets = a
        self.transitions = t
        self.initialState = i
        self.acceptState = accept


    ##############################################################
    # findNext(self,state,alpha)
    # This function returns the next state given a state and an alphabet
    # inputs: state - current state
    #         alpha - a given alphabet
    # return: next state
    def findNext(self,state,alpha):
        for i in self.transitions:
            for j in i:
                if j[0] == state and j[1] == alpha:
                    return i[1]
        return -1

    ##############################################################
    # simOnInput(self,string)
    # This function simulates a given string in a DFA.
    # input: string - the string to-be simulated
    # return: true or false (accept or reject)
    def simOnInput(self,string):
        currentState = self.initialState
        done = False
        for i in string:
            done =False
            if i not in self.alphabets:
                return False
            currentState=self.findNext(currentState,i)
        if currentState in self.acceptState:
            return True
        return False

    ##############################################################
    # printDFA(self)
    # This function prints information about the dfa to the console.
    # used for debugging only.
    def printDFA(self):
        print("states: ", self.states)
        print("alphabets: ", self.alphabets)
        print("transitions: : ", self.transitions)
        print("initial state: ", self.initialState)
        print("accept state: ", self.acceptState)


    ##############################################################
    # isValid(self)
    # This function checks if the dfa is valid.
    # return: true if valid. false if not.
    def isValid(self):
        # checks for missing parts of a dfa
        if self.alphabets == [] or self.transitions == [] or self.states == [] or self.initialState == None or self.initialState == []:
            return False
        count = 0
        alpha = []
        # checks the transition for validity
        for m in self.states:
            alpha = list(self.alphabets)
            for i in self.transitions:
                if i[0][0] == m:
                    count = count + 1
                    # checks if state has a transition with a non valid alphabet
                    if i[0][1] not in alpha:
                        return False
                    alpha.remove(i[0][1])
                    # checks if there is more transition than there are alphabetes
                    if count > len(self.alphabets):
                        return False
                    # checks for non valid state
                    if i[0][0] not in self.states:
                        return False
            # checks whether there is n number of transtions where n = number of alphabets
            if count < len(self.alphabets):
                return False
            if count == len(self.alphabets):
                count = 0
        return True

##############################################################
# crossTransition(dfa1, dfa2)
# This function create a new list of transition that contains
# a new transition table after performing a cross product on two DFAs.
# inputs: transition - list of transitions for dfa1
#         transition1 - list of transitions for dfa2
# return: a list of transitions for dfa1 and dfa2 after performing a cross product.
def crossTransition(transitions, transitions1):
    newTransition=[]
    for i in transitions:
        for j in transitions1:
            if i[0][1] == j[0][1]:
                newTransition.append([[i[0][0]+j[0][0],i[0][1]],i[1]+j[1]])

    return newTransition



##############################################################
# union(dfa1, dfa2)
# This function constructs the union of two DFAs using the cross product.
# inputs: dfa1 - first dfa
#         dfa2 - second dfa
# return: the union of dfa1 and dfa2
def union(dfa1, dfa2):
    states=[]
    alphabets=[]
    transitions=[]
    startState=[]
    acceptState=[]

    for i in dfa1.states:
        for j in dfa2.states:
            states.append(i+j)

    for i in dfa1.alphabets:
        for j in dfa2.alphabets:
            if(str(i)+ str(j)) not in alphabets:
                alphabets.append(str(i)+ str(j))
    transitions = crossTransition(dfa1.transitions,dfa2.transitions)
    for i in dfa1.initialState:
        for j in dfa2.initialState:
            startState.append(i+j)

    for i in dfa1.acceptState:
        for j in dfa2.acceptState:
            for f in states:
                if (i in f or j in f) and f not in acceptState:
                    acceptState.append(f)

            acceptState.append(i+j)

    dfa = DFA(states,alphabets,transitions,startState,acceptState)
    return dfa



##############################################################
# intersect(dfa1, dfa2)
# This function constructs the intersection of two DFAs using
# the cross product.
# inputs: dfa1 - first dfa
#         dfa2 - second dfa
# return: the intersection of dfa1 and dfa2
def intersect(dfa1, dfa2):
    states=[]
    alphabets=[]
    transitions=[]
    startState=[]
    acceptState=[]

    for i in dfa1.states:
        for j in dfa2.states:
            states.append(i+j)

    for i in dfa1.alphabets:
        for j in dfa2.alphabets:
            alphabets.append(i + j)
    transitions= crossTransition(dfa1.transitions,dfa2.transitions)
    for i in dfa1.initialState:
        for j in dfa2.initialState:
            startState.append(i+j)

    for i in dfa1.acceptState:
        for j in dfa2.acceptState:
            acceptState.append(i+j)

    dfa=DFA(states,alphabets,transitions,startState,acceptState)
    return dfa

##############################################################
# complement(dfa)
# This function takes in a dfa and constructs the complement of it.
# inputs: dfa - a list that contains information about the dfa.
# return: a happy DFA (complemented one)
def complement(dfa):
    states=dfa.states
    alphabets=dfa.alphabets
    transitions=dfa.transitions
    startState=dfa.initialState
    acceptState=[]

    for i in states:
        if i not in dfa.acceptState:
            acceptState.append(i)

    dfa=DFA(states,alphabets,transitions,startState,acceptState)
    return dfa


##############################################################
# empty(dfa)
# This function takes in a dfa and checks if its language is empty.
# return: true if empty. false if not.
def empty(dfa):

    if(dfa.acceptState==[] or dfa.acceptState==None):
        return True
    marked=[]
    queue = []
    queue.append(dfa.initialState[0])
    marked.append(dfa.initialState[0])
    while(len(queue)!=0):
        for i in dfa.transitions:
            if i[0][0]==queue[0]and i[1] not in marked:
                if i[1] in dfa.acceptState:
                    return False
                queue.append(i[1])
                marked.append(i[1])
        queue.pop(0)
    return True