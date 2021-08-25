#Ez_clipboard_sniff by GRAVTIT
import pyperclip, time, os, datetime, keyboard

datetime = datetime.datetime.now()
old = ''
#log = datetime.strftime('%d-%m-%Y') + ".txt"
log = str(datetime.date()) + ".txt"
if os.path.exists(log) and os.path.isfile(log) == True:
    log = open(str(datetime.date()) + ".txt", "a")
    log.write('!!! ' + str(datetime.time().replace(microsecond=0)) + ' Process restarted. File already created. Opened.\n')
    print('!!! ' + str(datetime.time().replace(microsecond=0)) + ' Process restarted. File was created. Opened.\n'+ os.path.join(os.getcwd(), str(log.name)) + '\nCtrl + Space to close process.\nEmpty line = non-text\n')
    log.close()
else:
    log = open(str(datetime.date()) + ".txt", "w")
    log.write(str(datetime.strftime('%A, %B the %dth, %Y')) + '\n!!! ' + datetime.time().replace(microsecond=0) + ' Process started. File created. Opened.\nCtrl + Space to close process.\nEmpty line = non-text\n')
    print(str(datetime.strftime('%A, %B the %dth, %Y')) + '\n' + datetime.time().replace(microsecond=0) + ' Process started. File created. Opened.\nCtrl + Space to close process.\nEmpty line = non-text' + os.path.join(os.getcwd(), str(log.name)) + '\n')
    log.close()
while keyboard.is_pressed('Ctrl + Space') == False:
    s = pyperclip.paste()
    if (s != old):
        log = open(str(datetime.date()) + ".txt", "a")
        print("> " + s + "\n" + "Added" )# + os.path.join(os.getcwd(), str(log.name)))
        log.write(str(datetime.time().replace(microsecond=0)) + " > " + s + "\n")
        old = s
        log.close()
    time.sleep(1)
log = open(str(datetime.date()) + ".txt", "a")
log.write('!!! ' + str(datetime.date()) + ' Process has been stopped. File is closed.\n')
log.close()
print('!!! ' + str(datetime.time().replace(microsecond=0)) + ' Process has been stopped. File is closed.\n')
exit()
