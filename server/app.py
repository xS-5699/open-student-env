from fastapi import FastAPI
from env.environment import StudentEnv
import uvicorn

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
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()