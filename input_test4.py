time_start_hours = float(input("What hour does the event start? "))
time_start_minutes = float(input("What minute does the event start? "))
duration_minutes = float(input("How long will the event last (in minutes)? "))
minutes = (duration_minutes + time_start_minutes) % 60
hours = ((time_start_hours) + ((duration_minutes + time_start_minutes) // 60)) % 24
print("Your event will end: " + str(int(hours)) + ":" + str(int(minutes)))