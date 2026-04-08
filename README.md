# OpenStudentEnv — RL Environment for Academic Task Management

## Overview

OpenStudentEnv is a real-world reinforcement learning environment that simulates academic workload management for students. The environment evaluates how well an AI agent can prioritize assignments, allocate time, and coordinate team members under realistic constraints.

This environment models a common real-world problem faced by students: managing multiple assignments with deadlines, varying difficulty levels, and limited resources.

The goal is to enable AI agents to learn effective decision-making strategies in academic planning scenarios.

---

## Real-World Motivation

Students constantly face:

- Multiple assignments
- Conflicting deadlines
- Group project coordination
- Limited available time
- Changing priorities

This environment simulates those real-world conditions and evaluates how effectively an AI agent can manage them.

---

## Environment Design

The environment follows the OpenEnv specification and implements:

- reset()
- step()
- state()

The AI agent interacts with the environment step-by-step and receives rewards based on decision quality.

---

## Observation Space

Each observation includes:

```python
{
  "assignments": [
    {
      "name": str,
      "deadline": int,
      "difficulty": int,
      "completed": bool
    }
  ],
  "time_available": int,
  "team_status": {
    "member1": str,
    "member2": str
  }
}

## Action Space

The agent outputs an action in JSON format:

{
  "prioritize": "assignment_name",
  "allocate_time": number,
  "assign_to": "member1 or member2"
}

## Reward Function

Rewards are assigned based on:

Positive Rewards:
- Completing assignments
- Prioritizing urgent tasks
- Efficient time allocation

Negative Rewards:
- Missing deadlines
- Poor prioritization
- Repeated assignments

## Tasks

### Easy
- 2 assignments
- Simple prioritization

### Medium
- 3 assignments
- Mixed deadlines

### Hard
- 5 assignments
- Conflicting deadlines

## Agent Grader

Each task returns score between:

0.0 - 1.0

Based on:
- Task completion
- Efficiency
- Decision quality

## Setup

pip install -r requirements.txt

python inference.py

## Docker

docker build -t open-student-env .

docker run open-student-env