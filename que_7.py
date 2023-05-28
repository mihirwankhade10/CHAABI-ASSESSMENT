"""Q7. Calculate the factorial of a number using lambda function."""

#Code 

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Test the lambda function
number = 5
result = factorial(number)
print(result)
