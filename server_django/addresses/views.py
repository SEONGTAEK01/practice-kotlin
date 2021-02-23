from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Addresses
from .serializer import AddressesSerializer

METHOD_GET = 'GET'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'
METHOD_DELETE = 'DELETE'


@csrf_exempt
def address_list(request):
    if request.method == METHOD_GET:
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == METHOD_POST:
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        return save_serializer(serializer)


def save_serializer(serializer):
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):
    obj = Addresses.objects.get(pk=pk)
    if request.method == METHOD_GET:
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.metod == METHOD_PUT:
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        return save_serializer(serializer)
    elif request.method == METHOD_DELETE:
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    if request.method == METHOD_POST:
        data = JSONParser.parse(request)
        obj = get_object_by_name(data)
        return compare_phone_number(obj.phone_number, data.get('phone_number'))


def compare_phone_number(in_phone_num, target_phone_num):
    is_same = in_phone_num == target_phone_num
    return HttpResponse(status=200) if is_same else HttpResponse(status=400)


def get_object_by_name(data):
    search_name = data['name']
    return Addresses.objects.get(name=search_name)
