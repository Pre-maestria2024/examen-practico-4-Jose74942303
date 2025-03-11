from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1
    
    if k == 0:
        print(0)
        return
    
    children = defaultdict(list)
    for _ in range(n - 1):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        children[u].append(v)
    
    if n == 0:
        print(0)
        return
    
    max_node = max(children.keys(), default=0)
    for vs in children.values():
        if vs:
            current_max = max(vs)
            if current_max > max_node:
                max_node = current_max
    
    size = max_node + 1
    groups = [0] * size
    streak = [0] * size
    
    stack = [(0, False)]
    
    while stack:
        node, visited = stack.pop()
        if not visited:
            stack.append((node, True))
            for child in reversed(children[node]):
                stack.append((child, False))
        else:
            if not children[node]:
                current_streak = 1
                sum_groups = 0
            else:
                sum_groups = sum(groups[child] for child in children[node])
                min_streak = min(streak[child] for child in children[node])
                current_streak = 1 + min_streak
            
            if current_streak >= k:
                groups[node] = sum_groups + 1
                streak[node] = 0
            else:
                groups[node] = sum_groups
                streak[node] = current_streak
    
    print(groups[0])

if __name__ == "__main__":
    main()
