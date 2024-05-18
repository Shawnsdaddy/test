from typing import (
    List,
)
from collections import deque


def can_visit_all_rooms_solution2(rooms: List[List[int]]) -> bool:
    global visited_index
    visited_index = {0: True}

    def dfs(room, visiting):
        need_to_visit = {}
        keys = []
        for e in visiting:
            keys.extend(room[e])
        keys = set(keys)
        for e in keys:
            if e not in need_to_visit and e not in visited_index:
                need_to_visit[e] = True
                visited_index[e] = True
        if len(need_to_visit) > 0:
            dfs(room, set(need_to_visit))

    dfs(rooms, {0})
    return len(visited_index) == len(rooms)


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    queue = deque()
    queue.append(0)
    visited = set([])
    while len(queue) > 0:
        key = queue.pop()
        visited.add(key)
        keys = rooms[key]
        for e in keys:
            if e not in visited:
                queue.append(e)
    return len(visited) == len(rooms)


print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))
