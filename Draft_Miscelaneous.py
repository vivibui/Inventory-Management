TransactionList = []
for instance in InventoryList: 
    if product_ID == int(instance.get_id()):
        TransactionList.append(instance) 
        
#%%    
        
def process_transaction(transaction_class, productID):
    
    transaction_list = []
    file = open('Inventory.txt', 'r')
    trans_id = file.readline().rstrip('\n')
    
    while trans_id != '':
        
        trans_name = file.readline().rstrip('\n')
        trans_quantity = file.readline().rstrip('\n')
        trans_price = file.readline().rstrip('\n')
        
        if int(trans_id) == int(productID): 
            transaction_class.set_id(trans_id)
            transaction_class.set_name(trans_name)
            transaction_class.set_quantity(trans_quantity)
            transaction_class.set_price(trans_price)
            
            trans_instance = transaction_class() 
            transaction_list.append(trans_instance)
            
        trans_id = file.readline().rstrip('\n')
        
    file.close()
    print(transaction_list)
    
    return transaction_list
#%%

my_transaction = transactionitem.TransactionItem()
TransactionList = []
for instance in InventoryList: 
    if product_ID == int(instance.get_id()):
        TransactionList.append(instance) 
            
        trans_id = product_ID
        trans_name = instance.get_name() 
        trans_quantity = instance.get_stock()
        trans_price = instance.get_price() 
            
        my_transaction.set_id(trans_id)
        my_transaction.set_name(trans_name)
        my_transaction.set_quantity(trans_quantity)
        my_transaction.set_price(trans_price) 
#%%





my_transaction = transactionitem.TransactionItem()
    TransactionList = []
    for instance in InventoryList: 
        if product_ID == int(instance.get_id()):
                
            trans_id = product_ID
            trans_name = instance.get_name() 
            trans_quantity = instance.get_stock()
            trans_price = instance.get_price() 
                
            my_transaction.set_id(trans_id)
            my_transaction.set_name(trans_name)
            my_transaction.set_quantity(trans_quantity)
            my_transaction.set_price(trans_price) 
            
            trans_instance = my_transaction
            
            TransactionList.append(trans_instance)
            
            
#%%
print_inventory(InventoryList)
        product_ID = get_item_id(InventoryList)
        if product_ID == 0: 
            flag = 0 
        else: 
            for instance in InventoryList:
                if product_ID == int(instance.get_id()):
                    product_instance = instance
                    
            new_quantity = get_quantity(product_instance)
            
            trans_id = product_ID
            trans_name = product_instance.get_name() 
            trans_quantity = new_quantity
            trans_price = float(product_instance.get_price())
                        
            my_transaction.set_id(trans_id)
            my_transaction.set_name(trans_name)
            my_transaction.set_quantity(trans_quantity)
            my_transaction.set_price(trans_price)
            
            TransactionList.append(my_transaction)
            
            flag = 1 
    
    print_invoice(TransactionList)
#%%

if new_quantity != None: 
                        
                        my_transaction.set_quantity(trans_quantity)
                        my_transaction.set_id(product_ID)
                        my_transaction.set_name(instance.get_name())
                        my_transaction.set_price(float(instance.get_price()))
                        total_cost = my_transaction.calc_cost()
                        
                    TransactionList.append(my_transaction)
                    TotalCostList.append(total_cost)
        
    print_invoice(TransactionList, TotalCostList)
    
    
    
#%%

for instance in InventoryList: 
                if product_ID == int(instance.get_id()):
                    return instance
                
                    trans_quantity, new_quantity = get_quant(instance)
                    trans_name = instance.get_name()
                    trans_price= float(instance.get_price())
                    
                    my_transaction.set_id(product_ID)
                    my_transaction.set_name(trans_name)
                    my_transaction.set_price(trans_price)
                    my_transaction.set_quantity(trans_quantity)
                    trans_cost = my_transaction.calc_cost()
                
                    if my_transaction.get_quantity() != None: 
                        object_list[0] = my_transaction.get_id()
                        object_list[1] = my_transaction.get_name()
                        object_list[2] = my_transaction.get_price()
                        TransactionList.append(object_list)
                        TotalCostList.append(trans_cost)          
            flag = 1
        
    print_invoice(TransactionList, TotalCostList) 