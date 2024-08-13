import time
from tqdm import tqdm
import matplotlib.pyplot as plt


def show_reason_8():
    print("""
    Reason #8: My Personal Code Wizard and Debugger Extraordinaire 🧙‍♂️💻

    1. Encouragement Level: Over 9000! Thanks to yoo I can code some crappy cringey shi like this
    2. Patience: Infinite (unlike my loops)! How come you never get anggy
    3. Debugging Skills: Can spot a missing semicolon from a mile away, you be casually flexing 14 years of experience powah
    4. Motivational Quotes: "Everything is fixable in programming" (except maybe my smol brain)
    5. Expert Mode: Activated when I'm about to throw my laptop out the window
    """)

    # Let's make a silly progress bar to show  Python journey

    time.sleep(40)

    print("\nLoading my Python skills... powered by love and tea!")
    for _ in tqdm(range(100)):
        time.sleep(0.1)

    print("\nTa-da! From 'Hello World' to 'Hello, I'm a coding wizard' in no time flat!(I know I'm not but let's just pretend UwU)")

    # Now, let's create a pie chart of "Things I've Learned Thanks to My Code Guru"

    time.sleep(10)
    skills = ['Python Basics', 'Debugging', 'Not Smashing Computer', 'Making Silly Programs', 'Impressing My mr Fluffball']
    sizes = [30, 25, 20, 15, 10]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

    plt.pie(sizes, labels=skills, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title("Things I've Learned Thanks to My Code Guru")
    plt.show()

    print("\nRemember: Behind every great coder is an even greater motivator... or in my case, a fluffy debugger! 🐾💕")
    print("Can't evah thank yooo enough!")


if __name__ == '__main__':
    show_reason_8()
