import math
import datetime



def  time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_for_12house = now.strftime("%I:%M:%S %p")
    current_date=now.strftime("%d/%m/%Y")
    print(f"currnt day {current_date} and current time is {current_time} and 12 hour time is {time_for_12house}")


def  cal(base, exp):
    result = math.pow(base,exp)
    print(f"the power of {base} raised to {exp} is {result}")



# b= int(input("Enter the base:"))
# r = int(input("Enter the exponent:"))
# #cal(b,r)
time()
  
