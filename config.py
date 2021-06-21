"""
created by Nagaj at 20/05/2021
"""
from typing import List
from turtle import Turtle


class SetUpTurtles:
    def __init__(self, data: List[dict]):
        self.data = data
        self.competitors = []

    def create(self):
        for competitor in self.data:
            self.add_competitor(competitor)
        return self.competitors

    def add_competitor(self, competitor: dict):
        comp = Turtle(shape=competitor["shape"])
        comp.penup()
        comp.color(competitor["color"])
        comp.goto(x=competitor["position"]["x"], y=competitor["position"]["y"])
        self.competitors.append(comp)