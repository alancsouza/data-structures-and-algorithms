# Example inspired by Data Structures & Algorithms in Python
# Chapter 5: Linked lists
from typing import Any, Optional


class Link:
    def __init__(self, data: Any, next=None):
        self.__data = data
        self.__next = next
    
    def get_data(self):
        return self.__data
    
    def set_data(self, data: Any):
        self.__data = data
    
    def get_next(self):
        return self.__next
    
    def set_next(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise ValueError("Next link must be a link or None")
        
    def is_last(self) -> bool:
        return self.__next is None
    
    def __str__(self) -> str:
        return str(self.get_data())

class LinkedList:
    def __init__(self):
        self.__first: Link = None
    
    def get_first(self):
        return self.__first
    
    def set_first(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            ValueError("First link must be a link or None")
    
    def first(self):
        if self.is_empty():
            raise AttributeError("No first item in empty list")
        return self.get_first().get_data()   

    def is_empty(self) -> bool:
        return self.__first is None
    
    def traverse(self, func = print) -> None:
        link = self.get_first()

        while link is not None:
            func(link.get_data())
            link = link.get_next()
    
    def insert(self, data) -> None:
        link = Link(data, self.get_first())

        self.set_first(link)
    
    def find(self, goal, key=lambda x: x) -> Optional[Link]:
        link = self.get_first()

        while link is not None:
            if key(link.get_data()) == goal:
                return link
            link = link.get_next()
    
    def search(self, goal, key=lambda x: x):
        link = self.find(goal, key)

        if link is not None:
            return link.get_data()
    
    def insert_after(self, goal, new_data, key=lambda x: x) -> bool:
        link = self.find(goal, key)

        if link is None:
            return False
        
        new_link = link(new_data, link.get_next())
        link.set_next(new_link)

        return True
    
    def __len__(self) -> int:
        l : int = 0
        link = self.get_first()
        while link is not None:
            l += 1
            link = link.get_next()
        
        return l
    
    def __str__(self) -> str:
        result: str = "["
        link = self.get_first()

        while link is not None:
            if len(result) > 1:
                result += " > "
            result += str(link)
            link = link.get_next()

        return result + "]"
