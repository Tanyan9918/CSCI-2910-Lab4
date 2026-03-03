from mtgapi import MTGApi
from deck import CommanderDeck

def choose_card_from_results(cards):
    if not cards:
        print("No cards found.")
        return None
    
    for i, card in enumerate(cards):
        print(f"{i + 1}. {card.name}")

    selection = input("Select number (or press Enter to cancel): ")

    if not selection.isdigit():
        return None
    
    index = int(selection) - 1

    if 0 <= index < len(cards):
        return cards[index]
    
    return None

def main():
    api = MTGApi()
    deck = CommanderDeck()

    while True:
        print("\n=== Commander Deck Builder ===")
        print("1. Search cards")
        print("2. Set commander")
        print("3. Add card to deck")
        print("4. Show deck")
        print("5. Validate deck")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter card name: ")
            cards = api.search_cards(name)
            choose_card_from_results(cards)

        elif choice == "2":
            name = input("Enter commander name: ")
            cards = api.search_cards(name)
            selected = choose_card_from_results(cards)

            if selected:
                deck.setCommander(selected)

        elif choice == "3":
            name = input("Enter card name: ")
            cards = api.search_cards(name)
            selected = choose_card_from_results(cards)

            if selected:
                deck.addCard(selected)

        elif choice == "4":
            deck.show()

        elif choice == "5":
            deck.validate()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()