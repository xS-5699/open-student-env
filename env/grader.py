def grade(total_reward, max_steps=3):
    """
    Normalize total reward into score between (0,1)
    """

    max_possible = max_steps * 1.0
    min_possible = max_steps * -0.5

    normalized = (total_reward - min_possible) / (max_possible - min_possible)

    normalized = max(0.01, min(0.99, normalized))

    return float(f"{normalized:.4f}")


def grade_task(task_name, total_reward):
    """
    Task-specific grading
    """

    difficulty_weights = {
        "easy": 0.95,
        "medium": 1.0,
        "hard": 1.05
    }

    base_score = grade(total_reward)

    weighted_score = base_score * difficulty_weights.get(task_name, 1.0)

    weighted_score = max(0.01, min(0.99, weighted_score))

    return float(f"{weighted_score:.4f}")