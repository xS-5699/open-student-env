import os
import json
import re
from env.grader import grade_task
from dotenv import load_dotenv
from openai import OpenAI
from env.environment import StudentEnv

load_dotenv()

# print("API KEY:", os.getenv("OPENAI_API_KEY")[:10])
# print("MODEL:", os.getenv("MODEL_NAME"))
# print("BASE URL:", os.getenv("API_BASE_URL"))

print("[START]")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("API_BASE_URL")
)

MODEL_NAME = os.getenv("MODEL_NAME")

env = StudentEnv()

tasks = ["easy", "medium", "hard"]

for task in tasks:

    print(f"\n[START TASK] {task}")

    state = env.reset(task)

    print("Initial State:", state)

    total_reward = 0
    done = False

    while not done:

        prompt = f"""
You are an AI student assistant.

You MUST return ONLY valid JSON.
No explanation.
No markdown.
No reasoning.
No extra text.

State:
{state}

Return format:
{{
"prioritize": "assignment_name",
"allocate_time": number,
"assign_to": "member1 or member2"
}}
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        action_text = response.choices[0].message.content

        print("Model Output:", action_text)

        try:
            json_match = re.search(r"\{.*\}", action_text, re.DOTALL)
            action = json.loads(json_match.group())
        except:
            action = {
                "prioritize": "AI Report",
                "allocate_time": 3,
                "assign_to": "member2"
            }

        state, reward, done, _ = env.step(action)

        total_reward += reward

        print("[STEP]", reward)

    score = grade_task(task, total_reward)

    print(f"[END TASK] {task} Total Reward:", total_reward)
    print(f"[SCORE] {task}:", score)


print("[END]")

import time
