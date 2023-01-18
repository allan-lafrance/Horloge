import time

current_time = None
current_time_system = None
alarm_time = (16, 00, 10)

def afficher_heure(heure):
    if heure is None:
        afficher_heure_systeme()
    else:
        print("{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2]))

def afficher_heure_systeme():
    global current_time_system
    current_time_system = time.localtime()
    print("{:02d}:{:02d}:{:02d}".format(current_time_system.tm_hour, current_time_system.tm_min, current_time_system.tm_sec))

def regler_heure(heure):
    global current_time
    current_time = heure

def regler_alarme(heure):
    global alarm_time
    alarm_time = heure

def check_alarm():
    global current_time, alarm_time, current_time_system
    if current_time_system is not None and (current_time_system.tm_hour, current_time_system.tm_min, current_time_system.tm_sec) == alarm_time:
        print("Alarme!")


while True:
    afficher_heure(current_time)
    check_alarm()
    if current_time is not None:
        current_time = (current_time[0], current_time[1], current_time[2] + 1)
        if current_time[2] >= 60:
            current_time = (current_time[0], current_time[1] + 1, 0)
        if current_time[1] >= 60:
            current_time = (current_time[0] + 1, 0, current_time[2])
        if current_time[0] >= 24:
            current_time = (0, current_time[1], current_time[2])
    time.sleep(1)