def order_sandwiches(*args):
    for elem in args:
        print(f"-{elem}")

    

order_sandwiches("Pomodoro", "Mozzarella")
order_sandwiches("Prociutto", "Olive", "Carciofi")
order_sandwiches("Porcini", "Tartufo", "Salsiccia")