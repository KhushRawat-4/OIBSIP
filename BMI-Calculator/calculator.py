def calculate_bmi(height, weight):
    """
    Calculate BMI.

    Args:
        height (float): Height in centimeters.
        weight (float): Weight in kilograms.

    Returns:
        float: BMI rounded to 2 decimal places.
    """

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    return round(bmi, 2)


def bmi_category(bmi):
    """
    Return BMI category and a short health message.
    """

    if bmi < 18.5:
        return (
            "Underweight",
            "You may benefit from gaining weight in a healthy way."
        )

    elif bmi < 25:
        return (
            "Normal Weight",
            "Your BMI is within the healthy range."
        )

    elif bmi < 30:
        return (
            "Overweight",
            "Regular exercise and a balanced diet may help."
        )

    else:
        return (
            "Obese",
            "Consider consulting a healthcare professional."
        )