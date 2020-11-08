from cs1graphics import *
from time import sleep
from random import randint

class Crab(Layer):
    """
    The Crab class can be used to create three different sized crab based on the input.
    
    The user can choose 'baby', 'mommy', or 'daddy' for the crab sizes.
    
    """
    
    def __init__(self):
        """        
        Creates a new crab instance based on the size input.
        
        Initial reference point is at the center of the body and is originally at (0, 0).

        An unedited crab will be red. 
        
        """
        super().__init__()
                
        self._body=Ellipse(40, 30, Point(0, 0))
        self._body.setFillColor('red')
        self._body.setBorderColor('red')
        
        self._eye1=Circle(2, Point(-5, -5))
        self._eye1.setFillColor('black')

        self._eye2=self._eye1.clone()
        self._eye2.move(10, 0)

        self._leg1=Path(Point(-16, 0), Point(-30, 0), Point(-35, 4))
        self._leg1.setBorderColor('red')
        self._leg1.setBorderWidth(3)

        self._leg2=self._leg1.clone()
        self._leg2.move(-1, 7)

        self._leg3=Path(Point(20, 0), Point(34, 0), Point(39, 4))
        self._leg3.setBorderColor('red')
        self._leg3.setBorderWidth(3)

        self._leg4=self._leg3.clone()
        self._leg4.move(-2, 7)
        
        self._arm1=Path(Point(-18, -5), Point(-28, -10), Point(-28, -20))
        self._arm1.setBorderColor('red')
        self._arm1.setBorderWidth(3)

        self._arm2 = self._arm1.clone()
        self._arm2.flip(180)
        self._arm2.move(36, 0)
                
                
        self.add(self._body)
        self.add(self._eye1)
        self.add(self._eye2)
        self.add(self._leg1)
        self.add(self._leg2)
        self.add(self._leg3)
        self.add(self._leg4)
        self.add(self._arm1)
        self.add(self._arm2)


    def Dance(self, number, time):
        """
        Calling this function makes the crab do a little dance.

        The user can choose between dance 1, 2, or 3. They can also choose the amount of time (in seconds) the crab will dance for. 

        Parameters:
            Dance number (int): Choose dance 1, 2, or 3.
            time (int): The amount of time (in seconds) that the crab will dance for.

        """
        if isinstance(number, int) == False or isinstance(time, int) == False :
            print('Please choose an integer value')
            
        if number == 1:  
            counter = 0     
            while time != counter: # Move arms around to make him dance
                sleep(0.25)
                self._arm1.rotate(40)
                self._arm2.rotate(40)
                sleep(0.25)
                self._arm2.rotate(-80)
                self._arm1.rotate(-80)
                sleep(0.25)
                self._arm1.rotate(80)
                self._arm2.rotate(80)
                sleep(0.25)
                self._arm1.rotate(-40)
                self._arm2.rotate(-40)
                counter +=1

        if number == 2:
            counter = 0     
            while time != counter: # Move while moving legs around
                sleep(0.25)
                self.move(10,0)
                self._leg1.rotate(10)
                self._leg4.rotate(10)
                self._leg2.rotate(-10)
                self._leg3.rotate(-10)
                sleep(0.25)
                self.move(-10,0)
                self._leg1.rotate(-10)
                self._leg4.rotate(-10)
                self._leg2.rotate(10)
                self._leg3.rotate(10)
                counter += 1

        if number == 3:
            counter = 0
            while time != counter: # Move arms and legs around
                sleep(0.25)
                self._arm1.rotate(40)
                self._arm2.rotate(40)
                self._leg1.rotate(10)
                self._leg4.rotate(10)
                self._leg2.rotate(-10)
                self._leg3.rotate(-10)
                sleep(0.25)
                self._arm2.rotate(-80)
                self._arm1.rotate(-80)
                self._leg1.rotate(-10)
                self._leg4.rotate(-10)
                self._leg2.rotate(10)
                self._leg3.rotate(10)
                sleep(0.25)
                self._arm1.rotate(80)
                self._arm2.rotate(80)
                self._leg1.rotate(10)
                self._leg4.rotate(10)
                self._leg2.rotate(-10)
                self._leg3.rotate(-10)
                sleep(0.25)
                self._arm1.rotate(-40)
                self._arm2.rotate(-40)
                self._leg1.rotate(-10)
                self._leg4.rotate(-10)
                self._leg2.rotate(10)
                self._leg3.rotate(10)
                counter +=1
                
    def randomColor(self, rainbow = False):
        """
        Calling this function will change the body color of the crab to a random color.

        The user has the option of making the colors rainbow by inputting True or False. The default value is False so it will not rainbow.

        The body will rainbow for 30 seconds if chosen.

        Parameters:
            rainbow (bool), otional: True makes the colors go through the rainbow, False makes the body set to a singular color. The default value is False

        """
        colors = {1: 'red', 2: 'orange', 3: 'yellow', 4: 'green', 5: 'blue', 6: 'violet'}
        counter = 0
        
        if isinstance(rainbow, bool) == False:
            print('Please input True or False')
            
        if rainbow:
            while counter != 60: # Change body color to every color of rainbow
                for i in range(1, 7):
                    self._body.setFillColor(colors[i])
                    self._body.setBorderColor(colors[i])
                    self._leg1.setBorderColor(colors[i])
                    self._leg2.setBorderColor(colors[i])
                    self._leg3.setBorderColor(colors[i])
                    self._leg4.setBorderColor(colors[i])
                    self._arm1.setBorderColor(colors[i])
                    self._arm2.setBorderColor(colors[i])
                    sleep(0.5)
                    counter +=1
        else:
            number = randint(1, 6) # Change body color to random color 
            self._body.setFillColor(colors[number])
            self._body.setBorderColor(colors[number])
            self._leg1.setBorderColor(colors[number])
            self._leg2.setBorderColor(colors[number])
            self._leg3.setBorderColor(colors[number])
            self._leg4.setBorderColor(colors[number])
            self._arm1.setBorderColor(colors[number])
            self._arm2.setBorderColor(colors[number])
            
    def dressUp(self, accessory):
        """
        This function lets the user dress up their crab.

        The user can add a bowtie and/or a top hat and/or monocle to their crab.

        Parameters:
            accessory (str): User can choose to add a bowtie, tophat, monocle, or hairbow
        """

        if isinstance(accessory, str) == False:
            print('Please input a string')

            
        if accessory == 'bowtie': 
            tie = Polygon(Point(0, 6), Point(-10, 1), Point(-10, 11), Point(0, 6), Point(10, 1), Point(10,11), Point(0, 6)) # Make bowtie
            tie.setFillColor('black')
            self.add(tie)

        if accessory == 'tophat':
            hat1 = Rectangle(30, 2, Point(0, -15)) # brim of hat
            hat1.setFillColor('black')
            hat2 = Rectangle(15, 10, Point(0, -20)) # top of hat
            hat2.setFillColor('black')
            self.add(hat1)
            self.add(hat2)

        if accessory == 'monocle':
            mono = Circle(6, Point(-5, -5))
            chain = Path(Point(-10, -5), Point(-20, -5))
            chain.setBorderColor('gold')
            self.add(mono)
            self.add(chain)

        if accessory == 'hairbow':
            bow = Polygon(Point(0, 6), Point(-10, 1), Point(-10, 11), Point(0, 6), Point(10, 1), Point(10,11), Point(0, 6)) # Make bowtie
            bow.setFillColor('pink')
            bow.setBorderColor('pink')
            bow.move(0, -20)
            self.add(bow)
            
    def muscleCrab(self, weightClass = 'middleweight'):
        """
        This function allows the user to either buff up or nerf their crab.

        The user can choose lightweight, middleweight, or heavyweight. The default is middleweight.

        Parameters:
            weightClass(str): The weightclass of the crab. Lightweight, middleweight, or heavyweight.

        """
        if isinstance(weightClass, str) == False:
            print('Please input lightweight, middleweight, or heavyweight.')

        # Changing width of arms and legs to make the carb more or less buff
        if weightClass == 'lightweight': 
            self._leg1.setBorderWidth(1)
            self._leg2.setBorderWidth(1)
            self._leg3.setBorderWidth(1)
            self._leg4.setBorderWidth(1)
            self._arm1.setBorderWidth(1)
            self._arm2.setBorderWidth(1)

        if weightClass == 'heavyweight':
            self._leg1.setBorderWidth(5)
            self._leg2.setBorderWidth(5)
            self._leg3.setBorderWidth(5)
            self._leg4.setBorderWidth(5)
            self._arm1.setBorderWidth(5)
            self._arm2.setBorderWidth(5)
        

