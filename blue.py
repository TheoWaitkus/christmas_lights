import serial

ser = serial.Serial("COM3")


ser.write("2".encode())

ser.close()