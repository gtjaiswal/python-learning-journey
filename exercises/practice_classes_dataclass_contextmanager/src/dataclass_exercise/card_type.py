from enum import Enum
import re

class CardType(Enum):
    VISA = r"^4\d{15}$"
    MASTERCARD = r"^(5[1-5]\d{14}|2(22[1-9]|2[3-9]\d|[3-6]\d{2}|7[01]\d|720)\d{12})$"
    AMEX = r"^3[47]\d{13}$"

    def get_val_pattern(self)->str:
        return self.value

    @classmethod
    def identify_card(cls, card_num:str):
        for card_type in cls :
            if re.match(card_type.get_val_pattern(), card_num) :
                return card_type
        return None

if __name__=="__main__":
    print(CardType.identify_card("4111111111111111"))
    print(CardType.identify_card("5500000000000004"))
    print(CardType.identify_card("340000000000009"))

    # Test enum directly by instantiating
    card_type = CardType.identify_card("4111111111111111")
    print(f"Card type: {card_type}")  # CardType.VISA
    print(f"Card name: {card_type.name}")  # VISA
    print(f"Card pattern: {card_type.get_val_pattern()}")  # ^4\d{15}$

    # Loop through all card types
    for card in CardType:
        print(f"{card.name}: {card.get_val_pattern()}")