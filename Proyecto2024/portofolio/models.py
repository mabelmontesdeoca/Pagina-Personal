from django.db import models

# Create your models here.
class Ciudad(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Persona(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    fechaNacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

class Telefono(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)

class Email(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
