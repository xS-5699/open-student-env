import random


class StudentEnv:

    def __init__(self):
        self.state_data = None
        self.done = False
        self.steps = 0
        self.max_steps = 3

    def reset(self, difficulty="medium"):

        if difficulty == "easy":
            assignments = [
                {"name": "Lab Report", "deadline": 2, "difficulty": 2, "completed": False},
                {"name": "Quiz", "deadline": 1, "difficulty": 1, "completed": False},
            ]

        elif difficulty == "hard":
            assignments = [
                {"name": "AI Report", "deadline": 1, "difficulty": 4, "completed": False},
                {"name": "Cyber Lab", "deadline": 2, "difficulty": 3, "completed": False},
                {"name": "Group Project", "deadline": 2, "difficulty": 5, "completed": False},
                {"name": "Research Paper", "deadline": 3, "difficulty": 4, "completed": False},
                {"name": "Presentation", "deadline": 1, "difficulty": 3, "completed": False},
            ]

        else:  # medium
            assignments = [
                {"name": "AI Report", "deadline": 1, "difficulty": 3, "completed": False},
                {"name": "Cyber Lab", "deadline": 3, "difficulty": 2, "completed": False},
                {"name": "Group Project", "deadline": 2, "difficulty": 4, "completed": False},
            ]

        self.state_data = {
            "assignments": assignments,
            "time_available": 4,
            "team_status": {
                "member1": "busy",
                "member2": "free"
            }
        }

        self.steps = 0
        self.done = False

        return self.state()

    def step(self, action):

        reward = 0.0
        self.steps += 1

        for assignment in self.state_data["assignments"]:
            if assignment["name"] == action["prioritize"]:
                assignment["completed"] = True
                reward += 0.5

        if action["allocate_time"] > 2:
            reward += 0.2

        if action["assign_to"] == "member2":
            reward += 0.2

        for assignment in self.state_data["assignments"]:
            assignment["deadline"] -= 1

        for assignment in self.state_data["assignments"]:
            if assignment["deadline"] < 0 and not assignment["completed"]:
                reward -= 0.3

        if self.steps >= self.max_steps:
            self.done = True

        return self.state(), reward, self.done, {}

    def state(self):
        return self.state_data