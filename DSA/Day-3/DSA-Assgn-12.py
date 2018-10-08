# DSA-Assgn-12

# This assignment needs DataStructures.py file in your package, you can get it from resources page

from res.DataStructures import Stack, Queue

class Ball:
    def __init__(self, color, name):
        self.__color = color
        self.__name = name

    def __str__(self):
        return (self.__color + " " + self.__name)

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name
class Game:
    
    def __init__(self, ball_stack):
        self.ball_container = ball_stack
        self.red_balls_container = Stack(2)
        self.green_balls_container = Stack(2)
        self.blue_balls_container = Stack(2)
        self.yellow_balls_container = Stack(2)

        
    def grouping_based_on_color(self):
        for i in range (self.ball_container.get_max_size()):
            ball = self.ball_container.pop()
            if ball.get_color() == "Red":
                self.red_balls_container.push(ball)
            elif ball.get_color() == "Green":
                self.green_balls_container.push(ball)
            elif ball.get_color() == "Yellow":
                self.yellow_balls_container.push(ball)
            elif ball.get_color() == "Blue":
                self.blue_balls_container.push(ball)      
        
    def rearrange_balls(self, color):
        if color == "Red":
            for x in range (2):
                ball =self.red_balls_container.pop()
                if ball.get_name() == "A":
                    a = ball
                else:
                    b = ball
            self.red_balls_container.push(b)
            self.red_balls_container.push(a)
        elif color == "Blue":
            for x in range (2):
                ball =self.blue_balls_container.pop()
                if ball.get_name() == "A":
                    a = ball
                else:
                    b = ball
            self.blue_balls_container.push(b)
            self.blue_balls_container.push(a)

    def display_ball_details(self, color):
        pass
# Implement Game class here

# Use different values to test your program
ball1 = Ball("Red", "A")
ball2 = Ball("Blue", "B")
ball3 = Ball("Yellow", "B")
ball4 = Ball("Blue", "A")
ball5 = Ball("Yellow", "A")
ball6 = Ball("Green", "B")
ball7 = Ball("Green", "A")
ball8 = Ball("Red", "B")
ball_list = Stack(8)
ball_list.push(ball1)
ball_list.push(ball2)
ball_list.push(ball3)
ball_list.push(ball4)
ball_list.push(ball5)
ball_list.push(ball6)
ball_list.push(ball7)
ball_list.push(ball8)

g1=Game(ball_list)
g1.grouping_based_on_color()


# Create objects of Game class, invoke the methods and test the program
