sandwich_orders = ['veg sandwich','pastrami','cheese sandwich','pastrami',
                  'crispy sandwich','pastrami','egg sandwich','corn sandwich']
finished_sandwiches =[]
print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)