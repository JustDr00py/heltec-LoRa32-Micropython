from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep


oledSDA = Pin(15, Pin.OUT, Pin.PULL_UP)
oledSCL = Pin(4, Pin.OUT, Pin.PULL_UP)
oledRST = Pin(16, Pin.OUT)
oledRST.value(1)

def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        payload = 'Hello ({0})'.format(counter)
        #print("Sending packet: \n{}\n".format(payload))
        display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packet_rssi()))
        lora.println(payload)
        oled.fill(0)
        oled.text("Sending packet: \n{}\n".format(payload), 0, 0)
	oled.show()
	
        counter += 1
        sleep(5)
