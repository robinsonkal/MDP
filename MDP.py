import random




def listoflists(matrix):##function that converts the matrix input into the matrix list
    matrixlist=[]
    counter=0
    rowlist=[]
    num=""

    for i in matrix:
        counter+=1
        if i.isdigit() or counter==len(matrix):
            num=num+i
        if i==" ":
            rowlist.append(int(num))
            num=""
        if i=="/" or counter==len(matrix):
            rowlist.append(int(num))
            matrixlist.append(rowlist)
            rowlist=[]
            num=""
    return matrixlist

class MDP():

    def __init__( self, grid ):

        ## In this assignment, there is one state per space in the grid.
        ## It is not required that you explicitly represent the states, but
        ## you may.  You are also given the transition probabilities.  Since
        ## the number of states is not constant (we will use different inputs),
        ## you may use a function (stub below) to calculate them.  For instance,
        ## if you start in a state on the left edge of the grid and move left,
        ## your program should realize that the agent should stay in the same
        ## state as a result.  The rewards for your MDP are contained in the
        ## input.
        self.values=grid

        ## Set of possible actions
        self.A = {'^':0, 'v':0, '>':0, '<':0}
        self.B = ['^','v','>','<']
        self.U=[]
        self.U1=[]
        self.expectedvalue=[]
        self.value_iteration()
        self.get_policy()

        ## An attribute to store state utility values.  You do not have to use
        ## a dictionary, but it helps keep the code clear.



    def expected_value( self, s ):
        ev=[]
        evup=self.A['^']*.70+self.A['>']*.1+self.A['<']*.1+self.A['v']*.1
        ev.append(evup)
        evdown=self.A['^']*.10+self.A['>']*.1+self.A['<']*.1+self.A['v']*.7
        ev.append(evdown)
        evright=self.A['^']*.10+self.A['>']*.7+self.A['<']*.1+self.A['v']*.1
        ev.append(evright)
        evleft=self.A['^']*.10+self.A['>']*.1+self.A['<']*.7+self.A['v']*.1
        ev.append(evleft)
        #print(ev,"EV")
        highest_expected_value=max(ev)
        counter=0
        check=0
        for i in ev:
            if i==highest_expected_value and check!=1:
                #print(highest_expected_value,"Stuff begins here")
                #print(counter)
                #print(self.B[counter])
                self.expectedvalue.append(self.B[counter])
                #print(self.expectedvalue)
                check=1
            counter+=1
        counter=0
        check=0

        ev=[]


        return highest_expected_value
        ## Return the probability of moving to state sprime after taking action
        ## a in state s.  If sprime is unreachable from s, return 0.

    def value_iteration( self ):
        highestnumrow=max(self.values)##Everything before a certain point is just generating values for later
        highestnum=max(highestnumrow)
        for i in range(len(self.values)):
            self.U.append(0)
        for o in self.values:
            self.U1.append(o)
        numberofrows=0
        m=0
        elementnum=0
        for l in self.values:
            for d in l:
                if d==highestnum:
                    startnumx=numberofrows
                    startnumy=m
                elementnum+=1
                m+=1
            numberofcol=m
            m=0
            numberofrows+=1
        counter=0
        rowcounter=0
        rowelementcounter=0
        self.U=[]
        for z in self.U1:
            self.U.append(z)
        rowcounter=0
        rowelementcounter=0
        counter=0
        for row in self.U:#start of value iteration
            for elements in row:
                #print(rowelementcounter,rowcounter,self.U1,"test")
                self.U1[rowcounter].pop(rowelementcounter)
                try:
                    self.A['^']=self.U[rowcounter+1][counter]
                except:
                    self.A['^']=elements
                try:
                    self.A['v']=self.U[rowcounter-1][counter]
                except:
                    self.A['v']=elements
                try:
                    self.A['>']=self.U[rowcounter][row[rowelementcounter+1]]
                except:
                    self.A['>']=elements
                try:
                    self.A['<']=self.U[rowcounter][row[rowelementcounter-1]]
                except:
                    self.A['<']=elements
                self.U1[rowcounter].insert(rowelementcounter,elements+.5+self.expected_value(elements))

                counter+=1
                rowelementcounter+=1
            rowelementcounter=0
            rowcounter+=1
        #print(self.U1)
        for x in self.U1:
            self.U.append(x)





        ## The value iteration algorithm.  You may use any value for gamma
        ## between 0 and 1 (typically set to something like 0.99).  The number
        ## of updates to carry out is not fixed, but you must run until the
        ## resulting policy converges and stops changing.  You can do this by
        ## iterating until the utility values stop changing by much.  Usually,
        ## this is accomplished by setting some parameter epsilon (small value,
        ## on the order of .1, .01, etc.), summing up the differences between
        ## state utility values before and after the update, and checking
        ## whether it is less than epsilon.

    def get_policy( self ):#gets policy
        templist=self.values
        counter=0
        rowcount=0
        elementcount=0
        for i in self.values:

            for j in i:
                templist[counter][rowcount]=self.expectedvalue[elementcount]
                elementcount+=1
                rowcount+=1
            rowcount=0

            counter+=1
        print(templist)
        return templist


userin=input("Put in matrix numbers, seperating rows with / and numbers with spaces. for example:1 2 3/4 5 6")
matrix=listoflists(userin)
print(matrix)
m=MDP(matrix)
