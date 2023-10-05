from django.shortcuts import render
from numpy import int32
from requests import post
from django.conf import settings 
from happytransformer import GENSettings


# Create your views here.
def home(request):
    print(request.POST)
    if request.method=="POST":    
         if getattr(settings, 'HAPPY_GEN'):  
            happy_gen = settings.HAPPY_GEN
            question=request.POST['question']
            maxlength=str(request.POST['maxlength'])
            args=GENSettings(no_repeat_ngram_size=2,max_length=int(maxlength))
            res = happy_gen.generate_text(question , args=args)
            #res = happy_gen(question, args, do_sample=True, temperature=0.9)
            return render(request, 'home.html',{"question":question,"maxlength": maxlength,"result": res.txt})
    
    return render(request, 'home.html',{})