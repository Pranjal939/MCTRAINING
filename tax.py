def multiply_list(numbers, multiplier):
    result = []
    for num in numbers:
        result.append(num * multiplier)
    return result
prices = [100, 250, 399, 50]

final_prices = multiply_list(prices, 1.2)
print("Prices after 20% tax:", final_prices)

print(final_prices)
