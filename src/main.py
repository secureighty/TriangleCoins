from src.Triangle import *
from src.DecisionNode import *
t = Triangle(3)

root = DecisionNode(t)

root.discover_children()