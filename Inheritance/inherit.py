class Father():
    def __init__(self):
        # self.fname = fname
        print("Father's constructor called")
    
    # def show_name(self):
    #     print(f"Father's name is {self.fname}")


class Son(Father):
    def __init__(self, sname, fname):
        print("Initializing Son class")
        # super().__init__(fname)
        self.sname = sname
        print("Son's constructor called")
    

    def show_son_name(self):
        print(f"Son's name is {self.sname}")


son = Son("John Jr.", "John Sr.")
# son.show_son_name()
# son.show_name()