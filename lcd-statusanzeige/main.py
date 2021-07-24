import lcddriver
from gpiozero import CPUTemperature, LoadAverage
from time import sleep, strftime
import os
import datetime
import psutil

sleeptime = 10
lcd = lcddriver.lcd()
lcd.lcd_clear()

def display_cpu():
    lcd.lcd_clear()
    lcd.lcd_display_string("CPUTemp: " + str(round(CPUTemperature().temperature, 1)) + "C", 1)
    lcd.lcd_display_string("Auslastung: " + str(int(LoadAverage(minutes=1).load_average*100/4))+"%", 2)

def display_time():
    lcd.lcd_clear()
    lcd.lcd_display_string("Zeit:" + strftime("%d.%m %H:%M"), 1)
    lcd.lcd_display_string("Up: " + str(datetime.timedelta(seconds=round(float(os.popen("awk '{print $1}' /proc/uptime").readline()), 1))), 2)

def display_ram():
    lcd.lcd_clear()
    lcd.lcd_display_string("RAM: " + str(psutil.virtual_memory().percent) + "%", 1)
    lcd.lcd_display_string("SWAP: " + str(psutil.swap_memory().percent) + "%", 2)

def display_error():
    lcd.lcd_clear()
    lcd.lcd_display_string("Fehler beim ", 1)
    lcd.lcd_display_string("Auslesen", 2)

while True:
    try:
        display_cpu()
        sleep(sleeptime)
        display_time()
        sleep(sleeptime)
        display_ram()
        sleep(sleeptime)
    except:
        display_error()
        sleep(sleeptime)
