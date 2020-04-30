from src.Triangle import *
from src.DecisionNode import *
t = Triangle(3)
root = DecisionNode(t)
root.discover_children()
t2 = Triangle(1)
root2 = DecisionNode(t2)
root2.discover_children()
finished_traversals = root.get_finished_traversals()
moved_coin = None
for traversal in finished_traversals:
    traversal.reverse()
    print(traversal)
    score = 0
    for move in traversal:
        if moved_coin != move[0]:
            score += 1
        moved_coin = move[2]
    print(score)


