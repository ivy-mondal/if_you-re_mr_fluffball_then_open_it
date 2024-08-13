import time
import matplotlib.pyplot as plt


def show_reason_3():
    print("""
        Reason #3: The Superhuman Listener (a.k.a. The 'Wait, You Actually Heard That?' Factor)

        1. Attention Span:
           - Longer than a giraffe's neck
           - Can focus on my ramblings for hours without dozing off

        2. Memory Bank:
           - Recalls I stored my project in which freaking directory in my computer when I'm crying about how I can't find my project
           - Remembers all project ideas and whatever shite I'm supposed to learn while I'm busy being a lazy arse

        3. Reaction Time:
           - Responds to my messages faster than a cat to a laser pointer
           - May have developed telepathic abilities

        4. Scientific* Conclusion:
           Mr. Attentive's listening skills > World's most advanced AI + all moms combined(except my mom ofc)
           * Science conducted by yours truly while ugly crying from happiness
        """)

    print("Behold, the graph of  listening prowess!")

    def create_listening_graph():
        categories = ['Mr. Attentive', 'My Mom', 'Average Joe', 'A Wall', 'My Ex']
        listening_levels = [100, 100, 30, 10, -5]  # Still as scientific as ever!

        plt.figure(figsize=(10, 6))
        bars = plt.barh(categories, listening_levels, color=['green', 'purple', 'blue', 'gray', 'red'])
        plt.title("Listening Level Comparison (Now Horizontal for Extra Pizzazz!)")
        plt.xlabel("Listening Level (in 'Actually Cares' Units)")

        for bar in bars:
            width = bar.get_width()
            plt.text(width, bar.get_y() + bar.get_height() / 2, f'{width}',
                     ha='left', va='center')

        plt.xlim(-10, 110)

        plt.annotate('Tied for 1st!', xy=(101, 0.5), xytext=(105, 0.5),
                     arrowprops=dict(facecolor='black', shrink=0.05),
                     ha='left', va='center')

        plt.savefig('listening_levels_horizontal.png')
        plt.close()

        time.sleep(40)

        img = plt.imread('listening_levels_horizontal.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    create_listening_graph()

    print("\nWould you look at that? It's a tie at the top!")
    print("Mr. Attentive and Mom: the dynamic duo I suspect shares same braincell")
    print("While others hear 'blah blah blah', you hear a symphony.")
    print("I'm not crying, you're crying! 😭✨")


if __name__ == '__main__':
    show_reason_3()
