import pyb
pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
pyb.main('ucode.py') # main script to run after this one
