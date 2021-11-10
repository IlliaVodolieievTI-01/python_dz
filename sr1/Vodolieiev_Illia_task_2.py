class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    @staticmethod
    def __check_value(value, min, max):
        if not isinstanse(value, int):
            raise TypeError("Wrong type of value!")
        elif(value > max and value < min):
            raise ValueError("Wrong value!")
        return True

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, elem):
        if Time.__check_value(elem, 0, 23):
            self.__hours = elem

    @minutes.setter
    def minutes(self, elem):
        if Time.__check_value(elem, 0, 59):
            self.__minutes = elem

    @seconds.setter
    def seconds(self, elem):
        if Time.__check_value(elem, 0, 59):
            self.__seconds = elem

    def print_time(self):
        return f"{self.__hours} hours\n {self.__minutes} minutes\n {self.__seconds} seconds\n"

    def print_time_pm(self):
        if self.__hours >= 12:
            pm_hours = self.__hours - 12
            return f"{pm_hours} pm\n {self.__minutes} minutes\n {self.__seconds} seconds\n"
        else:
        	return f"{self.__hours} am\n {self.__minutes} minutes\n {self.__seconds} seconds\n"


firsttime = Time(14, 34, 57)
secondtime = Time(1, 26, 53)
print(firsttime.print_time())
print(firsttime.print_time_pm())
print(secondtime.print_time())
print(secondtime.print_time_pm())

