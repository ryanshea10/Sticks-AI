# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Player():
    
    def __init__(self):
        self.__left__  = 1
        self.__right__ = 1
    
    def bump(self, new_left, new_right):
        self.__left__  = new_left
        self.__right__ = new_right
    
    def get_left_hand(self):
        return self.__left__
    
    def get_right_hand(self):
        return self.__right__
    
    def update_left_hand(self, increment):
        self.__left__ += increment
        
        if self.__left__ > 4:
            self.__left__ = 0
    
    def update_right_hand(self, increment):
        self.__right__ += increment
        
        if self.__right__ > 4:
            self.__right__ = 0

    def has_lost(self):
        if self.__left__ == 0 and self.__right__ == 0:
            return True
        else:
            return False


