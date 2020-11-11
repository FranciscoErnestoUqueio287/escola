from django.db.models import *
esc = (("Diurno","Diurno"),("Noturno","Noturno"))
r = (("aluno","aluno"),("professor","professor"),("directoria","directoria"))

class trabalho(Model):
    de = PositiveIntegerField(verbose_name="de",default=0,blank=False,null=False)
    de2 = CharField(verbose_name="de_",default="",blank=False,null=False,max_length=10,choices=r)
    comunicando = CharField(verbose_name="comunicando", null=False, blank=True, max_length=100)
    comunicado = TextField(verbose_name="comunicado", null=False, blank=True)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    arquivo = FileField(verbose_name="arquivo",upload_to="arquivos/", null=False,blank=True)
    REQUIRED_FIELDS = ["comunicando","password"]
    def __str__(self):
        return "Publicado por "+str(self.comunicando)
    class Meta:
        ordering = ["data_de_criacao"]
    
class comunicados(Model):
    de = PositiveIntegerField(verbose_name="de",default=0,blank=False,null=False)
    de2 = CharField(verbose_name="de_",default="",blank=False,null=False,max_length=10,choices=r)
    comunicado = TextField(verbose_name="comunicado", null=False, blank=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    comunicando = CharField(verbose_name="comunicando", null=True, blank=True, max_length=100)
    arquivo = FileField(verbose_name="arquivo",upload_to="arquivos/", null=False,blank=True)
    password = CharField(verbose_name="password", max_length=100, blank=False, null=False)
    REQUIRED_FIELDS = ["comunicando","password"]
    def __str__(self):
        return "Publicado por "+str(self.comunicando)
    class Meta:
        ordering = ["data_de_criacao"]
    
class directoria(Model):
    nome = CharField(verbose_name="nome",max_length=100, null=False, blank=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    data_de_nascimento = DateField(verbose_name="data_de_nascimento",null=False,blank=False)
    cargo = CharField(verbose_name="cargo", max_length=100, blank=True, null=False)
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    imagem = ImageField(verbose_name="imagem",upload_to="directoria/",null=False, blank=False)
    contacto = CharField(verbose_name="contacto", default="+258",null=False, blank=False, max_length=13)
    password = CharField(verbose_name="password", max_length=100, blank=False, null=False)
    REQUIRED_FIELDS = ["contacto","password"]
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ["data_de_criacao"]
    
class professor(Model):
    nome = CharField(verbose_name="nome", max_length=100, blank=False, null=False)
    data_de_nascimento = DateField(verbose_name="data_de_nascimento",null=False,blank=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    imagem = ImageField(verbose_name="imagem",upload_to="prof/",null=False, blank=True)
    classes = CharField(verbose_name="classes",null=False,blank=True,default="",max_length=50)
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    contacto = CharField(verbose_name="contacto", default="+258",null=False, blank=False, max_length=13)
    turmas = CharField(verbose_name="turmas", max_length=100, blank=False, null=False)
    password = CharField(verbose_name="password", max_length=100, blank=False, null=False)
    REQUIRED_FIELDS = ["contacto","password"]
    def __str__(self):
        return self.nome
i = []
for t in professor.objects.all():
    i.append((t.slug,t.nome))
class turma(Model):
    de = PositiveIntegerField(verbose_name="de",default=0,blank=False,null=False)
    de2 = CharField(verbose_name="de_",default="",blank=False,null=False,max_length=10,choices=r)
    referencia = CharField(verbose_name="referencia", max_length=100, blank=False, null=False)
    director_de_turma = CharField(verbose_name="director_de_turma", max_length=100, blank=False) #choices=i)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    chefe_de_turma = CharField(verbose_name="chefe_de_turma", max_length=100, blank=True, null=False)
    classe = PositiveIntegerField(verbose_name="classe", blank=False, null=False)
    sala = PositiveIntegerField(verbose_name="sala",blank=False,null=False)
    turno = CharField(verbose_name="turno", blank=False, null=False, max_length=100,choices=esc)
    imagem = ImageField(verbose_name="imagem",upload_to="directoria/",null=False, blank=True)
    password = CharField(verbose_name="password", max_length=100, blank=False, null=False)
    REQUIRED_FIELDS = ['referencia','password']
    def __str__(self):
        return self.referencia
    class Meta:
        ordering = ["data_de_criacao"]
y = []
for x in turma.objects.all():
    y.append((x.slug,x.referencia))
class aluno(Model):
    nome = CharField(verbose_name="nome", max_length=100, blank=False, null=False)
    numero_de_processo = PositiveIntegerField(verbose_name="numero_de_processo",blank=False,null=False)
    data_de_nascimento = DateField(verbose_name="data_de_nascimento",null=False,blank=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    imagem = ImageField(verbose_name="imagem",upload_to="alunos/",blank=True, null=False )
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    sala = PositiveIntegerField(verbose_name="sala",blank=False,null=False)
    contacto = CharField(verbose_name="contacto", default="+258",null=False, blank=False, max_length=13)
    classe = PositiveIntegerField(verbose_name="classe", blank=False, null=False)
    encarregado = CharField(verbose_name = "encarregado", blank=False, null=False, max_length=100)
    turma = CharField(verbose_name = "turma", blank=False, null=False, max_length=100) #,choices=y)
    turno = CharField(verbose_name="turno", blank=False, null=False, max_length=100,choices=esc)
    password = CharField(verbose_name="password", max_length=100, blank=False, null=False)
    REQUIRED_FIELDS = ['numero_de_processo','password']
    def __str__(self):
        return self.nome
class imagens(Model):
    imagem = ImageField(verbose_name="imagem",upload_to="img/",null=False, blank=False)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    class Meta:
        ordering = ["data_de_criacao"]



class conversa(Model):
    para = PositiveIntegerField(verbose_name="para",default=0,blank=False,null=False)
    de = PositiveIntegerField(verbose_name="de",default=0,blank=False,null=False)
    slug = SlugField(verbose_name="slug", default="",null=False, blank=True, max_length=60)
    de2 = CharField(verbose_name="de_",default="",blank=False,null=False,max_length=10,choices=r)
    visto_de = BooleanField(default=False,blank=False,null=False)
    visto_para = BooleanField(default=False,blank=False,null=False)
    para2 = CharField(verbose_name="para_",default="",blank=False,null=False,max_length=10, choices=r)
    arquivo = FileField(verbose_name="arquivo",upload_to="arquivos/", null=False,blank=True)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    conteudo = TextField(verbose_name="conteudo", null=False, blank=True)

'''class contactos(Model):
    nome = CharField(verbose_name="nome", max_length=100, blank=False, null=False)
    contacto = CharField(verbose_name="contacto", default="+258",null=False, blank=False, max_length=13)
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    #de = CharField(verbose_name="de",max_length=9,null=False,blank=False,choices=r)
    #quem = PositiveIntegerField(verbose_name="de",default=0,blank=False,null=False)'''    
class messagems(Model):
    data_de_criacao = DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    conteudo = TextField(verbose_name="conteudo", null=False, blank=True)
    arquivo = FileField(verbose_name="arquivo",upload_to="arquivos/", null=False,blank=True)
    class Meta:
        ordering = ["data_de_criacao"]
class conversas(Model):
    para = PositiveIntegerField(verbose_name="para",default=0,blank=False,null=False)
    de = PositiveIntegerField(verbose_name="de",default=0,blank=False,null=False)
    de2 = CharField(verbose_name="de_",default="",blank=False,null=False,max_length=10,choices=r)
    para2 = CharField(verbose_name="para_",default="",blank=False,null=False,max_length=10, choices=r)
    messagem = ForeignKey(messagems,on_delete=CASCADE,null=False,blank=True)
    def getting(self,typ,ed):
        if typ == "aluno":
            r =  aluno.objects.filter(id=ed).first()
        elif typ == "directoria":
            r =  directoria.objects.filter(id=ed).first()
        elif typ == "professor":
            r = professor.objects.filter(id=ed).first()
        
        if r == None:
            r  = "Desconhecido"
        return r
    def __str__(self):
        first = self.getting(typ=self.de2,ed=self.de)
        second = self.getting(typ=self.para2,ed=self.para)
        return "A messagem foi de um "+str(self.de2)+" de nome "+str(first)+" para um "+str(self.para2)+" de nome "+str(second)
    

    
