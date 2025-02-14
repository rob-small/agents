import sys

print("Python version:", sys.version)
print("Python executable:", sys.executable)

try:
    import math
    print("Math module loaded successfully")
except ImportError as e:
    print("Error loading math module:", e)

try:
    print("2 + 2 =", 2 + 2)
except Exception as e:
    print("Error performing arithmetic:", e)

print("Test complete")