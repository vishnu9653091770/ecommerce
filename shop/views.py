from django.http import HttpResponse as response


def index(request):
	return response("Hello index")
def about(request):
	return response("Hello about")