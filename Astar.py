import heapq
class Astar:


    def Search(self, root, goaly, goalx):

            open=[]
            heapq.heapify(open)
            close = dict()
            pathToSolve = list()
            heapq.heappush(open,(root.fcost,root))
            close[root.location] = True

            while (not len(open) == 0):
                currrentNode1 = heapq.heappop(open)
                currrentNode=currrentNode1[1]
                currrentNode.ExpandMove()

                if (currrentNode.isGoal(goalx, goaly)):

                    pathToSolve=self.findpath(currrentNode, pathToSolve)
                    return pathToSolve

                for i in range(len(currrentNode.childerin)):
                    if (currrentNode.childerin[i].isGoal(goalx, goaly)):
                        pathToSolve=self.findpath(currrentNode, pathToSolve)
                        return pathToSolve

                    try:
                        if not close[currrentNode.childerin[i].location]:
                            print()
                    except KeyError:
                        heapq.heappush(open,(currrentNode.childerin[i].fcost,currrentNode.childerin[i]))
                        close[currrentNode.childerin[i].location] = True

    def findpath(self, go, lis=[]):
        c = go
        lis.append(c)
        while (not c.pirent == None):
            c = c.pirent
            lis.append(c)
        return lis

