#Author: Vivian Bui
#Final Project
#Date: 05/10/2021
#Description: Transaction Class


class TransactionItem: 
    
    def __init__(self):
        self.__id = 0
        self.__name = 0
        self.__quantity = 0
        self.__price = 0
        
    def get_id(self):
        return self.__id 
    
    def set_id(self, new_id):
        self.__id = new_id
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
        return self.__name
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity
        return self.__quantity 
    
    def get_price(self):
        return self.__price 
    
    def set_price(self, new_price):
        self.__price = new_price
        return self.__price
    
    def calc_cost(self):
        cost = (self.__quantity)*(self.__price)
        return float(format(cost, '.2f'))
    
    def __str__(self):
        return (str(self.__id) + '\t' + format(self.__name, '20') + '\t' + format(self.__quantity, '5') + '\t' + '\t' + '\t' + '$' + format(self.__price) + '\t') 