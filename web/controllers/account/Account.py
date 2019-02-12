# -*- coding: utf-8 -*-
from flask import Blueprint, request
from common.libs.Helper import ops_render, iPagination
from common.models.User import User
from application import app, db

route_account = Blueprint('account_page',__name__)


@route_account.route("/index")
def index():
    resp_data = {}
    req = request.values

    page = int(req['page']) if ('page' in req and req['page']) else 1

    query = User.query

    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': '/account/index'
    }

    pages = iPagination(page_params)
    offset = (page-1)*app.config['PAGE_SIZE ']
    limit = app.config['PAGE_SIZE']*page

    list = query.order_by(User.uid.desc()).all()[offset:limit]
    resp_data['list'] = list
    resp_data['pages'] = pages
    return ops_render("account/index.html", resp_data)


@route_account.route("/info")
def info():
    return ops_render("account/info.html")


@route_account.route("/set")
def set():
    return ops_render("account/set.html")
