class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.remaining_capacity = capacity
        self.objects = []
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        if (self.remaining_capacity <= object.size):
            self.objects.append(object)
            self.remaining_capacity -= object.size

        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        for obj in self.objects:
            if obj.id == object_id:
                self.remaining_capacity += obj.size
                self.objects.remove(obj)
        pass
