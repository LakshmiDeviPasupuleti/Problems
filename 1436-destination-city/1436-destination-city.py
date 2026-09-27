class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        outgoing=set()
        for path in paths:
            outgoing.add(path[0])
        for path in paths:
            if path[1] not in outgoing :
                return path[1]