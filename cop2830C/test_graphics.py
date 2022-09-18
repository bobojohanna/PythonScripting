###
### http://anh.cs.luc.edu/handsonPythonTutorial/index.html
###

###
### http://anh.cs.luc.edu/python/hands-on/3.1/examples.zip
###

from graphics import *

### Instantiate Graphics Window
win = GraphWin('my window', 800, 800)

### Start your nested loops here
for x in range(10):

    for y in range(15):
        
        ### First pick a center point 
        pt = Point(30 + 100 * x/2, y * 50)

        # Then draw 
        rect = Rectangle(pt, pt)
        cir = Circle(pt, 25)
        line = Line(pt, Point(4,4))

        # Set the color
        rect.setOutline('orange')
        rect.setFill('green')

        line.setOutline('pink')
        line.setFill('pink')

        cir.setOutline('red')
        cir.setFill('yellow')

        # Then render
        # rect.draw(win)
        # cir.draw(win)
        line.draw(win)

### end your loop here

# Wait for a mouse click to close the Graphics window
message = Text(Point(win.getWidth()/10, 200), 'Click anywhere to exit.')
message.draw(win)
win.getMouse()



