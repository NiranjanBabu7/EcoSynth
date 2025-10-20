class BaseAgent:
    def __init__(self, name="BaseAgent"):
        self.name = name

    def step(self, observation):
        """Perform action based on observation"""
        raise NotImplementedError
