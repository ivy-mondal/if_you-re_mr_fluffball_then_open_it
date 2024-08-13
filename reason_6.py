import time
import matplotlib.pyplot as plt
import numpy as np


def show_reason_6():
    print("""
    Reason #6: The Guy Who Became My Mom's Honorary Son (What Sorcery Is This?)

    1. Mom's Approval Rating:
       - Higher than her standards for India's prime minister
       - More positive than her reaction to my A+ report card

    2. Suspicious Activity:
       - All guys are baaaadd, except mr fluffball
       - If guy in 10m radius of her precious daughter:
           if mr fluffy:
              gentle smile
           else:
              mama bear mode activated: death stare!

    3. Shared Brain Cell Count:
       - You two are more in sync than our Wi-Fi connection
       - Howwwwww do you two always arrive at same conclusion?!

    4. Ganging Up Frequency:
       - More often than I eat chocolate (I want chocolate waaaah!)
       - More consistent than my sleep schedule

    5. Lost Son Probability:
       - Higher than the chances of me understanding quantum physics
       - She won't shut up about how you must be her long lost son or something....
    """)

    categories = ['Mom\'s Approval', 'Suspicion Immunity', 'Shared Brain Cells', 'Ganging Up Power', 'Honorary Son Status']
    yo_values = [9.9, 9.8, 9.5, 9.7, 9.9]
    average_guy_values = [2.0, 0.5, 1.0, 0.1, 0.0]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width / 2, yo_values, width, label='Mr Fluffy', color='lightblue')
    rects2 = ax.bar(x + width / 2, average_guy_values, width, label='Average Guy', color='lightgrey')

    ax.set_ylabel('Mom\'s Love-o-meter')
    ax.set_title('You vs Average Guy in Mom\'s Eyes')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha='right')
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    ax.annotate("Mom's new favorite child? 😱",
                xy=(4, 9.9),
                xytext=(3, 7),
                ha='center', va='bottom',
                bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="b", lw=2),
                arrowprops=dict(arrowstyle="->"))

    plt.savefig('mom_love_bar.png')
    plt.close()

    time.sleep(50)

    img = plt.imread('mom_love_bar.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print("mr fluffy is in da family now, yayyy!")
    print('Mom legit scares me by saying ,"if you evah hurt him I am disowning yo and adopting him instead"')
    print("still love yoo anyways 😜")


if __name__ == '__main__':
    show_reason_6()
