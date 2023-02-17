from botik.api.api import Api

api: Api = None


def setApi(api_target: Api):
    global api
    api = api_target


__init__ = [api, setApi]
