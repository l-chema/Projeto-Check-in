from django.db import models

class Adolescente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    data_nascimento = models.DateField()
    GENERO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, null=False)
    pg = models.CharField(max_length=50, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class DiaEvento(models.Model):
    data = models.DateField(unique=True)

    def __str__(self):
        return self.data.strftime('%d/%m/%Y')

class Presenca(models.Model):
    adolescente = models.ForeignKey(Adolescente, on_delete=models.CASCADE)
    dia = models.ForeignKey(DiaEvento, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)