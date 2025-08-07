from machine import Pin, TouchPad
import time

toque = TouchPad(Pin(4))

while True:
    sensa = toque.read()
    print('el valor capacitivo es:', sensa)
    time.sleep (.3)
