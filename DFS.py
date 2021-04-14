from collections import deque
class DFS:

 def Search(self, root, goaly, goalx):
    open = deque()
    close = dict()
    pathToSolve = list()
    open.append(root)
    close[root.location] = True

    while (not len(open) == 0):

        currrentNode = open.pop()
        currrentNode.ExpandMove()



        for i in range(len(currrentNode.childerin)):
            if (currrentNode.childerin[i].isGoal(goalx, goaly)):
                self.findpath(currrentNode.childerin[i], pathToSolve)
                return pathToSolve

            try:
                if not close[currrentNode.childerin[i].location]:
                    print()
            except KeyError:
                open.append(currrentNode.childerin[i])
                close[currrentNode.childerin[i].location] = True


 def findpath(self, go, lis=[]):
    c = go
    lis.append(c)
    while (not c.pirent == None):
        c = c.pirent
        lis.append(c)