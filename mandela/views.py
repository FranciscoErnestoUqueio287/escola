from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
import random
from django.utils import translation, timezone
from django.views.decorators.csrf import csrf_exempt
from django.urls.base import reverse
from django.db.models import Q
import random
#from django.contrib.gis.geos.Point
def iding(t=None):
    if t == None:
        pass
    elif t=="turma":
        j = random.randrange(1234567890,100000000000)
        r = turma.objects.filter(id=j).first()
        if r != None:
            iding("turma")
        else:
            return j
    elif t=="professor":
        j = random.randrange(1234567890,100000000000)
        r = professor.objects.filter(id=j).first()
        if r != None:
            iding("professor")
        else:
            return j
    elif t=="trabalho":
        j = random.randrange(1234567890,100000000000)
        r = trabalho.objects.filter(id=j).first()
        if r != None:
            iding("trabalho")
        else:
            return j
    elif t=="aluno":
        j = random.randrange(1234567890,100000000000)
        r = aluno.objects.filter(id=j).first()
        if r != None:
            iding("aluno")
        else:
            return j
    elif t=="comunicado":
        j = random.randrange(1234567890,100000000000)
        r = comunicado.objects.filter(id=j).first()
        if r != None:
            iding("comunicado")
        else:
            return j
    elif t=="imagens":
        j = random.randrange(1234567890,100000000000)
        r = imagens.objects.filter(id=j).first()
        if r != None:
            iding("imagens")
        else:
            return j
    elif t=="directoria":
        j = random.randrange(1234567890,100000000000)
        r = directoria.objects.filter(id=j).first()
        if r != None:
            iding("directoria")
        else:
            return j
def commm(request):
    return render(request,"allcom.html",{"comunicados":comunicados.objects.all()})
def imaging(request):
    im = imagens.objects.all()
    return render(request,"imagens.html",{"imagens":im})
def sobre(request):
    return render(request,"aboutschool.html",{"info":"Escola Secúndaria Nelson Mandela","more1":"Criada em: 2003, iniciada em 01 de abril de 2004.","more2":"Teve ajuda de empresas como a mozal lda e outras.","more3":"Situa-se em Djuba na rua Matola-rio.","more4":"Lecciona as classes: (8ª, 9ª, 10ª, 11ª, 12ª)."})
