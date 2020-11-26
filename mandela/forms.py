from django.forms import *
from .models import *

class Conversa(ModelForm):
    class Meta:
        model = conversa
        fields = "__all__"
class Aluno(ModelForm):
    class Meta:
        model = aluno
        #fields = ["nome","numero_de_processo","data_de_nascimento","imagem","contacto","encarregado","turma","turno","password"]
        fields = "__all__"
class Professor(ModelForm):
    class Meta:
        model = professor
        fields = "__all__"

class Directoria(ModelForm):
    class Meta:
        model = directoria
        fields = "__all__"

class Trabalho(ModelForm):
    class Meta:
        model = trabalho
        fields = "__all__"

class Comunicado(ModelForm):
    class Meta:
        model = comunicados
        fields = "__all__"

class Turma(ModelForm):
    class Meta:
        model = turma
        fields = "__all__"
class Trabalho(ModelForm):
    class Meta:
        model = trabalho
        fields = "__all__"
class Imagem(ModelForm):
    class Meta:
        model = imagens
        fields = "__all__"
