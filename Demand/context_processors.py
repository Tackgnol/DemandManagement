from Demand.models import Activity

def IsManager(request):
    if request.user.is_authenticated:
        get = Activity.objects.filter(Manager = request.user)
        if get.exists():
            return {'IsManager' : True}
        else:
            return {'IsManager' : False}
    else:
        return {'IsManager': False}

