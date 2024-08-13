import time
import matplotlib.pyplot as plt


def show_reason_1():
    print("Reason 1: The adorableness UwU")
    print("==============================")
    print("ohh shi...where do I even start?!")
    print("My mr meow is like da most adorable fluffball everrr")
    print("You're so charmingly awkward at times, my heart be exploding from cuteness overload :p")
    print("On my personal Adoooorableeeness Scale, you're right up there with my mom and my cats.")
    print("That's right,yo achieved legendary status!")
    print("Even my beloved anime husbandos, Tartaglia and Aventurine, can't compete.")
    print("Don't believe me? Check out this graph!")
    print()

    characters = ['mr fluffy', 'mom', 'disco & company', 'Tartaglia', 'Aventurine']
    adorableness = [10, 10, 10, 9.5, 9.5]

    plt.figure(figsize=(10, 6))
    plt.bar(characters, adorableness, color=['red', 'pink', 'orange', 'blue', 'green'])

    plt.xlabel('Characters')
    plt.ylabel('Adorableness Level')
    plt.title("Ivy's Adorableness Scale")

    for i, v in enumerate(adorableness):
        plt.text(i, v, str(v), ha='center', va='bottom')

    plt.savefig('adorableness.png')
    plt.close()

    time.sleep(60)

    img = plt.imread('adorableness.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print()
    print("See? The numbers don't lie. You're at the top of the cuteness food chain!")
    print("Sorry, anime boys, but real-life awkward charm wins this round! 💖")


if __name__ == "__main__":
    print("Testing reason_1.py...")
    show_reason_1()
    print("If you see the graph and text above, it's working!")
