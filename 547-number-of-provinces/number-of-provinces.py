from scipy.sparse.csgraph import connected_components as cc
from numpy import array as arr


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        return cc(arr(isConnected))[0]
