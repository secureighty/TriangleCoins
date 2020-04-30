class Node:
    def __init__(self, number):
        self.number = number
        self.relations = []
        self.on = True

    def __str__(self):
        # result = "("+self.number.__str__() + ", "
        result = ""
        if self.on:
            result += "1"
        else:
            result += "0"
        # result += ")"
        return result

    def add_relation(self, source, destination):
        """
        add a new relation to the node. A relation is a move that might at some point be possible.
        :param source: the adjacent node in the relation
        :param destination: the destination node in the relation
        :return:
        """
        self.relations.append([self, source, destination])

    def is_on(self):
        return self.on

    def toggle(self):
        self.on = not self.on

    def get_valid_moves(self):
        """
        get all valid moves for a node
        :return: array of relations. rel[0] is self. rel[1] is source. rel[2] is dest.
        2 jumps over 0 to reach 1
        """
        result = []
        if self.on:
            for relation in self.relations:
                if relation[1].is_on() and not relation[2].is_on():
                    result.append([relation[0].number, relation[1].number, relation[2].number])
        return result
