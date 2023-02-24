from app.interceptors.interceptors import (
    Interceptor,
    WinterFRPInterceptor,
    LateReturnPenaltyInterceptor,
)


class InterceptorFactory:
    def get_winter_frp_interceptor(self) -> Interceptor:
        """Get the winter frequent renter points interceptor"""
        return WinterFRPInterceptor()

    def get_late_return_penalty_interceptor(self) -> Interceptor:
        """Get the late return penalty interceptor"""
        return LateReturnPenaltyInterceptor()
