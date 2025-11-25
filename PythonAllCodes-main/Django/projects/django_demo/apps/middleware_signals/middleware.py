import time
from django.utils.deprecation import MiddlewareMixin


class TimingMiddleware(MiddlewareMixin):
    """Simple middleware that times view execution and adds a header."""

    def process_request(self, request):
        request._start_time = time.perf_counter()

    def process_response(self, request, response):
        start = getattr(request, '_start_time', None)
        if start is not None:
            duration = (time.perf_counter() - start) * 1000.0
            response['X-View-Duration-ms'] = f"{duration:.2f}"
        return response
