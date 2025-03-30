import math

def solve_cubic(a, b, c, d):
    b /= a
    c /= a
    d /= a

    p = (3 * c - b**2) / 3
    q = (2 * b**3 - 9 * b * c + 27 * d) / 27
    delta = (q**2 / 4) + (p**3 / 27)

    if delta > 0:
        u = (-q / 2 + math.sqrt(delta))**(1/3)
        v = (-q / 2 - math.sqrt(delta))**(1/3)
        y1 = u + v
    else:
        r = math.sqrt(-p**3 / 27)
        theta = math.acos(-q / (2 * r))
        y1 = 2 * (-p / 3)**0.5 * math.cos(theta / 3)

    x1 = y1 - b / 3
    return x1

choices = int(input('''Choose an equation type:
1. Cubic equation
2. Quartic equation
3. Quadratic equation
'''))

if choices == 1:
    print("The root of a cubic equation is in the form ax^3 + bx^2 + cx + d = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    roots = solve_cubic(a, b, c, d)
    print("The root of the equation is:", roots)

elif choices == 2:
    print("The root of a quartic equation is in the form ax^4 + bx^3 + cx^2 + dx + e = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    e = float(input("Enter e: "))

    b /= a
    c /= a
    d /= a
    e /= a

    p = (c - (3 * b**2) / 8)
    q = (d - (b * c) / 2 + (b**3) / 8)
    r = (e - (b * d) / 4 + (b**2 * c) / 16 - (3 * b**4) / 256)

    y = solve_cubic(1, 2 * p, p**2 - 4 * r, -q**2)

    R = math.sqrt(p + 2 * y)
    D1 = math.sqrt(y**2 - 4 * r)
    D2 = math.sqrt(2 * y - p - (2 * q / R))

    x1, x2 = (R - D1) / 2, (R + D1) / 2
    x3, x4 = (R - D2) / 2, (R + D2) / 2

    shift = b / 4
    root1, root2, root3, root4 = x1 - shift, x2 - shift, x3 - shift, x4 - shift

    print("The roots of the equation are:", root1, root2, root3, root4)

elif choices == 3:
    print("The root of a quadratic equation is in the form ax^2 + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print("Equation has no real roots")
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("The roots of the equation are:", root1, root2)