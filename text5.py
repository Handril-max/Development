
import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, quantity in balls.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls):
        balls_drawn = []
        if num_balls >= len(self.contents):
            balls_drawn = self.contents
            self.contents = []
        else:
            indices = random.sample(range(len(self.contents)), num_balls)
            balls_drawn = [self.contents[i] for i in indices]
            self.contents = [ball for i, ball in enumerate(self.contents) if i not in indices]
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_matches = 0

    for _ in range(num_experiments):
        balls = copy.deepcopy(hat.contents)
        balls_drawn = hat.draw(num_balls_drawn)
        success = True

        for color, quantity in expected_balls.items():
            if balls_drawn.count(color) < quantity:
                success = False
                break

        if success:
            num_matches += 1

    return num_matches / num_experiments


hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"red":1, "green":2}, num_balls_drawn=4, num_experiments=10000)
print(probability)