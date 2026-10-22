# main.py - calls the function defined in math_utils.py (a different file).

from math_utils import compound_interest

if __name__ == "__main__":
    amount = compound_interest(principal=1000, rate=0.05, years=10, times_per_year=12)
    print(f"1000 invested at 5% for 10 years (monthly compounding) = {amount:.2f}")
