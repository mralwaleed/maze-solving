import collections
from collections import deque


class BFS:

    def Search(self, root, goalx, goaly):
        open = deque()
        close = dict()
        pathToSolve = list()
        open.append(root)
        close[root.location] = True


        while ( not len(open) == 0):

            currrentNode = open.popleft()
            currrentNode.ExpandMove()



            if (currrentNode.isGoal(goaly, goalx)):
                self.findpath(currrentNode, pathToSolve)
                return pathToSolve

            for i in range(len(currrentNode.childerin)):
                if (currrentNode.childerin[i].isGoal(goalx, goaly)):
                    self.findpath(currrentNode, pathToSolve)
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
