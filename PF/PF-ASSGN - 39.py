# PF-Assgn-39
# This verification is based on string match.     

# Global variables
menu = ('Veg Roll', 'Noodles', 'Fried Rice' , 'Soup')
quantity_available = [2, 200, 3, 0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    items = list(item_tuple[::2])
    ordered = list(item_tuple[1::2])
    for x in range (0, len(items)):
        if items[x] not in menu:
            print(items[x], "is not available")
        elif quantity_available[menu.index(items[x])] == 0:
            print (items[x], 'stock is over')
        elif items[x] in menu:
            print (items[x], "is available")
            check_quantity_available(menu.index(items[x]), ordered[x])
'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index, quantity_requested):
    if quantity_available[index]-quantity_requested!=-1:
        quantity_available[index]-=quantity_requested
        return True
    else:
        return False
    # Remove pass and write your logic here to return an appropriate boolean value.


# Provide different values for items ordered and test your program
#place_order("Veg Roll",2,"Noodles",2)
#place_order("Soup", 1, "Veg Roll", 2, "Fried Rice1", 1)
place_order ('Fried Rice',2,'Soup',1)