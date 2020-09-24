from statistics import mean


def run_timing():
    times = []
    while True:
        user_input = input("Enter 10 km time: ")
        if user_input:
            times.append(float(user_input))
        else:
            break
    print(f"Average of {mean(times)}, over {len(times)} runs")
