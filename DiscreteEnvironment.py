from __future__ import division
import numpy


class DiscreteEnvironment(object):

    def __init__(self, resolution, lower_limits, upper_limits):

        # Store the resolution
        self.resolution = resolution #1

        # Store the bounds
        self.lower_limits = lower_limits #[0,0]
        self.upper_limits = upper_limits #[4,4]

        # Calculate the dimension
        self.dimension = len(self.lower_limits) #2

        # Figure out the number of grid cells that are in each dimension
        self.num_cells = self.dimension*[0]
        for idx in range(self.dimension):
            self.num_cells[idx] = numpy.ceil((upper_limits[idx] - lower_limits[idx])/self.resolution)


    def ConfigurationToNodeId(self, config):
        
        # TODO:
        # This function maps a node configuration in full configuration
        # space to a node in discrete space
        #
        node_id = 0
        return node_id

    def NodeIdToConfiguration(self, nid):
        
        # TODO:
        # This function maps a node in discrete space to a configuraiton
        # in the full configuration space
        #
        config = [0] * self.dimension
        return config
        
    def ConfigurationToGridCoord(self, config):
        
        # TODO:
        # This function maps a configuration in the full configuration space
        # to a grid coordinate in discrete space
        #
        coord = [0] * self.dimension
        for idx in range(self.dimension):
            coord[idx] = numpy.ceil(config[idx])
            
        print ("the given continuous config is ", config)
        print("the new discrete coords is", coord)
        
        return coord

    def GridCoordToConfiguration(self, coord):
        
        # TODO:
        # This function smaps a grid coordinate in discrete space
        # to a configuration in the full configuration space
        #
        config = [0] * self.dimension
        for idx in range(self.dimension):
                config[idx] = coord[idx]*self.resolution + self.resolution/2;
        print ("coordinates are--->",coord)
        print("configuration---->", config)        
        return config

    def GridCoordToNodeId(self,coord):
        
        # TODO:
        # This function maps a grid coordinate to the associated
        # node id 
        node_id = 0
        return node_id

    def NodeIdToGridCoord(self, node_id):
        
        # TODO:
        # This function maps a node id to the associated
        # grid coordinate
        coord = [0] * self.dimension
        return coord
        
        
def main():
        print("in main")
        o = DiscreteEnvironment(4,[0,0],[4,4])     
        o.ConfigurationToGridCoord([1.2,4.6])
        o.GridCoordToConfiguration([1,3])
if __name__ == '__main__':  
        main()  
