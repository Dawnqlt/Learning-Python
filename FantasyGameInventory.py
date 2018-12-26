''' Fantasy Game Inventory - 
Automate the Boring stuff with Python
'''
def displayInventory(i):
    print('Inventory:')
    a = ''
    for k, v in i.items():
        a = str(v)+ " "+k
        print(a)
    print('Total number of items:',str(sum(i.values())))


dragonLoot = ['gold coin', 'dagger', 'gold coin', 
              'gold coin', 'ruby']

def addToInventory(inventory,addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item,0)+1
    return inventory
            
inv = {'gold coin': 42, 'rope': 1, 'torch': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)