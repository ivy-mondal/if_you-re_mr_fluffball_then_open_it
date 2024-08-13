import random
import time


def show_reason_9():
    print("""
    Reason #9: My Safe Space for Ultimate Goofiness 🤪🎉

    You never judge my:
    1. Random UwU outbursts
    2. Terrible puns
    3. Not so funny jokes
    3. Dramatic coding sessions
    4. Coming up with absolutely absurd ideas 
    5. Belief that programmers do magic!
    """)

    def chaotic_uwu():
        uwu_phrases = ["UwU", "OwO", "^w^", ":3", "nya~"]
        for _ in range(10):
            print(random.choice(uwu_phrases), end=" ")
            time.sleep(1)
        print("\n")

    time.sleep(30)
    print("\nInitiating goofy mode in 3... 2... 1...")
    chaotic_uwu()

    # Now, let's create a "love meter" that always maxes out
    time.sleep(20)
    print("\nCalculating love level:")
    for i in range(101):
        print(f"Love level: {i}%", end="\r")
        time.sleep(0.1)
    print("Love level: ERROR - OVERFLOW! Too much love to compute! 💖💖💖")

    print("\nRemember: In the grand code of life, you're my favorite function! Keep being adorkable!")
    print("btw I absolutely love your Language Dove too,imma learn Russian one day for sure, promiseee! Definitely just waiting for funny mode ;p")
    print("I know there is no graph here but I neva said there is gonna be graph everywhere , ehe")


if __name__ == '__main__':
    show_reason_9()
