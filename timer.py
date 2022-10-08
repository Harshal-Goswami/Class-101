import time

seconds = int(input("Enter the time in number of Seconds : "))

def countdown_timer(seconds):

  while seconds > 0 :
    mins = int(seconds / 60)
    secs = int(seconds % 60)

    timer = f'{mins} : {secs}'

    print(timer)

    seconds -= 1

  print("Time Up !")



countdown_timer(seconds)