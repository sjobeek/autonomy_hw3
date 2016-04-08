import Queue
import collections

class AStarPlanner(object):
    
    def __init__(self, planning_env, visualize):
        self.planning_env = planning_env
        self.visualize = visualize
        self.nodes = dict()
    
    def cost_to_go(self,current_id):
        return self.planning_env.ComputeDistance(goal_id,current_id)

    def edge_cost(self,parent_id,child_id):
        return self.planning_env.ComputeDistance(parent_id,child_id)


        # TODO: Here you will implement the AStar planner
        #  The return path should be a numpy array
        #  of dimension k x n where k is the number of waypoints
        #  and n is the dimension of the robots configuration space


    def Plan(self, start_config, goal_config):

        if self.visualize and hasattr(self.planning_env, 'InitializePlot'):
            self.planning_env.InitializePlot(goal_config)


        #initializations
        plan = []
        
        global  start_id 
        start_id = self.planning_env.discrete_env.ConfigurationToNodeId(start_config)
        global goal_id  
        goal_id = self.planning_env.discrete_env.ConfigurationToNodeId(goal_config)
        
        open_list = dict()
        closed_list = dict()
        dict_cost_to_come = dict()

        # back pointer dictionary maintains the parent id for each child

        back_pointer = dict()
        back_pointer[start_id] = None
        dict_cost_to_come[start_id] = 0
        open_list[start_id] = 0

        while len(open_list) != 0:
            node_current_id= sorted(open_list,key=open_list.get)[0]
            current_total_cost = open_list.get(node_current_id)
            # print "node_current_id", node_current_id
            # print "current_total_cost", current_total_cost

            del open_list[node_current_id]
            if node_current_id == goal_id:
                break
            successors = self.planning_env.GetSuccessors(node_current_id)

            no_neighbour = len(successors)
            for each in range(no_neighbour):
                successor_current_id = successors.pop()
                successor_current_cost = dict_cost_to_come[node_current_id] + self.edge_cost(successor_current_id,node_current_id)

                if successor_current_id in open_list and successor_current_cost > dict_cost_to_come[successor_current_id]:
                    continue
                back_pointer[successor_current_id] = node_current_id
                dict_cost_to_come[successor_current_id] = successor_current_cost
                open_list[successor_current_id] = successor_current_cost + self.cost_to_go(successor_current_id)
                self.planning_env.PlotEdge(self.planning_env.discrete_env.NodeIdToConfiguration(node_current_id), self.planning_env.discrete_env.NodeIdToConfiguration(successor_current_id))

            closed_list[node_current_id] = current_total_cost
        
        plan_id = goal_id
        while plan_id != start_id:
            plan.append(self.planning_env.discrete_env.NodeIdToConfiguration(back_pointer[plan_id]))
            plan_id = back_pointer[plan_id]

        plan.reverse()

        return plan
