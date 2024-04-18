class Employee:

    from timesheet_entry import Timesheetentry
    import datetime as dt

    timesheets = []


    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + " " + self.last
    
    def logminutes(self, project, minutes):
        now = self.dt.datetime.now()
        timesheetentry = self.Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)

    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes

    
if __name__ == "__main__":
    test = Employee("John", "Doe")
    print(test)
    assert(str(test) == "John Doe") #Test the __str__ method
    test.logminutes("project1", 60)
    test.logminutes("project1", 30)
    minutes = test.gettotaltime()
    print(minutes)
    assert(minutes == 90) #Test the gettotaltime method

    print("All tests passed!")