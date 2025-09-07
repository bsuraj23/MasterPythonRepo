from collections import deque

dq = deque()

# Add elements
dq.append(1)         # Right side
dq.appendleft(2)     # Left side
print(dq)            # deque([2, 1])

# Remove elements
dq.pop()             # Removes from right (1)
dq.popleft()         # Removes from left (2)
