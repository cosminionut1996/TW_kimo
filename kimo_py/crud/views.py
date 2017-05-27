from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage

from kimo.models import Utilizator


class CRUD(View):
    def get(self, request):
        return render(request, 'crud/crud.html')


class CrudInsert(View):
    def get(self, request):
        return render(request, 'crud/insert.html', context={
            'id': Utilizator.objects.all().count() + 1
        })

    def post(self, request):
        e = 'Success'
        try:
            Utilizator.objects.create(
                nume=request.POST.get('nume'),
                prenume=request.POST.get('prenume'),
                subscriptie='FREE' if 'sw_licenta' not in request.POST else 'PAID',
                adresa=request.POST.get('adresa'),
                telefon=request.POST.get('telefon'),
                username=request.POST.get('username'),
                parola=request.POST.get('parola'),
                expirare=request.POST.get('expirare'),
                id=Utilizator.objects.all().count() + 1,
            )
        except Exception as exc:
            e = exc
        return render(request, 'crud/insert.html', context={
            'error': e,
            'id': Utilizator.objects.all().count() + 1
        })


class CrudRead(View):
    @staticmethod
    def select_from_table(request):
        rows = int(request.GET.get('rows', 50))
        page = int(request.GET.get('page', 1))

        _dict = dict()
        for _ in request.session['POST_DATA']:
            if request.session['POST_DATA'][_]:
                _dict[_] = request.session['POST_DATA'][_]

        if 'sw_licenta' in _dict:
            _dict['subscriptie'] = 'PAID'
            del _dict['sw_licenta']
        else:
            _dict['subscriptie'] = 'FREE'

        del _dict['csrfmiddlewaretoken']

        r = Utilizator.objects.filter(**_dict)

        paginator = Paginator(r, rows)
        try:
            users = paginator.page(page)
        except EmptyPage:
            if page < 1:
                users = paginator.page(1)
            else:
                users = paginator.page(paginator.num_pages)

        return render(request, 'crud/read_response.html', context={
            "query_result": users,
            "page": page,
            "rows": rows,
        })

    def get(self, request):
        if not request.GET.get('rows') and not request.GET.get('page') \
                or 'POST_DATA' not in request.session:
            return render(request, 'crud/read_form.html')
        return self.select_from_table(request)

    def post(self, request):
        request.session['POST_DATA'] = request.POST
        return self.select_from_table(request)


class CrudUpdate(View):
    def get(self, request):
        return render(request, 'crud/update.html')

    def post(self, request):
        if not request.POST.get('id'):
            return render(request, 'crud/update.html', context={
                "error": "id not given"
            })
        Utilizator.objects.filter(id=request.POST.get('id')).update(
            nume=request.POST.get('nume'),
            prenume=request.POST.get('prenume'),
            subscriptie='FREE' if 'sw_licenta' not in request.POST else 'PAID',
            adresa=request.POST.get('adresa'),
            telefon=request.POST.get('telefon'),
            username=request.POST.get('username'),
            parola=request.POST.get('parola'),
            expirare=request.POST.get('expirare'),
        )
        return render(request, 'crud/update.html', context={
            "error": "Success"
        })


class CrudDelete(View):
    def get(self, request):
        return render(request, 'crud/delete.html')

    def post(self, request):
        _id = request.POST.get('id')
        try:

            er = Utilizator.objects.get(id=_id)
            res = str(er.id) + ' ' + str(er.nume) + ' ' + str(er.prenume) + ' ' +\
                  str(er.username)
            er.delete()
        except Exception as exc:
            res = exc
        return render(request, 'crud/delete.html', context={
            'error': res
        })


class ExportTable(View):
    def get(self, request):
        return render(request, 'crud/export.html')

    def post(self, request):
        export_name = request.POST.get("export")
        print(export_name)
        return render(request, 'crud/export.html', context={
            'error': export_name
        })
