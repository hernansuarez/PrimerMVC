from django.shortcuts import render
from Familia.models import Familiar

def familia(request):
    documentoDeTexto = Familiar.objects.all()
    return render(request, 'FamiliaTemplate.html',{'documentoDeTexto': documentoDeTexto})