#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'renjunwei'

'''
async web application.
'''

from aiohttp import web

router = web.RouteTableDef()

@router.get('/')
async def index(request):
    return web.Response(text='this is my first python app!')

app = web.Application()
app.add_routes(router)
web.run_app(app)



