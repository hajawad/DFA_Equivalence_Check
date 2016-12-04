#!/usr/bin/python
# DFA
class DFA(object):
    states= []
    alphabets=[]
    transitions=[]
    initialState=None
    acceptState=[]
    def __init__(self,s,a,t,i,accept):
        self.states=s
        self.alphabets=a
        self.transitions=t
        self.initialState=i
        self.acceptState = accept

   # def makeDfa(self,s,a,t,i,accept):
   #     dfa=DFA(s,a,t,i,accept)
   #     return dfa




    #gives the next state given an input.
    def findNext(self,state,alpha):
        for i in self.transitions:
            for j in i:
                if j[0] ==state and j[1]==alpha:
                    return i[1]
        return -1

    #Runs a string in a DFA and returns accept or reject
    def simOnInput(self,string):
        currentState= self.initialState
        done=False
        for i in string:
            done =False
            if i not in self.alphabets:
                return False
            currentState=self.findNext(currentState,i)
        if currentState in self.acceptState:
            return True
        return False
    def printDFA(self):
        print("states: ", self.states)
        print("alphabets: ", self.alphabets)
        print("transitions: : ", self.transitions)
        print("initial state: ", self.initialState)
        print("accept state: ", self.acceptState)


def crossTransition(transitions, transitions1):
    newTransition=[]
    for i in transitions:
        for j in transitions1:
            if i[0][1]==j[0][1]:
                newTransition.append([[i[0][0]+j[0][0],i[0][1]],i[1]+j[1]])

    return newTransition

######################################
#########union###################
####### Takes in two dfa's##########
###### Outputs union##############
#################################

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
            alphabets.append(i + j)
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

    dfa=DFA(states,alphabets,transitions,startState,acceptState)
    return dfa
######################################
#########Intersect###################
####### Takes in two dfa's##########
###### Outputs intersect##############
#################################
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
    transitions=crossTransition(dfa1.transitions,dfa2.transitions)
    for i in dfa1.initialState:
        for j in dfa2.initialState:
            startState.append(i+j)

    for i in dfa1.acceptState:
        for j in dfa2.acceptState:
            acceptState.append(i+j)

    dfa=DFA(states,alphabets,transitions,startState,acceptState)
    return dfa

########################################################
#########complement######################################
####### Takes in a dfa and complements it#################
###### Outputs a happy DFA (complemented one)##############
###########################################################
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

########################################################
#################Empty################################
####### checks if a language is empty#################
###### Outputs true if empty or false if not##############
###########################################################

def empty(dfa):
    if(dfa.acceptState==[] or dfa.acceptState==None):
        return True
    marked=[]
    queue = []
    queue.append(dfa.initialState)
    marked.append(dfa.initialState)
    while(len(queue)!=0):
        for i in dfa.transitions:
            if i[0][0]==queue[0] and i[1] not in marked:
                if i[1] in dfa.acceptState:
                    return False
                queue.append(i[1])
                marked.append(i[1])
        queue.pop(0)
    return False


