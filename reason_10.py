import random
import time


def generate_fake_spreadsheet():
    print("\n----- Love Efficiency Spreadsheet -----")
    print("| Day | Love Units | Productivity Boost |")
    print("|-----|------------|---------------------|")
    for day in range(1, 8):
        love_units = random.randint(50, 100)
        productivity = love_units * 1.5
        print(f"| {day:3} | {love_units:10} | {productivity:19.2f} |")
    print("----------------------------------------")
    print("Conclusion: Love makes you 273.5% more awesome!")


def final_reason():
    print("Final Reason: Because You Make My Heart Sing! 🎵❤️")
    print("Soooo ahem we'll let ms. Taylor Swift take the console, we present to you 'Daylight'")

    lyrics = """
        My love was as cruel as the cities I lived in
        Everyone looked worse in the light
        There are so many lines that I've crossed unforgiven
        I'll tell you the truth, but never goodbye
        I don't wanna look at anything else now that I saw you
        I don't wanna think of anything else now that I thought of you
        I've been sleeping so long in a 20-year dark night
        And now I see daylight, I only see daylight
        """

    print("\nLyrics:")
    for line in lyrics.strip().split('\n'):
        print(f"    🎵 {line.strip()}")

    time.sleep(50)
    print("\nTranslation for non-musical people (INTJ edition):")
    print("1. Past relationships = Inefficient urban planning")
    print("2. Emotional growth = Optimizing life algorithms")
    print("3. New love = Discovering a more efficient energy source")
    print("4. Daylight = Clarity in decision-making processes")

    time.sleep(10)
    print("\nIn conclusion: You've improved my life's efficiency by 273.5%!")
    print("P.S. I've created a spreadsheet to prove this. Want to review it together?")
    time.sleep(10)
    generate_fake_spreadsheet()

    print("If you thought this was nice then I have to admit, although the ideas were mine and I had a vision, I suck at putting them to practice so I had to bug prof goof like a lot :(     Does it make my love for yo less legit?")


if __name__ == '__main__':
    final_reason()
