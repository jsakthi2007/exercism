"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students (<= 40)."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Return scores that are at or above the threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create grade thresholds from D to A."""
    # Failing is <= 40
    passing_range = highest - 40
    interval = passing_range // 4

    return [
        41,
        41 + interval,
        41 + interval * 2,
        41 + interval * 3
    ]


def student_ranking(student_scores, student_names):
    """Return ranking list in required format."""
    result = []
    for i in range(len(student_scores)):
        rank = i + 1
        result.append(f"{rank}. {student_names[i]}: {student_scores[i]}")
    return result


def perfect_score(student_info):
    """Return first student with score 100."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []