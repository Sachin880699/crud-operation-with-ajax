from django.shortcuts import render , HttpResponse
from.models import *
from django.http import JsonResponse

def home(request):
    animal_obj = Animal.objects.all()
    animal_list_obj = AnimalList.objects.all()
    context  = {
        "animal_obj":animal_obj,
        "animal_list_obj":animal_list_obj
    }
    return render(request,'home.html',context)

import json
def animal_list_filter(request):
    if request.method == 'POST':
        try:
            animal_id   = request.POST.get("select_animal_obj")
            raw_list = []
            animal_obj = Animal.objects.get(id = animal_id)
            for rec in animal_obj.breed.all():
                json_dict = {}
                json_dict['id'] = rec.id
                json_dict['breed_name'] = rec.breed_name
                raw_list.append(json_dict)
            return HttpResponse(json.dumps(raw_list))
        except:
            context = {"message": False}
            return HttpResponse(json.dumps(context))

def add_new_animal(request):
    if request.method == "POST":
        animal_id       = request.POST.get("animal_id")
        breed_id        = request.POST.get("breed_id")
        date            = request.POST.get("date")
        animal_obj      = Animal.objects.get(id = animal_id)
        breed_obj       = Breed.objects.get(id = breed_id)
        AnimalList.objects.create(
            name        = animal_obj,
            breed       = breed_obj,
            date        = date
        )
        try:
            raw_list = []
            for rec in AnimalList.objects.all():
                json_dict = {}
                json_dict['id'] = rec.id
                json_dict['name'] = rec.name.name
                json_dict['breed'] = rec.breed.breed_name
                json_dict['created_date'] = str(rec.date)
                raw_list.append(json_dict)
            return HttpResponse(json.dumps(raw_list))
        except Exception as e:
            context = {"message": False}
            return HttpResponse(json.dumps(context))


def delete_animal(request):
    if request.method == "POST":
        animal_id       = request.POST.get("animal_id")
        AnimalList.objects.get(id = animal_id).delete()
    try:
        raw_list = []
        for rec in AnimalList.objects.all():
            json_dict = {}
            json_dict['id'] = rec.id
            json_dict['name'] = rec.name.name
            json_dict['breed'] = rec.breed.breed_name
            json_dict['created_date'] = str(rec.date)
            raw_list.append(json_dict)
        return HttpResponse(json.dumps(raw_list))
    except:
        context = {"message": False}
        return HttpResponse(json.dumps(context))
