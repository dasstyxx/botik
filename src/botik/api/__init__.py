from botik.api.api import Api

api: Api = None


def set_api(api_target: Api):
    global api
    api = api_target


def get_api(): return api


__init__ = [get_api, set_api]
