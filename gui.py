#!/usr/bin/python

import Tkinter
import dfa_project
import tkFont
import tkMessageBox

dfa1_transitions = []
dfa2_transitions = []

text_fields = []

#######resets all entry fields#######
def reset():
    E1.delete(0,'end')
    E2.delete(0,'end')
    E3.delete(0, 'end')
    E4.delete(0, 'end')
    E5.delete(0, 'end')
    E6.delete(0, 'end')
    E7.delete(0, 'end')
    E8.delete(0, 'end')
    E9.delete(0, 'end')
    E10.delete(0, 'end')
    E11.delete(0, 'end')
    E12.delete(0, 'end')
    E13.delete(0, 'end')
    E14.delete(0, 'end')
    del dfa1_transitions[:]
    del dfa2_transitions[:]
    status.configure(text=" ")

def create_transitions_list1():
    dfa1_transitions.append([[E9.get(),E11.get()],E10.get()])
    E9.delete(0, 'end')
    E10.delete(0, 'end')
    E11.delete(0, 'end')
    print(dfa1_transitions)

def create_transitions_list2():
    dfa2_transitions.append([[E12.get(), E14.get()], E13.get()])
    E12.delete(0, 'end')
    E13.delete(0, 'end')
    E14.delete(0, 'end')
    print(dfa2_transitions)

top = Tkinter.Tk()
default_font = tkFont.Font(family="Times",size=13,weight="bold")
header_font = tkFont.Font(family="Helvetica",size=23,weight="bold")
dfa1_frame = Tkinter.Frame(top)
dfa1_frame.pack(side=Tkinter.LEFT)
dfa2_frame = Tkinter.Frame(top)
dfa2_frame.pack(side=Tkinter.RIGHT)

Label = Tkinter.Label(dfa1_frame, text="DFA1 ",font=header_font)
Label.pack(side=Tkinter.TOP)

Label1 = Tkinter.Label(dfa2_frame, text="DFA2 ",font=header_font)
Label1.pack(side=Tkinter.TOP)

#######TEXT FIELDS FOR DFAs STATES######
frame1 = Tkinter.Frame(dfa1_frame)
frame1.pack(side=Tkinter.TOP)
L1 = Tkinter.Label(frame1, text="STATES: ",font=default_font)
L1.pack(side=Tkinter.LEFT)
E1 = Tkinter.Entry(frame1, bd=5)
E1.pack(side=Tkinter.LEFT)
text_fields.append(E1.get())

frame2 = Tkinter.Frame(dfa2_frame)
frame2.pack(side=Tkinter.TOP)

L2 = Tkinter.Label(frame2, text="STATES: ",font=default_font)
L2.pack(side=Tkinter.LEFT)
E2 = Tkinter.Entry(frame2, bd=5)
E2.pack(side=Tkinter.RIGHT)
text_fields.append(E2.get())


#######TEXT FIELDS FOR DFAs ALPHABETS########
frame3 = Tkinter.Frame(dfa1_frame)
frame3.pack(side=Tkinter.TOP)
L3 = Tkinter.Label(frame3, text="ALPHABETS: ",font=default_font)
L3.pack(side=Tkinter.LEFT)
E3 = Tkinter.Entry(frame3, bd=5)
E3.pack(side=Tkinter.LEFT)
text_fields.append(E3.get())

frame4 = Tkinter.Frame(dfa2_frame)
frame4.pack(side=Tkinter.TOP)
L4 = Tkinter.Label(frame4, text="ALPHABETS: ",font=default_font)
L4.pack(side=Tkinter.LEFT)
E4 = Tkinter.Entry(frame4, bd=5)
E4.pack(side=Tkinter.RIGHT)
text_fields.append(E4.get())




######TEXT FIELDS FOR DFAs INITIAL STATE########
frame5 = Tkinter.Frame(dfa1_frame)
frame5.pack(side=Tkinter.TOP)
L5 = Tkinter.Label(frame5, text="INIT. STATE: ",font=default_font)
L5.pack(side=Tkinter.LEFT)
E5 = Tkinter.Entry(frame5, bd=5)
E5.pack(side=Tkinter.LEFT)
text_fields.append(E5.get())

frame6 = Tkinter.Frame(dfa2_frame)
frame6.pack(side=Tkinter.TOP)
L6 = Tkinter.Label(frame6, text="INIT. STATE: ",font=default_font)
L6.pack(side=Tkinter.LEFT)
E6 = Tkinter.Entry(frame6, bd=5)
E6.pack(side=Tkinter.RIGHT)
text_fields.append(E6.get())

#######TEXT FIELDS FOR DFAs FINAL STATE(s)#########
frame7 = Tkinter.Frame(dfa1_frame)
frame7.pack(side=Tkinter.TOP)
L7 = Tkinter.Label(frame7, text="FINAL STATE: ",font=default_font)
L7.pack(side=Tkinter.LEFT)
E7 = Tkinter.Entry(frame7, bd=5)
E7.pack(side=Tkinter.LEFT)
text_fields.append(E7.get())

frame8 = Tkinter.Frame(dfa2_frame)
frame8.pack(side=Tkinter.TOP)
L8 = Tkinter.Label(frame8, text="FINAL STATE: ",font=default_font)
L8.pack(side=Tkinter.LEFT)
E8 = Tkinter.Entry(frame8, bd=5)
E8.pack(side=Tkinter.RIGHT)
text_fields.append(E8.get())

