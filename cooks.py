def calculate_cook_bonus(present_days):
    """
    Calculates bonus for a cook based on number of present days.
    """
    if present_days >= 26:
        return 5000
    elif present_days >= 20:
        return 3000
    elif present_days >= 15:
        return 1500
    else:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python cook_bonus.py <cook_id> <name> <present_days>")
    else:
        cook_id = int(sys.argv[1])
        name = sys.argv[2]
        present_days = int(sys.argv[3])

        bonus = calculate_cook_bonus(present_days)

        print("\n--- Cook Bonus Details ---")
        print("Cook ID:", cook_id)
        print("Cook Name:", name)
        print("Present Days:", present_days)
        print("Bonus:", bonus)
