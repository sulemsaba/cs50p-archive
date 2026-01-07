# grocery.py — Week 3

def main():
    groceries = {}

    while True:
        try:
            get_item = input().strip()
        except EOFError:
            break

        if not get_item:
            continue

        get_item = get_item.lower()
        groceries[get_item] = groceries.get(get_item, 0) + 1

    for get_item in sorted(groceries):
        print(f"{groceries[get_item]} {get_item.upper()}")


if __name__ == "__main__":
    main()
