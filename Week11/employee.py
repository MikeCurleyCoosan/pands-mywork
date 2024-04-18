class Employee:

    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + " " + self.last
    
if __name__ == "__main__":
    test = Employee("John", "Doe")
    print(test)
    assert ("John Doe" == str(test))