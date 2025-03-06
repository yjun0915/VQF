from methods.NewtonsMethod import newton
from scipy.optimize import minimize

def compare_newton_bfgs():
    p = lambda x: x**3 - x**2  - 1
    dp = lambda x: 3*x**2 - 2*x
    bfgs = minimize(fun=p, x0=3, method='BFGS')
    approx = newton(f=p, df=dp, x0=3, epsilon=1, max_iter=10)
    print(f"{bfgs.x} and {approx}")

if __name__ == "__main__":
    compare_newton_bfgs()