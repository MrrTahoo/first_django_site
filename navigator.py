# Custom created file by : Muhammad Taha

from django.http import HttpResponse
from django.shortcuts import render


def viewer(request):
    params = {'name': 'Taha', 'place': 'Pakistan'}
    return render(request, "web_viewed.html", params)


def removepunc(request):
    dj = request.GET.get('user_inp', 'default')
    rp = request.GET.get('removepunc', 'off')
    uc = request.GET.get('uppercase', 'off')
    newlr = request.GET.get('newlr', 'off')
    esr = request.GET.get('esr', 'off')
    cc = request.GET.get('cc', 'off')
    if rp == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in dj:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'atext': analyzed, 'purpose': 'Remove Puntuation'}
        return render(request, 'analysed_text.html', params)

    elif uc == "on":
        analyzed = ""
        for char in dj:
            analyzed = analyzed + char.upper()
        params = {'atext': analyzed, 'purpose': 'Capatilise'}
        return render(request, 'analysed_text.html', params)

    elif newlr == "on":
        analyzed = ""
        for char in dj:
            if char != "\n":
                analyzed = analyzed + char
        params = {'atext': analyzed, 'purpose': 'Removed New Line'}
        return render(request, 'analysed_text.html', params)

    elif esr == "on":
        analyzed = ""
        for index, char in enumerate(dj):
            if not(dj[index] == " " and dj[index + 1] == " "):
                analyzed = analyzed + char
        params = {'atext': analyzed, 'purpose': 'Removed Extra Space'}
        return render(request, 'analysed_text.html', params)

    elif cc == "on":
        analyzed = 0
        for char in dj:
            if char != " ":
                analyzed = analyzed + 1
        params = {'atext': analyzed, 'purpose': 'Character Count'}
        return render(request, 'analysed_text.html', params)
    else:
        return HttpResponse('Error')
