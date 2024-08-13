import time
import matplotlib.pyplot as plt
import numpy as np


def show_reason_2():
    print("""
    Reason #2: Intellectual Superiority (a.k.a. "The Smart Cookie Factor")

    1. Problem-Solving Prowess:
       - Consistently provides solutions to my wildest ideas
       - Success rate: ~99.9% (margin of error: my stubbornness)

    2. First Impression:
       - Initial thought: "Wow, this guy's brain is on another level!"
       - Impression has only strengthened over time

    3. Comparative Analysis:
       - Subject (Mr meow) vs. Control Group (rest of humanity)
       - Result: Subject's intelligence far exceeds control group
       - Note: Analysis may be influenced by high affection levels

    4. Objective* Conclusion:
       Mr. Fluffball's intelligence > Universe's smartest person's intelligence
       * Objectivity may be compromised due to overwhelming bias

    Further research ongoing, but results suggest strong correlation 
    between Mr. Fluffball's intelligence and my increasing adoration.
    (* all credits for the literary masterpiece goes to Claude Sonnet 3.5, I just provided the base idea, format and organizing done by prof goof)
    """)
    print("Don't believe me? Check out this graph!")

    def create_graph():
        categories = ['Mr. Fluffball', 'Einstein', 'Stephen Hawking', 'Me trying to code']
        intelligence = [1000, 160, 160, -5]  # IQ scores (totally accurate, trust me)

        plt.figure(figsize=(10, 6))
        bars = plt.bar(categories, intelligence, color=['red', 'blue', 'green', 'yellow'])
        plt.title("Totally Unbiased Intelligence Comparison")
        plt.ylabel("Intelligence Level (Fluffball Units)")

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height}',
                     ha='center', va='bottom')
        plt.ylim(-10, 1100)

        plt.savefig('intelligence.png')
        plt.close()

        time.sleep(60)

        img = plt.imread('intelligence.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    create_graph()

    print("\nAs you can see, Mr. Fluffball's intelligence is off the charts!")
    print("Einstein and Hawking are left in the dust, and my coding skills... well, let's not talk about that.")
    print("It's clear that Mr. Fluffball is the smartest cookie in the jar! 🍪🧠")


if __name__ == '__main__':
    show_reason_2()
