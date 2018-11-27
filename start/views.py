import os
from start.cloud import Cloud
from django.http import HttpResponse
from django.shortcuts import render
from start.models import IDcard
# Create your views here.

def index(requests):
    return render(requests, 'index.html')

def appraise(requests):
    th = Cloud()
    if requests.method == 'POST':
        img = requests.FILES.get("img", None)
        if not img:
            return HttpResponse("你还没有选择照片")
        s = os.path.abspath(os.path.join(os.getcwd(), './ok'))
        apps = open(os.path.join(s, img.name), "wb+")
        for chunk in img.chunks():
            apps.write(chunk)
        apps.close()
        file = os.path.join(s, img.name)
        people = th.appraise(file)
        name = people['name']
        sex = people['sex']
        nation = people['nation']
        birth = people['birth']
        address = people['address']
        id = people['id']
        card ={
            'name': name,
            'sex': sex,
            'nation': nation,
            'birth': birth,
            'addresee': address,
            'id': id
        }
        man = IDcard(name, sex, nation, birth,
                     address, id)
        man.save()
        os.remove(os.path.join(s, img.name))
        return render(requests, 'show.html', context=card)

def showall(requests):
    people_list = IDcard.objects.all()
    print(people_list)
    content_list ={
        'people_list': people_list,
    }
    return render(requests, 'showall.html', context=content_list)