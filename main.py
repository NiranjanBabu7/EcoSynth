from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.environmental_agent import EnvironmentalAgent
from backend.utils.visualization import plot_environment

app = FastAPI(title="EcoSynth Backend")

# Allow frontend (React dev server) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # default Vite React dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent
env_agent = EnvironmentalAgent()

@app.get("/api/sensor_data")
def get_sensor_data():
    """Return current environmental state."""
    data = env_agent.get_state()
    return data

@app.get("/api/plot")
def get_plot():
    """Return a plot image of current environment."""
    plot_path = plot_environment(env_agent.get_state())
    return {"plot": plot_path}
