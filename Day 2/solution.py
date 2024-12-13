PATH = "input.txt"

def increasing(arr: list) -> bool:
    for i in range(1, len(arr)):
        if not (3 >= arr[i] - arr[i-1] >= 1):
            return False
    return True

def decreasing(arr: list) -> bool:
    for i in range(1, len(arr)):
        if not (3 >= arr[i-1] - arr[i] >= 1):
            return False
    return True

with open(PATH, "r") as lines:
    count = 0
    for report in lines:
        report = [int(r) for r in report.split()]
        if increasing(report) or decreasing(report):
            count += 1
            print(report)
    print(count)