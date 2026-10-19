class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        # Find all suspicious methods
        group = {k}
        queue = deque([k])

        while queue:
            method = queue.popleft()

            for nxt in graph[method]:
                if nxt not in group:
                    group.add(nxt)
                    queue.append(nxt)

        # Check for incoming edges from outside the group
        for a, b in invocations:
            if a not in group and b in group:
                return list(range(n))

        # Remove suspicious methods
        return [i for i in range(n) if i not in group]