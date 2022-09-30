

from django.shortcuts import render
from AppCoder.models import Familiar


def familiares(request):

   familiar1 = Familiar(nombre = "Maria", num = 1123773163, nacionalidad = "Argentina", nacimiento = "1985-03-28", email = "maria@gmail.com")
   familiar1.save()
   familiar2 = Familiar(nombre = "Jose", num = 1123348374, nacionalidad = "Argentina", nacimiento = "2003-03-28", email = "jose@gmail.com" )
   familiar2.save()
   familiar3 = Familiar(nombre = "Alberto", num = 1127372833, nacionalidad = "Argentina", nacimiento = "1977-04-15", email = "alberto@gmail.com" )
   familiar3.save()

   contexto={
      "familiar_1" :(f"Nombre:{familiar1.nombre} Telefono:{familiar1.num} Nacionalidad:{familiar1.nacionalidad} Fecha de nacimiento:{familiar1.nacimiento} Email:{familiar1.email}"),
      "familiar_2" :(f"Nombre:{familiar2.nombre} Telefono:{familiar2.num} Nacionalidad:{familiar2.nacionalidad} Fecha de nacimiento:{familiar2.nacimiento} Email:{familiar2.email}"),
      "familiar_3" :(f"Nombre:{familiar3.nombre} Telefono:{familiar3.num} Nacionalidad:{familiar3.nacionalidad} Fecha de nacimiento:{familiar3.nacimiento} Email:{familiar3.email}")
   }


    
   return render(request, 'AppCoder/familiares.html', contexto) 