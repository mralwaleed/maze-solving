import math





class NodeH:


    def __init__(self,x,y,nim,goalY,goalX,chose):
        self.x = x
        self.y = y
        self.pirent = None
        self.childerin = list()
        self.data=nim
        self.location='(' + "%s" %x + ',' + "%s" %y + ')'
        self.goalX=goalX
        self.goalY=goalY
        self.chose=chose
        if self.chose == 1:
            self.HU =self.Manhattan()
        else:
            self.HU = self.Euclidean()


    def __lt__(self, other):
        return self.HU < other.HU

    def MoveToRight(self):

        if(self.y+1<len(self.data[self.x]) and self.data[self.x][self.y+1]==1):
            right = NodeH(self.x,self.y+1,self.data,self.goalX,self.goalY,self.chose)
            self.childerin.append(right)
            self.childerin[-1].pirent = self
            #print("Right is ", right.x, " , ", right.y)
            #print("right P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)



    def MoveToLift(self):

        if(self.y-1>=0 and self.data[self.x][self.y-1]==1):
            Lift = NodeH(self.x,self.y-1,self.data,self.goalX,self.goalY,self.chose)
            self.childerin.append(Lift)
            #print("Lift is ", Lift.x, " , ", Lift.y)
            self.childerin[-1].pirent = self
            #print("lift P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)

    def MovetoUp(self):
        if(self.x-1>=0 and self.data[self.x-1][self.y]==1):
            Up = NodeH(self.x-1,self.y,self.data,self.goalX,self.goalY,self.chose)
            #print("Up is ",Up.x," , ",Up.y)
            self.childerin.append(Up)
            self.childerin[-1].pirent= self
            #print("up P",self.childerin[-1].pirent.y,",",self.childerin[-1].pirent.x)

    def MoveToDown(self):


        if(self.x+1<len(self.data) and self.data[self.x+1][self.y]==1):
            Down = NodeH(self.x+1,self.y,self.data,self.goalX,self.goalY,self.chose)
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

    def Manhattan(self):
         hx=0
         hy=0
         if self.goalX>self.x:
             hx=self.goalX-self.x
         else:
            if self.goalX<self.x:
                hx=self.x-self.goalX
            else:
                hx=0

         if self.goalY > self.y:
             hy = self.goalY - self.y
         else:
             if self.goalY < self.y:
                 hy = self.y -self.goalY
             else:
                hy = 0

         return hx+hy

    def Euclidean(self):
         hx = 0
         hy = 0
         if self.goalX>self.x:
             hx=self.goalX-self.x
         else:
            if self.goalX<self.x:
                hx=self.x-self.goalX
            else:
                hx=0
         hx=hx*hx
         if self.goalY > self.y:
             hy = self.goalY - self.y
         else:
             if self.goalY < self.y:
                 hy = self.y -self.goalY
             else:
                hy = 0
         hy=hy*hy

         resualtH=hx+hy
         resualtH=int(math.sqrt(resualtH))
         return resualtH