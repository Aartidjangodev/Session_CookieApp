from django.shortcuts import render

# Create your views here.
def setCookie(request):
    response=render(request,'setCookies.html')
    response.set_cookie('cname','john')
    return response
def getCookie(request):
    vname=request.COOKIES.get('cname')
    return render(request,'getCookie.html',{'ckname':vname})
def delCookie(request):
    response=render(request,'delCookie.html')
    response.delete_cookie('cname')
    return response
def setSession(request):
    request.session['sname']='Alice'
    return render(request,'setSession.html')
def getSession(request):
    vname=request.session.get('sname')
    return render(request,'getSession.html',{'SNname':vname})
def delSession(request):
    request.session.flush()
    return render(request,'delSession.html')

