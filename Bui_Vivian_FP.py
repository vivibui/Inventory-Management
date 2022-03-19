#Author: Vivian Bui
#Final Project
#Date: 05/10/2021
#Description: Program to manage inventory and keep track of purchase/return





#Process the initial inventory file
def process_inventory(inventory_class):
    
    #Initiate list to store instances 
    inventory_list = []
    
    #Open the initial inventory file
    file = open('Inventory.txt', 'r')
    
    #Read the first line 
    product_id = file.readline().rstrip('\n')
    
    #Create loop to read file and store instances to list
    while product_id != '':
        
        product_name = file.readline().rstrip('\n')
        product_stock = file.readline().rstrip('\n')
        product_price = file.readline().rstrip('\n')
       
        product_instance = inventory_class(product_id, product_name, product_stock, product_price)
        
        inventory_list.append(product_instance)
        
        product_id = file.readline().rstrip('\n')
    
    #Close the file
    file.close()
    
    #Return a list of instances of initial inventory 
    return inventory_list

    
    






#Print the menu
def print_inventory(productlist):
    
    print()
    
    #Print header
    header = 'ID\tItem\tPrice\tQty Available'
    print(header.expandtabs(14))
    
    #Print list of items
    for product in productlist:
        print(product)
    print('Enter 0 when finished.')


 






#Get the ID of an item that customer wants to purchase or return
def get_item_id(inventory_list):
    
    #Initiate list to store the ID 
    ID_list = []
    for item in inventory_list: 
        item_ID = int(item.get_id())
        ID_list.append(item_ID)
    
    #Create loop to validate input for ID 
    flag = 1
    while flag == 1: 
        try:
            get_id = int(input('Please input the item ID you want to purchase/return: '))
            
            #Loop ends when enter 0
            if get_id == 0: 
                flag = 0 
            
            else: 
                #Loop continues if ID cannot be found in ID list
                if get_id not in ID_list: 
                    print()
                    print('Item not found. Please try again.')
                    flag = 1 
                #Loop ends if ID is found in the list
                else: 
                    flag = 0

        except: 
            print()
            print('Invalid input.')
            flag = 1
    
    #Return the ID of an item customer inputted 
    return get_id









#Get quantity (purchase or return) of the selected item 
def get_quant(Instance): 
    
    #Create loop to get quantity 
    flag = 2
    while flag == 2: 
        try: 
            get_stock = int(input('Please enter the desired quantity (negative quantity for return): '))
            
            #Purchased item
            if get_stock >= 0: 
                new_stock = Instance.purchase(get_stock)
                if new_stock == True: 
                    trans_stock = get_stock
                else: 
                    print('Sorry, we do not have enough stock.') 
                    trans_stock = None 
                flag = 0
            
            #Returned item
            else: 
                new_stock = Instance.restock(get_stock)
                if new_stock == True: 
                    trans_stock = get_stock 
                else: 
                    trans_stock = None 
                flag = 0 
        
        except: 
            print('Please enter a valid number.')
            flag = 2
    
    #Return the quantity inputted for transaction
    return trans_stock

            

    





#Print the invoice
def print_invoice(transaction_list, totalcost_list, tax_rate): 
    
    #Print header
    header = 'ID\tItem\tQuantity\tPrice\tTotal'
    print()
    print()
    print('---------------------------Invoice---------------------------')
    print(header.expandtabs(14))
    
    
    #Print list of purchased or returned items 
    count = 0
    subtotal = 0
    
    #Print ID, name, quantity, price
    for product in transaction_list:
        print(product, end='')
        print('\t' + '$' + str(totalcost_list[count]))
        count+=1
    
    #Print total cost of a purchased or returned item
    for cost in totalcost_list: 
        subtotal+=cost
    
    
    #Calculate tax and total 
    tax = subtotal*tax_rate
    total = subtotal + tax
    
    #Print subtotal, tax, and total cost 
    print()
    print()
    print('Price: $' + str(format(subtotal, '.2f')))
    print('Tax: $' + str(format(tax,'.2f')))
    print('Total: $' + str(format(total, '.2f')))
    



 




