import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        url = 'https://v1.genr.ai/api/circuit-element/generate-captions'
        image_url = request.POST.get('image_url')
        headers = {'Authorization': 'Bearer your_token_here'}
        data = {'imageUrl': image_url}
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            response_text = response.json()['caption']
            context = {'response_text': response_text}
            return render(request, 'recognize/index.html', context)
        else:
            return HttpResponse('Error')
    else:
        return render(request, 'recognize/index.html')
