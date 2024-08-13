import time
import random
import matplotlib.pyplot as plt


def show_reason_7():
    print("""
    Reason #7: Hugs on Demand - The Human Snuggle Machine 🤗

    1. Hug Availability: 24/7, rain or shine, zombie apocalypse or alien invasion
    2. Hug Quality: From "warm fuzzy" to "OMG I can't breathe but I love it"
    3. Hug Speed: Faster than you can say "gib hugg noww"
    4. Hug Variety: Bear hugs, koala hugs, octopus hugs, you name it!
    5. Hug Duration: As long as you need, even if his arms fall asleep (such dedication!)
    [I can only imagine for now, but we gonna makeeeeeeeeee it sooooner pweeeeeseeee , rightttttttttttt?!]
    """)

    # Generate some fake hug data
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hugs = [random.randint(15, 20) for _ in range(7)]

    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(days, hugs, marker='o', linestyle='-', linewidth=2, markersize=12)
    plt.title("Weekly Hug-o-meter: Embrace the Love!", fontsize=16)
    plt.xlabel("Day of Week", fontsize=12)
    plt.ylabel("Number of Hugs", fontsize=12)

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.fill_between(days, hugs, alpha=0.2)

    for i, hug in enumerate(hugs):
        plt.annotate(f"{hug} hugs", (days[i], hug), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.text(0.5, 0.05, "Warning: Excessive hugging may cause extreme happiness!",
             ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='pink', alpha=0.5, edgecolor='red', boxstyle='round,pad=0.5'))

    plt.tight_layout()
    plt.savefig('hug_stats.png')
    plt.close()

    time.sleep(30)
    img = plt.imread('hug_stats.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print('prof goof said to me,"Aww, are not you just the sweetest little koala bear hanging onto your human tree? 🐨 "')
    print("Congrats! You've unleashed the power of the Hug-o-matic 3000!")
    print("Side effects may include: warm fuzzies, uncontrollable smiling, and severe attachment issues.")
    print("Remember: A hug a day keeps the grumpy away! 🌈✨")


if __name__ == '__main__':
    show_reason_7()