#Write the updated inventory to a new file 
def write_updated_inventory(inventorylist, updated_trans_list, trans_id_list):
    
    
    #Open and/or create the new file 
    file_new = open('UpdatedInventory.txt', 'w')
    
    
    #Initiate lists
    #List of ID of all item in the initial inventory 
    full_id_list = []
    #List of items (instances) that are neither purchased and nor returned
    inventory_minus_trans_list = []
    
    
    #Write all items with updated quantity to the file
    for item in updated_trans_list: 
        
        item_trans_ID = item.get_id()
        item_trans_name = item.get_name()
        item_trans_quantity = item.get_quantity()
        item_trans_price = item.get_price()
        
        file_new.write(str(item_trans_ID) + '\n')
        file_new.write(item_trans_name + '\n')
        file_new.write(str(item_trans_quantity) + '\n')
        file_new.write(str(item_trans_price) + '\n')
    
        
    #Create list of ID of all item in the initial inventory 
    for item in inventorylist: 
        productID = int(item.get_id())
        full_id_list.append(productID)
    
    
    #Create a list that stores ID of all items that are neither purchased and nor returned    
    list_difference = list(set(full_id_list) - set(trans_id_list))
        
    
    #Create a list of items (instances) that are neither purchased and nor returned
    for item in inventorylist: 
        for num in list_difference: 
            if int(item.get_id()) == num: 
                inventory_minus_trans_list.append(item)
    
                
    #Write the rest of items from the menu to the file 
    for item in inventory_minus_trans_list: 
        
        item_diff_ID = item.get_id()
        item_diff_name = item.get_name()
        item_diff_quantity = item.get_stock()
        item_diff_price = item.get_price()
        
        file_new.write(str(item_diff_ID) + '\n')
        file_new.write(item_diff_name + '\n')
        file_new.write(str(item_diff_quantity) + '\n')
        file_new.write(str(item_diff_price) + '\n')
    
    
    #Close the file 
    file_new.close()
    
    
    
    
    
    
    
    
    
def main():
    
    
    #Import modules 
    import inventory
    import transactionitem 
    import copy
    
    
    #Create object for Transaction Item class 
    my_transaction = transactionitem.TransactionItem() 
    
    
    #Call process inventory function and get list of initial inventory
    InventoryList = process_inventory(inventory.Inventory)
    
    
    #Initiate lists
    #List of purchased or returned items with info from initial inventory file 
    slice_inventory = []
    #List of purchased or returned items 
    TransactionList = []
    #List of the cost for each purchased or returned items 
    TotalCostList = []
    #List of updated quantity for each purchased or returned items 
    NewQuantityList = []
    #List of updated information for each instance in TransactionList  
    UpdatedTransList = []
    #List of ID of instances comes from UpdatedTransList 
    TransactionIDList = []
    
    
    #Initiate tax rate 
    SALE_TAX = 0.085
    
    
    #Create loop for the main program 
    flag = 1
    loop = -1
    
    while flag == 1: 
        
        #Print the menu
        print_inventory(InventoryList)
        
        #Get ID 
        product_ID = get_item_id(InventoryList)
        
        #Ends program if inputted ID is zero 
        if product_ID == 0: 
            flag = 0   
        
        else: 
            
            #Create a list of purchased or returned items with info from initial inventory file
            for item in InventoryList:
                if product_ID == int(item.get_id()):
                    slice_inventory.append(item)
                    break
            
            loop += 1
            
            #Get the ID, name, price, and quantity for each purchased or returned item 
            item = slice_inventory[loop]
            item_stock = int(item.get_stock())
            trans_ID = item.get_id()
            trans_name = item.get_name()
            trans_price = float(item.get_price())
            trans_quantity = get_quant(item)
            
            #Set ID, name, price, and quantity and calculate cost for each purchased or returned item 
            if trans_quantity != None: 
                
                my_transaction.set_id(trans_ID)
                my_transaction.set_name(trans_name)
                my_transaction.set_price(trans_price)
                my_transaction.set_quantity(trans_quantity)
                cost = my_transaction.calc_cost()            
                
                #Find the quantity in-stock after purchased/returned for each item 
                new_quantity = item_stock - trans_quantity
                
                #Create list of purchased/returned items 
                TransactionList.append(copy.deepcopy(my_transaction))
                #Create list of the cost for each purchased or returned items 
                TotalCostList.append(cost)
                #Create list of updated quantity for each purchased or returned items
                NewQuantityList.append(new_quantity)
    
    
    #Print the invoice 
    if loop == -1:
        print()
        print('Thank you for visiting.')
    else: 
        print_invoice(TransactionList, TotalCostList, SALE_TAX) 
    
    
    #Loop to create lists: 
    #UpdatedTransList: updated information for each instance in TransactionList   
    #TransactionIDList: IDs of instances comes from UpdatedTransList
    count = 0 
    for trans_item in TransactionList: 
        trans_item.set_quantity(NewQuantityList[count])
        itemID = int(trans_item.get_id())
        UpdatedTransList.append(copy.deepcopy(trans_item))
        TransactionIDList.append(itemID)
        count +=1
    
    
    #Write the updated inventory to a file 
    write_updated_inventory(InventoryList, UpdatedTransList, TransactionIDList)   
      
         
main()