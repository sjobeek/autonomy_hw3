import numpy
from DiscreteEnvironment import DiscreteEnvironment

class HerbEnvironment(object):
    
    def __init__(self, herb, resolution):
        
        self.robot = herb.robot
        self.lower_limits, self.upper_limits = self.robot.GetActiveDOFLimits()
        self.discrete_env = DiscreteEnvironment(resolution, self.lower_limits, self.upper_limits)

        # account for the fact that snapping to the middle of the grid cell may put us over our
        #  upper limit
        upper_coord = [x - 1 for x in self.discrete_env.num_cells]
        upper_config = self.discrete_env.GridCoordToConfiguration(upper_coord)
        for idx in range(len(upper_config)):
            self.discrete_env.num_cells[idx] -= 1

        # add a table and move the robot into place
        table = self.robot.GetEnv().ReadKinBodyXMLFile('models/objects/table.kinbody.xml')
        
        self.robot.GetEnv().Add(table)

        table_pose = numpy.array([[ 0, 0, -1, 0.7], 
                                  [-1, 0,  0, 0], 
                                  [ 0, 1,  0, 0], 
                                  [ 0, 0,  0, 1]])
        table.SetTransform(table_pose)
        
        # set the camera
        camera_pose = numpy.array([[ 0.3259757 ,  0.31990565, -0.88960678,  2.84039211],
                                   [ 0.94516159, -0.0901412 ,  0.31391738, -0.87847549],
                                   [ 0.02023372, -0.9431516 , -0.33174637,  1.61502194],
                                   [ 0.        ,  0.        ,  0.        ,  1.        ]])
        self.robot.GetEnv().GetViewer().SetCamera(camera_pose)
    
    def GetSuccessors(self, node_id):

        successors = []

        # TODO: Here you will implement a function that looks
        #  up the configuration associated with the particular node_id
        #  and return a list of node_ids that represent the neighboring
        #  nodes
       
        neighbors = []
        coord = self.discrete_env.NodeIdToGridCoord(node_id)
        for i in range(0, len(coord)):

            coord_list1,coord_list2 = list(coord)
            coord_list1[i] = coord_list1[i] + 1
            coord_list2[i] = coord_list2[i]-1
            print coord_list1, coord_list2
            neighbors.append(coord_list1[i])
            neighbors.append(coord_list2[i])
            successors = []
            
  #collision check and boundary check
                print "appending successor"
                successors.append(self.discrete_env.GridCoordToNodeId(neighbors[i]))
        return successors

    def ComputeDistance(self, start_id, end_id):
        # TODO: Here you will implement a function that 
        # computes the distance between the configurations given
        # by the two node ids
        
        dist = 0
        start = self.discrete_env.NodeIdToConfiguration(start_id)     
        end = self.discrete_env.NodeIdToConfiguration(end_id) 
        total = 0
        for i in range(0, len(start)):
            total = math.pow((start[i] - end[i]),2)
            
        dist = math.sqrt(total)*10
        #print "distance: " + str(dist)
        return dist
        
      

    def ComputeHeuristicCost(self, start_id, goal_id):
        cost = 0
        start_config = self.discrete_env.NodeIdToConfiguration(start_id)
        goal_config = self.discrete_env.NodeIdToConfiguration(goal_id)
        length = len(start_config)
        distance = [0]*length
        weights = [1,2,1,2,1,2,1]
        for i in range(len(goal_id)):
            distance[i] = goal_config[i] - start_config[i]
        for j in range(len(distance)):
            cost = cost + (disance[j]*weights[i])     
       
	cost = sum([dist[i]*wts[i] for i in range(len(dist))])

        # TODO: Here you will implement a function that 
        # computes the heuristic cost between the configurations
        # given by the two node ids
        
        return cost

