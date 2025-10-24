class Solution:
    # driller
    def dfs(self, adj):
        
        def util(currentNode):
            
            result.append(currentNode)
            visited.add(currentNode)
            
            for branch in adj[currentNode]:
                # avoid the function call to check visited
                if branch not in visited:
                    util(branch)
        
        visited = set()
        result = list()
        util(0)
        return result
