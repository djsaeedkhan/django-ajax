from django.shortcuts import render
from django.http import HttpResponse

#-----------------------------------------------------
def mygetview(request):
    if request.method == 'GET':
        print("**get**")
        data = request.GET['mydata']
        astr = "<html><b> you sent a get request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request,"null.html")


def mypostview(request):
    if request.method == 'POST':
        print("**post**")
        data = request.POST['mydata']
        astr = "<html><b> you sent a post request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request,"null.html")


def myajaxview(request):
    if request.method == 'POST':
        if request.is_ajax():
            print("**ajax post**")
            data = request.POST['mydata']
            astr = "<html><b> you sent an ajax post request </b> <br> Saeed  kjgubvu returned data: %s</html>" % data
            return HttpResponse(astr)
    return render(request,"null.html")


def myajaxformview(request):
    #if request.method == 'POST':
        #if request.is_ajax():
    import json
    print("**ajax form post**")
    #for k, v in request.POST.items():
    #    print
    #    k, v

    #print("field1 data: %s" % request.POST['field1'])
    #print("field2 data: %s" % request.POST['field2'])
    mydata = [{'foo': 1, 'baz': 2}]
    return HttpResponse(json.dumps(mydata), content_type="application/json")
    return render(request,"null.html")

def foo(request):
    return render(request, "ajax.html")
