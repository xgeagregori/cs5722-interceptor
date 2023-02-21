from abc import ABC, abstractmethod

from app.framework.movie_type import MovieType


class Price(ABC):
    @abstractmethod
    def get_price_code(self) -> MovieType:
        """Get price code"""
        pass

    @abstractmethod
    def get_charge(self, days_rented: int) -> float:
        """Get charge for movie"""
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        """Get frequent renter points for movie"""
        return 1


class ChildrensPrice(Price):
    def get_price_code(self) -> MovieType:
        """Get price code"""
        return MovieType.CHILDRENS

    def get_charge(self, days_rented: int) -> float:
        """Get charge for movie"""
        this_amount = 1.5
        if days_rented > 3:
            this_amount += (days_rented - 3) * 1.5
        return this_amount


class NewReleasePrice(Price):
    def get_price_code(self) -> MovieType:
        """Get price code"""
        return MovieType.NEW_RELEASE

    def get_charge(self, days_rented: int) -> float:
        """Get charge for movie"""
        return days_rented * 3.0

    def get_frequent_renter_points(self, days_rented: int) -> int:
        """Get frequent renter points for movie"""
        return 2 if days_rented > 1 else 1


class RegularPrice(Price):
    def get_price_code(self) -> MovieType:
        """Get price code"""
        return MovieType.REGULAR

    def get_charge(self, days_rented: int) -> float:
        """Get charge for movie"""
        this_amount = 2.0
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5
        return this_amount
