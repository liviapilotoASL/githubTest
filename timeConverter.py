"""
This program converts seconds to hrs, mins, secs
Livia Piloto
21 Jan 2022
Intro to Programming P8
"""

#Get a number of seconds from the user.
secs = int(input("Enter the number of seconds: "))

#Calculate the number of hours.
hours = secs // 3600

#Calculate the number of remaining minutes.
mins = (secs // 60) % 60

#Calculate the number of remaining seconds
seconds = secs % 60

#Display the results (hours, minutes, seconds)
print(str(hours) + ":" + str(mins) + ":" + str(seconds))
