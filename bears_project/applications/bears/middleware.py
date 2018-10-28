# import requests

from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class IlovebearMiddleware(MiddlewareMixin):
    """
    Middleware to check created cookie
    and
    delete cookie after redirect to i_love_bears
    """
    def process_response(self, request, response):
        if request.COOKIES.get('i_love_cookies', None):
            response.delete_cookie('i_love_cookies')
        return response

    def process_request(self, request):
        """
        check if cookie exist or not
        :param request:
        :return:
        """
        if request.COOKIES.get('i_love_cookies', None):
            print(request.COOKIES['i_love_cookies'])
        else:
            print(' No cookies')
        return None