from datetime import datetime, timedelta
while True:
    order = input('what is your order: ')
    live = input('where do you live(Bangkok, Nonthaburi, Nakhon Ratchasima)): ')
    ans = live.lower()
    timestart = datetime.now()
    if ans == 'bangkok':
        print('we will deliver the order within 30 minutes!')
        timedeliver = timestart + timedelta(minutes=30)
        print('the order will be delivered to you before:', timedeliver.strftime(" %d/%m/%y %H:%M:%S"))
    
    elif ans == 'nonthaburi':
        print('we will deliver the order within an hour!')
        timedeliver = timestart + timedelta(hours=1)
        print('the order wil be delivered to you before:', timedeliver.strftime(" %d/%m/%y %H:%M:%S"))
    
    elif ans == 'nakhon ratchasima':
        print('we will deliver the order within 3 hours!')
        timedeliver = timestart + timedelta(hours=3)
        print('the order wil be delivered to you before:',timedeliver.strftime(" %d/%m/%y %H:%M:%S"))
    else:
        print('we have no service at your destination :(')
        break
    
    anstimestop = input('please enter the time that you recieved the order(Date/Month/Year Hours:Minutes:Seconds): ')
    timestop = datetime.strptime(anstimestop, "%d/%m/%y %H:%M:%S")
    checktimestop = timestop.timestamp()
    checktimedeliver = timedeliver.timestamp()
    if  float(checktimestop - checktimedeliver) > 0:
        print('we apologized for being late on your order :(')
        print('we are late by:', str(timestop-timedeliver), 'Hours:Minutes:Seconds.Microseconds ')
        break
    elif int(checktimestop - checktimedeliver) == 0:
        print('we made it just in time')
        break
    else:
        print('we delivered it faster than the deadline!')
        print('we are late by:', str(timestop-timedeliver), 'Hours:Minutes:Seconds.Microseconds ')
        break
