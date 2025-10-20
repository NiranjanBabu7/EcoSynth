import pandas as pd
import numpy as np
from backend.agents.agent import BaseAgent  # Removed the .py extension

class EnvironmentalAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="EnvironmentalAgent")
        # Load sensor data
        self.sensor_data = pd.read_csv("backend/data/sensor_data.csv")
        self.current_index = 0

    def get_state(self):
        """Return current environment state"""
        if self.current_index >= len(self.sensor_data):
            self.current_index = 0
        state = self.sensor_data.iloc[self.current_index].to_dict()
        self.current_index += 1
        return state

