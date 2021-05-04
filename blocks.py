from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager:
    def __init__(self):
        self.all_blocks = []

    def generate(self, x, y):
        block = Turtle()
        block.shape("square")
        block.shapesize(stretch_wid=1, stretch_len=3)
        block.color(random.choice(COLORS))
        block.pu()
        block.goto(x, y)
        return block

    def create(self):
        for i in range(6):
            for j in range(30):
                x = -390 + (j * 60)
                y = 290 - (i * 20)
                bl = self.generate(x, y)
                self.all_blocks.append(bl)

    def destroy(self, block):
        block.hideturtle()
        self.all_blocks.remove(block)

