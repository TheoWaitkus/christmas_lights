import serial_helper
import serial
import time





red = 140
green = 50
blue = 12


delay = .1

def main (helper, num_lights, light_state):
    light_state.running = True
    helper.clear()
    while(True):
        for j in range(20):
            for i in range(num_lights):
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    light_state.exit_thread = False
                    light_state.running = False
                    return
                if (i % 2 == 0):
                    helper.change(i,red,green,blue)
                    
            helper.update()
            helper.flush()
            time.sleep(delay)
            helper.clear()
            helper.flush()
            for i in range(num_lights):
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    light_state.exit_thread = False
                    light_state.running = False
                    return
                if (i % 2 == 1):
                    helper.change(i,red,green,blue)
                    
            helper.update()
            helper.flush()
            time.sleep(delay)
            helper.clear()
            helper.flush()
            
        for j in range(5):
            for i in range(num_lights):
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    light_state.exit_thread = False
                    light_state.running = False
                    return
                if (i % 2 == 0):
                    helper.change(i,red,green,blue)
                    
            helper.update()
            helper.flush()
            time.sleep(delay)
            helper.clear()
            helper.flush()
            
            time.sleep(delay/2)
                    
            helper.update()
            helper.flush()
            time.sleep(delay/2)
            helper.clear()
            helper.flush()
        for j in range(5):
            for i in range(num_lights):
                if(light_state.exit_thread):
                    helper.update()
                    helper.flush()
                    helper.clear()
                    helper.flush()
                    light_state.exit_thread = False
                    light_state.running = False
                    return
                if (i % 2 == 1):
                    helper.change(i,red,green,blue)
                    
            helper.update()
            helper.flush()
            time.sleep(delay)
            helper.clear()
            helper.flush()
            
            time.sleep(delay/2)
                    
            helper.update()
            helper.flush()
            time.sleep(delay/2)
            helper.clear()
            helper.flush()
            
            
            
        
    
    
