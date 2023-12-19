def max_planets(n, intervals):
    intervals.sort(key=lambda x: x[1])  # Sap xep theo thu tu tang dan cua thoi gian
    max_planets = 0
    current_time = 0

    for interval in intervals:
        start_time, end_time = interval

        if start_time >= current_time:
            max_planets += 1
            current_time = end_time # Update time now 

    return max_planets

# Input
n = int(input())
intervals = []
for _ in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))

# Tinh so hanh tin kham pha duoc
result = max_planets(n, intervals)

# Output
print(result)