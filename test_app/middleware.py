# -*- coding: utf-8 -*-
def ip_track(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print request.META['REMOTE_ADDR']
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware