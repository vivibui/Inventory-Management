#Author: Vivian Bui
#Final Project
#Date: 05/10/2021
#Description: Inventory Class
    
    
class Inventory: 
    
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = int(new_stock)
        self.__price = new_price
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_stock(self):
        return self.__stock
    
    def get_price(self):
        return self.__price
    
    def restock(self, new_stock):
        self.__stock -= new_stock 
        if self.__stock >=0: 
            return True
        else: 
            self.__stock += new_stock
            return False
        
    def purchase(self, purch_qty):
        self.__stock -= purch_qty
        if self.__stock >=0: 
            return True
        else: 
            self.__stock += purch_qty
            return False
        
    def __str__(self): 
         return (self.__id + '\t' + format(self.__name, '20') + '\t'+ '$' + format(self.__price, '10') + '\t' + format(self.__stock, '6'))
        
    

