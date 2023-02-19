import program1, program2, program3, program4, program5, program6, program7, program8, program9, program10, program11
import random
import threading
import time



def main(helper, num_lights, light_state):

    def start_lightshow(light_show : str):
        f = eval(light_show + ".main")
        global exit_thread
        f(helper, num_lights, light_state)
    
    num = str(random.randint(1,11))
    super_thread = threading.Thread(target = start_lightshow, args=("program"+num,))
    super_thread.start()
    
    for i in range(150):
        time.sleep(.1)
        if(light_state.exit_random):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_random = False
            light_state.running_random = False
            return
    
    light_state.exit_thread = True
    while(light_state.exit_thread and light_state.running):
        time.sleep(.1)
    light_state.exit_thread = False
    
    if(light_state.exit_random):
            helper.update()
            helper.flush()
            helper.clear()
            helper.flush()
            light_state.exit_random = False
            light_state.running_random = False
            return
            
    main(helper,num_lights,light_state)
    
    
