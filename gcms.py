from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bins = AVLTree(lambda a, b : a.id < b.id)
        self.objects = AVLTree(lambda a,b : a.id<b.id)

        pass 

    def add_bin(self, bin_id, capacity):
        bin_obj = Bin(bin_id,capacity)
        self.bins.insert(bin_obj)

        pass

    def add_object(self, object_id, size, color):
        obj_obj = Object(object_id, size, color)
        





        raise NoBinFoundException

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        obj_nodes = self.objects.in_order_traversal()

        for tup in obj_nodes:
            if (tup[0] == object_id):
                
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        pass
    
    