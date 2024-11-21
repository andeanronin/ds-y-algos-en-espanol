
# Class Daynames works as a Node, with two instance variables: the Node's day_name 
                                                            #  and the Node's next_day

class Daynames:   # node of name daynames
    def __init__(self, day_name=None): 
        self.day_name = day_name 
        self.next_day = None 

    def print_weekday(self):
        print(f"Today is {self.day_name}")

    def print_tomorrow(self):
        if self.next_day == None:
            print("No value set for next day yet.")
        else: 
            print(f"Tomorrow is {self.next_day.day_name}")

if __name__ == "__main__":  
    # Creates Daynames object named Monday with dataval = 'Monday'
    monday = Daynames('Monday')
    monday.print_weekday()

    # Creates object of the Daynames class with dataval = 'Tuesday'
    tuesday = Daynames('Tuesday')
    tuesday.print_weekday()

    #  Calls the print_tomorrow function of Daynames class for Object Monday, 
    monday.print_tomorrow() # Prints None (Monday's next_day = None)

    # Set's monday's next_day variable to the Tuesday object creating a link between Monday & Tuesday
    monday.next_day = tuesday
    monday.print_tomorrow() 
    print("")

    # Creates Wednesday Ojbect 
    wednesday = Daynames('Wednesday')
    tuesday.next_day = wednesday        # Sets Tuesday's next_day value to wednesday object 
    
    thursday = Daynames('Thursday')

    # Iterates through Monday-Tuesday 
    first_day = monday
    while first_day:
      print(first_day.day_name)
      first_day = first_day.next_day    # doesn't print 'Thursday' because link isn't established yet
