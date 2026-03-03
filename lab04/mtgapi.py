import requests
from models import Card

BASE_URL = "https://api.magicthegathering.io/v1"

class MTGApi:
    def __init__(self):
        self.session = requests.Session()

    def search_cards(self, name: str, page_size: int = 20) -> list[Card]:
        url = f"{BASE_URL}/cards"
        params = {
            "name": name,
            "pageSize": page_size
        }

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return [] 
        
        data = response.json()

        cards = []
        for card_data in data.get("cards", []):
            try:
                cards.append(Card.model_validate(card_data))
            except Exception:
                pass

        return cards
   