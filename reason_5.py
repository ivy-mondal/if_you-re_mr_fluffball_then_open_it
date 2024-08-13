import time
import matplotlib.pyplot as plt
import numpy as np


def show_reason_5():
    print("""
    Reason #5: My Personal Human Lighthouse in the Storm of Life

    1. Comfort Level:
       - Warmer than blanket in cold winter night
       - Cozier than hugging a sleeping cat 

    2. Patience Meter:
       - Higher than Mt. Everest
       - Longer than the Trans-Siberian Railway

    3. Reliability Rating:
       - More dependable than gravity
       - Steadier than a cat's judgmental stare

    4. Project Support:
       - From "I want to make spinning globe" to "Let's move to Mars"
       - Always says "it's fine :)" (even when it's not)

    5. Life Event Companion:
       - There for both "give name to my cat" and "whoops me almost died, teehee"
       - Brings fluffiness to all occasions
    """)

    categories = ['Comfort', 'Patience', 'Reliability', 'Support', 'Companionship']
    values = [10, 10, 10, 10, 9]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, categories)
    ax.set_ylim(0, 10)
    ax.set_title("Lighthouse of Love: Stability in the Storm of Life")

    ax.annotate("1 point deducted\nbecause you miss calls 😛",
                xy=(angles[-2], values[-2]),
                xytext=(angles[-2], 12),
                ha='center', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="b", lw=2),
                arrowprops=dict(arrowstyle="->"))

    plt.savefig('comfyy.png')
    plt.close()

    time.sleep(40)

    img = plt.imread('comfyy.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print("\nWow! Look at that chart! Mr comfy is basically a superhero!")
    print("You're like a Swiss Army knife of love, but less pointy and more huggable.")
    print("Quick, someone call Marvel! We've found their next Avenger: Captain Comfy!")
    print("(Just don't expect him to stick to the call schedule... 😉)")


if __name__ == '__main__':
    show_reason_5()
