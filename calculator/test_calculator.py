import sys
sys.path.append('.')
from pkg.calculator import Calculator

calculator = Calculator()

try:
    result = calculator.evaluate("3 + 7 * 2")
    print(result)
except Exception as e:
    print(f"Error: {e}")