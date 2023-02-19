import serial_helper
import serial
import time
from external import exit_thread







def main(helper, num_lights, light_state):
    light_state.running = True

    while(True):
        
        
        
        
        if(light_state.exit_thread):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_thread = False
            light_state.running = False
            return
                
        cmd = input()
        if (cmd == "clear"):
            helper.update()
            helper.flush()
            helper.clear()
            helper.update()
            helper.flush()
        else:
            helper.change(int(cmd),100,0,0)
            helper.update()
            helper.flush()

