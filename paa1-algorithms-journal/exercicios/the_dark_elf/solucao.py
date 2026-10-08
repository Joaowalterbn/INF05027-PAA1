T = int(input())

for case in range(T):
    N, M = [int(x) for x in input().split()]

    reindeers = []

    for _ in range(N):
        reindeers_data = input().split()
        name = reindeers_data[0]
        weight = int(reindeers_data[1])
        age = int(reindeers_data[2])
        height = float(reindeers_data[3])

        reindeers.append((name, weight, age, height))
