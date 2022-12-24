def solution(string):
    a, b, c = map(int, string.split(" "))
    d = b**2 - 4 * a * c
    if a == 0:
        print(f" уравнение == {-c / b}")
    else:
        if d > 0:
            return (- b - (d ** 0.5)) / (2 * a), (- b + (d ** 0.5)) / (2 * a)
        elif d == 0:
            return - b + (d ** 0.5) / 2 * a
    return "нет решения"


print(solution(input("enter rations below:\n")))
