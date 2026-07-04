def validate_input(height, weight):
    """
    Validate height and weight entered by the user.

    Returns:
        (bool, message)
    """

    try:
        height = float(height)
        weight = float(weight)

    except ValueError:
        return False, "Height and Weight must be valid numbers."

    # Positive values
    if height <= 0:
        return False, "Height must be greater than 0 cm."

    if weight <= 0:
        return False, "Weight must be greater than 0 kg."

    # Realistic human limits
    if height < 50 or height > 300:
        return False, "Height should be between 50 cm and 300 cm."

    if weight < 10 or weight > 500:
        return False, "Weight should be between 10 kg and 500 kg."

    return True, ""