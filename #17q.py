N = int(input("Enter the value of N: "))

even_sum = 0

for num in range(2, N + 1, 2):
    even_sum += num

print(f"The sum of even numbers from 1 to {N} is {even_sum}.")
