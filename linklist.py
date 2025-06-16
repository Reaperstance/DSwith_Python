class Node:
    def __init__(self, name):
        self.info = name
        self.link = None

class SlList:
    def __init__(self):
        self.start = None

    def rear_insertion(self, item):
        nd = Node(item)
        if self.start is None:
            self.start = nd
            return
        temp = self.start

        while temp.link is not None:
            temp = temp.link
        temp.link = nd

    def front_insertion(self, item):
        nd = Node(item)
        nd.link = self.start
        self.start = nd

    def insertion_after_specific_item(self, item, value):
        temp = self.start
        while temp is not None:
            if temp.info == item:
                nd = Node(value)
                nd.link = temp.link
                temp.link = nd
                print("The item", value, "has been successfully inserted after", item)
                return
            temp = temp.link
        print("The item", item, "was not found in the list.")

    def insert_at_position(self, pos, item):
        nd = Node(item)
        prev = temp = self.start
        i= 1
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
        self.start = temp.link
        del temp
        print("The first item has been successfully deleted from the list.")

    def delete_last_node(self):
        if self.start is None:
            print("The list is empty. Nothing to delete.")
            return
        
        temp = self.start
        prev = temp
        while temp.link is not None:
            prev = temp
            temp = temp.link

        prev.link = None
        del temp
        print("The last item has been successfully deleted from the list.")

    def delete_specf_node(self, item):
        temp = self.start
        prev = None

        if temp is None:
            print("The list is empty. Nothing to delete.")
            return

        while temp is not None:
            if temp.info == item:
                if prev is None:
                    self.start = temp.link
                else: 
                    prev.link = temp.link
                del temp
                print("The item", item, "has been successfully deleted from the list.")
                return
            prev = temp
            temp = temp.link

        print("The item", item, "was not found in the list.")

    def display(self):
        temp = self.start
        if temp is None:
            print("The list is empty.")
            return
        while temp is not None:
            print(temp.info, end=" ► ")
            temp = temp.link
        print("None")

ob = SlList()

while True:
    print("\nMenu:")
    print("1. Insert at Rear")
    print("2. Insert at Front")
    print("3. Insert After Specific Item")
    print("4. Insert at Specific Position")
    print("5. Delete Specific Item")
    print("6. Delete Start Node")
    print("7. Delete Last Node")
    print("8. Display List")
    print("9. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        item = input("Enter the item to insert at rear: ")
        ob.rear_insertion(item)
    elif ch == 2:
        item = input("Enter the item to insert at front: ")
        ob.front_insertion(item)
    elif ch == 3:
        item = input("Enter the item after which you want to insert: ")
        value = input("Enter the item to insert: ")
        ob.insertion_after_specific_item(item, value)
    elif ch == 4:
        position = int(input("Enter the position to insert the item: "))
        item = input("Enter the item to insert: ")
        ob.insert_at_position(position, item)
    elif ch == 5:
        item = input("Enter the item to delete: ")
        ob.delete_specf_node(item)
    elif ch == 6:
        ob.delete_start_node()
    elif ch == 7:
        ob.delete_last_node()
    elif ch == 8:
        ob.display()
    elif ch == 9:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")