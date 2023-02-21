from abc import ABC, abstractmethod

from app.interceptors.context import Context


class Interceptor(ABC):
    @abstractmethod
    def intercept(self, context: Context):
        """Intercept the event"""
        pass


class WinterFRPInterceptor(Interceptor):
    def intercept(self, context: Context):
        """Intercept the event"""
        date = context.get_date()

        if date.month == 12:
            context.set_winter_frequent_renter_points(2)
            print(f"[Bonus]: +2 winter frequent renter points")


class LateReturnPenaltyInterceptor(Interceptor):
    def intercept(self, context: Context):
        """Intercept the event"""
        rentals = context.get_customer_rentals()

        for rental in rentals:
            if rental.get_days_rented() > 7:
                context.add_penalty_points(1)
                print(
                    f"[Warning]: Late return penalty +{2.0 * context.get_penalty_points()}"
                )
