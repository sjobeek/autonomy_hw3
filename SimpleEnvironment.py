import numpy
import pylab as pl
from DiscreteEnvironment import DiscreteEnvironment
import math

class SimpleEnvironment(object):
    
    def __init__(self, herb, resolution):
        self.robot = herb.robot
        self.lower_limits = [-5., -5.]
        self.upper_limits = [5., 5.]
        self.discrete_env = DiscreteEnvironment(resolution, self.lower_limits, self.upper_limits)

        # add an obstacle
        table = self.robot.GetEnv().ReadKinBodyXMLFile('models/objects/table.kinbody.xml')
        self.robot.GetEnv().Add(table)

        table_pose = numpy.array([[ 0, 0, -1, 1.5], 
                                  [-1, 0,  0, 0], 
                                  [ 0, 1,  0, 0], 
                                  [ 0, 0,  0, 1]])
        table.SetTransform(table_pose)

    def GetSuccessors(self, node_id):

        successors = []

        # TODO: Here you will implement a function that looks
        #  up the configuration associated with the particular node_id
        #  and return a list of node_ids that represent the neighboring
        #  nodes

        # order of nodes: successors = [4,3,2,1]
        #            3
        #            |
        #    2 --- node_id --- 4
        #            |
        #            1
        
        if node_id % self.discrete_env.num_cells[0] != (self.discrete_env.num_cells[0] -1) :
            if self.CheckCollision(DiscreteEnvironment.NodeIdToGridCoord(node_id + 1)):
                successors.append(node_id + 1)

        if node_id / self.discrete_env.num_cells[0] != 0:
            if self.CheckCollision(DiscreteEnvironment.NodeIdToGridCoord(node_id - self.discrete_env.num_cells[0])):
                successors.append(node_id - self.discrete_env.num_cells[0])

        if node_id % self.discrete_env.num_cells[0] != 0:
            if self.CheckCollision(DiscreteEnvironment.NodeIdToGridCoord(node_id - 1):
                successors.append(node_id - 1)

        if node_id / self.discrete_env.num_cells[0] != (self.discrete_env.num_cells[1] -1):
            if self.CheckCollision(DiscreteEnvironment.NodeIdToGridCoord(node_id + self.discrete_env.num_cells[0])):
                successors.append(node_id + self.discrete_env.num_cells[0])

        return successors

    def ComputeDistance(self, start_id, end_id):

        dist = 0

        # TODO: Here you will implement a function that 
        # computes the distance between the configurations given
        # by the two node ids

        start_x,start_y = self.discrete_env.NodeIdToGridCoord(start_id) 
        end_x, end_y    = self.discrete_env.NodeIdToGridCoord(end_id)
        
        dist_x = math.pow( start_x - end_x , 2 )
        dist_y = math.pow( start_y - end_y , 2 )

        dist = math.sqrt( dist_x + dist_y )

        return dist

    def ComputeHeuristicCost(self, start_id, goal_id):
        
        cost = 0

        # TODO: Here you will implement a function that 
        # computes the heuristic cost between the configurations
        # given by the two node ids
        cost = self.ComputeDistance(start_id,goal_id)

        return cost

    def CheckCollision(self, config):
        tempTrans = self.robot.GetTransform()
        self.robot.SetTransform(numpy.array([1, 0, 0, config[0]],
                                            [0, 1, 0, config[1]],
                                            [0, 0, 1,         0],
                                            [0, 0, 0,         1]]))
        return self.robot.GetEnv().CheckCollision(self.robot,table)

    def InitializePlot(self, goal_config):
        self.fig = pl.figure()
        pl.xlim([self.lower_limits[0], self.upper_limits[0]])
        pl.ylim([self.lower_limits[1], self.upper_limits[1]])
        pl.plot(goal_config[0], goal_config[1], 'gx')

        # Show all obstacles in environment
        for b in self.robot.GetEnv().GetBodies():
            if b.GetName() == self.robot.GetName():
                continue
            bb = b.ComputeAABB()
            pl.plot([bb.pos()[0] - bb.extents()[0],
                     bb.pos()[0] + bb.extents()[0],
                     bb.pos()[0] + bb.extents()[0],
                     bb.pos()[0] - bb.extents()[0],
                     bb.pos()[0] - bb.extents()[0]],
                    [bb.pos()[1] - bb.extents()[1],
                     bb.pos()[1] - bb.extents()[1],
                     bb.pos()[1] + bb.extents()[1],
                     bb.pos()[1] + bb.extents()[1],
                     bb.pos()[1] - bb.extents()[1]], 'r')
                    
                     
        pl.ion()
        pl.show()
        
    def PlotEdge(self, sconfig, econfig):
        pl.plot([sconfig[0], econfig[0]],
                [sconfig[1], econfig[1]],
                'k.-', linewidth=2.5)
        pl.draw()

        
