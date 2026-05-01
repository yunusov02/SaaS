import pathlib

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request: HttpRequest):

    print(this_dir)

    html_file_path = this_dir / 'test.html'

    hthml_ = html_file_path.read_text(encoding='utf-8')

    return HttpResponse(hthml_)

    # return HttpResponse('<h1> Hello, World! </h1>')
    # return "Hello World" --> raise error


