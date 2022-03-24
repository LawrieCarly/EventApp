from django.shortcuts import render

# Create your views here.
def error_404(request, exception):
    data = {
        "message": '404 - Not Found',
        "exception": exception
    }
    return render(request, 'errors/error.html', data)

def error_403(request, exception):
    data = {
        "message": '403 - Unauthorised',
        "exception": exception
    }
    return render(request, 'errors/error.html', data)


def error_500(request):
    data = {
        "message": '500 - Internal Server Error',
        "exception": None
    }
    return render(request, 'errors/error.html', data)


def error_400(request, exception):
    data = {
        "message": '400 - Bad Request',
        "exception": exception
    }
    return render(request, 'errors/error.html', data)