#!/usr/bin/env python

from sys import argv
from time import time
from node import *

class Solver(object):
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def print_path(self, state):
        path = []
        while state:
            path.append(state)
            state = state.prev
        path.reverse()
        print("\n-->\n".join([str(state) for state in path]))

    def bfs(self, depth = 50):
        queue = [self.start]
        visited = set()
        found = False

        while queue:
            state = queue.pop()
            if state == self.goal:
                found = state
                break
            if state in visited or state.step > depth:
                continue
            visited.add(state)
            for s in state.next():
                queue.insert(0, s)
            #print "queue status" 
            #print queue
        if found:
            self.print_path(found)
            print "Find solution"
        else:
            print("No solution found")

    def astar(self, depth = 75):
		priority_queue = PriorityQueue()
		h_val = self.start.manhattan_distance()
		f_val = h_val + self.start.step
		print "first value="+str(f_val)
		priority_queue.push(self.start, f_val)
		visited = set()
		found = False
		while not priority_queue.isEmpty():
			state = priority_queue.pop()
			if state == self.goal:
				found = state
				break
			if state in visited or state.step > depth:
				continue
			visited.add(state)
			for s in state.next():
				h_val_s = s.manhattan_distance()
				f_val_s = h_val_s + s.step
				print "func value ="+str(f_val_s)
				priority_queue.push(s, f_val_s)
                                print priority_queue
		if found:
			self.print_path(found)
		else:
			print("No solution found")


if __name__ == "__main__":
    script, strategy = argv
    start = Node([2,8,3,1,6,4,7,0,5])
    goal = Node([1,2,3,8,0,4,7,6,5])

    search = Solver(start, goal)

    if strategy == "bfs":
		search.bfs()
    elif strategy == "astar":
		search.astar()
    else:
        print "Wrong strategy"
