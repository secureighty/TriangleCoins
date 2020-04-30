from src.Triangle import *


class DecisionNode:
    def __init__(self, triangle, parent=None, move_option=None):
        """
        :param parent: which node did I come from?
        :param move_option: the move made to get the cursor to this child
        """
        self.parent = parent
        self.children = []
        self.move_option = move_option
        self.t = triangle
        self.finished_node = False

        # list of moves to reach a finished node from this node
        self.finished_traversals = []

        # DecisionNode is not a pedophile
        self.explored_children = []

    def add_child(self, child):
        self.children.append(child)

    def discover_children(self, t=None, indent=0):
        """
        :param t: triangle at this state
        :return: array of child DecisionNodes
        """
        MAX_SHOWN_DEPTH = 999
        # if I didn't put a triangle, I mean you should use this instance's
        if t is None:
            t = self.t
        # show me what's going on
        if indent <= MAX_SHOWN_DEPTH:
            print(('|'+'\t') * (indent)+"this node has the triangle")
            for line in str(t).split("\n"):
                print(('|'+'\t') * (indent)+line)
            print(('|'+'\t') * (indent)+"which it got by making this move")
            print(('|'+'\t') * (indent)+str(self.move_option))
            print(('|'+'\t') * (indent)+"this node is "+str(indent)+" recursions deep")
        # don't explore already explored children
        children_moves = t.get_all_moves()
        moves_to_not_make = []
        for child in self.explored_children:
            moves_to_not_make.append(child.move_option)
        for move in moves_to_not_make:
            if move in children_moves:
                if indent <= MAX_SHOWN_DEPTH:
                    print(('|'+'\t') * (indent)+"I found", move, "in children moves:", children_moves, "and moves_not_to_make:", moves_to_not_make,". removing from children moves")
                children_moves.remove(move)
        # if I've made every move I could, stop.
        if indent <= MAX_SHOWN_DEPTH:
            print(('|'+'\t') * (indent) + "My options are "+str(children_moves))
        if len(children_moves) == 0:
            if indent <= MAX_SHOWN_DEPTH:
                print(('|'+'\t') * (indent) + "Ran out of moves. Marked my last move, "+ str(self.move_option)+" explored")
            self.parent.explored_children.append(self)
            on_nodes = 0
            for node in t.board:
                if node.is_on():
                    on_nodes += 1
            if on_nodes == 1:
                self.finished_node = True
                print(('|'+'\t') * (indent) + str("This node is completed"))
                self.inform_ancestors()
        else:
            for i in children_moves:
                self.children.append(DecisionNode(move_option=i, parent=self, triangle=self.t))
            for n in range(0, len(self.children)):
                j = self.children[n]
                # make a new triangle to pass on
                new_t = self.copy_triangle()
                new_t.move(j.move_option)
                if indent < MAX_SHOWN_DEPTH:
                    print(('|'+'\t') * (indent))
                    print(('|'+'\t') * (indent) + "branch number:", n+1)
                    print(('|'+'\t') * (indent) + "----------------------------------")
                j.discover_children(new_t, indent=indent+1)

    def get_depth(self):
        depth = 0
        check = self
        while check is not None:
            depth += 1
            check = check.parent
        return depth

    def copy_triangle(self):
        """
        make a copy of this instance's triangle
        :return: copied triangle
        """
        new_t = Triangle(self.t.removed_node)
        move_list = []
        marker = self
        while marker.move_option is not None:
            move_list.append(marker.move_option)
            marker = marker.parent
        move_list.reverse()
        for move in move_list:
            new_t.move(move)
        return new_t

    def inform_ancestors(self, path=None):
        if path is None:
            path = []
        if self.parent is not None:
            path.append(self.move_option[0:])
            self.finished_traversals.append(path)
            self.parent.inform_ancestors(path)
        else:
            self.finished_traversals.append(path)

    def get_finished_traversals(self):
        result = self.finished_traversals
        return result
