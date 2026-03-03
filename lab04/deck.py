from models import Card

BasicLands = {
    "Forest",
    "Island",
    "Mountain",
    "Plains",
    "Swamp"
}

class CommanderDeck:
    def __init__(self):
        self.commander = None
        self.cards = []

    def setCommander(self, card: Card):
        if not card.supertypes or "Legendary" not in card.supertypes:
            print("Not a valid Commander, Commander must be Legendary")
            return
        
        self.commander = card
        print(f"{card.name} is now your commander.")

    def addCard(self, card: Card):
        if not self.commander:
            print("You must set a Commander first")
            return
        
        if card.name not in BasicLands:
            for existing_card in self.cards:
                if existing_card.name == card.name:
                    print("Commander only allows 1 copy of each card")
                    return
            
        commander_colors = set(self.commander.colorIdentity or [])
        card_colors = set(card.colorIdentity or [])

        if not card_colors.issubset(commander_colors):
            print("Card does not match you commander's color identity")
            return
        
        self.cards.append(card)
        print(f"Added {card.name}")

    def totalCards(self):
        if self.commander:
            return len(self.cards) + 1
        return len(self.cards)
    
    def validate(self):
        if not self.commander:
            print("No commander selected")
            return False

        if self.totalCards() != 100:
            print(f"Deck must have exactly 100 cards. You have {self.totalCards()}.")
            return False
        
        print("Deck is valid")
        return True
    
    def show(self):
        print("\n ===== Commander Deck =====")

        if self.commander:
            print(f"\nCommander: {self.commander.name}")
        else:
            print("\nNo commander selected")

        print("\nMain Deck:")
        for card in self.cards:
            print(card.name)

        print(f"\nTotal cards: {self.totalCards()}")    
