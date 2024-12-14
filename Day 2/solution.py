# Part 1

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
    print("Part 1 count:", count)


# Part 2

def increasing_with_dampener(arr: list) -> bool:
    
    
    for i in range(1, len(arr)):
        if not (3 >= arr[i] - arr[i-1] >= 1):
            return False
    return True

def decreasing_with_dampener(arr: list) -> bool:
    for i in range(1, len(arr)):
        if not (3 >= arr[i-1] - arr[i] >= 1):
            return False
    return True

with open(PATH, "r") as lines:
    count = 0
    for report in lines:
        report = [int(r) for r in report.split()]
        print(report)
        if increasing_with_dampener(report) or decreasing_with_dampener(report):
            count += 1
        else:
            for i in range(0, len(report)):
                tmp_report = report[:i] + report[i+1:]
                if increasing_with_dampener(tmp_report) or decreasing_with_dampener(tmp_report):
                    count += 1
                    break
    print("Part 2 count:", count)
