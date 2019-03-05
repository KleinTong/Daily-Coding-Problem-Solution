from priority_queue import PriorityQueue
import math


class Node:
    def __init__(self, point, distance):
        self.point = point
        self.distance = distance


    def __eq__(self, other):
        return self.distance == other.distance


    def __lt__(self, other):
        return self.distance < other.distance


    def __gt__(self, other):
        return self.distance > other.distance


    def __str__(self):
        return str(self.point)


def k_nearest(points, center, k):
    pq = PriorityQueue()
    for point in points:
        distance_square = (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2
        distance = math.sqrt(distance_square)
        node = Node(point, distance)
        pq.enque(node)

    for _ in range(k):
        print(pq.deque())


if __name__ == '__main__':
    points = [(0, 0), (5, 4), (3, 1)]
    center = (1, 2)
    k_nearest(points, center, 2)
