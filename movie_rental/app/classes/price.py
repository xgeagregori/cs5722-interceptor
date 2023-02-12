from abc import ABC, abstractmethod

from app.classes.movie_type import MovieType

class Price(ABC):
    @abstractmethod
    def get_price_code(self) -> MovieType:
        pass

    @abstractmethod
    def get_charge(self, days_rented: int) -> float:
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return 1

class ChildrensPrice(Price):
    def get_price_code(self) -> MovieType:
        return MovieType.CHILDRENS

    def get_charge(self, days_rented: int) -> float:
        this_amount = 1.5
        if days_rented > 3:
            this_amount += (days_rented - 3) * 1.5
        return this_amount

class NewReleasePrice(Price):
    def get_price_code(self) -> MovieType:
        return MovieType.NEW_RELEASE

    def get_charge(self, days_rented: int) -> float:
        return days_rented * 3.0

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return 2 if days_rented > 1 else 1

class RegularPrice(Price):
    def get_price_code(self) -> MovieType:
        return MovieType.REGULAR

    def get_charge(self, days_rented: int) -> float:
        this_amount = 2.0
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5
        return this_amount