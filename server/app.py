from fastapi import FastAPI
from env.environment import StudentEnv

app = FastAPI()
env = StudentEnv()

@app.post("/reset")
def reset():
    return {"state": env.reset("medium")}

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state()

def main():
    return app