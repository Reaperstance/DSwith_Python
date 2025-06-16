class Node:
    def __init__(self, name):
        self.info = name
        self.link = None

class SlList:
    def __init__(self):
        self.start = None

    def front_insert(self,item):
        nd = Node(item)

        if self.start == None:

            self.start = nd
            nd.link = self.start

        else:
            temp = self.start

            while temp.link != self.start:
                temp = temp.link
        nd.link = self.start
        self.start = nd
        temp.link = self.start