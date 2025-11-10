print('''
Implementing Stack and Queue using List Data Type:
   Stack : 
      Stack is a linear data structure.
      It will store data in linear format.
      Stores items in a Last-In/First-Out (LIFO) or First-in/Last-Out (FILO) manner.
      The element store in last it will be in first number.
      Stack is used in  way suppose we have place books on top of each other first is c, 2nd c++, 3rd python. While picking this books we starts from python.

      Stack Operation:
        1) Push    = Inserting an elements.
        2) Pop     = Deletion an element (last element)
        3) Peek    = Display Last element
        4) Display = Display list
        5) Exit
           ___ 
        4 |___|
        3 |_2_| <= top 
        2 |_9_|
        1 |_6_|
        0 |_5_|
          Stack
           
\n''')

print("Implementing Stack")

l = []
while True:
    c = int(input('''
    1 Push Elements.
    2 Pop Elements.
    3 Peek Element.
    4 Display Stack.
    5 Exit.   
'''))
    if c == 1:
        n = input("Enter The Value :")
        l.append(n)
        print(l)

    elif c == 2:
        if len(l)== 0:
            print("Empty stack")
        else:
            l.pop()
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l[-1])

    elif c == 4:
        print(l)

    elif c == 5:
        break

    else:
        print("Invalid Operation")
        
print('''
Queue In Python:
      The Queue is a linear data structure.
      Strores items in first in first out (FIFO) manner.

Queue Operation:
      1) Enqueue : Adds an item to the queue.
      2) Dequeue : Remove an item from the queue.
      3) Front   : Get the front item from queue.
      4) Rear    : Get the last item from queue.
      5) Exit
      
      Rear                     Front
       ____________________________
      | 7 | 6 | 5 | 4 | 3 | 2 |   |  =>
      |___|___|___|___|___|___|___|
\n''')      

l = []
while True:
    c = int(input('''
    1 Push Elements.
    2 Pop First Elements.
    3 Front Element.
    4 Last Element.
    5 Display Queue.
    6 Exit.   
'''))
    if c == 1:
        n = input("Enter The Value :")
        l.append(n)
        print(l)

    elif c == 2:
        if len(l)== 0:
            print("Empty stack")
        else:
            del l[0]
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l[0])

    elif c == 4:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l[-1])

    elif c == 5:
        print(l)

    elif c == 6:
        break

    else:
        print("Invalid Operation")
        
