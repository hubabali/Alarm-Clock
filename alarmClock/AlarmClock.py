from playsound import playsound
import time


CLEAR = "\033[2J" #clears entire terminal screen
CLEAR_AND_RETURN = "\033[H" #return the cursor to home position. prints over what was currently there

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #wait for 1 second and continue or else alarm will go fast asl
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #125 seconds //60 = 2
        seconds_left = time_left % 60 #gets u remainder after dvision


        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")#make the numbers display better by 02d as 00:00 instead of 0:0
    
    playsound("alarm.mp3")

minutes = int(input("how many minutes?: "))
seconds = int(input("how many seconds?: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)