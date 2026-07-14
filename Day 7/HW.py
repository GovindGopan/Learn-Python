inventory = []

def add_item(item):
    inventory.append(item)

def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    for item in inventory:
        show_item(item)

    total_item = count_items(inventory)
    print("\nTotal items: ", total_item)

def count_items(items):
    if len(items) == 0:
        return 0
    else:
        return 1 + count_items(items[1:])

show_item = lambda item: print(f"Item in Stock: {item}")

main()