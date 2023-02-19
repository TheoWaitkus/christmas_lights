import cherrypy
import subprocess
from external import exit_thread
import threading
import program1
import program2, program3, program4, program5, program6, randomizer, program7, program8, program9, program10, program11
import coord
import serial
import time
import serial_helper
import random

cherrypy.server.socket_host = '192.168.1.113'
cherrypy.server.socket_port = 8080

HTML = '''   <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<style>

a {font-size: 50px}

</style>

<a href = "/kill">KILL</a>

<br>

<a href = "/randomizer">Randomizer</a>

<br>

<a href = "/program1">snake</a>

<br>

<a href = "/program2">blinky</a>

<br>

<a href = "/program3">8spiral</a>

<br>

<a href = "/program4">red green slice</a>

<br>

<a href = "/program5">8slice</a>

<br>

<a href = "/program6">smooth spiral</a>

<br>

<a href = "/program7">knock off fireworks</a>

<br>

<a href = "/program8">silver and gold</a>

<br>

<a href = "/program9">fireworks</a>

<br>

<a href = "/program10">game of life</a>

<br>

<a href = "/program11">random slice</a>

<br>







</body>
</html> '''
    
ser = serial.Serial("COM3", baudrate=2000000)

time.sleep(2)

serial_helper = serial_helper.SerialHelper(ser)

class LightState:
    def __init__(self):
        self.exit_thread = False
        self.running = False
        self.exit_random = False
        self.running_random = False

light_state = LightState()




def start_lightshow(light_show : str):
    f = eval(light_show + ".main")
    global exit_thread
    f(serial_helper, NUM_LIGHTS, light_state)


def start_randomizer():
    randomizer.main(serial_helper, NUM_LIGHTS, light_state)


light_state.exit_thread = True
while(light_state.exit_thread and light_state.running):
    time.sleep(.1)
light_state.exit_thread = False
light_state.running = False
light_state.exit_random = True
while(light_state.exit_random and light_state.running_random):
    time.sleep(.1)
light_state.exit_random = False
light_state.running_random = False

NUM_LIGHTS = 500

class HelloWorld(object):


    @cherrypy.expose
    def index(self):
        return HTML
        
        
    @cherrypy.expose    
    def program1(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program1",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program1"
        
        
    @cherrypy.expose    
    def program2(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program2",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program2"
        
    @cherrypy.expose    
    def kill(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        '''serial_helper.update()
        serial_helper.flush()'''
        serial_helper.clear()
        serial_helper.update()
        serial_helper.flush()
        raise cherrypy.HTTPRedirect('/') 
        return "Hello world!"
        
    @cherrypy.expose    
    def program3(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program3",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program4(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program4",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program5(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program5",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program6(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program6",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def randomizer(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        light_state.running_random = True
        duper_thread = threading.Thread(target = start_randomizer)
        duper_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program2"
        
    @cherrypy.expose    
    def program7(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program7",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program8(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program8",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program9(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program9",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program10(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program10",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    @cherrypy.expose    
    def program11(self):
        light_state.exit_thread = True
        while(light_state.exit_thread and light_state.running):
            time.sleep(.1)
        light_state.exit_thread = False
        light_state.running = False
        light_state.exit_random = True
        while(light_state.exit_random and light_state.running_random):
            time.sleep(.1)
        light_state.exit_random = False
        light_state.running_random = False
        super_thread = threading.Thread(target = start_lightshow, args=("program11",))
        super_thread.start()
        raise cherrypy.HTTPRedirect('/') 
        return "program3"
        
    


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())