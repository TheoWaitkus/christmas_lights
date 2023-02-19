import serial
import time

class SerialHelper:

    def __init__ (self, ser):
        self.ser = ser
        self.bite = b''
        self.change_code = 1
        self.update_code = 0
        self.clear_code = 2

    def flush (self):
        self.ser.write(self.bite)
        self.bite = b''
        self.ser.flush()

    def change (self, pos, r, g, b):
        self.bite += int.to_bytes(self.change_code, 1, "big")
        if(pos > 255):
            self.bite += int.to_bytes(255, 1, "big")
            self.bite += int.to_bytes(pos-255, 1, "big")
        else:
            self.bite += int.to_bytes(pos, 1, "big")
            self.bite += int.to_bytes(0, 1, "big")
        self.bite += int.to_bytes(g, 1, "big")
        self.bite += int.to_bytes(r, 1, "big")
        self.bite += int.to_bytes(b, 1, "big")
        

    def update (self):
        self.bite += int.to_bytes(self.update_code, 1, "big")
        

    def clear (self):
        self.bite += int.to_bytes(self.clear_code, 1, "big")
        
    def close (self):
        self.ser.close()
       





