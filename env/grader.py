def grade(total_reward, max_steps=3):
    """
    Normalize total reward into score between 0.0 and 1.0

    Parameters:
    - total_reward : float
    - max_steps : int (episode length)

    Returns:
    - score between 0.0 and 1.0
    """

    max_possible = max_steps * 1.0
    min_possible = max_steps * -0.5

    normalized = (total_reward - min_possible) / (max_possible - min_possible)

    normalized = max(0.01, min(0.99, normalized))

    return round(normalized, 3)


def grade_task(task_name, total_reward):
    """
    Task-specific grading (easy, medium, hard)

    Harder tasks slightly weighted for fairness
    """

    difficulty_weights = {
        "easy": 1.0,
        "medium": 1.1,
        "hard": 1.2
    }

    base_score = grade(total_reward)

    weighted_score = base_score * difficulty_weights.get(task_name, 1.0)

    weighted_score = max(0.01, min(0.99, weighted_score))

    return round(weighted_score, 3)