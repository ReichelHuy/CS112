n = int(input())
tasks = []

for _ in range(n):
    ti, di = map(int, input().split())
    tasks.append((ti, di))

tasks.sort(key=lambda x: (x[0], -x[1])) 

total_earnings = 0
current_time = 0

for task in tasks:
        total_earnings += task[1] - (current_time + task[0])
        current_time += task[0]

print(total_earnings)