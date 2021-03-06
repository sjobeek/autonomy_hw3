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
        grid_cord = self.ConfigurationToGridCoord(config)
        node_id = self.GridCoordToNodeId(grid_cord)
        return node_id
    

    def NodeIdToConfiguration(self, nid):
        
        # TODO:
        # This function maps a node in discrete space to a configuraiton
        # in the full configuration space
        #
        coord = self.NodeIdToGridCoord(nid)

        config = self.GridCoordToConfiguration(coord)
        return config
        
    def ConfigurationToGridCoord(self, config):
        
        # TODO:
        # This function maps a configuration in the full configuration space
        # to a grid coordinate in discrete space
        #

        coord = [0] * self.dimension
        for idx in range(self.dimension):
            coord[idx] = int(numpy.floor((config[idx] - self.lower_limits[idx]) / self.resolution ))
        return coord

    def GridCoordToConfiguration(self, coord):
        
        # TODO:
        # This function smaps a grid coordinate in discrete space
        # to a configuration in the full configuration space
        #
        config = [0] * self.dimension
        for idx in range(self.dimension):
          config[idx] = float(self.lower_limits[idx] + coord[idx] * self.resolution + self.resolution/2.0)
        return config

    def GridCoordToNodeId(self,coord):
        
        # TODO:
        # This function maps a grid coordinate to the associated
        # node id 
        node_id = 0
        multip = 1
        for idx in range(self.dimension):
            node_id += multip * coord[idx]
            multip *= self.num_cells[idx]
        return node_id


    def NodeIdToGridCoord(self, node_id):
        
        # TODO:
        # This function maps a node id to the associated
        # grid coordinate

        multipliers = [0] * self.dimension
        multip = 1
        for idx in range(self.dimension):
            multipliers[idx] = multip
            multip *= self.num_cells[idx]

        coord = [0] * self.dimension
        for multip_idx in reversed(range(self.dimension)):
            coord[multip_idx] = int(node_id / multipliers[multip_idx])
            node_id %= multipliers[multip_idx]
        return coord