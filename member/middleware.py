# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponseRedirect, redirect


try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):

        allow_path = {'/admin/', '/favicon.ico/',
                      '/media/', '/static/', '/member/login/', }

        if request.path.startswith("/admin") == True or request.path.startswith("/member") == True or request.path.startswith("/favicon.ico") == True or request.path.startswith("/media") == True or request.path.startswith("/static") == True:
        # if request.path in allow_path:
            pass
        else:
            if request.session.get('phone', None):
                pass
            else:
                return redirect('/member/login/')
