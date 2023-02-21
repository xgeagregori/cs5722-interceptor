from app.framework.price import ChildrensPrice, NewReleasePrice, RegularPrice
from app.framework.movie_type import MovieType


class Movie:
    def __init__(self, title, price_code):
        self.title: str = title
        self.set_price_code(price_code)

    def get_price_code(self) -> int:
        """Get price code"""
        return self.price.get_price_code()

    def set_price_code(self, arg):
        """Set price code"""
        if arg == MovieType.REGULAR:
            self.price = RegularPrice()
        elif arg == MovieType.NEW_RELEASE:
            self.price = NewReleasePrice()
        elif arg == MovieType.CHILDRENS:
            self.price = ChildrensPrice()
        else:
            raise ValueError("Incorrect Price Code")

    def get_title(self) -> str:
        """Get title"""
        return self.title

    def get_charge(self, days_rented: int) -> float:
        """Get charge for movie"""
        return self.price.get_charge(days_rented)

    def get_frequent_renter_points(self, days_rented: int) -> int:
        """Get frequent renter points for movie"""
        return self.price.get_frequent_renter_points(days_rented)