######TEXT FIELDS FOR DFA1 TRANSITIONS########
frame9 = Tkinter.Frame(dfa1_frame)
frame9.pack(side=Tkinter.TOP)
L9 = Tkinter.Label(frame9, text="TRANSITION: ",font=default_font)
L9.pack(side=Tkinter.LEFT)
L10 = Tkinter.Label(frame9,text="FROM: ",font=default_font)
L10.pack(side=Tkinter.LEFT)
E9 = Tkinter.Entry(frame9, bd=5,width="3")
E9.pack(side=Tkinter.LEFT)
L11 = Tkinter.Label(frame9,text="TO: ",font=default_font)
L11.pack(side=Tkinter.LEFT)
E10 = Tkinter.Entry(frame9, bd=5,width="3")
E10.pack(side=Tkinter.LEFT)
L12 = Tkinter.Label(frame9,text="ON: ",font=default_font)
L12.pack(side=Tkinter.LEFT)
E11 = Tkinter.Entry(frame9, bd=5,width="3")
E11.pack(side=Tkinter.LEFT)
ADD_TRANSITION = Tkinter.Button(frame9, text="ADD TRANSITION",font=default_font,command=create_transitions_list1)
ADD_TRANSITION.pack(side=Tkinter.LEFT)

######TEXT FIELDS FOR DFA2 TRANSITIONS########
frame10 = Tkinter.Frame(dfa2_frame)
frame10.pack(side=Tkinter.TOP)
L13 = Tkinter.Label(frame10, text="TRANSITION: ",font=default_font)
L13.pack(side=Tkinter.LEFT)
L14 = Tkinter.Label(frame10,text="FROM: ",font=default_font)
L14.pack(side=Tkinter.LEFT)
E12 = Tkinter.Entry(frame10, bd=5,width="3")
E12.pack(side=Tkinter.LEFT)
L15 = Tkinter.Label(frame10,text="TO: ",font=default_font)
L15.pack(side=Tkinter.LEFT)
E13 = Tkinter.Entry(frame10, bd=5,width="3")
E13.pack(side=Tkinter.LEFT)
L16 = Tkinter.Label(frame10,text="ON: ",font=default_font)
L16.pack(side=Tkinter.LEFT)
E14 = Tkinter.Entry(frame10, bd=5,width="3")
E14.pack(side=Tkinter.LEFT)
ADD_TRANSITION1 = Tkinter.Button(frame10, text="ADD TRANSITION",font=default_font, command=create_transitions_list2)
ADD_TRANSITION1.pack(side=Tkinter.LEFT)



def checkEquality():


    dfa1_s = E1.get().split(",")
    dfa1_a = E3.get().split(",")
    dfa1_i = E5.get().split(",")
    dfa1_f = E7.get().split(",")

    dfa1 = dfa_project.DFA(dfa1_s,dfa1_a,dfa1_transitions,dfa1_i,dfa1_f)

    dfa2_s = E2.get().split(",")
    dfa2_a = E4.get().split(",")
    dfa2_i = E6.get().split(",")
    dfa2_f = E8.get().split(",")

    dfa2 = dfa_project.DFA(dfa2_s, dfa2_a, dfa2_transitions, dfa2_i, dfa2_f)
    print("DFA1 States: "+ str(dfa1.states))
    print("DFA1 Alphabets: "+ str(dfa1.alphabets))
    print("DFA1 Transition: "+ str(dfa1.transitions))
    print("DFA1 initial state: "+ str(dfa1.initialState))
    print("DFA1 accept state: "+ str(dfa1.acceptState))

    print("DFA2 States: "+ str(dfa2.states))
    print("DFA2 Alphabets: "+ str(dfa2.alphabets))
    print("DFA2 Transition: "+ str(dfa2.transitions))
    print("DFA2 initial state: "+ str(dfa2.initialState))
    print("DFA2 accept state: "+ str(dfa2.acceptState))
    print(dfa1.isValid())
    print(dfa2.isValid())
    if (dfa1.isValid() and dfa2.isValid()):
        dfa1_complement = dfa_project.complement(dfa1)
        dfa2_complement = dfa_project.complement(dfa2)
        dfa12c_intersect = dfa_project.intersect(dfa1, dfa2_complement)
        dfa21c_intersect = dfa_project.intersect(dfa2, dfa1_complement)
        dfaau = dfa_project.union(dfa12c_intersect, dfa21c_intersect)

        if(dfa_project.empty(dfaau) == True):
            status.configure(text="DFA1 and DFA2 are EQUAL!", font=header_font)
        else:
            status.configure(text="DFA1 and DFA2 are not EQUAL!", font=header_font)
    else:
        if(dfa1.isValid() == False and dfa1.isValid() == False):
            tkMessageBox.showinfo("DFA1 and DFA2 are invalid","DFA1 and DFA2 have an incorrect DFA format")
        elif(dfa1.isValid() == False):
            tkMessageBox.showinfo("DFA1 is invalid", "DFA1 has an incorrect DFA format")
        else:
            tkMessageBox.showinfo("DFA2 is invalid", "DFA2 has an incorrect DFA format")





#######CREATE THE BOTTOM BUTTONS#########
frame6 = Tkinter.Frame(top)
frame6.pack(side=Tkinter.TOP)
CHECK_EQUAL = Tkinter.Button(frame6, text="CHECK EQUALITY",font=default_font,command=checkEquality)
CHECK_EQUAL.pack(side=Tkinter.LEFT)

RESET = Tkinter.Button(frame6,text="RESET",font=default_font,command= reset)
RESET.pack(side=Tkinter.RIGHT)

frame11 = Tkinter.Frame(top)
frame11.pack(side=Tkinter.TOP)
status = Tkinter.Label(frame11, text=" ", font=default_font,pady="50")
status.pack(side=Tkinter.BOTTOM)

top.mainloop()