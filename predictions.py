# from ast import Dict
from collections import defaultdict


Talladega = defaultdict(list)
Talladega["Joey Logano"] = {
    "points": 12000,
}
Talladega["Ryan Blaney"] = {
    "points",
    11000,
}
Talladega["Denny Hamlin"] = {
    "points",
    11000,
}
Talladega = {"Joey Logano": 12000, "Ryan Blaney": 11000, "Denny Hamlin": 9000}
print(Talladega)
print(Talladega["Joey Logano"])
for x in Talladega:
    # for y in x[0]:
    print(f"{type(Talladega[x])} {x:12} - {Talladega[x]:,}")


total = []


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
        total.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1 :]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    subset_sum([12000, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000], 50000)
    print(total)
