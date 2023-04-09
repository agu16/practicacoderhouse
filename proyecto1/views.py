from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def mi_vista (request):
    return HttpResponse("<h1>Hola gordiña como estas?</h1>")

def mostrar_fecha(request):
    return HttpResponse(f"<p> {datetime.now()} </p>")

def saludar(request, nombre, apellido):
    return HttpResponse(f"<h1>Hola {nombre} {apellido} como estas?</h1>")

def mi_primer_template(request):
    
    archivo= open(r"C:\Users\agust\OneDrive\Desktop\python\templates\mi_primer_template.html", "r")
     
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse (template_renderizado)
