import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        drawn_balls = []
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            drawn_balls.append(ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        match = True
        for ball, count in expected_balls.items():
            if drawn_balls.count(ball) < count:
                match = False
                break
        
        if match:
            success_count += 1

    probability = success_count / num_experiments
    return probability


