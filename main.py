"""
created by Nagaj at 19/05/2021
"""
import random
from typing import List
from turtle import Turtle, Screen
from data import turtles_data
from constants import WIN, LOSE, SCREEN_TITLE, SCREEN_PROMPT


class Race:
    STOP = 230

    def __init__(self, competitors: List[Turtle]):
        self.competitors = competitors
        self.winner = None

    def start_race(self):
        while True:
            for competitor in self.competitors:
                competitor.forward(random.randint(1, 10))
                if competitor.xcor() >= Race.STOP:
                    self.winner = competitor
                    return self.winner

    def race_result(self, user_bet: str):
        winner_color = self.winner.pencolor().lower()
        user_bet = user_bet.lower()
        if winner_color == user_bet:
            print(WIN.format(user_bet))
        else:
            print(LOSE.format(winner_color))


class SetUpTurtles:
    def __init__(self, data: List[dict]):
        self.data = data
        self.competitors = []

    def create(self):
        for competitor in self.data:
            comp = Turtle(shape=competitor["shape"])
            comp.penup()
            comp.color(competitor["color"])
            comp.goto(x=competitor["position"]["x"], y=competitor["position"]["y"])
            self.competitors.append(comp)
        return self.competitors


def start():

    # ########## setup screen #############
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(
        title=SCREEN_TITLE, prompt=SCREEN_PROMPT
    )

    # ############## race   ############
    turtles = SetUpTurtles(turtles_data)
    competitors = turtles.create()
    race = Race(competitors=competitors)
    race.start_race()
    race.race_result(user_bet)

    # ############ wait click to finish  ##############
    screen.exitonclick()


if __name__ == '__main__':
    start()
