def main():

    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    displayInventory(stuff)

def displayInventory(inv):

    size = len(inv)

    total = 0

    print("Inventory: ")

    for i, j in inv.items():
        print(i + " " + str(j))
        
        total = total + j

    print("Total number o items: " + str(total))

def addToInventory(inv, items):

    for i, j in items:

        inv.setdefault(i,0)

        inv[i] = inv[i] + j

if __name__ == "__main__":
    main()
