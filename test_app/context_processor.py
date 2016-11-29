import datetime


def current_time(request):
    return {"cur_time": datetime.datetime.now()}