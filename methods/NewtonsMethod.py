def newton(f, df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print(f"Found solution after {n} iterations")
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            print("Zero derivative. No solution found.")
            return None
        xn -= fxn/dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None