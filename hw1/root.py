"""
Lab 1 starter code
"""
def bisection(f, a, b, tol=1e-6, max_iters=50):
    """
    Implementation of the Bisection root finding algorithm

    Parameters
    ----------
    f
        A callable object representing a univariate function
    a
        The lower guess (should be set such that f(a) < 0)
    b
        The upper guess (should be set such that f(b) > 0)
    tol, optional
        Tolerance for the solver, by default 1e-6
    max_iters, optional
        Maximum number of iterations before raising RuntimeError, by default 50

    Raises
    ------
    RuntimeError
        If number of iterations exceeds max_iters
    """
    # Your implementation
    # NOTE: you should use a `while` loop for this implementation
    
    
    is_opposite_sign = lambda x, y: any((abs(f(x)) == f(x),abs(f(y)) == f(y))) and not all( (abs(f(x)) == f(x), abs(f(y)) == f(y)) )
    while max_iters > 0:
        midpoint = (a+b)/2
        output = f(midpoint)
        if abs(output)<=tol:
            return midpoint
        else:
            if is_opposite_sign(midpoint, a):
                b = midpoint                 
            elif is_opposite_sign(midpoint, b):
                a = midpoint
        max_iters -= 1
    raise RuntimeError("Iterations insufficient to reach tolerance.")
                
        


def newton(f, fp, x0, tol=1e-6, max_iters=50):
    """
    Implementation of Newton's root finding algorithm

    Parameters
    ----------
    f
        A callable object representing a univariate function
    fp
        A callable object representing the first derivative (f prime) of the
        univariate function
    x0
        Initial guess
    tol, optional
        Tolerance for the solver, by default 1e-6
    max_iters, optional
        Maximum number of iterations before raising RuntimeError, by default 50

    Raises
    ------
    RuntimeError
        If number of iterations exceeds max_iters
    """
    # Your implementation
    # NOTE: you should use a `for` loop for this implementation
    for _ in range(max_iters-1):
        if abs(f(x0)) < tol:
            return x0
        
        x0 = x0-f(x0)-fp(x0)
    
    raise RuntimeError("Iterations insufficient to reach tolerance.")
        
