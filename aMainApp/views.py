from django.shortcuts import render
from django.http import HttpResponse
from .models import gelenMesajlar, makaleYaz
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
    
    htmlFilePath = "index.html"
    return render(request, htmlFilePath)



def about(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
    
    model1 = makaleYaz.objects
    model1 = model1.get(makaleninBenzersizIdsi=108)
    
    context = {
        'makale1ismi': model1.makaleismi,  'makale1OnSoz': model1.onsoz , 'makale1Fotograf': model1.image1, "makale": model1.paragraf1
    }
        
    htmlFilePath = "about.html"
    return render(request, htmlFilePath, context)

def about_form(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        konu = request.POST['konu']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
        data = {
            'name': name,
            'email': mail,
            'subject': konu,
            'message': message
        }
        
        message = '''
        Yeni Mesaj: {}
        
        Kimden: {}
        Telefon Numarası: {}
        '''.format(data['message'], data['email'], telno)
        send_mail(
            data['subject'],
            message,
            data['email'],
            ["murat.cngz00@gmail.com"]
        )
        
    htmlFilePath = "about_form.html"
    return render(request, htmlFilePath)


#----------------------------------------------------------------------------------------------------------------------------------------#
def podcast(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
    htmlFilePath = "podcast.html"
    return render(request, htmlFilePath)


def bencesi(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
    htmlFilePath = "podcasts/bencesi.html"
    return render(request, htmlFilePath)
#----------------------------------------------------------------------------------------------------------------------------------------#










#----------------------------------------------------------------------------------------------------------------------------------------#
def mentorluk1(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
    htmlFilePath = "mentorluk/mentorluk1.html"
    return render(request, htmlFilePath)



def mentorluk2(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
    htmlFilePath = "mentorluk/mentorluk2.html"
    return render(request, htmlFilePath)



def mentorluk3(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
    htmlFilePath = "mentorluk/mentorluk3.html"
    return render(request, htmlFilePath)
#----------------------------------------------------------------------------------------------------------------------------------------#








#----------------------------------------------------------------------------------------------------------------------------------------#
def articles(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
    
    
    model = makaleYaz.objects.all()
    
    context = {
        'yazilar': model
    }
    
    htmlFilePath = "articles.html"
    return render(request, htmlFilePath, context)


def yazilar(request):
    htmlFilePath = "articles/yazi.html"

    return render(request, htmlFilePath)





def toyp_odul(request):
    htmlFilePath = "articles/toyp_odul.html"
    return render(request, htmlFilePath)











#----------------------------------------------------------------------------------------------------------------------------------------#










#----------------------------------------------------------------------------------------------------------------------------------------#
def books(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
    
    model1 = makaleYaz.objects
    model1 = model1.get(makaleninBenzersizIdsi=109)
    
    model2 = makaleYaz.objects
    model2 = model2.get(makaleninBenzersizIdsi=110)
    
    context = {
        'makale1ismi': model1.makaleismi,  'makale1OnSoz': model1.onsoz , 'makale1Fotograf': model1.image1, "makale1": model1.paragraf1,
        'makale2ismi': model2.makaleismi,  'makale2OnSoz': model2.onsoz , 'makale2Fotograf': model2.image1, "makale2": model2.paragraf1
    }
        
    htmlFilePath = "books.html"
    return render(request, htmlFilePath, context)




def secilmishuzursuzluk(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
        
    model1 = makaleYaz.objects
    model1 = model1.get(makaleninBenzersizIdsi=110)
    
    context = {
        'makale1ismi': model1.makaleismi,  'makale1OnSoz': model1.onsoz , 'makale1Fotograf': model1.image1, "makale": model1.paragraf1
    }
        
    htmlFilePath = "books/secilmishuzursuzluk.html"
    return render(request, htmlFilePath, context)




def varligiminkabuledildigigun(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['telno'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        telno = request.POST['telno']
        message = request.POST['message']
        
        model = gelenMesajlar(name=name, mail=mail, telno=telno, message=message)
        model.save()
    
    model1 = makaleYaz.objects
    model1 = model1.get(makaleninBenzersizIdsi=109)
    
    context = {
        'makale1ismi': model1.makaleismi,  'makale1OnSoz': model1.onsoz , 'makale1Fotograf': model1.image1, "makale": model1.paragraf1
    }
        
    htmlFilePath = "books/varligiminkabuledildigigun.html"
    return render(request, htmlFilePath, context)
#----------------------------------------------------------------------------------------------------------------------------------------#


def haberler(request):
    
    htmlFilePath = "haberler.html"
    return render(request, htmlFilePath)


def projeler(request):
    htmlFilePath = "projeler/projelerAnaSayfa.html"
    return render(request, htmlFilePath)