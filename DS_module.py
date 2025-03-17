# this class represent a hash table to store table in the table using hash function

class HashTable:
    def __init__(self):
        self.table = {}
        self.key = 0
        self.wordValue = 0
        self.table_capacity = 0
        self.alphabet = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
    'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26 
}

# third level abstraction method

    def  index_words_into_the_table(self, data, sizeData):
        words = self.split_into_word(data)
        table = self.process(words, sizeData)
        return table

    #this method set the different value used by the hash table

    def setTable(self):
        data = input('Enter the data to be stored in the table: ')
        capacity = int(input('Enter the size of the table (max size: 256): '))
        sizeData = self.size_value(data)
        table_capacity = self.set_table_capacity(capacity)
        state = self.isDataOverflow(sizeData, table_capacity)
        return sizeData, table_capacity, state, data

# second level abstraction method

    def set_table_capacity (self, capacity):
        if (capacity == 256):
            self.table_capacity = 1000000
        else:
            self.table_capacity = capacity
        return self.table_capacity

    def isDataOverflow(self, data_size, capacity):
        if (capacity >= data_size):
            print('Data size is enough for the table')
            return True
        else:
            print('Data size is too much for the table')
            return False

    # this method take a word as input and add it to the hash table

    def process(self, words, sizeData):
        for word in words:
            key = self.keyValue(word)
            index = self.findIndex(key, sizeData)
            table = self.addWord(index, word)
        return table

    def keyValue(self, word):
        letters = self.split_word_into_letter(word)
        for letter in letters:
            letterValue = self.find_letter_value(letter)
            self.key = self.wordKeyValue(letterValue)
        return self.key


# first level abstraction method

    def addWord(self, index, word):
        self.table[index] = word
        return self.table

    def size_value(self, data):
        cleanData = data.replace(" ", "")
        data_size = len(cleanData)
        return data_size

    def split_into_word(self, data):
        individual_words = data.split(' ')
        return individual_words

    def split_word_into_letter(self, individual_word):
        letters = list(individual_word)
        return letters

    def find_letter_value(self, letter):
        letter = letter.lower()
        letterValue = self.alphabet[letter]
        self.key = letterValue
        return self.key

    def wordKeyValue(self, key):
        self.wordValue += key
        return self.wordValue

    def findIndex(self, key, size):
        index = key % size
        return index

class LMS_hastable(HashTable):
    def __init__(self):
        self.capacity = 100
        self.ascii_value = 0
        list_of_book = [[] for _ in range(self.capacity)]
   
    def find_number_value(self, number):
        value = ord(number)
        return value

    def hashFunction(self, ISBN):
        numbers = self.split_word_into_letter(ISBN)
        for number in numbers:
            self.ascii_value += self.find_number_value(number)
        index = self.findIndex(self.ascii_value, self.capacity)
        return index

    def insert_book(self, ISBN, book):
        index = hashFunction(ISBN)
        for pair in self.list_of_book[index]:
            if pair[0] == ISBN:
                pair[1] = book
                return 
            else:
                self.list_of_book[index].append([ISBN, book])
    
    def display_list_of_book(self):
        print(self.list_of_book)


# this class represent a stack data structure FILO to handle data

class Stack:
    def __init__(self):     
        self.stack = []

    def push(self, item):
        self.stack.append(item) #O(1)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() #o(1)
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]   #O(1)
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0 #O(1)

    def size(self):
        return len(self.stack) #O(1)

    def print_stack(self):
        for item in reversed(self.stack):
            print(item)

# this class represent a frequencyCount data strucutre that count the frequnecy use of an object

class frequencyCount:
    def __init__(self):
        self.bookList = {'Bible': 0, 'Dictionnary':0, 'Novel':0, 'Geography':0}
        self.most_popular_search = []

    def addBook(self, bookName):
        self.bookList[bookName] = 0

    def searchBook(self, bookName):
        if bookName in self.bookList:
            self.increment(bookName)
            return bookName
        else:
            return "This book is not in the list"

    def Display_book_frequency(self):
        for bookName, count in self.bookList:
            print(f'{bookName}:{count} times')

    def increment(self, bookName):
        if bookName in self.bookList:
            self.bookList[bookName] += 1
        else:
            self.bookList[bookName] = 0

    def sort_value(self):
        valueList = [self.bookList[key] for key in self.bookList]
        valueList.sort()
        valueList.reverse()
        return valueList

    def popular_search(self, valueList):
        self.most_popular_search.clear()
        sorted_items  = sorted(self.bookList.items(), key = lambda x: x[1], reverse = True)
        for key, value in sorted_items:
            if value in valueList:
                self.most_popular_search.append(key)
        return self.most_popular_search

    def display_popular_search(self):
        valueList = self.sort_value()
        popularSearch = self.popular_search(valueList)
        return popularSearch

# this class represent a node in a simple linked list
# a node is the basic unit of a linked list

class Node:
    def __init__(self, data):
        self.data = data    # stores the data of the node
        self.next = None    # Points to the next node (initially none)

# this class represent the implementation of a linked list

class LinkedList:
    def __init__(self):
        self.head = None    # the list start empty

    def insert_at_beginning(self, data):
        print(data)
        new_node = Node(data)   # create a new node
        new_node.next = self.head   # Link the new node to the previous head
        self.head = new_node    # update the point to the new node

    def instert_at_end(self, data):
        new_node = Node(data)   
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:        # traverse to the last node
            last = last.next
        last.next = new_node    # link the last node to the new node

    def delete(self, key):
        current = self.head
        if current and current.data == key:     # if the node to delete is the head
            self.head = current.next            # Move the head to the next node
            current = None
            return
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next
        if not current: #if the node to delete is not found 
            return "Node not found"

        prev.next = current.next    #Unlink the node
        current = None
    
    def print_list(self):
            current = self.head
            if not current:
                print('List is empty')
                return

            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None") # end of the list


