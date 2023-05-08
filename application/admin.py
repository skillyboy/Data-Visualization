from django.contrib import admin
from application.models import *


class DataIndustryAdmin(admin.ModelAdmin):
    list_display = (
        "topic",
        "sector",
        "country",
        "add_date",
        "publish_date",
    )
    search_fields = (
        "title",
        "topic",
        "region",
        "sector",
        "country",
        "pestle",
        "impact",
        "insight",
    )
    list_filter = ("country", "sector", "region")
    date_hierarchy = "publish_date"


admin.site.register(DataIndustry, DataIndustryAdmin)



