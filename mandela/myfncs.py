class criatr(CreateView):
    template_name = "signtr.html"
    model = trabalho
    form_class = Trabalho
    def post(self, request,*args,**kwargs):
        if len(request.POST) > 0:
            if request.POST["password"] == request.POST["password2"]:
                e = request.POST['qual']
                nome = request.POST['nome_da_pessoa']
                password = request.POST["passe_da_pessoa"]
                erro = "Ninguem com esses dados"
                quem = None
                if e == "professor":
                    quem = professor.objects.filter(nome=nome,password=password).first()
                elif e == "aluno":
                    quem == aluno.objects.filter(nome=nome,password=password).first()
                elif e == "directoria":
                    quem = directoria.objects.filter(nome=nome,password=password).first()
                if quem == None:
                    erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                    return render(request,"signtr.html",{"erro":erro})
                elif quem != None:
                    form = Trabalho(comunicando=quem.nome,comunicado=request.POST['trabalho'],arquivo=request.FILES['arquivo'],password=request.POST['password'])
                    if form.is_valid():
                        form.save()
                        t = trabalho.objects.filter(comunicando=quem.nome,password=request.POST['password'],comunicado=request.POST['comunicado']).first()
                        if t != None:
                            t.slug = request.POST["csrfmiddlewaretoken"]
                            t.save()
                        if e == "professor":
                            return redirect("/p/"+str(quem.slug)+"/")
                        if e == "aluno":
                            return redirect("/a/"+str(quem.slug)+"/")
                        if e == "directoria":
                            return redirect("/d/"+str(quem.slug)+"/")
                        else:
                            redirect("/p/")
                    else:
                        erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                        return render(request,"signtr.html",{"erro":erro})
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request,"signtr.html",{"erro":erro})
        else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request,"signtr.html",{"erro":erro})

class criat(CreateView):
    template_name = "signt.html"
    model = turma
    form_class = Turma
    def post(self, request,*args,**kwargs):
        if len(request.POST) > 0:
            if request.POST["password"] == request.POST["password2"]:
                e = request.POST['qual']
                nome = request.POST['nome_da_pessoa']
                password = request.POST["passe_da_pessoa"]
                erro = "Ninguem com esses dados"
                quem = None
                if e == "professor":
                    quem = professor.objects.filter(contacto=nome,password=password).first()
                elif e == "aluno":
                    quem == aluno.objects.filter(contacto=nome,password=password).first()
                elif e == "directoria":
                    quem = directoria.objects.filter(contacto=nome,password=password).first()
                if quem == None:
                    erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                    return render(request,"signt.html",{"erro":erro})
                elif quem != None:
                    form = Turma(request.POST,request.FILES)
                    if form.is_valid():
                        form.save()
                        t = turma.objects.filter(referencia=request.POST["referencia"],password=request.POST['password'],classe=request.POST['classe']).first()
                        if t != None:
                            t.slug = request.POST["csrfmiddlewaretoken"]
                            t.save()
                        if e == "professor":
                            return redirect("/p/"+str(quem.slug)+"/")
                        if e == "aluno":
                            return redirect("/a/"+str(quem.slug)+"/")
                        if e == "directoria":
                            return redirect("/d/"+str(quem.slug)+"/")
                        else:
                            redirect("/")
                    else:
                        erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                        return render(request,"signt.html",{"erro":erro})
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request,"signt.html",{"erro":erro})
        else:
            erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
            return render(request,"signt.html",{"erro":erro}) 

class criac(CreateView):
    template_name = "criac.html"
    model = comunicados
    form_class = Comunicado
    def post(self, request,*args,**kwargs):
        if len(request.POST) > 0:
            if request.POST["password"] == request.POST["password2"]:
                e = request.POST['qual']
                nome = request.POST['nome_da_pessoa']
                password = request.POST["passe_da_pessoa"]
                erro = "Ninguem com esses dados"
                quem = None
                if e == "professor":
                    quem = professor.objects.filter(nome=nome,password=password).first()
                elif e == "aluno":
                    quem == aluno.objects.filter(nome=nome,password=password).first()
                elif e == "directoria":
                    quem = directoria.objects.filter(nome=nome,password=password).first()
                if quem == None:
                    erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                    return render(request,"signc.html",{"erro":erro})
                elif quem != None:
                    form = Comunicado(comunicando=quem.nome,comunicado=request.POST['trabalho'],password=request.POST['password'])
                    if form.is_valid():
                        form.save()
                        t = comunicados.objects.filter(comunicando=quem.nome,password=request.POST['password'],comunicado=request.POST['comunicado']).first()
                        if t != Nome:
                            t.slug = request.POST["csrfmiddlewaretoken"]
                            t.save()
                        if e == "professor":
                            return redirect("/p/"+str(quem.slug)+"/")
                        if e == "aluno":
                            return redirect("/a/"+str(quem.slug)+"/")
                        if e == "directoria":
                            return redirect("/d/"+str(quem.slug)+"/")
                        else:
                            redirect("/")
                    else:
                        erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                        return render(request,"signc.html",{"erro":erro})
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request,"signc.html",{"erro":erro})
        else:
            erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
            return render(request,"signc.html",{"erro":erro})


