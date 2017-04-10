import heapq
class Node(object):
	n = 0
	def __init__(self, board, prev_state = None):
	    assert len(board) == 9
	    self.board = board[:];
	    self.prev = prev_state
	    self.step = 0
            self.next_method = -1
	    Node.n += 1
	    if self.prev:
		self.step = self.prev.step + 1
	def __eq__(self, other):
	    return self.board == other.board
	def __hash__(self):
	    h = [0, 0, 0]
	    h[0] = self.board[0] << 6 | self.board[1] << 3 | self.board[2]
	    h[1] = self.board[3] << 6 | self.board[4] << 3 | self.board[5]
	    h[2] = self.board[6] << 6 | self.board[7] << 3 | self.board[8]
	    h_val = 0
	    for h_i in h:
		h_val = h_val * 31 + h_i
	    return h_val
	def __str__(self):
	    string_list = [str(i) for i in self.board]
	    sub_list = (string_list[:3], string_list[3:6], string_list[6:])
	    return "\n".join([" ".join(l) for l in sub_list])

	def manhattan_distance(self):
	    distance = 0
	    goal = [1,2,3,8,0,4,7,6,5]
	    for i in range(1,9):
		xs, ys = self.__i2pos(self.board.index(i))
		xg, yg = self.__i2pos(goal.index(i))
		distance += abs(xs-xg) + abs(ys-yg)
	    return distance

	def next(self):
		next_moves = []
		i = self.board.index(0)
		next_moves = (self.move_up(i), self.move_down(i), self.move_left(i), self.move_right(i))
		return [s for s in next_moves if s]

	def move_right(self, i):
                self.next_method=0
		x, y = self.__i2pos(i)
		if y < 2:
			right_state = Node(self.board, self)
			right = self.__pos2i(x, y+1)
			right_state.__swap(i, right)
			return right_state

	def move_left(self, i):
                self.next_method=1
		x, y = self.__i2pos(i)
		if y > 0:
			left_state = Node(self.board, self)
			left = self.__pos2i(x, y - 1)
			left_state.__swap(i, left)
			return left_state

	def move_up(self, i):
                self.next_method=2
		x, y = self.__i2pos(i)
		if x > 0:
			up_state = Node(self.board, self)
			up = self.__pos2i(x - 1, y)
			up_state.__swap(i, up)
			return up_state

	def move_down(self, i):
                self.next_method=3
		x, y = self.__i2pos(i)
		if x < 2:
			down_state = Node(self.board, self)
			down = self.__pos2i(x + 1, y)
			down_state.__swap(i, down)
		        return down_state

	def __swap(self, i, j):
		self.board[j], self.board[i] = self.board[i], self.board[j]

	def __i2pos(self, index):
		return (int(index / 3), index % 3)

	def __pos2i(self, x, y):
		return x * 3 + y

class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0
    def __str__(self):
        return "now queue status"+ str(self.heap) +"\n" + "queue count =" + str(self.count)
    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1
    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item
    def isEmpty(self):
        return len(self.heap) == 0
