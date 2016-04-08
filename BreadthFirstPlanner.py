import Queue


class BreadthFirstPlanner(object):
    


    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        
    def Plan(self, start_config, goal_config):
        
        plan = []
        back_pointer = dict()

        # TODO: Here you will implement the breadth first planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space
        # q = Queue.Queue()

        # start_id = self.planning_env.discrete_env.ConfigurationToNodeId(start_config)
        # a =  self.planning_env.GetSuccessors(0)

        # q.put(start_config)

        # current_node = 

        # while 



        plan.append(start_config)
        plan.append(goal_config)
   
        return plan
