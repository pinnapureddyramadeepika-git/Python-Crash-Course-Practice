def sandwiches(*items):
    print("\n Making the sandwich with the following items: ")
    for item in items:
        print(f"-{items}")
sandwiches('tomato')
sandwiches('cucumber','cheese','onion')    
sandwiches('chillies','origano powder')