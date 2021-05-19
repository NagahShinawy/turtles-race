"""
created by Nagaj at 20/05/2021
"""

import random
from turtle import Turtle
from typing import List

from constants import WIN, LOSE


class Race:
    STOP = 230

    def __init__(self, competitors: List[Turtle]):
        self.competitors = competitors
        self.winner = None
        self.competitors_moves = dict()

    def start_race(self):
        self.competitors_moves = {competitor.pencolor(): 0 for competitor in self.competitors}
        while True:
            for competitor in self.competitors:
                self.harryup(competitor)
                if self.is_race_finished(competitor):
                    self.winner = competitor
                    return self.winner

    def race_result(self, user_bet: str):
        winner_color = self.winner.pencolor().lower()
        user_bet = user_bet.lower()
        if winner_color == user_bet:
            print(WIN.format(user_bet))
        else:
            print(LOSE.format(winner_color))

    def top_10_turtles(self):
        top_10 = {color: moves for color, moves in
                  sorted(self.competitors_moves.items(), key=lambda item: item[1], reverse=True)}
        for color, moves in top_10.items():
            print(f"{color} ==> {moves}")

    def harryup(self, competitor):
        move = random.randint(1, 10)
        competitor.forward(move)
        self.competitors_moves[competitor.pencolor()] += move

    @staticmethod
    def is_race_finished(competitor):
        return competitor.xcor() >= Race.STOP
