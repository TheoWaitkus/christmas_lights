import serial_helper
import serial
import time


num_lights = 100

sleep_dur = .00000000001


ser = serial.Serial("COM3", baudrate=2000000)

time.sleep(4)

helper = serial_helper.SerialHelper(ser)



helper.clear()
time.sleep(sleep_dur)

start = time.time()



for i in range(0, num_lights):
    
    
    helper.change(i, 100, 100, 0)
    


helper.update()

helper.flush()

end = time.time()

print(str(end-start) + " seconds")

helper.close()