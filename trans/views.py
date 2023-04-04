from django.shortcuts import render
import googletrans
from gtts import gTTS

def index(request):
    bf = request.GET.get('bf', '')
    fr = request.GET.get('fr', '')
    to = request.GET.get('to', '')

    context = {
        'ndict' : googletrans.LANGUAGES,
        'fr' : fr,
        'to' : to,
    }

    if bf : 
        trans = googletrans.Translator()
        after = trans.translate(bf, src=fr, dest=to)
        af = after.text
        sbf = gTTS(bf, lang=fr)
        saf = gTTS(af, lang=to)
        context.update({
            'bf' : bf,
            'af' : af,
            'sbf' : sbf,
            'saf' : saf
        })
    return render(request, 'trans/index.html', context)
