from methods.NewtonsMethod import newton

if __name__ == "__main__":
    p = lambda x: x**3 - x**2  - 1
    dp = lambda x: 3*x**2 - 2*x
    approx = newton(f=p, df=dp, x0=3, epsilon=1, max_iter=10)
    print(approx)