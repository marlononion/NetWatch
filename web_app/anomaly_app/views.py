from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class ResultsView(View):
    def get(self, request):
        return redirect('index')

    def post(self, request):
        avg_packet_size = request.POST['avg_packet_size']
        total_packets = request.POST['total_packets']

        # Realize a detecção de anomalias com o modelo
        # Aqui você pode usar o modelo previamente treinado para fazer previsões

        # Renderizar a página de resultados com a previsão
        return render(request, 'results.html', {'prediction': prediction})