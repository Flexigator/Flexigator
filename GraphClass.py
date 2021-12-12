class Graph(object):
  def __init__(self, connectivityMap, initiate = True):
    self._connectivityMap = connectivityMap
    self._weightedEdges = False
    self._weightedVerticies = False

    if initiate:
      self.__initiate()

  def __initiate(self):
    for edge in self._connectivityMap:
      # Weighted edges
      if not self._weightedEdges and isinstance(edge, tuple):
        self._weightedEdges = True

      for target in self.getConnections(edge):
        # Weighted verticies
        if not self._weightedVerticies and isinstance(target, tuple):
          self._weightedVerticies = True

  def getConnections(self, edge):
    return self._connectivityMap[edge]

  def hasWeightedEdges(self):
    return getattr(self, '_weightedEdges')

  def hasWeightedVerticies(self):
    return getattr(self, '_weightedVerticies')

  def isEuler(self):
    return getattr(self, '_isEuler')

  def __str__(self):
    return f'kek'

g1 = Graph({
  ("a", 2): ["b", "c"],
  "b": ["a", ("c", 5)],
  "c": ["a", "b"]
})

print(f'Weighted edges: {g1.hasWeightedEdges()}; Weighted verticies: {g1.hasWeightedVerticies()}')
