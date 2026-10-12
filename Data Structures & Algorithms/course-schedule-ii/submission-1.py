class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]
        ans=[]

        for crs,pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1
        
        q=deque()

        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)
        
        finish=0

        while q:
            n=q.popleft()
            ans.append(n)
            finish+=1
            for nei in adj[n]:
                indegree[nei]-=1

                if indegree[nei]==0:
                    q.append(nei)
        
        return ans if finish==numCourses else []


        