##Inital method MAIN!!!
def __init__():

    #dfa1 = DFA(['q1', 'q2', 'q3', 'q4'], [0, 1],[[['q1',1],'q2'],[['q2',0],'q1'],[['q1',0],'q1'],[['q2',1],'q3']],
             #[['q3',1],'q4'],[['q3',0],'q3'],[['q4',1],'q4'],[['q4',0],'q4']],['q1'], ['q3'])
    #dfa1.printDFA()

    #dfa2 = DFA(['k1', 'k2', 'k3'], [0, 1], #states and alphabets
            #[[['k1',1],'k2'],[['k2',0],'k1'],[['k1',0],'k1'],[['k2',1],'k3'],[['k3',1],'k3'],[['k3',0],'k3']], #transitions
            #['k1'], ['k3']) #start and accept state




    dfaa1 = DFA(['q1','q2','q3','q4'],['a','b'],[[['q1','a'],'q2'],[['q1','b'],'q1'],[['q2','a'],'q2'],[['q2','b'],'q3'],[['q3','a'],'q3'],[['q3','b'],'q4'],[['q4','a'],'q4'],[['q4','b'],'q4']],['q1'],['q4'])
    dfaa2 = DFA(['k1', 'k2', 'k3', 'k4'], ['a', 'b'],\
                [[['k1', 'a'], 'k2'], [['k1', 'b'], 'k1'], [['k2', 'a'], 'k2'], [['k2', 'b'], 'k3'], [['k3', 'a'], 'k3'],\
                 [['k3', 'b'], 'k4'], [['k4', 'a'], 'k4'], [['k4', 'b'], 'k4']], ['k1'], ['k4'])

    print(dfaa1)
    print(dfaa2)


    dfaa1c = complement(dfaa1)
    dfaa2c = complement(dfaa2)
    dfaa12c = intersect(dfaa1, dfaa2c)
    dfaa21c = intersect(dfaa2, dfaa1c)
    dfaau = union(dfaa12c, dfaa21c)

    print("Equality check: ", empty(dfaau))

    #dfa2.printDFA()
    #dfa1c = complement(dfa1)
    #dfa2c = complement(dfa2)
    #dfa12c = intersect(dfa1,dfa2c)
    #dfa21c = intersect(dfa2,dfa1c)
    #dfau = union(dfa12c,dfa21c)
    #print(empty(dfau))
    #dfau.printDFA()

    #print("states: ", dfa[0])
    #print("alphabets: ", dfa[1])
    #print("transitions: : ", dfa[2])
    #print("initial state: ", dfa[3])
    #print("accept state: ", dfa[4])

# TODO: transition
#def cross_product(first_dfa, second_dfa):
#    # states, alphabets, transitions, initial state, accept state
#    dfa1 = (first_dfa[0], first_dfa[1], first_dfa[2], first_dfa[3], first_dfa[4])
#    dfa2 = (second_dfa[0], second_dfa[1], second_dfa[2], second_dfa[3], second_dfa[4])
#
#    dfa = []
#    states = []
#    alphabets = []
#    transitions = []
#    accept_state = []
#    initial_state = (dfa1[3], dfa2[3])
#
#    for s1 in dfa1[0]:
#        for s2 in dfa2[0]:
#            states.append((s1, s2))
#
#    for i in dfa1[1]:
#        if i not in alphabets:
#            alphabets.append(i)
#
#    for i in dfa2[1]:
#        if i not in alphabets:
#            alphabets.append(i)
#
#    for i in states:
#        if i[0] in dfa1[4] or i[1] in dfa2[4]:
#            accept_state.append((i[0], i[1]))
#
#    dfa.append(states)
#    dfa.append(alphabets)
#    dfa.append(transitions)
#    dfa.append(initial_state)
#    dfa.append(accept_state)
#
#    return dfa
#
#
#def intersect_dfa(first_dfa,second_dfa):
#    int_dfa=[[],[],[],[],[]]
#    for i in first_dfa[0]:
#        for y in second_dfa[0]:
#            int_dfa[0].append((i,y))
#
#    for i in first_dfa[1]:
#        for j in second_dfa[1]:
#            int_dfa[1].append(i)
#            if (i==j):
#                continue
#            int_dfa[1].append(j)
#    int_dfa[3].append((first_dfa[3],second_dfa[3]))
#    int_dfa[4].append((first_dfa[4],second_dfa[4]))
#
#    return int_dfa
#
#def complement(dfa):
#    for i in dfa[0]:
#        for y in dfa[4]:
#            if (i==y):
#                continue
#            dfa[4].append(i)
#    return dfa
#
#def union (first_dfa, second_dfa):
#    int_dfa=[[],[],[],[],[]]
#    for i in first_dfa[0]:
#        for j in second_dfa[0]:
#            int_dfa[0].append((i,j))
#
#    for i in first_dfa[1]:
#        for j in second_dfa[1]:
#            int_dfa[1].append(i)
#            if (i==j):
#                continue
#            int_dfa[1].append(j)
#    int_dfa[3].append((first_dfa[3],second_dfa[3]))
#
#    for i in first_dfa[4]:
#        int_dfa[4].append(i)
#    for i in second_dfa[4]:
#        int_dfa[4].append(i)
#
#
#    return int_dfa

if __name__ == "__main__":
    __init__()