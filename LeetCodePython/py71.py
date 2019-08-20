# 简化路径 linux
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []
        for path_item in path_list:
            if path_item == "":
                continue
            if path_item == "..":
                if stack:
                    stack.pop()
            elif path_item != '.':
                stack.append(path_item)
        
        return "/" + "/".join(stack)