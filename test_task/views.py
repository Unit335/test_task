from django.shortcuts import render


def rekruto(request):
    name = request.GET.get("name", "")
    msg = request.GET.get("message", "")
    err = ''
    if not msg:
        err = 'You should forward message via \'message\' parameter.'
    if not name:
        name = 'Anonym'
        err = err + '\nName should be forwarded via \'name\' parameter'
    return render(request, 'index.html', {'title': name, 'msg': msg, 'error': err})