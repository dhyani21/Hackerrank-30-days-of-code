'''
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable.

'''
def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))
