"""
created by Nagaj at 19/05/2021
"""
from turtle import Screen

from constants import SCREEN_TITLE, SCREEN_PROMPT, RACE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT
from data import turtles_data
from config import SetUpTurtles
from race import Race


def start():
    # ########## setup screen #############
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(BLACK)
    screen.title(RACE)
    user_bet = screen.textinput(
        title=SCREEN_TITLE, prompt=SCREEN_PROMPT
    )

    # ############## race   ############
    turtles = SetUpTurtles(turtles_data)
    competitors = turtles.create()
    race = Race(competitors=competitors)
    race.start_race()
    race.race_result(user_bet)
    race.top_10_turtles()
    # ############ wait click to finish  ##############
    screen.exitonclick()


if __name__ == '__main__':
    start()
