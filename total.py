total_cost = 0
with open('product.csv','r') as file:
    for line in file:
        product,price = line.strip().split(',')
        total_cost += float(price)
    print(f"total cost :${total_cost:.2f}")

