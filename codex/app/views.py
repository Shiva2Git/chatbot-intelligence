from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import openai, os,requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from .models import Image
load_dotenv()

api_key=os.getenv("OPENAI_KEY",None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and  request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt= prompt,
            max_tokens=256,
            temperature=0.5
        )
        print(response)

        chatbot_response = response["choices"][0]["text"]
    return render(request,"b.html",{"response":chatbot_response})


def image_chat(request):
    obj=None
    #chatbot_response = None
    if api_key is not None and  request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        response = openai.Image.create(
            prompt = user_input,
            size='256x256'
        )
        img_url=response["data"][0]["url"]

        response = requests.get(img_url)
        img_file=ContentFile(response.content)

        count=Image.objects.count() + 1
        fname=f"image-{count}.jpg"

        obj=Image(phrase=user_input)
        obj.ai_image.save(fname,img_file)
        obj.save()

    return render(request,"main.html",{"object":obj})

    