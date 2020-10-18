from scipy.sparse import *
import numpy as np
import time

def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  0 -1  1  0  0
            1  0  1  0  0 -1  0
            2  0  0  0 -1  0  1
            3  0  0  1  0  0 -1
            4 -1  1  0  0  0  0
        The size of the matrix is (5,6)
    '''
    mat = csr_matrix(sets)
    edge_num = mat.shape[0]
    for i in range(edge_num):
      end = (mat[0]==1).indices[0] # ending node of first edge
      critical = csr_matrix(mat.T[end]==-1).indices # 1 to -1 (starting at 'end' in first row)

      if len(critical)==0: # deadend, no need to consider
        mat = mat[1:]
        continue

      # detect cycle
      start = (mat[0]==-1).indices[0] #starting node of first edge
      cycle = csr_matrix(mat.T[start]==1).indices # -1 to 1 (ending at 'start' in first row)
      if np.in1d(critical, cycle).any():
        return True

      # append new edges and delete first edge
      new_edge = []
      origin = mat[0].toarray()[0]
      for row in critical:
        new_edge.append(origin + mat[row].toarray()[0])
      mat = csr_matrix(vstack([mat[1:], new_edge]))
    return False
