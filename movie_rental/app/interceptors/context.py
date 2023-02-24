from datetime import datetime

from ..framework.customer import Customer


class Context:
    def __init__(self, date: datetime, customer: Customer):
        self.customer = customer
        self.date = date

    def get_customer_rentals(self):
        """Get customer rentals"""
        return self.customer.get_rentals()
    
    def get_winter_frequent_renter_points(self):
        """Get winter frequent renter points for customer"""
        return self.customer.get_winter_frequent_renter_points()

    def get_penalty_points(self):
        """Get penalty points for customer"""
        return self.customer.get_penalty_points()

    def get_date(self):
        """Get date of rental"""
        return self.date

    def add_winter_frequent_renter_points(self, points: int):
        """Set winter frequent renter points for customer"""
        self.customer.add_winter_frequent_renter_points(points)

    def add_penalty_points(self, points: int):
        """Add penalty points to customer"""
        self.customer.add_penalty_points(points)
