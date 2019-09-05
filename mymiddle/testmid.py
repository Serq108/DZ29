from django.utils.deprecation import MiddlewareMixin


class TestMid(MiddlewareMixin):

    def process_request(self, request):
        print('TESTTESTTESTTESTTESTTEST')
        return None