@csrf_exempt
def pagina_inicial(request):
    if request.method == "POST":
        if len(request.POST) > 0:
            if len(request.POST["procurar"]) > 0:
                p = request.POST["procurar"]
                p1 = p
                p = [p,p]
                p.append(p[0].lower())
                p.append(p[1].lower())
                p.append(p[0].upper())
                p.append(p[1].upper())
                p.append(p[0].title())
                p.append(p[0].capitalize())
                p.append(p[1].title())
                p.append(p[1].capitalize())
                if type(p) == int:
                    turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) | Q(classe__in=p) | Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(classe__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                    alunos = aluno.objects.filter(Q(nome__in=p)|Q(numero_de_processo__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(numero_de_processo__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                    professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                    comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                    trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                    artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                else:
                    try:
                        for x in p1.split(" "):
                            p.append(x)
                            p.append(x.lower())
                            p.append(x.upper())
                            p.append(x.title())
                            p.append(x.capitalize())
                    except:
                        pass
                    turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) |  Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                    alunos = aluno.objects.filter(Q(nome__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                    professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                    comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                    trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                    artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                return render(request,"procurandopor.html",artigos)
            else:
                return render(request,"404.html",{"relatorio":"Sempre que pesquisar algo, o que desejas pesquisar sempre tem de ter mais de um carater"})
        else:
            return render(request,"404.html",{"relatorio":"Esse lugar nao e permitido para voce, se quiseres acessar tem de ser alguem da criacão da pagina"})
    else:
        turmas = turma.objects.all()
        alunos = aluno.objects.all()
        professores = professor.objects.all()
        trabalhos = trabalho.objects.all()
        im = imagens.objects.all()
        com = comunicados.objects.all()
        return render(request, "index.html",{"imagens":im,"comunicados":com,"t":turmas,"a":alunos,"d":directoria.objects.all(),"p":professores,"tr":trabalhos})
class criaa(CreateView):
    template_name = "sign.html"
    model = aluno
    form_class = Aluno
    def post(self, request,*args,**kwargs):
        form = Aluno(request.POST,request.FILES)
        if form.is_valid():
            if request.POST["password"] == request.POST["password2"] and len(request.POST["password"]) >= 8:
                w = aluno.objects.filter(numero_de_processo=request.POST["numero_de_processo"]).first()
                if w == None:
                    form.save()
                    i = aluno.objects.filter(nome=request.POST["nome"],numero_de_processo=request.POST["numero_de_processo"],contacto=request.POST["contacto"]).first()
                    if i != None:
                        e = aluno.objects.filter(slug=request.POST["csrfmiddlewaretoken"]).first()
                        if e == None:
                            i.slug = request.POST["csrfmiddlewaretoken"]
                        else:
                            r = iding("aluno")
                            r = str(r)+request.POST["csrfmiddlewaretoken"]
                        i.save()
                        return redirect("/a/"+str(i.slug)+"/")
                    else:
                        return redirect("/a/")
                else:
                    erro = "Não foi possivel criar essa conta porque esse numero de processo esta sendo usado"
                    return render(request, "sign.html",{"erro":erro+str(form.errors),"user":request.POST})
            else:
                erro = "O password tem de ter mais de 8 carateres ou os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request, "sign.html",{"erro":erro,"user":request.POST})
        else:
            erro ="Houve um erro que actualmente não sabemos qual"
            if len(request.POST['nome']) <= 1:
                erro = "Preencha o nome correctamente"
            elif len(request.POST['password']) < 8:
                erro = "A palavra passe tem de ser bem definida e tem de ter mais de 8 carateres"
            return render(request, "sign.html",{"erro":erro+str(form.errors),"user":request.POST})

class criap(CreateView):
    template_name = "signp.html"
    model = professor
    form_class = Professor
    def post(self, request,*args,**kwargs):
        form = Professor(request.POST,request.FILES)
        if form.is_valid():
            if request.POST["password"] == request.POST["password2"] and len(request.POST["password"]) >= 8:
                form.save()
                i = professor.objects.filter(nome=request.POST["nome"],contacto=request.POST["contacto"]).first()
                if i != None:
                    rr = i.id
                    i.slug = request.POST["csrfmiddlewaretoken"]
                    i.save()
                    return redirect("/p/"+str(i.slug)+"/")
                else:
                    return redirect("/p/")
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada e tem de conter mais de 8 carateres"+str(form.errors)
                return render(request, "signp.html",{"erro":erro,"user":request.POST})
        else:
            erro =""
            if len(request.POST['nome']) > 0:
                erro = "Preencha o nome correctamente"+str(form.errors)
            elif len(request.POST['password']) > 0:
                erro = "A palavra passe tem de ser bem definida"+str(form.errors)
            return render(request, "signp.html",{"erro":erro,"user":request.POST})
def entrar(request):
    return render(request,"dir.html")
def upaluno(request,pk):
    if request.method == "POST":
        user = aluno.objects.filter(slug=pk).first()
        if user != None:
            try:
                if request.POST["nome"] != user.nome:
                    n = request.POST["nome"]
                    if len(n) > 9:
                        user.nome = n
                if request.POST["numero_de_processo"] != user.numero_de_processo:
                    n = request.POST["numero_de_processo"]
                    if int(n) > 1000:
                        user.numero_de_processo = int(n)
                if request.POST["data_de_nascimento"] != user.data_de_nascimento:
                    n = request.POST["data_de_nascimento"]
                    if len(n) > 3:
                        user.data_de_nascimento = n
                if request.POST["encarregado"] != user.encarregado:
                    n = request.POST["encarregado"]
                    if len(n) > 9:
                        user.encarregado = n
                if request.POST["contacto"] != user.contacto:
                    n = request.POST["contacto"]
                    if len(n) > 8:
                        user.contacto = n
                if request.POST["sala"] != user.sala:
                    n = request.POST["sala"]
                    if int(n) > 0 and int(n) < 33:
                        user.sla = int(n)
                if request.POST["turno"] != user.turno:
                    n = request.POST["turno"]
                    if n in ("diurno","noturno"):
                        user.turno = n
                if request.POST["turma"] != user.turma:
                    n = request.POST["turma"]
                    if len(n) >= 2:
                        user.turma = n
                if request.POST["classe"] != user.classe:
                    n = request.POST["classe"]
                    if int(n) > 7 and int(n) < 13:
                        user.classe = int(n)
                if len(request.FILES["imagem"]) > 3:
                    n = request.FILES["imagem"]
                    user.imagem = n
            except:
                pass
            user.save()
            return render(request,"upping.html",{'user':user})
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        user = aluno.objects.filter(slug=pk).first()
        c = request.META.get("PATH_INFO")
        c = c.split("/")
        c = [c[0],c[1],c[2]]
        c = "/".join(c)
        if user == None:
             return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            return render(request,"upping.html",{'user':user})
def upprof(request,pk):
    if request.method == "POST":
        e = request.POST["group"]
        try:
            n = request.POST["thevalue"]
        except:
            n = request.FILES["thevalue"]
        user = professor.objects.filter(slug=pk).first()
        c = request.META.get("PATH_INFO")
        c = c.split("/")
        c = [c[0],c[1],c[2]]
        c = "/".join(c)
        q = None
        if user == None:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            if e == "nome":
                user.nome = n
            elif e == "contacto":
                user.contacto = n
            elif e == "idade":
                user.data_de_nascimento = n
            elif e == "turma":
                user.turmas = n
            elif e == "imagem":
                user.imagem = n
            elif e == "classe":
                user.classes = n
            elif e == "password":
                user.password = n
            user.save()
            return render(request,"updatepr.html",{'user':user})
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        user = professor.objects.filter(slug=pk).first()
        c = request.META.get("PATH_INFO")
        c = c.split("/")
        c = [c[0],c[1],c[2]]
        c = "/".join(c)
        if user == None:
             return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            return render(request,"updatepr.html",{'user':user})

def updir(request,pk):
    if request.method == "POST":
        e = request.POST["group"]
        try:
            n = request.POST["thevalue"]
        except:
            n = request.FILES["thevalue"]
        user = directoria.objects.filter(slug=pk).first()
        c = request.META.get("PATH_INFO")
        c = c.split("/")
        c = [c[0],c[1],c[2]]
        c = "/".join(c)
        q = None
        if user == None:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            if e == "nome":
                user.nome = n
            elif e == "contacto":
                user.contacto = n
            elif e == "idade":
                user.data_de_nascimento = n
            elif e == "imagem":
                user.imagem = n
            elif e == "cargo":
                user.cargo = n
            elif e == "password":
                user.password = n
            user.save()
            return render(request,"updi.html",{'user':user})
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        user = directoria.objects.filter(slug=pk).first()
        c = request.META.get("PATH_INFO")
        c = c.split("/")
        c = [c[0],c[1],c[2]]
        c = "/".join(c)
        if user == None:
             return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            return render(request,"updi.html",{'user':user})
        
            
class criad(CreateView):
    template_name = "signd.html"
    model = directoria
    form_class = Directoria
    def post(self, request,*args,**kwargs):
        form = Directoria(request.POST,request.FILES)
        if form.is_valid():
            if request.POST["password"] == request.POST["password2"] and len(request.POST["password"]) >= 8:
                form.save()
                i = directoria.objects.filter(nome=request.POST["nome"],contacto=request.POST["contacto"],cargo=request.POST["cargo"],data_de_nascimento=request.POST["data_de_nascimento"]).first()
                if i != None:
                    e = directoria.objects.filter(slug=request.POST["csrfmiddlewaretoken"]).first()
                    if e == None:
                        i.slug = request.POST["csrfmiddlewaretoken"]
                    else:
                        r = iding("directoria")
                        r.slug = str(r)+request.POST["csrfmiddlewaretoken"]
                    i.save()
                    return redirect("/d/"+str(i.slug)+"/")
                else:
                    erro = "A conta ja existe"
                    return render(request, "signd.html",{"erro":erro,"user":request.POST})
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada e verifique se a palavra-passe tem mais de 8 carateres"+str(form.errors)
                return render(request, "signd.html",{"erro":erro,"user":request.POST})
        else:
            erro =""
            if len(request.POST['nome']) > 0:
                erro = "Preencha o nome correctamente"+str(form.errors)
            elif len(request.POST['password']) > 0:
                erro = "A palavra passe tem de ser bem definida"+str(form.errors)
            return render(request, "signd.html",{"erro":erro,"user":request.POST})


def pr(request,pk):
    if pk != None:
        pk = professor.objects.filter(slug=pk).first()
        if pk != None:
            if request.method == "GET":
                com = ""
                tra = ""
                dt = {}
                p = pk.turmas
                p = str(p).split(",")
                conver = conversas.objects.filter(Q(de2 = "professor",de=pk.id) | Q(para2 = "professor",para=pk.id)).distinct().all()
                turma_coisas = turma.objects.filter(Q(referencia__in=p)).all()
                dt = aluno.objects.filter(turma__in = p).all()
                coma = comunicados.objects.filter(comunicando=pk.nome,de=pk.id,de2="professor").all()
                traa = trabalho.objects.filter(comunicando=pk.nome,de=pk.id,de2="professor").all()
                if len(turma_coisas) == 0:
                    turma_coisas = {}
                    turma_coisas["turmas"] = "A/As turma(a/as) "+str(pk.turmas)+" não existe, por favor insira a referencia correcta da sua turma"
                else:
                    dt = aluno.objects.filter(turma__in = p).all()
                    if len(dt) == 0:
                        dt = ""
                    else:
                        com = comunicados.objects.filter(Q(comunicando__in=[i.nome for i in dt]) | Q(comunicando=pk.nome)).all()
                        tra = trabalho.objects.filter(Q(comunicando__in=[i.nome for i in dt]) | Q(comunicando=pk.nome)).all()
                return render(request,"professor.html",{"time":timezone.now(),"user":pk,"conversas":conver,"trabalhos":traa,"comunicados":coma,"aluno":dt,"turma":turma_coisas,"trabalho":tra,"comunicado":com})
            elif request.method == "POST":
                p = pk.turmas
                p = str(p).split(",")
                conver = conversas.objects.filter(Q(de2 = "professor",de=pk.id) | Q(para2 = "professor",para=pk.id)).distinct().all()
                turma_coisas = turma.objects.filter(Q(referencia__in=p)).all()
                dt = aluno.objects.filter(turma__in = p).all()
                if len(turma_coisas) == 0:
                    turma_coisas = {}
                    turma_coisas["turmas"] = "A/As turma(a/as) "+str(pk.turmas)+" não existe, por favor insira a referencia correcta da sua turma"
                else:
                    dt = aluno.objects.filter(turma__in = p).all()
                    if len(dt) == 0:
                        dt = {}
                        dt["nome"] = "Não existem alunos nest(a/as) turm(a/as):"+str(pk.turmas)
                    else:
                        com = comunicados.objects.filter(Q(comunicando__in=[i.nome for i in dt]) | Q(comunicando=pk.nome)).all()
                        tra = trabalho.objects.filter(Q(comunicando__in=[i.nome for i in dt]) | Q(comunicando=pk.nome)).all()
                p = "Não existe o director da sua turma porque ela tambem não existe"
                com = ""
                tra = ""
                com = comunicados.objects.filter(comunicando=pk.nome,de=pk.id,de2="professor").all()
                tra = trabalho.objects.filter(comunicando=pk.nome,de=pk.id,de2="professor").all()
                if len(request.POST) > 0:
                    if len(request.POST["procurar"]) > 0:
                        p = request.POST["procurar"]
                        p1 = p
                        p = [p,p]
                        p.append(p[0].lower())
                        p.append(p[1].lower())
                        p.append(p[0].upper())
                        p.append(p[1].upper())
                        p.append(p[0].title())
                        p.append(p[0].capitalize())
                        p.append(p[1].title())
                        p.append(p[1].capitalize())
                        if type(p) == int:
                            turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) | Q(classe__in=p) | Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(classe__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                            alunos = aluno.objects.filter(Q(nome__in=p)|Q(numero_de_processo__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(numero_de_processo__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                            professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                            comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                        else:
                            try:
                                for x in p1.split(" "):
                                    p.append(x)
                                    p.append(x.lower())
                                    p.append(x.upper())
                                    p.append(x.title())
                                    p.append(x.capitalize())
                            except:
                                pass
                            turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) |  Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                            alunos = aluno.objects.filter(Q(nome__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                            professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                            comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()

                            artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                        return render(request,"professor.html",{"time":timezone.now(),"user":pk,"conversas":conver,"aluno":dt,"turma":turma_coisas,"trabalho":tra,"comunicado":com,"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1})
                    else:
                        return render(request,"404.html",{"relatorio":"Sempre que quiser pesquisar algo, tem de ter mais de um caratere"})
            else:
                return render(request,"404.html",{"relatorio":"Sempre que quiser pesquisar algo, tem de ter mais de um caratere"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def dt(request,pk):
    if pk != None:
        pk = directoria.objects.filter(slug=pk).first()
        if pk != None:
            if request.method == "GET":
                p = "Não existe o director da sua turma porque ela tambem não existe"
                com = ""
                tra = ""
                dt = {}
                conver = conversas.objects.filter(Q(de2 = "directoria",de=pk.id) | Q(para2 = "directoria",para=pk.id)).distinct().all()
                com = comunicados.objects.filter(comunicando=pk.nome,de=pk.id,de2="directoria").all()
                tra = trabalho.objects.filter(comunicando=pk.nome,de=pk.id,de2="directoria").all()            
                return render(request,"directoria.html",{"time":timezone.now(),"user":pk,"conversas":conver,"trabalho":tra,"comunicado":com})
            elif request.method == "POST":
                p = "Não existe o director da sua turma porque ela tambem não existe"
                com = ""
                tra = ""
                dt = {}
                conver = conversas.objects.filter(Q(de2 = "directoria",de=pk.id) | Q(para2 = "directoria",para=pk.id)).distinct().all()
                com = comunicados.objects.filter(comunicando=pk.nome,de=pk.id,de2="directoria").all()
                tra = trabalho.objects.filter(comunicando=pk.nome,de=pk.id,de2="directoria").all()
                if len(request.POST) > 0:
                    if len(request.POST["procurar"]) > 0:
                        p = request.POST["procurar"]
                        p1 = p
                        p = [p,p]
                        p.append(p[0].lower())
                        p.append(p[1].lower())
                        p.append(p[0].upper())
                        p.append(p[1].upper())
                        p.append(p[0].title())
                        p.append(p[0].capitalize())
                        p.append(p[1].title())
                        p.append(p[1].capitalize())
                        if type(p) == int:
                            turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) | Q(classe__in=p) | Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(classe__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                            alunos = aluno.objects.filter(Q(nome__in=p)|Q(numero_de_processo__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(numero_de_processo__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                            professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                            comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                        else:
                            try:
                                for x in p1.split(" "):
                                    p.append(x)
                                    p.append(x.lower())
                                    p.append(x.upper())
                                    p.append(x.title())
                                    p.append(x.capitalize())
                            except:
                                pass
                            turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) |  Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                            alunos = aluno.objects.filter(Q(nome__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                            professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                            comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()

                            artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                        return render(request,"directoria.html",{"time":timezone.now(),"user":pk,"conversas":conver,"trabalho":tra,"comunicado":com,"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1})
                    else:
                        return render(request,"404.html",{"relatorio":"Sempre que quiser pesquisar algo, a pesquisa tem de conter mais de um caratere"})
                
                
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def al(request,pk):
    if pk != None:
        pk = aluno.objects.filter(slug=pk).first()
        if pk != None:
            if request.method == "GET":
                p = "Não existe o director da sua turma porque ela tambem não existe"
                com = ""
                tra = ""
                dt = {}
                conver = conversas.objects.filter(Q(de2 = "aluno",de=pk.id) | Q(para2 = "aluno",para=pk.id)).distinct().all()
                turma_coisas = turma.objects.filter(referencia=pk.turma).first()
                coma = comunicados.objects.filter(comunicando=pk.nome,de=pk.id,de2="aluno").all()
                traa = trabalho.objects.filter(comunicando=pk.nome,de=pk.id,de2="aluno").all()
                if turma_coisas == None:
                    turma_coisas = "A turma "+str(pk.turma)+" não existe, por favor insira a referencia correcta da sua turma"
                    dt = {}
                    dt["nome"] = "Ninguem"
                else:
                    dt = professor.objects.filter(nome=turma_coisas.director_de_turma).first()
                    if dt == None:
                        dt = {}
                        dt["nome"] = "Não existe o director da sua turma, mas precisamente não foi encontrado nenhum professor de nome "+str(turma_coisas.director_de_turma)
                    elif dt != None:
                        com = comunicados.objects.filter(comunicando=dt.nome).all()
                        tra = trabalho.objects.filter(comunicando=dt.nome).all()
                    
                return render(request,"aluno.html",{"time":timezone.now(),"user":pk,"conversas":conver,"trabalhos":traa,"comunicados":coma,"director":dt,"turma":turma_coisas,"trabalho":tra,"comunicado":com})
            elif request.method == "POST":
                p = "Não existe o director da sua turma porque ela tambem não existe"
                com = ""
                tra = ""
                conver = conversas.objects.filter(Q(de2 = "aluno",de=pk.id) | Q(para2 = "aluno",para=pk.id)).distinct().all()
                com = comunicados.objects.filter(comunicando=pk.nome,de=pk.id,de2="aluno").all()
                tra = trabalho.objects.filter(comunicando=pk.nome,de=pk.id,de2="aluno").all()
                turma_coisas = turma.objects.filter(referencia=pk.turma).first()
                if turma_coisas == None:
                    turma_coisas = "A turma "+str(pk.turma)+" não existe, por favor insira a referencia correcta da sua turma"
                    dt = {}
                    dt["nome"] = "Ninguem"
                else:
                    dt = professor.objects.filter(nome=turma_coisas.director_de_turma).first()
                    if dt == None:
                        dt = {}
                        dt["nome"] = "Não existe o director da sua turma, mas precisamente não foi encontrado nenhum professor de nome "+str(turma_coisas.director_de_turma)
                    elif dt != None:
                        com = comunicados.objects.filter(comunicando=dt.nome,de=pk.id).all()
                        tra = trabalho.objects.filter(comunicando=dt.nome,de=pk.id).all()
                if len(request.POST) > 0:
                    if len(request.POST["procurar"]) > 0:
                        p = request.POST["procurar"]
                        p1 = p
                        p = [p,p]
                        p.append(p[0].lower())
                        p.append(p[1].lower())
                        p.append(p[0].upper())
                        p.append(p[1].upper())
                        p.append(p[0].title())
                        p.append(p[0].capitalize())
                        p.append(p[1].title())
                        p.append(p[1].capitalize())
                        if type(p) == int:
                            turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) | Q(classe__in=p) | Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(classe__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                            alunos = aluno.objects.filter(Q(nome__in=p)|Q(numero_de_processo__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(numero_de_processo__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                            professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                            comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                        else:
                            try:
                                for x in p1.split(" "):
                                    p.append(x)
                                    p.append(x.lower())
                                    p.append(x.upper())
                                    p.append(x.title())
                                    p.append(x.capitalize())
                            except:
                                pass
                            turmas = turma.objects.filter(Q(referencia__in=p) | Q(director_de_turma__in=p) |  Q(chefe_de_turma__in=p) | Q(referencia__contains=p1) | Q(director_de_turma__contains=p1) | Q(chefe_de_turma__contains=p1)).all()
                            alunos = aluno.objects.filter(Q(nome__in=p)|Q(contacto__in=p)|Q(turma__in=p)|Q(turno__in=p)|Q(encarregado__in=p) | Q(nome__contains=p1)|Q(contacto__contains=p1)|Q(turma__contains=p1)|Q(turno__contains=p1)|Q(encarregado__contains=p1)).all()
                            professores = professor.objects.filter(Q(nome__in=p)|Q(turmas__in=p)|Q(nome__contains=p1)|Q(turmas__contains=p1)).all()
                            comunicado = comunicados.objects.filter(Q(comunicado__in=p)|Q(comunicando__in=p)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()
                            trabalhos = trabalho.objects.filter(Q(arquivo__in=p)|Q(comunicado__in=p)|Q(comunicando__in=p)|Q(arquivo__contains=p1)|Q(comunicado__contains=p1)|Q(comunicando__contains=p1)).all()

                            artigos = {"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1}
                        return render(request,"aluno.html",{"time":timezone.now(),"user":pk,"conversas":conver,"turma":turma_coisas,"trabalho":tra,"comunicado":com,"turmas":turmas,"alunos":alunos,"professores":professores,"comunicados":comunicado,"trabalhos":trabalhos,"searched":p1})
                    else:
                        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada, a pesquisa tem de ter mais de 1 caratere:"})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
@csrf_exempt
def loga(request):
    if request.method == "POST":
        if len(request.POST) > 0:
            a = aluno.objects.filter(contacto = request.POST['contacto'],password=request.POST['password']).first()
            if a == None:
                erro = "Nenhum aluno encontrado usando tais dados,  por favor verifique os dados insiridos"
                return render(request,"loga.html",{"erro":erro})
            else:
                return redirect("/a/"+str(a.slug)+"/")
        else:
            erro = "Preencha o furmulario por favor"
            return render(request,"loga.html",{"erro":erro})
    else:
        return render(request,"loga.html",{"erro":"Bem-vindo a escola\n#Proteja-se"})
@csrf_exempt
def logp(request):
    if request.method == "POST":
        if len(request.POST) > 0:
            a = professor.objects.filter(contacto = request.POST['contacto'],password=request.POST['password']).first()
            if a == None:
                erro = "Nenhum professor encontrado usando tais dados, por favor verifique os dados insiridos"
                return render(request,"loga.html",{"erro":erro})
            else:
                return redirect("/p/"+str(a.slug)+"/")
        else:
            erro = "Preencha o furmulario por favor"
            return render(request,"loga.html",{"erro":erro})
    else:
        return render(request,"loga.html",{"erro":"Bem-vindo a escola\n#Proteja-se"})
@csrf_exempt
def logd(request):
    if request.method == "POST":
        if len(request.POST) > 0:
            a = directoria.objects.filter(contacto = request.POST['contacto'],password=request.POST['password']).first()
            if a == None:
                erro = "Nenhum usuario encontrado usando tais dados, por favor verifique os dados insiridos"
                return render(request,"loga.html",{"erro":erro})
            else:
                return redirect("/d/"+str(a.slug)+"/")
        else:
            erro = "Preencha o furmulario por favor"
            return render(request,"loga.html",{"erro":erro})
    else:
        return render(request,"loga.html",{"erro":"Bem-vindo a escola\n#Proteja-se"})
def e404(request):
    return render(request,"404.html")
def e500(request):
    return render(request,"500.html")
def e403(request):
    return render(request,"403.html")
def e304(request):
    return render(request,"304.html")

def mesdr(request,pk):
    if pk != None:
        if request.method == "GET":
            user = directoria.objects.filter(slug=pk).first()
            if user == None:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"smsenddr.html",{"user":user})
        elif request.method == "POST":
            if len(request.POST) > 0:
                user = directoria.objects.filter(slug=pk).first()
                if user != None:
                    c = request.POST['receptor']
                    t = request.POST["para"]
                    para = None
                    if t == "Professor":
                        para = professor.objects.filter(contacto=c).first()
                    elif t == "Aluno":
                        para = aluno.objects.filter(contacto=c).first()
                    elif t == "Directoria":
                        para = directoria.objects.filter(contacto=c).first()
                    if para == None:
                        pa = "Nao existe tal contacto de numero %s"%c
                        return render(request,"smsenddr.html",{"user":user,"sucesso":pa})
                    else:
                        pa = "Ennviado com sucesso a messagem para %s de contacto %s"%(para.nome,para.contacto)
                        try:
                            m = messagems(conteudo=request.POST["conteudo"],arquivo=request.FILES["arquivo"])
                        except:
                            m = messagems(conteudo=request.POST["conteudo"],arquivo="")
                        m.save()
                        co = conversas(de=user.id,de2="directoria",para=para.id,para2=t.lower(),messagem=m)
                        co.save()
                        return render(request,"smsenddr.html",{"user":user,"sucesso":pa})
                if user == None:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                user = professor.objects.filter(slug=pk).first()
                if user == None:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
                else:
                    return render(request,"smsenddr.html",{"user":user})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def mespr(request,pk):
    if pk != None:
        if request.method == "GET":
            user = professor.objects.filter(slug=pk).first()
            if user == None:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"smsendpr.html",{"user":user})
        elif request.method == "POST":
            if len(request.POST) > 0:
                user = professor.objects.filter(slug=pk).first()
                if user != None:
                    c = request.POST['receptor']
                    t = request.POST["para"]
                    para = None
                    if t == "Professor":
                        para = professor.objects.filter(contacto=c).first()
                    elif t == "Aluno":
                        para = aluno.objects.filter(contacto=c).first()
                    elif t == "Directoria":
                        para = directoria.objects.filter(contacto=c).first()
                    if para == None:
                        pa = "Nao existe tal contacto de numero %s"%c
                        return render(request,"smsendpr.html",{"user":user,"sucesso":pa})
                    else:
                        pa = "Ennviado com sucesso a messagem para %s de contacto %s"%(para.nome,para.contacto)
                        try:
                            m = messagems(conteudo=request.POST["conteudo"],arquivo=request.FILES["arquivo"])
                        except:
                            m = messagems(conteudo=request.POST["conteudo"],arquivo="")
                        m.save()
                        co = conversas(de=user.id,de2="professor",para=para.id,para2=t.lower(),messagem=m)
                        co.save()
                        return render(request,"smsendpr.html",{"user":user,"sucesso":pa})
                if user == None:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                user = professor.objects.filter(slug=pk).first()
                if user == None:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
                else:
                    return render(request,"smsendpr.html",{"user":user})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def mesal(request,pk):
    if pk != None:
        if request.method == "GET":
            user = aluno.objects.filter(slug=pk).first()
            if user == None:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"smsend.html",{"user":user})
        elif request.method == "POST":
            if len(request.POST) > 0:
                user = aluno.objects.filter(slug=pk).first()
                if user != None:
                    c = request.POST['receptor']
                    t = request.POST["para"]
                    para = None
                    if t == "Professor":
                        para = professor.objects.filter(contacto=c).first()
                    elif t == "Aluno":
                        para = aluno.objects.filter(contacto=c).first()
                    elif t == "Directoria":
                        para = directoria.objects.filter(contacto=c).first()
                    if para == None:
                        pa = "Nao existe tal contacto de numero %s"%c
                        return render(request,"smsend.html",{"user":user,"sucesso":pa})
                    else:
                        pa = "Ennviado com sucesso a messagem para %s de contacto %s"%(para.nome,para.contacto)
                        try:
                            m = messagems(conteudo=request.POST["conteudo"],arquivo=request.FILES["arquivo"])
                        except:
                            m = messagems(conteudo=request.POST["conteudo"],arquivo="")
                        m.save()
                        co = conversas(de=user.id,de2="aluno",para=para.id,para2=t.lower(),messagem=m)
                        co.save()
                        return render(request,"smsend.html",{"user":user,"sucesso":pa})
                if user == None:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                user = professor.objects.filter(slug=pk).first()
                if user == None:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
                else:
                    return render(request,"smsend.html",{"user":user})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def mesprsee(request,pk,l):
    if pk != None and l != None:
        user = professor.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                m = conversas.objects.filter(id=l).first()
                if m != None:
                    cj = m
                    try:
                        mi = messagems(conteudo=request.POST["conteudo"],arquivo=request.FILES["arquivo"])
                    except:
                        mi = messagems(conteudo=request.POST["conteudo"],arquivo="")
                    mi.save()
                    co = conversas(de=user.id,para=cj.para,de2="professor",para2=cj.para2,messagem=mi)
                    co.save()
                    conver = conversas.objects.filter(Q(de2 = m.de2,de=m.de,para=m.para,para2=m.para2)|Q(de2=m.para2,de=m.para,para=m.de,para2=m.de2)).all()
                    return render(request,"seempr.html",{"user":user,"messagem":co,"conversas":conver})
                else:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            if user != None:
                m = conversas.objects.filter(id=l).first()
                if m != None:
                    conver = conversas.objects.filter(Q(de2 = m.de2,de=m.de,para=m.para,para2=m.para2)|Q(de2=m.para2,de=m.para,para=m.de,para2=m.de2)).all()
                    return render(request,"seempr.html",{"user":user,"messagem":m,"conversas":conver})
                else:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def mesdrsee(request,pk,l):
    if pk != None and l != None:
        user = directoria.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                m = conversas.objects.filter(id=l).first()
                if m != None:
                    cj = m
                    try:
                        mi = messagems(conteudo=request.POST["conteudo"],arquivo=request.FILES["arquivo"])
                    except:
                        mi = messagems(conteudo=request.POST["conteudo"],arquivo="")
                    mi.save()
                    co = conversas(de=user.id,para=cj.para,de2="director",para2=cj.para2,messagem=mi)
                    co.save()
                    conver = conversas.objects.filter(Q(de2 = m.de2,de=m.de,para=m.para,para2=m.para2)|Q(de2=m.para2,de=m.para,para=m.de,para2=m.de2)).all()
                    return render(request,"seemdr.html",{"user":user,"messagem":co,"conversas":conver})
                else:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            if user != None:
                m = conversas.objects.filter(id=l).first()
                if m != None:
                    conver = conversas.objects.filter(Q(de2 = m.de2,de=m.de,para=m.para,para2=m.para2)|Q(de2=m.para2,de=m.para,para=m.de,para2=m.de2)).all()
                    return render(request,"seemdr.html",{"user":user,"messagem":m,"conversas":conver})
                else:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    
def mesalsee(request,pk,l):
    if pk != None and l != None:
        user = aluno.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                m = conversas.objects.filter(id=l).first()
                if m != None:
                    cj = m
                    try:
                        mi = messagems(conteudo=request.POST["conteudo"],arquivo=request.FILES["arquivo"])
                    except:
                        mi = messagems(conteudo=request.POST["conteudo"],arquivo="")
                    mi.save()
                    co = conversas(de=user.id,para=cj.para,de2="aluno",para2=cj.para2,messagem=mi)
                    co.save()
                    conver = conversas.objects.filter(Q(de2 = m.de2,de=m.de,para=m.para,para2=m.para2)|Q(de2=m.para2,de=m.para,para=m.de,para2=m.de2)).all()
                    return render(request,"seemal.html",{"user":user,"messagem":co,"conversas":conver})
                else:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
        else:
            if user != None:
                m = conversas.objects.filter(id=l).first()
                if m != None:
                    conver = conversas.objects.filter(Q(de2 = m.de2,de=m.de,para=m.para,para2=m.para2)|Q(de2=m.para2,de=m.para,para=m.de,para2=m.de2)).all()
                    return render(request,"seemal.html",{"user":user,"messagem":m,"conversas":conver})
                else:
                    return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def comal(request,pk):
    if pk != None:
        user = aluno.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                print(request.POST)
                conn = request.POST["comunicado"]
                sucesso = ""
                try:
                    if len(conn) > 10:
                        r = comunicados(de=user.id,de2="aluno",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    elif len(request.FILES["arquivo"]) > 2:
                        r = comunicados(de=user.id,de2="aluno",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    else:
                        sucesso = "Sem sucesso, impossivel comunicar um texto com menos de 10 palavras"
                except:
                    if len(conn) > 10:
                        r = comunicados(de=user.id,de2="aluno",comunicado=conn,comunicando=user.nome,arquivo="")
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel comunicar um texto com menos de 10 palavras"
                mcom = comunicados.objects.filter(de=user.id,de2="aluno",comunicando=user.nome).all()
                com = comunicados.objects.all()
                return render(request,"comunicados.html",{"user":user,"mcom":mcom,"comunicados":com,"sucesso":sucesso})
        else:
            if user != None:
                mcom = comunicados.objects.filter(de=user.id,de2="aluno",comunicando=user.nome).all()
                com = comunicados.objects.all()
                return render(request,"comunicados.html",{"user":user,"mcom":mcom,"comunicados":com,"sucesso":"Bem-vindos aos comunicados"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})


def compr(request,pk):
    if pk != None:
        user = professor.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                print(request.POST)
                conn = request.POST["comunicado"]
                sucesso = ""
                try:
                    if len(conn) > 10:
                        r = comunicados(de=user.id,de2="professor",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    elif len(request.FILES["arquivo"]) > 2:
                        r = comunicados(de=user.id,de2="professor",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    else:
                        sucesso = "Sem sucesso, impossivel comunicar um texto com menos de 10 letras"
                except:
                    if len(conn) > 10:
                        r = comunicados(de=user.id,de2="professor",comunicado=conn,comunicando=user.nome,arquivo="")
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel comunicar um texto com menos de 10 letras"
                mcom = comunicados.objects.filter(de=user.id,de2="aluno",comunicando=user.nome).all()
                com = comunicados.objects.all()
                return render(request,"comunicadop.html",{"user":user,"mcom":mcom,"com":com,"sucesso":sucesso})
        else:
            if user != None:
                mcom = comunicados.objects.filter(de=user.id,de2="professor",comunicando=user.nome).all()
                com = comunicados.objects.all()
                return render(request,"comunicadop.html",{"user":user,"mcom":mcom,"com":com,"sucesso":"Bem-vindos aos comunicados"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def comdr(request,pk):
    if pk != None:
        user = directoria.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                conn = request.POST["comunicado"]
                sucesso = ""
                try:
                    if len(conn) > 10:
                        r = comunicados(de=user.id,de2="directoria",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    elif len(request.FILES["arquivo"]) > 2:
                        r = comunicados(de=user.id,de2="directoria",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    else:
                        sucesso = "Sem sucesso, impossivel comunicar um texto com menos de 10 letras"
                except:
                    if len(conn) > 10:
                        r = comunicados(de=user.id,de2="directoria",comunicado=conn,comunicando=user.nome,arquivo="")
                        r.save()
                        sucesso = "Carregado o comunicado com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel comunicar um texto com menos de 10 letras"
                mcom = comunicados.objects.filter(de=user.id,de2="directoria",comunicando=user.nome).all()
                com = comunicados.objects.all()
                return render(request,"comunicadod.html",{"user":user,"mcom":mcom,"com":com,"sucesso":sucesso})
        else:
            if user != None:
                mcom = comunicados.objects.filter(de=user.id,de2="directoria",comunicando=user.nome).all()
                com = comunicados.objects.all()
                return render(request,"comunicadod.html",{"user":user,"mcom":mcom,"com":com,"sucesso":"Bem-vindos aos comunicados"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def tral(request,pk):
    if pk != None:
        user = aluno.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                conn = request.POST["comunicado"]
                sucesso = ""
                try:
                    if len(conn) > 10:
                        r = trabalho(de=user.id,de2="aluno",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    elif len(request.FILES["arquivo"]) > 2:
                        r = trabalho(de=user.id,de2="aluno",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel criar trabalho com um texto com menos de 10 letras"
                except:
                    if len(conn) > 10:
                        r = trabalho(de=user.id,de2="aluno",comunicado=conn,comunicando=user.nome,arquivo="")
                        r.save()
                    else:
                        sucesso = "Sem sucesso, impossivel criar trabalho com um texto com menos de 10 letras"
                mcom = trabalho.objects.filter(de=user.id,de2="aluno",comunicando=user.nome).all()
                com = trabalho.objects.all()
                return render(request,"trabalho.html",{"user":user,"mcom":mcom,"comunicados":com,"sucesso":sucesso})
        else:
            if user != None:
                mcom = trabalho.objects.filter(de=user.id,de2="aluno",comunicando=user.nome).all()
                com = trabalho.objects.all()
                return render(request,"trabalho.html",{"user":user,"mcom":mcom,"comunicados":com,"sucesso":"Bem-vindos aos comunicados"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})


def trpr(request,pk):
    if pk != None:
        user = professor.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                conn = request.POST["comunicado"]
                sucesso = ""
                try:
                    if len(conn) > 10:
                        r = trabalho(de=user.id,de2="professor",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    elif len(request.FILES["arquivo"]) > 2:
                        r = trabalho(de=user.id,de2="professor",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel criar trabalho com um texto com menos de 10 letras"
                except:
                    if len(conn) > 10:
                        r = trabalho(de=user.id,de2="professor",comunicado=conn,comunicando=user.nome,arquivo="")
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel criar trabalho com um texto com menos de 10 letras"
                mcom = trabalho.objects.filter(de=user.id,de2="aluno",comunicando=user.nome).all()
                com = trabalho.objects.all()
                return render(request,"trabalhop.html",{"user":user,"mcom":mcom,"com":com,"sucesso":sucesso})
        else:
            if user != None:
                mcom = trabalho.objects.filter(de=user.id,de2="professor",comunicando=user.nome).all()
                com = trabalho.objects.all()
                return render(request,"trabalhop.html",{"user":user,"mcom":mcom,"com":com,"sucesso":"Bem-vindos aos comunicados"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def trdr(request,pk):
    if pk != None:
        user = directoria.objects.filter(slug=pk).first()
        if request.method == "POST":
            if user != None:
                conn = request.POST["comunicado"]
                sucesso = ""
                try:
                    if len(conn) > 10:
                        r = trabalho(de=user.id,de2="directoria",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    elif len(request.FILES["arquivo"]) > 2:
                        r = trabalho(de=user.id,de2="directoria",comunicado=conn,arquivo=request.FILES["arquivo"],comunicando=user.nome)
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso e com seu devido arquivo "+str(request.FILES["arquivo"])
                    else:
                        sucesso = "Sem sucesso, impossivel criar trabalho com um texto com menos de 10 letras"
                except:
                    if len(conn) > 10:
                        r = trabalho(de=user.id,de2="directoria",comunicado=conn,comunicando=user.nome,arquivo="")
                        r.save()
                        sucesso = "Carregado o trabalho com sucesso"
                    else:
                        sucesso = "Sem sucesso, impossivel criar trabalho com um texto com menos de 10 letras"
                mcom = trabalho.objects.filter(de=user.id,de2="directoria",comunicando=user.nome).all()
                com = trabalho.objects.all()
                return render(request,"trabalhod.html",{"user":user,"mcom":mcom,"com":com,"sucesso":sucesso})
        else:
            if user != None:
                mcom = trabalho.objects.filter(de=user.id,de2="directoria",comunicando=user.nome).all()
                com = trabalho.objects.all()
                return render(request,"trabalhod.html",{"user":user,"mcom":mcom,"com":com,"sucesso":"Bem-vindos aos comunicados"})
            else:
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})


def seem(request,pk,l):
    if pk != None:
        user  = aluno.objects.filter(slug=pk).first()
        if user != None:
            curcom = comunicados.objects.filter(id=l).first()
            if curcom != None:
                if request.method == "POST":
                    curcom.delete()
                    return redirect("/a/"+str(user.slug)+"/comunicados/")
                else:
                    return render(request,"seeco.html",{"user":user,"com":curcom})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def seemp(request,pk,l):
    if pk != None:
        user  = professor.objects.filter(slug=pk).first()
        if user != None:
            curcom = comunicados.objects.filter(id=l).first()
            if curcom != None:
                if request.method == "POST":
                    curcom.delete()
                    return redirect("/p/"+str(user.slug)+"/comunicados/")
                else:
                    return render(request,"seecop.html",{"user":user,"com":curcom})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def seemd(request,pk,l):
    if pk != None:
        user  = directoria.objects.filter(slug=pk).first()
        if user != None:
            curcom = comunicados.objects.filter(id=l).first()
            if curcom != None:
                if request.method == "POST":
                    curcom.delete()
                    return redirect("/d/"+str(user.slug)+"/comunicados/")
                else:    
                    return render(request,"seecod.html",{"user":user,"com":curcom})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})


def trma(request,pk,l):
    if pk != None:
        user  = aluno.objects.filter(slug=pk).first()
        if user != None:
            curcom = trabalho.objects.filter(id=l).first()
            if curcom != None:
                if request.method == "POST":
                    curcom.delete()
                    return redirect("/a/"+str(user.slug)+"/trabalhos/")
                else:
                    return render(request,"seetr.html",{"user":user,"com":curcom})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def trmp(request,pk,l):
    if pk != None:
        user  = professor.objects.filter(slug=pk).first()
        if user != None:
            curcom = trabalho.objects.filter(id=l).first()
            if curcom != None:
                if request.method == "POST":
                    curcom.delete()
                    return redirect("/p/"+str(user.slug)+"/trabalhos/")
                else:
                    return render(request,"seetrpr.html",{"user":user,"com":curcom})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def trmd(request,pk,l):
    if pk != None:
        user  = directoria.objects.filter(slug=pk).first()
        if user != None:
            curcom = trabalho.objects.filter(id=l).first()
            if curcom != None:
                if request.method == "POST":
                    curcom.delete()
                    return redirect("/d/"+str(user.slug)+"/trabalhos/")
                else:    
                    return render(request,"seetrdr.html",{"user":user,"com":curcom})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def criata(request,pk):
    if pk != None:
        user = aluno.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                turmas = turma.objects.all()
                return render(request,"signtr.html",{"user":user,"turmas":turmas})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def criatd(request,pk):
    if pk != None:
        user = directoria.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                return render(request,"signtrd.html",{"user":user})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def criatp(request,pk):
    if pk != None:
        user = professor.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
            else:
                turmas = turma.objects.all()
                return render(request,"signtrp.html",{"user":user,"turmas":turmas})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def crtp(request,pk):
    if pk != None:
        user = professor.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                try:
                    t = turma(de=user.id,de2="professor",classe=request.POST["classe"],referencia=request.POST["referencia"],director_de_turma=request.POST["director_de_turma"],chefe_de_turma=request.POST["chefe_de_turma"],sala=request.POST["sala"],turno=request.POST["turno"],password=request.POST["password"],imagem=request.FILES['imagem'])
                except:
                    t = turma(de=user.id,de2="professor",classe=request.POST["classe"],referencia=request.POST["referencia"],director_de_turma=request.POST["director_de_turma"],chefe_de_turma=request.POST["chefe_de_turma"],sala=request.POST["sala"],turno=request.POST["turno"],password=request.POST["password"])
                for x in request.POST:
                    if len(request.POST[x]) >= 1:
                        pass
                    else:
                        if x == "imagem":
                            pass
                        else:
                            return render(request,"signtrpr.html",{"erro":"Falha, verifique as informacoes acima sobre o "+str(x)})
                if len(request.POST["director_de_turma"]) > 9 and len(request.POST["password"]) > 9:
                    pass
                else:
                    return render(request,"signtrpr.html",{"erro":"Falha, garanta que o director de turma e o password tenham mais de 10 carateres"})
                if request.POST["password"] == request.POST["password2"]:
                    r = turma.objects.filter(slug=request.POST["csrfmiddlewaretoken"]).first()
                    if r == None:
                        t.slug = request.POST["csrfmiddlewaretoken"]
                    else:
                        g = iding(t="turma")
                        t.slug = "turma"+str(g)
                        t.save()
                        t.id = g
                    t.save()
                    return redirect("/p/"+str(user.slug)+"/")
                else:
                    return render(request,"signtrpr.html",{"user":user,"erro":"Os password tem de ser iguais"})
            else:
                return render(request,"signtrpr.html",{"user":user})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})

def crt(request,pk):
    if pk != None:
        user = aluno.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                try:
                    t = turma(de=user.id,de2="aluno",classe=request.POST["classe"],referencia=request.POST["referencia"],director_de_turma=request.POST["director_de_turma"],chefe_de_turma=request.POST["chefe_de_turma"],sala=request.POST["sala"],turno=request.POST["turno"],password=request.POST["password"],imagem=request.FILES['imagem'])
                except:
                    t = turma(de=user.id,de2="aluno",classe=request.POST["classe"],referencia=request.POST["referencia"],director_de_turma=request.POST["director_de_turma"],chefe_de_turma=request.POST["chefe_de_turma"],sala=request.POST["sala"],turno=request.POST["turno"],password=request.POST["password"])
                for x in request.POST:
                    if len(request.POST[x]) >= 1:
                        pass
                    else:
                        if x == "imagem":
                            pass
                        else:
                            return render(request,"signt.html",{"erro":"Falha, verifique as informacoes acima sobre o "+str(x)})
                if len(request.POST["director_de_turma"]) > 9 and len(request.POST["password"]) > 9:
                    pass
                else:
                    return render(request,"signt.html",{"erro":"Falha, garanta que o director de turma e o password tenham mais de 10 carateres"})
                if request.POST["password"] == request.POST["password2"]:
                    r = turma.objects.filter(slug=request.POST["csrfmiddlewaretoken"]).first()
                    if r == None:
                        t.slug = request.POST["csrfmiddlewaretoken"]
                    else:
                        g = iding(t="turma")
                        t.slug = "turma"+str(g)
                        t.save()
                        t.id = g
                    t.save()
                    return redirect("/a/"+str(user.slug)+"/")
                else:
                    return render(request,"signt.html",{"user":user,"erro":"Os password tem de ser iguais"})
            else:
                return render(request,"signt.html",{"user":user})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def turseepr(request,pk,l):
    if l != None and pk != None:
        user = professor.objects.filter(slug=pk).first()
        tur = turma.objects.filter(slug=l).first()
        if user != None and tur != None:
            if request.method == "POST":
                e = request.POST["group"]
                try:
                    t = request.POST["thevalue"]
                except:
                    t = request.FILES["thevalue"]
                if len(t) > 0:
                    if e == "classe":
                        tur.classe = t
                    elif e == "turno":
                        tur.turno = t
                    elif e == "director_de_turma":
                        tun.director_de_turma = t
                    elif e == "chefe_de_turma":
                        tur.chefe_de_turma = t
                    elif e == "sala":
                        tur.sala = t
                    elif e == "referencia":
                        tur.referencia = t
                    elif e == "password":
                        tur.password = t
                    elif e == "imagem":
                        tur.imagem = t
                else:
                    return render(request,"turmap.html",{"user":user,"turma":tur})
                tur.save()
                return render(request,"turmap.html",{"user":user,"turma":tur})
            else:
                return render(request,"turmap.html",{"user":user,"turma":tur})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accao desejada"})
def turseeal(request,pk,l):
    if l != None and pk != None:
        user = aluno.objects.filter(slug=pk).first()
        tur = turma.objects.filter(slug=l).first()
        if user != None and tur != None:
            if request.method == "POST":
                e = request.POST["group"]
                try:
                    t = request.POST["thevalue"]
                except:
                    t = request.FILES["thevalue"]
                if len(t) > 0:
                    if e == "classe":
                        tur.classe = t
                    elif e == "turno":
                        tur.turno = t
                    elif e == "director_de_turma":
                        tun.director_de_turma = t
                    elif e == "chefe_de_turma":
                        tur.chefe_de_turma = t
                    elif e == "sala":
                        tur.sala = t
                    elif e == "referencia":
                        tur.referencia = t
                    elif e == "password":
                        tur.password = t
                    elif e == "imagem":
                        tur.imagem = t
                else:
                    return render(request,"turma.html",{"user":user,"turma":tur})
                tur.save()
                return render(request,"turma.html",{"user":user,"turma":tur})
            else:
                return render(request,"turma.html",{"user":user,"turma":tur})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accão desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accão desejada"})

def alunoseealuno(request,pk,pl):
    if pk!= None and pl != None:
        user = aluno.objects.filter(slug=pk).first()
        us = aluno.objects.filter(slug=pl).first()
        if user != None and us != None:
            return render(request,"seealuno.html",{"user":user,"us":us})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accão desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accão desejada"})

def prseealuno(request,pk,pl):
    if pk!= None and pl != None:
        user = professor.objects.filter(slug=pk).first()
        us = aluno.objects.filter(slug=pl).first()
        if user != None and us != None:
            return render(request,"seealunopr.html",{"user":user,"us":us})
        else:
            return render(request,"404.html",{"relatorio":"Impossivel concluir a accão desejada"})
    else:
        return render(request,"404.html",{"relatorio":"Impossivel concluir a accão desejada"})
def col(request,pk):
    if pk!=None:
        user = aluno.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                e = request.POST["search"]
                colegas = aluno.objects.filter(Q(nome=e)|Q(nome__contains=e)).all()
                return render(request,"colegas.html",{"colegas":colegas,"user":user})
            else:
                colegas = aluno.objects.filter(turma=user.turma).all()
                return render(request,"colegas.html",{"colegas":colegas,"user":user})
        else:
            return render(request,"404.html",{"relatorio":"Não possivel acessar a sua conta"})
def chat(request,pk):
    if pk!=None:
        user = aluno.objects.filter(slug=pk).first()
        if user != None:
            if request.method == "POST":
                e = request.POST["grupo"]
                if e == "procurar":
                    e = request.POST["search"]
                    m = messagens.objects.filter(conteudo__contains=e).all()
                    m = conversa.objects.filter(messagem=m).all()
                    return render(request,"mensagens.html",{"user":user,"conversas":m})
                elif e == "enviar":
                    m = conversas.objects.filter(Q(de=user.id,de2="aluno")|Q(para=user.id,para2="aluno")).all()
                    e = {}
                    e["para"] = request.POST["para"]
                    e["contacto"] = request.POST["contacto"]
                    e["conteudo"] = request.POST["conteudo"]
                    try:
                        e["arquivo"] = request.FILES["arquivo"]
                        me = messagems(conteudo=e["conteudo"],arquivo=e["arquivo"])
                        c = e["contacto"]
                        t = request.POST["para"]
                        if t == "professor":
                            user2 = professor.objects.filter(contacto=c).first()
                        elif t == "aluno":
                            user2 = aluno.objects.filter(contacto=c).first()
                        elif t == "directoria":
                            user2 = directoria.objects.filter(contacto=c).first()
                        if user2 == None:
                            pa = "Nao existe tal contacto de numero %s"%c
                            return render(request,"mensagens.html",{"user":user,"conversas":m,"erro":pa,"arquivo":e["arquivo"],"contacto":e["contacto"],"conteudo":e["conteudo"]})
                        else:
                            me.save()
                            con = conversas(de=user.id,de2="aluno",para=user2.id,para2=t,messagem=me)
                            con.save()
                            return render(request,"mensagens.html",{"user":user,"conversas":m,"erro":con})
                    except:
                        if len(e["conteudo"]) > 10:
                            t = request.POST["para"]
                            me = messagems(conteudo=e["conteudo"],arquivo="")
                            c = e["contacto"]
                            if t == "professor":
                                user2 = professor.objects.filter(contacto=c).first()
                            elif t == "aluno":
                                user2 = aluno.objects.filter(contacto=c).first()
                            elif t == "directoria":
                                user2 = directoria.objects.filter(contacto=c).first()
                            if user2 == None:
                                pa = "Nao existe tal contacto de numero %s"%c
                                return render(request,"mensagens.html",{"user":user,"conversas":m,"erro":pa,"contacto":e["contacto"],"conteudo":e["conteudo"]})
                            else:
                                me.save()
                                con = conversas(de=user.id,de2="aluno",para=user2.id,para2=t,messagem=me)
                                con.save()
                                return render(request,"mensagens.html",{"user":user,"conversas":m,"erro":con})
                        else:
                            pa = "Não tem conteudo suficiente, tem de ter mais de 10 carateres"
                            m = conversas.objects.filter(Q(de=user.id,de2="aluno")|Q(para=user.id,para2="aluno")).all()
                            return render(request,"mensagens.html",{"user":user,"conversas":m,"erro":pa,"contacto":e["contacto"],"conteudo":e["conteudo"]})
            else:
                m = conversas.objects.filter(Q(de=user.id,de2="aluno")|Q(para=user.id,para2="aluno")).all()
                return render(request,"mensagens.html",{"user":user,"conversas":m})
        else:
            return render(request,"404.html",{"relatorio":"Não possivel acessar a sua conta"})
