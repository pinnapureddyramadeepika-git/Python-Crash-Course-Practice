sandwich_orders = ['veg sandwich','cheese sandwich','crispy sandwich',
                   'egg sandwich','corn sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
       print(f"Today {sandwich} was made.")
