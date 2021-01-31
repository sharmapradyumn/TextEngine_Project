from django.http import HttpResponse
from django.shortcuts import render # render for taking html page from templates
def index(request):
    return render(request,'index.html') # requsting for index.html  using render
def about(request):
    return  render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def Analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default') # using post method getting data from textarea, name='text'
    removepunc=request.POST.get('removepunc','off') # getting data using switch or checkbox
    capital=request.POST.get('capital','off')
    lower=request.POST.get('lower','off')
    endres=""
    Purpose=""
    if removepunc == "on": # rmoving punctuations
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'Purpose': 'Removed Punctuations', 'Result': analyzed} # sending data to html page using dictionary{key:value} and in html form {{key}}
        endres=analyzed
        Purpose+="RemovePunc AND  " 
        #return render(request, 'analyze.html', params)
    if capital == "on":
        if endres == "":
            capitalchar=""
            for char in djtext:
                capitalchar=capitalchar+char.upper()
            params = {'Purpose': 'Capital Char', 'Result': capitalchar}
            endres=capitalchar
            Purpose+="Capitalize AND "
        else: 
            capitalchar=""
            for char in endres:
                capitalchar=capitalchar+char.upper()
            params = {'Purpose': 'Capital Char', 'Result': capitalchar}
            endres=capitalchar
            Purpose+="Capitalize AND  "
            
        #return render(request, 'analyze.html', params)
    if lower == "on":
        if endres=="":
            lowerchar=""
            for char in djtext:
                lowerchar=lowerchar+char.lower()
            params = {'Purpose': 'Small Char', 'Result': lowerchar}
            endres=lowerchar
            Purpose+="Lower "
        else:
            lowerchar=""
            for char in endres:
                lowerchar=lowerchar+char.lower()
            params = {'Purpose': 'Small Char', 'Result': lowerchar}
            endres=lowerchar
            Purpose+="Lower "
        #return render(request, 'analyze.html', params)
    if(capital == 'on' or removepunc == 'on' or lower == 'on'):
        params = {'Purpose': Purpose, 'Result': endres}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("<h1>'Error'- 404 -- Bhai Ek Switch to On Kr DE</h1>")
#def Analyze(request):
   # djtext=request.GET.get('textinputlerhahu',"yedfaulth")
    #removepunc=request.GET.get('removepunc',"off")

    #parm={'Purpose':'removepunctation','Result': djtext}
    #return render(request,'analyze.html',parm)
#def Capital(request):
    #return HttpResponse("<h1>Welcome On My Capital</h1>")
#def Small(request):
    #return HttpResponse("<h1>Welcome On My Small</h1>")
