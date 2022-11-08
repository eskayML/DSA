#
class Graph(dict):
  def add(self, v) # add a vertex
  	self[v] = set()
  
  def add_edge(self, u ,v): # add an edge from u to v
    self[u].add(v)
    self[v].add(u)

G = Graph() # Create a graph called G
for v in 'abcdefghijklm'.split():
  G.add(v) #add each letter as a vertex
  
for u,v in 'ab ac ai cd fg fl km'.split():
  G.add_edge(u,v) #add an edge from a to b, a to c, a to i and so on

print(G)
###RESULT### This is how our graph looks
#{'a': {'i', 'b', 'c'}, 'b': {'a'}, 'c': {'d', 'a'}, 'd': {'c'}, 'e': set(), 'f': {'l', 'g'}, 'g': {'f'}, 'h': set(), 'i': {'a'}, 'j': set(), 'k': {'m'}, 'l': {'f'}, 'm': {'k'}}

print("These are the neighbors of a: ", G['a'])
###RESULT### These are the neighbors of a, replace the indexing of G to get neighbors of a different vertex
#These are the neighbors of a: {'b', 'c', 'i'}

#Perform a breadth-first search
def breadth_first_search(G, start):
  waiting = [start] #pick a vertex to start the search
  found = {start}
  
  while len(waiting) != 0:
    w = waiting.pop(0)
    for x in G[w]: #This line loops through the neighbors of vertex w
      if x not in found:
        waiting.append(x)
        found.add(x)
  return found
