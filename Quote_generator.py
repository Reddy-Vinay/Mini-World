import random

def get_quote(category):
    quotes = {
        'motivation': [
            "If you are still waiting for a perfect time, then you’re on mistake. Just, do it right now.. - {name}",
            "Your time is limited, don't waste it living someone else's life. - {name}",
            " Haters are everywhere. Blocking them out is the safest way to ignore them and move forward with our life goals.. - {name}"
        ],
        'success': [
            "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - {name}",
            "The road to success and the road to failure are almost exactly the same. - {name}",
            "Success usually comes to those who are too busy to be looking for it. - {name}"
        ],
        'life': [
            "Life is really simple, but we insist on making it complicated. - {name}",
            "Life is like riding a bicycle. To keep your balance, you must keep moving. - {name}",
            "Life is 10% what happens to us and 90% how we react to it. - {name}"
        ],
        'love': [
            "The best thing to hold onto in life is each other. - {name}",
            "Love yourself first and everything else falls into line. - {name}",
            "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - {name}"
        ]
    }
    return random.choice(quotes[category])

def main():
    name = input("Enter your name: ")
    
    while True:
        print("Select a category for the quote:")
        print("1. Motivation")
        print("2. Success")
        print("3. Life")
        print("4. Love")
        category_choice = input("Enter the number of your chosen category: ")

        categories = {
            '1': 'motivation',
            '2': 'success',
            '3': 'life',
            '4': 'love'
        }
        category = categories.get(category_choice)

        if category:
            quote = get_quote(category)
            personalized_quote = quote.replace("{name}", name)
            print("Here's your personalized quote:")
            print(personalized_quote)
            break
        else:
            print("Invalid category choice. Please try again.")

if __name__ == '__main__':
    main()
