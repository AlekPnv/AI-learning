import time

def countdown_timer():
    while True:
        try:
            user_time: int = int(input("Countdown in seconds: "))
            if user_time < 1:
                print("Timer cannot go below 1 second.\n")
                continue
            
        except ValueError:
            print("Invalid number.\n")
            continue
        
        try:
            for remaining in range(user_time, 0, -1):
                seconds = remaining  % 60
                minutes = int(remaining // 60) % 60
                hours = int(remaining // 3600)
                
                print(f"Time left: {hours:02}:{minutes:02}:{seconds:02}")
                time.sleep(1)
            
            print("Time's up!")

        except KeyboardInterrupt:
            print("Ctrl+C -> cancel early")

        if input("\nStart another timer? [y/n]: ").lower() != "y":
            break
            
            
if __name__ == "__main__":
    countdown_timer()