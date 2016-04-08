import Queue


class BreadthFirstPlanner(object):
    


    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        
    def Plan(self, start_config, goal_config):
        
        if self.visualize and hasattr(self.planning_env, 'InitializePlot'):
            self.planning_env.InitializePlot(goal_config)
        plan = []
        back_pointer = dict()
        # back_pointer = {child:parent}

        # TODO: Here you will implement the breadth first planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space
        q = Queue.Queue()
        start_id = self.planning_env.discrete_env.ConfigurationToNodeId(start_config)
        goal_id  = self.planning_env.discrete_env.ConfigurationToNodeId(goal_config)
        q.put(start_id)
        back_pointer[start_id] = None
        current_id = q.get()

        while current_id != goal_id:
            successors = self.planning_env.GetSuccessors(current_id)
            no_neighbour = len(successors)
            for each in range(no_neighbour):
                poped = successors.pop()
                if poped not in back_pointer.keys():
                    self.planning_env.PlotEdge(self.planning_env.discrete_env.NodeIdToConfiguration(current_id), self.planning_env.discrete_env.NodeIdToConfiguration(poped))
                    q.put(poped)
                    back_pointer[poped] = current_id
            current_id = q.get()

        plan_id = goal_id
        while plan_id != start_id:
            plan.append(self.planning_env.discrete_env.NodeIdToConfiguration(back_pointer[plan_id]))
            plan_id = back_pointer[plan_id]

        plan.reverse()
   
        return plan
