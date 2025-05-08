import random

def roll_dice_generator(max_roll_num=1000):
    """
    Rolls a die the specified number of times and calculates the frequency and percentage of each face.

    Args:
        max_roll_num: The number of times to roll the die.
    """

    die_face_freqs = {face: 0 for face in range(1, 7)}

    for _ in range(max_roll_num):
        rand_point = random.random()  # Generate a random number between 0 and 1
        interval = 1 / 6  # Calculate the interval for each face

        if rand_point < interval:
            face = 1
        elif rand_point <= 2 * interval:
            face = 2
        elif rand_point < 3 * interval:
            face = 3
        elif rand_point < 4 * interval:
            face = 4
        elif rand_point < 5 * interval:
            face = 5
        else:
            face = 6

        die_face_freqs[face] += 1

    # Print the table header
    print("{:<10} {:<15} {:<15}".format("Face", "Frequency", "Percentage"))
    print("-" * 40)

    total_freq = 0
    total_percentage = 0.0

    # Print the frequency and percentage for each face
    for face in range(1, 7):
        frequency = die_face_freqs[face]
        percentage = (frequency / max_roll_num) * 100
        print("{:<10} {:<15} {:<15.2f}".format(face, frequency, percentage))
        total_freq += frequency
        total_percentage += percentage

    # Print the total row
    print("-" * 40)
    print("{:<10} {:<15} {:<15.2f}".format("Total", total_freq, total_percentage))

if __name__ == "__main__":
    roll_dice_generator()