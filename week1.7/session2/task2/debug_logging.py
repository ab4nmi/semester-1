# Week 1.7, Session 2: Task 2 - logging

import logging
def calculate_average(scores):
    """gets the avrage of the scores list"""
    # add logging configuration
    logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)

    # you can turn the logging off
    # logging.disable(logging.CRITICAL)

    logger = logging.getLogger()
    logger.info(f"calculate_average(): started")

    total_score = sum(scores)
    total_assignments = len(scores)

    # log the total score and num of assignments
    logger.debug(f"total score: {total_score}, assignments: {total_assignments}")

    # changed // to / cos it was rounding down
    average = total_score / total_assignments

    # log the avrage
    logger.debug(f"avrage is {average}")

    return round(average,2)

print(calculate_average([85, 90, 88]))
# 
#Expected Output: 87.67
# Actual Output:   87.67