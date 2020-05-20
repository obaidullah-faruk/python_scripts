# class Outer:

#     def __init__(self):
#         self.inner = self.Inner()

#     def reveal(self):
#         self.inner.inner_display("Calling inner class method from outer class")

#     class Inner:
#         def inner_display(self, msg):
#             print(msg)

# outer = Outer()
# outer.reveal()

# Outer().Inner().inner_display("Calling the inner class method directly.")

# inner = outer.Inner()
# inner.inner_display("Just print it")

class Outer:

    def __init__(self):
        self.inner = self.Inner()
        self.innerinner = self.inner.InnerInner()

    def show_classes(self):
        print("This is the outer class")
        print(inner)
        print(innerinner)
    
    class Inner:
        """First Inner Class"""

        def __init__(self):
            self.innerinner = self.InnerInner()

        def show_classes(self):
            print("This is the inner class")
            print(self.innerinner)

        def inner_display(self, msg):
            print("This is Inner Class")
            print(msg)

        class InnerInner:

            def inner_display(self, msg):
                print("This is multilevel inner class")
                print(msg)

outer = Outer()
inner = outer.Inner()
innerinner = inner.InnerInner()
innerinner.inner_display("Just Print It!")