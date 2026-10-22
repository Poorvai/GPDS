# A simple custom function for a mathematical formula.

def compound_interest(principal, rate, years, times_per_year=1):
    """Return the final amount using A = P * (1 + r/n) ** (n * t).

    principal      : starting amount (P)
    rate           : annual interest rate as a decimal, e.g. 0.05 for 5% (r)
    years          : number of years (t)
    times_per_year : compounding frequency (n)
    """
    return principal * (1 + rate / times_per_year) ** (times_per_year * years)
