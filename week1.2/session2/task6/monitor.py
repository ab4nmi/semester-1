# Week 1.2, Session 2: Task 6
# get inputs
temp = int(input("enter temperature: "))
pressure = int(input("enter pressure: "))
status = int(input("is it running? 1 for yes 0 for no: "))

# check temp
if temp > 80:
    print("temp is too high, shut down the machine")
elif temp >= 50 and temp <= 80:
    print("temp is withn safe limits")
else:
    print("temp is low, no action needed")

# check presure
if pressure > 100:
    print("high pressure detected, maintenance needed")
elif pressure >= 70 and pressure <= 100:
    print("pressure is stable")
else:
    print("pressure is low, system is operating normally")

                            # check status
if status == 1:
    if temp > 80 or pressure > 100:
        print("unsafe conditions, shut down the machine")
    else:
        print("machine is running normally")
elif status == 0:
    print("machine is stopped, no action needed")