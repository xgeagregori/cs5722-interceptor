from app.classes.price import ChildrensPrice, NewReleasePrice, RegularPrice
from app.classes.movie_type import MovieType

class Movie:
    def __init__(self, title, price_code):
        self.title: str = title
        self.set_price_code(price_code)

    def get_price_code(self) -> int:
        return self.price.get_price_code()

    def set_price_code(self, arg):
        if arg == MovieType.REGULAR:
            self.price = RegularPrice()
        elif arg == MovieType.NEW_RELEASE:
            self.price = NewReleasePrice()
        elif arg == MovieType.CHILDRENS:
            self.price = ChildrensPrice()
        else:
            raise ValueError("Incorrect Price Code")

    def get_title(self) -> str:
        return self.title

    def get_charge(self, days_rented: int) -> float:
        return self.price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return self.price.get_frequent_renter_points(days_rented)
