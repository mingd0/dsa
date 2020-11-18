import random


ALGORITHMS = [
        'Bubble sort',
        'Insertion sort',
        'Selection sort',
        'Merge sort',
    ]

def main():
    print(f"""Random algorithm: {random.choice(ALGORITHMS)}
          Implementation, worst-case time & space complexity""")

if __name__ == "__main__":
    main()
    



    
