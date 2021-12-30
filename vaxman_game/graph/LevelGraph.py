
from enum import Enum 
from queue import PriorityQueue

import random

class LevelGraph:  
  class Move(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2    
    DOWN = 3

  NEIGHBOUR_OFFSET = [(0,-1),  (-1,0), (0,1), (1,0)]  
  MAX_DIST = 100000

  class Vertex:
    def __init__(self, idx, pos=(0,0)):
      self.idx = idx 
      self.pos = pos 
      self.edges = []

    def add_edge(self, v2, move):
      self.edges.append((v2, move))

  def __init__(self, lines):    
    self.V = []
    self.parse_graph(lines)    

  def get_a_random_vertex_pos(self):
    v_idx = random.randint(0, len(self.V)-1)
    return self.V[v_idx].pos

  def parse_graph(self, lines):
    self.height = len(lines)
    self.width = len(lines[0])
    self.map_pos_vertex = {} 
    vertex_idx = 0

    # parse vertices
    # ==============
    for row in range(self.height):
      for col in range(self.width):
        if lines[row][col] != "1":
          self.V.append(self.Vertex(idx=vertex_idx, pos=(row, col)))
          self.map_pos_vertex[(row, col)] = vertex_idx
          vertex_idx += 1

    # parse edges
    # ===========
    self.parse_edges(lines)
    
  def is_inside_level(self, p):
    return 0 <= p[0] and p[0] < self.height and 0 <= p[1] and p[1] < self.width

  def parse_edges(self,lines):
    for v in self.V:
      for i in range(len(self.NEIGHBOUR_OFFSET)):
        n = self.NEIGHBOUR_OFFSET[i]
        q = (v.pos[0] + n[0], v.pos[1] + n[1])
        
        if self.is_inside_level(q) and lines[q[0]][q[1]] != "1":          
          q_idx = self.map_pos_vertex[q]          
          v.add_edge(self.V[q_idx], self.Move(i))

  def shortest_path(self, orig, target):
    # BASED ON Dijkstra Algorithm
    # https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra
    dist = [self.MAX_DIST] * len(self.V)
    visited = [False] * len(self.V)
    path = [(0,0)] * len(self.V)

    orig_idx = self.map_pos_vertex[orig]
    target_idx = self.map_pos_vertex[target]

    pq = PriorityQueue()
    dist[orig_idx] = 0

    pq.put((dist[orig_idx], orig_idx))

    while not pq.empty():      
      p = pq.get()
      u_idx = p[1]      

      if not visited[u_idx]:
        u = self.V[u_idx]
        visited[u_idx] = True                

        for n in u.edges:
          v = n[0]
          move = n[1]

          if dist[v.idx] > (dist[u.idx] + 1):
            dist[v.idx] = dist[u.idx] + 1
            pq.put((dist[v.idx], v.idx))
            path[v.idx] = (u.idx, move) 

    p_idx, p_move = path[target_idx]
    r_path_moves = [p_move] # reversed path moves
    
    while p_idx != orig_idx:
      p_idx, p_move = path[p_idx]
      r_path_moves.append(p_move)

    return list(reversed(r_path_moves)), path, orig_idx, target_idx


  def __str__(self):
    s = ""
    for v in self.V:
      s += str(v.idx) + ": "
      for e in v.edges:
        s += str(e[0].idx) + " "
      s += "\n"
    
    return s
      