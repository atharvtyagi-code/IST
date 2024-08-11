class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        elif self.data > data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = Node(data)

    def inorder_traversal(self):
        list = []

        if self.left:
            list += self.left.inorder_traversal()

        list.append(self.data)

        if self.right:
            list += self.right.inorder_traversal()

        return list

    def search(self, n):
        if n in list:
            if n == self.data:
                return True
            
            if n < self.data:
                if self.left:
                    self.left.search(n)
                    return True

                else:
                    return False
                
            if n > self.data:
                if self.right:
                    self.right.search(n)
                    return True

                else:
                    return False
                
        if n not in list:
            return False

def build_tree(list):
    root = Node(list[0])

    for i in range(1, len(list)):
        root.add_child(list[i])

    return root

print("1: Create a tree")
print("2: Search for a node")
print("3: Arrange the tree in inorder")
print("4: Add a child")
print("5: Exit")
choice = int(input("Choose a number between 1 and 5: "))

if choice == 1:
    if __name__ == "__main__":
        list = [50, 22, 34, 92, 24, 53, 29, 99, 20, 32, 100, 2, 8, 5, 10, 15]
        num = build_tree(list)
        print(num)

elif choice == 2:
    if __name__ == "__main__":
        list = [50, 22, 34, 92, 24, 53, 29, 99, 20, 32, 100, 2, 8, 5, 10, 15]
        num = build_tree(list)
        n = int(input("Enter the number you are looking for: "))
        print(num.search(n))

elif choice == 3:
    if __name__ == "__main__":
        list = [50, 22, 34, 92, 24, 53, 29, 99, 20, 32, 100, 2, 8, 5, 10, 15]
        num = build_tree(list)
        print(num.inorder_traversal())

elif choice == 4:
    if __name__ == "__main__":
        list = [50, 22, 34, 92, 24, 53, 29, 99, 20, 32, 100, 2, 8, 5, 10, 15]
        num = build_tree(list)
        add = int(input("Enter the node you want to add: "))
        num.add_child(add)
        print(num.inorder_traversal())

elif choice == 5:
    print("Program exited!")

else:
    print("You can only choose the numbers between 1 and 5.")