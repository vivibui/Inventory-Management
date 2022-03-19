




def process_inventory():
    inventory_list = []
    file = open('Inventory.txt', 'r')
    product_id = file.readline().rstrip('\n')
    
    while product_id != '':
        sub_list = [0,0,0,0]
        sub_list[0] = product_id
        product_name = file.readline().rstrip('\n')
        product_stock = file.readline().rstrip('\n')
        product_price = file.readline().rstrip('\n')
       
        sub_list[1] = product_name
        sub_list[2] = product_stock
        sub_list[3] = product_price
        
        inventory_list.append(sub_list)
        
        product_id = file.readline().rstrip('\n')
        
    file.close()
    return inventory_list





def print_inventory(productlist):
    header = 'ID\tItem\tPrice\tQty Available'
    print(header.expandtabs(23))
    for product in productlist:
        line_display = product[0] + '\t' + product[1] + '\t' + '$' + product[3] + '\t' + product[2]
        print(line_display.expandtabs(23))
    
     
    

    

def main():
    InventoryList = process_inventory() 
    print_inventory(InventoryList)
    
main()
    
#%%

    
    
    def get_item_id(inventoryList): 
    flag = 1
    while flag == 1: 
        try: 
            itemID = int(input('Enter  '))        
    

  get_item_id(InventoryList)