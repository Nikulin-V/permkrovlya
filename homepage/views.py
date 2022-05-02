from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'homepage/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class FileView(TemplateView):
    file_name = None

    def get(self, request, *args, **kwargs):
        try:
            return FileResponse(
                open(f'static/files/{self.file_name}', 'rb'),
                content_type='application/pdf'
            )
        except FileNotFoundError:
            raise Http404('Файл не найден')
