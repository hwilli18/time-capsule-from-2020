'''
---------------------------
      Updated 2020
---------------------------

Python code for Raspberry Pi

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

About Raspberry Pi (from Wikipedia as of January 30th 2020)

The Raspberry Pi (/paɪ/) is a series of small single-board computers developed in the United Kingdom by the Raspberry Pi Foundation to promote the teaching of basic computer science in schools and in developing countries. The original model became far more popular than anticipated, selling outside its target market for uses such as robotics. It does not include peripherals (such as keyboards and mice) or cases. However, some accessories have been included in several official and unofficial bundles.

The organisation behind the Raspberry Pi consists of two arms. The first two models were developed by the Raspberry Pi Foundation. After the Pi Model B was released, the Foundation set up Raspberry Pi Trading, with Eben Upton as CEO, to develop the third model, the B+. Raspberry Pi Trading is responsible for developing the technology while the Foundation is an educational charity to promote the teaching of basic computer science in schools and in developing countries.

According to the Raspberry Pi Foundation, more than 5 million Raspberry Pis were sold by February 2015, making it the best-selling British computer. By November 2016 they had sold 11 million units, and 12.5m by March 2017, making it the third best-selling "general purpose computer". In July 2017, sales reached nearly 15 million. In March 2018, sales reached 19 million.

Most Pis are made in a Sony factory in Pencoed, Wales. Some are made in China and Japan.


'''

from Tkinter import *
import tkFont
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def ledON():
    print("LED button pressed")
    if GPIO.input(40) :
        GPIO.output(40,GPIO.LOW)
                ledButton["text"] = "LED OFF"
    else:
        GPIO.output(40,GPIO.HIGH)
                ledButton["text"] = "LED ON"

def exitProgram():
    print("Exit Button pressed")
       GPIO.cleanup()
    win.quit()  


win.title("LED GUI")


exitButton  = Button(win, text = "1", font = myFont, command = ledON, height     =2 , width = 8) 
exitButton.pack(side = LEFT, anchor=NW, expand=YES)

ledButton = Button(win, text = "2", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=CENTER, expand=YES)

ledButton = Button(win, text = "3", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = RIGHT, anchor=NE, expand=YES)

ledButton = Button(win, text = "4", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=W, expand=YES)

ledButton = Button(win, text = "5", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=W, expand=YES)

ledButton = Button(win, text = "6", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=W, expand=YES)

ledButton = Button(win, text = "7", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=W, expand=YES)

ledButton = Button(win, text = "8", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=W, expand=YES)

ledButton = Button(win, text = "9", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=N, expand=YES)

ledButton = Button(win, text = "0", font = myFont, command = ledON, height = 2, width =8 )
ledButton.pack(side = TOP, anchor=NW, expand=YES)


mainloop()
