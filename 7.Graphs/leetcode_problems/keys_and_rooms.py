class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        self.dfs(0, visited, rooms)
        return all(visited)

    def dfs(self, curRoom, visited, roomsAndKeys):
        visited[curRoom] = True
        currentRoomKeys = roomsAndKeys[curRoom]
        for key in currentRoomKeys:
            if not visited[key]:
                self.dfs(key, visited, roomsAndKeys)