if __name__ == '__main__':

    paper = Canvas(600, 600)
    paper.setBackgroundColor('light blue')

    # Making a happy little crab family
    babyCrab = Crab()
    babyCrab.dressUp('monocle')
    babyCrab.muscleCrab('lightweight')
    babyCrab.move(360, 360)
    babyCrab.scale(0.75)
    paper.add(babyCrab)

    sisterCrab = Crab()
    sisterCrab.dressUp('hairbow')
    sisterCrab.move(260, 360)
    paper.add(sisterCrab)

    mommyCrab = Crab()
    mommyCrab.dressUp('monocle')
    mommyCrab.dressUp('hairbow')
    mommyCrab.scale(1.5)
    mommyCrab.move(200, 300)
    paper.add(mommyCrab)

    daddyCrab = Crab()
    daddyCrab.dressUp('tophat')
    daddyCrab.dressUp('bowtie')
    daddyCrab.scale(1.75)
    daddyCrab.move(400, 300)
    daddyCrab.muscleCrab('heavyweight')
    paper.add(daddyCrab)
    
    sleep(2)
    text = Text('Dance Party!')
    text.move(300, 100)
    text.setFontSize(20)
    text.setFontColor('purple')
    paper.add(text)

    sleep(1)
    babyCrab.randomColor()
    babyCrab.Dance(2, 5)
    sisterCrab.Dance(1, 5)
    mommyCrab.Dance(3, 5)
    daddyCrab.Dance(3, 5)
    sisterCrab.randomColor(True)
