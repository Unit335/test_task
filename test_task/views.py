from django.shortcuts import render


def rekruto(request):
    name = request.GET.get("name", "")
    msg = request.GET.get("message", "")
    if not msg:
        msg = 'You should forward message via \'message\' parameter.'
    if not name:
        name = 'Anonym'
        msg = msg + '\nName should be forwarded via \'name\' parameter'
    return render(request, 'index.html', {'title': name, 'cal': msg})