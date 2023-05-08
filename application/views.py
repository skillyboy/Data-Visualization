import json
from django.shortcuts import render
from .models import *
from datetime import datetime

import django_filters
from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render

from application.models import *

# Create your views here.

app_name = 'dashboard'

def industry_summary_list(request):
    filter_data = DataIndustryFilter(request.GET, queryset=DataIndustry.objects.all())
    paginator = Paginator(filter_data.qs, 25)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"filter.html",{"filter": filter_data, "page_obj": page_obj})



def likelihood(request):
    data = {
        "data": [],
        "lable1": [],
        "lable2": [],
    }
    summaries = DataIndustry.objects.all()[:200]
    for summary in summaries:
        if summary.country or summary.region:
            data["data"].append(summary.likelihood)
            data["lable1"].append(summary.country)
            data["lable2"].append(summary.region)
    context = {
        "data": data,
        "title": "Likelihood",
        "limits": 15,
        "type1": "bar",
        "type2": "line",
    }
    return render(request, 'chart-bar.html', context)
                  


def intensity(request):
    data = {
        "data": [],
        "lable1": [],
        "lable2": [],
    }
    summaries = DataIndustry.objects.all()[:200]
    for summary in summaries:
        if summary.country or summary.region:
            data["data"].append(summary.intensity)
            data["lable1"].append(summary.country)
            data["lable2"].append(summary.region)
    context = {
        "data": data,
        "title": "Intensity",
        "limits": 100,
        "type1": "bar",
        "type2": "line",
    }
    return render( request,"chart-bar.html",context )


def relevance(request):
    data = {
        "data": [],
        "lable1": [],
        "lable2": [],
    }
    summaries = DataIndustry.objects.all()[:200]
    for summary in summaries:
        if summary.country or summary.region:
            data["data"].append(summary.relevance)
            data["lable1"].append(summary.country)
            data["lable2"].append(summary.region)
    context = {
        "data": data,
        "title": "Revelance",
        "limits": 15,
        "type1": "bar",
        "type2": "line",
    }
    return render( request, "chart-bar.html",context)


class DataIndustryFilter(django_filters.FilterSet):
    end_year = django_filters.DateFilter(
        field_name="end_year",
        lookup_expr="lte",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )
    topic = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    sector = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    region = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    pestle = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    sources = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    country = django_filters.CharFilter(
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = DataIndustry
        fields = [ "end_year", "topic", "sector", "region", "pestle", "sources", "country",
]





# def parse_data(request):
#     with open('jsondata.json', encoding='utf-8') as f:
#         data = json.load(f)
#         for item in data:
#             try:
#                 parsed_data = Data.parse(item)
#                 obj, created = Data.objects.get_or_create(**parsed_data)
#                 if not created:
#                     # The object already existed, do something here if needed
#                     pass
#             except ValueError as e:
#                 # Handle the error and log it or display an appropriate message
#                 print(f"Error parsing data: {e}")
#     return render(request, 'parse_data.html')




















