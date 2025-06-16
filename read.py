class file1:
    def readit(self):
        with open("D:/pprog/file1.txt","r") as file:
            con = file.read()
            print(con)
ob1 = file1()
ob1.readit()