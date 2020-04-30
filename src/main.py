from src.Triangle import *
from src.DecisionNode import *


# neither 1 nor 5 had any answers
t = Triangle(3)

# construct the tree
root = DecisionNode(t)
root.discover_children()
finished_traversals = root.get_finished_traversals()

# now display solutions and their scores (only 14, no pruning)
moved_coin = None


def prettyprint(array):
    result = ""
    for move in traversal:
        result += ", ("+str(move[0])+" - "+str(move[2])+")"
    return result[2:]


for traversal in finished_traversals:
    traversal.reverse()
    print(prettyprint(traversal))
    score = 0
    for move in traversal:
        if moved_coin != move[0]:
            score += 1
        moved_coin = move[2]
    print("This solution scores "+str(score)+"\n")


# I should have written this in java

# no, wait, I should have worked on my calculus instead of doing this.
