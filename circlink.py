class node:
    def __init__(self, item):
        self.item = item
        self.link = None

class Clinklist:
    def __init__(self):
        self.start = None
        self.temp = None

    def rear_insertion(self, item):
        nd = node(item)
        if self.start is None:
            self.start = nd
            nd.link = self.start
            self.temp = nd
        else:
            self.temp.link = nd
            nd.link = self.start
            self.temp = nd

        print("The item", item, "has been successfully inserted at the rear of the list")

    def front_insertion(self, item):
        nd = node(item)
        if self.start is None:
            self.start = nd
            temp = nd
            nd.link = self.start
            print("The item", item, "has been successfully inserted at the front of the list")
            return
        temp = self.start
        while temp.link != self.start:
            temp = temp.link
        nd.link = self.start
        temp.link = nd
        self.start = nd
        print("The item", item, "has been successfully inserted at the front of the list")

    def insertion_after_specific_item(self, item, value):
        temp = self.start
        while temp is not None:
            if temp.item == item:
                nd = node(value)
                nd.link = temp.link
                temp.link = nd
                print("The item", value, "has been successfully inserted after", item)
                return
            temp = temp.link
        print("The item", item, "was not found in the list.")

    def insert_at_position(self, pos, item):
        nd = node(item)
        prev = temp = self.start
        i = 1
        while temp is not None and i < pos:
            prev = temp
            temp = temp.link
            i += 1
        if temp is None:
            prev.link = nd
            return
        if prev is None:
            nd.link = self.start
            self.start = nd
            return
        prev.link = nd
        nd.link = temp
        print("The item", item, "has been successfully inserted at position", pos)

    def delete_start_node(self):
        if self.start is None:
            print("The list is empty. Nothing to delete.")
            return

        temp = self.start

        if self.start.link == self.start:
            self.start = None
        else:
            last = self.start
            while last.link != self.start:
                last = last.link

            self.start = temp.link
            last.link = self.start

        del temp
        print("The first item has been successfully deleted from the list")

    def delete_last_node(self):
        if self.start is None:
            print("The list is empty. Nothing to delete.")
            return

        temp = self.start
        prev = None

        while temp.link != self.start:
            prev = temp
            temp = temp.link

        if prev is None:
            self.satrt = None
        else:
            prev.link = self.start
        del temp
        print("The last node has been successfully deleted from the list.")        

    def display(self):
        if self.start is None:
            print("The list is empty.")
            return
        current = self.start
        while True:
            print(current.item, end=" → ")
            current = current.link
            if current == self.start:
                break
        print(self.start.item)

cl = Clinklist()

while True:
    print("\nMenu:")
    print("1. Insert at Rear")
    print("2. Insert at Front")
    print("3. Insert after specific item")
    print("4. Insert at Position")
    print("5. Delete First Node")
    print("6. Delete Last Node")
    print("7. Display List")
    print("8. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        item = input("Enter the item to insert at rear: ")
        cl.rear_insertion(item)
    elif ch == 2:
        item = input("Enter the item to insert at front: ")
        cl.front_insertion(item)
    elif ch == 3:
        item = input("Enter the item after which you want to insert: ")
        value = input("Enter the item to insert: ")
        cl.insertion_after_specific_item(item, value)
    elif ch == 4:
        position = int(input("Enter the position to insert the item: "))
        item = input("Enter the item to insert: ")
        cl.insert_at_position(position, item)
    elif ch == 5:
        print("Deleting the first node")
        cl.delete_start_node()
    elif ch == 6:
        print("Deleting the last node")
        cl.delete_last_node()
    elif ch == 7:
        cl.display()
    elif ch == 8:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")