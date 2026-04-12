def grade(total_reward, max_steps=3):

    max_possible = max_steps * 1.0
    min_possible = max_steps * -0.5

    normalized = (total_reward - min_possible) / (max_possible - min_possible)

    normalized = max(0.05, min(0.95, normalized))

    return normalized


def grade_task(task_name, total_reward):

    difficulty_weights = {
        "easy": 0.9,
        "medium": 1.0,
        "hard": 1.1
    }

    base_score = grade(total_reward)

    weighted_score = base_score * difficulty_weights.get(task_name, 1.0)

    weighted_score = max(0.05, min(0.95, weighted_score))

    return round(weighted_score, 3)