class criat(CreateView):
    template_name = "signt.html"
    model = turma
    form_class = Turma
    def post(self, request,*args,**kwargs):
        if len(request.POST) > 0:
            if request.POST["password"] == request.POST["password2"]:
                e = request.POST['qual']
                nome = request.POST['nome_da_pessoa']
                password = request.POST["passe_da_pessoa"]
                erro = "Ninguem com esses dados"
                quem = None
                if e == "professor":
                    quem = professor.objects.filter(contacto=nome,password=password).first()
                elif e == "aluno":
                    quem == aluno.objects.filter(contacto=nome,password=password).first()
                elif e == "directoria":
                    quem = directoria.objects.filter(contacto=nome,password=password).first()
                if quem == None:
                    erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                    return render(request,"signt.html",{"erro":erro})
                elif quem != None:
                    form = Turma(request.POST,request.FILES)
                    if form.is_valid():
                        form.save()
                        t = turma.objects.filter(referencia=request.POST["referencia"],password=request.POST['password'],classe=request.POST['classe']).first()
                        if t != None:
                            t.slug = request.POST["csrfmiddlewaretoken"]
                            t.save()
                        if e == "professor":
                            return redirect("/p/"+str(quem.slug)+"/")
                        if e == "aluno":
                            return redirect("/a/"+str(quem.slug)+"/")
                        if e == "directoria":
                            return redirect("/d/"+str(quem.slug)+"/")
                        else:
                            redirect("/")
                    else:
                        erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                        return render(request,"signt.html",{"erro":erro})
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request,"signt.html",{"erro":erro})
        else:
            erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
            return render(request,"signt.html",{"erro":erro}) 

class criac(CreateView):
    template_name = "criac.html"
    model = comunicados
    form_class = Comunicado
    def post(self, request,*args,**kwargs):
        if len(request.POST) > 0:
            if request.POST["password"] == request.POST["password2"]:
                e = request.POST['qual']
                nome = request.POST['nome_da_pessoa']
                password = request.POST["passe_da_pessoa"]
                erro = "Ninguem com esses dados"
                quem = None
                if e == "professor":
                    quem = professor.objects.filter(nome=nome,password=password).first()
                elif e == "aluno":
                    quem == aluno.objects.filter(nome=nome,password=password).first()
                elif e == "directoria":
                    quem = directoria.objects.filter(nome=nome,password=password).first()
                if quem == None:
                    erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                    return render(request,"signc.html",{"erro":erro})
                elif quem != None:
                    form = Comunicado(comunicando=quem.nome,comunicado=request.POST['trabalho'],password=request.POST['password'])
                    if form.is_valid():
                        form.save()
                        t = comunicados.objects.filter(comunicando=quem.nome,password=request.POST['password'],comunicado=request.POST['comunicado']).first()
                        if t != Nome:
                            t.slug = request.POST["csrfmiddlewaretoken"]
                            t.save()
                        if e == "professor":
                            return redirect("/p/"+str(quem.slug)+"/")
                        if e == "aluno":
                            return redirect("/a/"+str(quem.slug)+"/")
                        if e == "directoria":
                            return redirect("/d/"+str(quem.slug)+"/")
                        else:
                            redirect("/")
                    else:
                        erro = "Selecione que tipo de funcionario ou cargo na escola e preencha com dados correctos"
                        return render(request,"signc.html",{"erro":erro})
            else:
                erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
                return render(request,"signc.html",{"erro":erro})
        else:
            erro = "Os passwords são diferentes, por favor insira o mesmo valor para cada"
            return render(request,"signc.html",{"erro":erro})

def iding(t=None):
    if t == None:
        pass
    elif t=="turma":
        j = random.randrange(1234567890,100000000000)
        r = turma.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
    elif t=="professor":
        j = random.randrange(1234567890,100000000000)
        r = professor.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
    elif t=="trabalho":
        j = random.randrange(1234567890,100000000000)
        r = trabalho.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
    elif t=="aluno":
        j = random.randrange(1234567890,100000000000)
        r = aluno.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
    elif t=="comunicado":
        j = random.randrange(1234567890,100000000000)
        r = comunicado.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
    elif t=="imagens":
        j = random.randrange(1234567890,100000000000)
        r = imagens.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
    elif t=="directoria":
        j = random.randrange(1234567890,100000000000)
        r = directoria.objects.filter(id=j).first()
        if r != None:
            iding()
        else:
            return j
