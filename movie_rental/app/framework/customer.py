from app.framework.rental import Rental


class Customer:
    def __init__(self, name):
        self.rentals: list[Rental] = []
        self.name: str = name
        self.winter_frequent_renter_points: int = 0
        self.penalty_points: int = 0

    def get_name(self) -> str:
        """Get customer name"""
        return self.name

    def add_rental(self, arg):
        """Add rental to customer"""
        self.rentals.append(arg)

    def get_rentals(self) -> list[Rental]:
        """Get customer rentals"""
        return self.rentals

    def statement(self) -> str:
        """Generate statement for customer"""
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self.rentals:
            # Show figures for this rental
            result += (
                "\t"
                + each.get_movie().get_title()
                + "\t"
                + str(each.get_charge())
                + "\n"
            )

        # Add footer lines
        result += "Amount owed is " + str(self.get_total_charge()) + "\n"
        result += (
            "You earned "
            + str(self.get_total_frequent_renter_points())
            + " frequent renter points"
        )

        return result

    def html_statement(self) -> str:
        """Generate HTML statement for customer"""
        result = "<h1>Rental Record for <em>" + self.get_name() + "</em></h1>\n"

        result += "<table>\n"
        result += "<tr><th>Movie</th><th>Days</th><th>Amount</th></tr>\n"

        for each in self.rentals:
            # Show figures for this rental
            result += (
                "<tr><td>"
                + each.get_movie().get_title()
                + "</td><td>"
                + str(each.get_days_rented())
                + "</td><td>"
                + str(each.get_charge())
                + "</td></tr>\n"
            )

        # Add footer lines
        result += "</table>\n"
        result += (
            "<p>Amount owed is <em>" + str(self.get_total_charge()) + "</em></p>\n"
        )
        result += (
            "<p>You earned <em>"
            + str(self.get_total_frequent_renter_points())
            + "</em> frequent renter points</p>"
        )

        return result

    def get_total_charge(self) -> float:
        """Return the total charge on the customer's account."""
        result = 0
        for each in self.rentals:
            result += each.get_charge()

        # Add charge for penalty points
        result += 2.0 * self.penalty_points

        return result

    def get_total_frequent_renter_points(self) -> int:
        """Return the total frequent renter points on the customer's account."""
        result = 0
        for each in self.rentals:
            result += each.get_frequent_renter_points()

        # Add winter frequent renter points
        result += self.get_winter_frequent_renter_points()

        return result

    def get_winter_frequent_renter_points(self) -> int:
        """Return the number of winter frequent renter points on the customer's account."""
        return self.winter_frequent_renter_points

    def set_winter_frequent_renter_points(self, points: int):
        """Set the number of winter frequent renter points on the customer's account."""
        self.winter_frequent_renter_points = points

    def get_penalty_points(self) -> int:
        """Return the number of penalty points on the customer's account."""
        return self.penalty_points

    def add_penalty_points(self, points: int):
        """Add penalty points to the customer's account."""
        self.penalty_points += points
