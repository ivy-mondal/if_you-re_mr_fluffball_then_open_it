import random
import time
import matplotlib.pyplot as plt


def show_reason_4():
    print("""
    Reason #4: The Human Cat (a.k.a. The 'Did You Just Meow?' Phenomenon)

    1. Meow Responsiveness:
       - Faster than I can say "pweeasee"
       - May actually be part feline (DNA test pending)

    2. Meow Quality:
       - Better than my cats because they don't give a shi about me unless they hunggy
       - Has been known to make real cats jealous(because I said so)

    3. Meow Variety:
       - Can produce different meows on demand , normal-> Russian, they sound same though :)
       - Might secretly be voice actor for cat food commercials(definitely true)

    4. Scientific* Conclusion:
       Mr meow's meowing abilities > Actual cats + All cat videos on the internet combined
       * Science conducted by yours truly while giggling uncontrollably
    """)

    print("Prepare yourself for the Meow-O-Meter!")

    def create_meow_graph():
        meow_types = ['Cute', 'Demanding', 'Sleepy', 'Hungry', 'Playful']
        meow_ratings = [random.randint(80, 100) for _ in range(5)]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(meow_types, meow_ratings, color='orange')
        plt.title("mr meow's Meow-O-Meter")
        plt.ylabel("Meow Cuteness Level")

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height}%', ha='center', va='bottom')

        plt.ylim(0, 110)

        plt.savefig('meow_o_meter.png')
        plt.close()

        time.sleep(40)  # Brief pause for dramatic effect

        img = plt.imread('meow_o_meter.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    create_meow_graph()

    print("\nWow! Look at those meow-nificent scores!")
    print("Your  meowing skills are off the charts!")
    print("Yoo not just any cat, you're most fluffy and adorable hooman meow evahh 😻")
    print("Please don't die from cringe :(")


if __name__ == '__main__':
    show_reason_4()
