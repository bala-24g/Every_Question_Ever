class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses

        for course,prereq in prerequisites:
            graph[course].append(prereq)
            indegree[prereq]+=1
        
        dq=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                dq.append(i)
        ans=[]
        while dq:
            course=dq.popleft()
            ans.append(course)
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i]==0:
                    dq.append(i)
        if len(ans)==numCourses:
            return ans[::-1]
        else:
            return []

                



#Topo sort