from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Template – Gestión de Negocio</h1>
    <p>Aplicación desplegada correctamente en Render 🚀</p>
    <p>Admin: <a href="/admin/">/admin/</a></p>
    """)