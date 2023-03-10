class Dispatcher:
    def __init__(self):
        self.interceptors = []

    def attach(self, interceptor):
        """Attach an interceptor to the dispatcher"""
        self.interceptors.append(interceptor)

    def detach(self, interceptor):
        """Detach an interceptor from the dispatcher"""
        self.interceptors.remove(interceptor)

    def update(self, context):
        """Update the dispatcher"""
        self.dispatch(context)

    def dispatch(self, context):
        """Dispatch the context to the interceptors"""
        for interceptor in self.interceptors:
            interceptor.intercept(context)
