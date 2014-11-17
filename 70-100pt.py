# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,65, fill="red")
rocket = drawpad.create_oval(398,580,402,585, fill="red")
direction = 5
rocketFired = False

class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocketFired
        global rocket
        x1,y1,x2,y2 = drawpad.coords(enemy)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        
        if rocketFired == True:
            drawpad.move(rocket,0,-5)
            didWeHit = self.collisionDetect()
            if didWeHit:
                print "hello"
                drawpad.delete(enemy) 

        x1,y1,x2,y2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        if ry1 <= 0 :
            rocketFired = False
            drawpad.move(rocket,(x1-rx1),(y1-ry1))
            
        drawpad.after(1,self.animate)

    def collisionDetect(self):
		global drawpad
                global player
                global enemy
                global rocket
                x1, y1, x2, y2 = drawpad.coords(enemy)
                rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
                if (rx1 > x1 and rx2 < x2) and (ry1 > y1 and ry2 < y2):
                    return True
                else:

                    return False












        

    def key(self,event):
        global player
        global rocketFired
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-15)
                drawpad.move(rocket,0,-15)
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-15,0)
                drawpad.move(rocket,-15,0)
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,15)
                drawpad.move(rocket,0,15)
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,15,0)
                drawpad.move(rocket,15,0)
        if event.char == " ":
            rocketFired = True
            self.rockets = self.rockets - 1
            self.rocketsTxt.config(text=str(self.rockets))




 
            

            
            

        




        

app = myApp(root)
root.mainloop()