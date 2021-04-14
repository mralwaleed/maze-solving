


class Node:


    def __init__(self,x,y,nim):
        self.x = x
        self.y = y
        self.pirent = None
        self.childerin = list()
        self.data=nim
        self.location='(' + "%s" %x + ',' + "%s" %y + ')'


    def MoveToRight(self):

        if(self.y+1<len(self.data[self.x]) and self.data[self.x][self.y+1]==1):
            right = Node(self.x,self.y+1,self.data)
            self.childerin.append(right)
            self.childerin[-1].pirent = self
            #print("Right is ", right.x, " , ", right.y)
            #print("right P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)



    def MoveToLift(self):

        if(self.y-1>=0 and self.data[self.x][self.y-1]==1):
            Lift = Node(self.x,self.y-1,self.data)
            self.childerin.append(Lift)
            #print("Lift is ", Lift.x, " , ", Lift.y)
            self.childerin[-1].pirent = self
            #print("lift P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)

    def MovetoUp(self):
        if(self.x-1>=0 and self.data[self.x-1][self.y]==1):
            Up = Node(self.x-1,self.y,self.data)
            #print("Up is ",Up.x," , ",Up.y)
            self.childerin.append(Up)
            self.childerin[-1].pirent= self
            #print("up P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)

    def MoveToDown(self):


        if(self.x+1<len(self.data) and self.data[self.x+1][self.y]==1):
            Down = Node(self.x+1,self.y,self.data)
            self.childerin.append(Down)
            self.childerin[-1].pirent= self
           # print("Down is ", Down.x, " , ", Down.y)
          #  print("Down P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)



    def isGoal(self,x,y):
        isgoal = False
        if(self.x==x and self.y == y):
            isgoal = True
        return isgoal



    def print(self):
        print(self.x,",",self.y)


    def ExpandMove(self):
        self.MoveToLift()
        self.MoveToRight()
        self.MoveToDown()
        self.MovetoUp()

