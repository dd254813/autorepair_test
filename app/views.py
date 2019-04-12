from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from app.mixins import UniversalMixins
from app.models import (Customer,
                        Schedule,
                        Worker)

"""
Класс BaseView формирует словарь с данными о мастерах, рабочем времени организации, рабочих днях.
Также, по необходимости, формирует список зарезервированного времени.

функция sing_up_for_diagnostic осуществляет запись информации в БД.
На этапе подготовки к записи происходит проверка на наличие свободного времени,
в случае его отсутствия возвращается результат с отказом.
Предотвращает овозникновение ошибки при попытке записи на одно и тоже время
разными пользователями в текущий момент.

функция get_holded_time поддерживает работу ajax для оботражения на
странице только свободного времени у мастера.
"""


class BaseView(UniversalMixins, View):
    def get(self, request, *args, **kwargs):
        mixin_data = super(BaseView, self)
        context = mixin_data.get_main()
        return render(request,'base.html', context)


def sing_up_for_diagnostic(request):
    if request.is_ajax():
        date = request.GET.get('date')
        time = request.GET.get('time')
        worker = request.GET.get('worker')
        fio = request.GET.get('fio')
        car = request.GET.get('car')
        worker = Worker.objects.get(name=worker)
        if Schedule.objects.filter(worker=worker, date=date, time_m=time).exists():
            #print('На данное время к этому мастеру уже существует запись!!!')
            return JsonResponse({'result':"На данное время к этому мастеру уже существует запись!!!"}, safe=False)
        customer = Customer.objects.create(name=fio, car=car)
        new_order = Schedule.objects.create(
            worker=worker,
            customer=customer,
            date=date,
            time_m=time
        )
        new_order.save()
        return JsonResponse({'result': "Вы записаны к мастеру {} на диагностику авто".format(worker.name)}, safe=False)


def get_holded_time(request):
    if request.is_ajax():
        date = request.GET.get('date')
        worker = request.GET.get('worker')
        worker = Worker.objects.get(name=worker)
        holded_time = Schedule.objects.filter(worker=worker, date=date)
        arr = []
        if len(holded_time)>0:
            for time in holded_time:
                arr.append(time.time_m)
        return JsonResponse({'result': arr}, safe=False)
