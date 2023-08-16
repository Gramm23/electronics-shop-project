from src.item import Item


class LanguageMixin:
    ENG = "EN"
    RUS = "RU"

    def __init__(self):
        self._language = self.ENG

    def change_lang(self):
        if self._language == self.ENG:
            self._language = self.RUS
        else:
            self._language = self.ENG
        return self


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)

    @property
    def language(self):
        return self._language



