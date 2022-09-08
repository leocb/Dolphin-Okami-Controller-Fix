from System import Int16
import ctypes

if starting:
	#Aux Vars (So we dont keep doing the same math over and over)
	enabled = False
	ScreenResX = 1920 #<--------------------- CHANGE THIS TO YOUR DOLPHIN FULLSCREEN RESOLUTION WIDTH
	ScreenResY = 1080 #<--------------------- CHANGE THIS TO YOUR DOLPHIN FULLSCREEN RESOLUTION HEIGHT
	HalfScreenX = ScreenResX/2
	HalfScreenY = ScreenResY/2
	halfInt16 = Int16.MaxValue/2
	#WASD
	analogX = 0
	analogY = 0
	analogDestX = 0
	analogDestY = 0
	speed = 500.0 #No need to tweak this, unless you find it too fast, then lower it, any higher values will cause amaterasu to slow down
	# mouse
	mousex = 0
	mousey = 0
	mouseMulX = 16384/HalfScreenX
	mouseMulY = 16384/HalfScreenY
	
#are we enabled to recieve input?
if (enabled):
	#"absolute" mouse position
	mousex += mouse.deltaX * mouseMulX
	mousey += mouse.deltaY * mouseMulY
	
	#Analog directions ------------------------------------------------ CHANGE MOVEMENT RELATED (WASD) BINDINGS HERE:
	if (keyboard.getKeyDown(Key.W) and not keyboard.getKeyDown(Key.S)):
		analogDestY = 16384
	elif (keyboard.getKeyDown(Key.S) and not keyboard.getKeyDown(Key.W)):
		analogDestY = -16384
	else:
		analogDestY = 0
	
		
	if (keyboard.getKeyDown(Key.D) and not keyboard.getKeyDown(Key.A)):
		analogDestX = 16384
	elif (keyboard.getKeyDown(Key.A) and not keyboard.getKeyDown(Key.D)):
		analogDestX = -16384
	else:
		analogDestX = 0
	
	if ((keyboard.getKeyDown(Key.D) or keyboard.getKeyDown(Key.A))and(keyboard.getKeyDown(Key.W) or keyboard.getKeyDown(Key.S))):
		analogDestX = analogDestX*.8
		analogDestY = analogDestY*.8
	#----------------------------------------------------------------------STOP CHANGING THE BINDINGS HERE
	
	#Smooth analog
	dist = math.sqrt((analogDestX-analogX)*(analogDestX-analogX)+(analogDestY-analogY)*(analogDestY-analogY));
	deltaX = analogDestX-analogX
	deltaY = analogDestY-analogY
	
	if (analogX == 0 and analogY == 0):  #Imediate mode: if we weren't pressing anything, then instant "tap" the analog stick
	    analogX = analogDestX
	    analogY = analogDestY
	elif (dist > speed): #If we were holding the analog, smooth over any change in direction
	    deltaX /= dist*1.5
	    deltaY /= dist*1.5
	    analogX += deltaX * speed
	    analogY += deltaY * speed
	else: #SNAP to the final position
	    analogX = analogDestX
	    analogY = analogDestY


	
# watch (debug)
	#diagnostics.watch(dist)
		
else: #if we're not accepting inputs, hold still
	mousex = 0
	mousey = 0
	analogX = 0
	analogY = 0
	
	
# limit mouse range
if (mousex >  halfInt16): 
	mousex = halfInt16
elif (mousex < -halfInt16):
	mousex = -halfInt16
	
if (mousey > halfInt16):
	mousey = halfInt16
elif (mousey < -halfInt16):
	mousey = -halfInt16


	
# abs mouse to vJoy (Painting)
vJoy[0].x = mousex
vJoy[0].y = mousey

# mouse to vJoy (Fleetfoot and camera)
vJoy[0].rx = mouse.deltaX * mouseMulX *10
vJoy[0].ry = mouse.deltaY * mouseMulY *10

# WASD to vJoy (Movement)
vJoy[0].z = analogX
vJoy[0].rz = analogY

if (mouse.getPressed(1) and enabled): #Reset brush to center screen when holding the brush
	mousex = 0
	mousey = 0
	

if (enabled): #Send button presses to vJoy
	ctypes.windll.user32.SetCursorPos(960, 540) #Lock the mouse in the middle of the screen (Prevent issues)
	vJoy[0].setButton(0,int(keyboard.getKeyDown(Key.Space)))
	vJoy[0].setButton(1,int(keyboard.getKeyDown(Key.Q)))
	vJoy[0].setButton(2,int(keyboard.getKeyDown(Key.R)))
	vJoy[0].setButton(3,int(keyboard.getKeyDown(Key.D1)))
	vJoy[0].setButton(4,int(keyboard.getKeyDown(Key.D2)))
	vJoy[0].setButton(5,int(keyboard.getKeyDown(Key.F)))
	vJoy[0].setButton(6,int(keyboard.getKeyDown(Key.LeftShift)))
	vJoy[0].setButton(7,int(mouse.leftButton))
	vJoy[0].setButton(8,int(mouse.rightButton))
	vJoy[0].setButton(9,int(mouse.middleButton))
	vJoy[0].setButton(10,int(keyboard.getKeyDown(Key.E)))
	vJoy[0].setButton(11,int(keyboard.getKeyDown(Key.LeftAlt)))




# toggle accept inputs
toggle = keyboard.getPressed(Key.D0) or keyboard.getPressed(Key.NumberPad0)

if toggle:
    enabled = not enabled