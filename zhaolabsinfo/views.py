import datetime
from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "zhaolabsinfo/pages/index.html"

class HomeView(IndexView):
    template_name = "zhaolabsinfo/pages/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context["pageTitle"] = "Zhao Laboratory"
        return context

class BioView(generic.ListView):
    model = Bio
    template_name = "zhaolabsinfo/pages/bio.html"
    context_object_name = "pageData"
    
    def get_queryset(self):
        data = {}
        data["pageTitle"] = "Bio"
        data["bioItems"] = {}
        items = Bio.objects.all().values()
        for item in items:
            positionType = item["positionType"]
            if positionType in data["bioItems"]:
                data["bioItems"][positionType].append(item["positionInfo"])
            else:
               data["bioItems"][positionType] = [(item["positionInfo"])]
        data["bioItemsKeys"] = list(data["bioItems"].keys())
        return data

    
class TeachingView(generic.ListView):
    model = Teaching
    template_name = "zhaolabsinfo/pages/teaching.html"
    context_object_name = "pageData"

    def get_queryset(self):
            data = {}
            data["pageTitle"] = "Teaching"
            data["courses"] = {}
            items = Teaching.objects.all().values()
            for item in items:
                type = item["level"]
                if type in data["courses"]:
                    data["courses"][type].append(item)
                else:
                    data["courses"][type] = [item]

            data["coursesKeys"] = list(data["courses"].keys())
            return data
    
class OpportunitiesView(generic.ListView):
    template_name = "zhaolabsinfo/pages/opportunities.html"
    model = Opportunity
    context_object_name = "pageData"

    def get_queryset(self):
        data = {}
        data["pageTitle"] = "Opportunities"
        data["opportunities"] = Opportunity.objects.all()
        return data
    
class PublicationView(generic.ListView):
    template_name = "zhaolabsinfo/pages/publications.html"
    model = Publication
    context_object_name = "pageData"

    def get_queryset(self):
        data = {}
        data["pageTitle"] = "Publications"
        data["publications"] = {}
        data["publicationYearRanges"] = []
        items = Publication.objects.all().order_by("-year").values()
        minYear = 3000
        maxYear = 0
        prevYear = 0
        currentYear = datetime.datetime.now().date().year
        for item in items:
            keyYear = 0
            if item["year"] % 10 >= 5:
                keyYear = item["year"] + (10 - (item["year"] % 10))
            else:
                keyYear = item["year"] + (10 - (item["year"] + 5) % 10)
            if keyYear < minYear:
                minYear = keyYear
            if keyYear > maxYear:
                maxYear = keyYear
            
            if prevYear != keyYear:
                data["publicationYearRanges"].append({"min": keyYear - 5, "max": keyYear - 1 if currentYear > keyYear - 1 else ""})
                data["publications"][keyYear - 5] = [item]
            else:
                data["publications"][keyYear - 5].append(item)

            prevYear = keyYear
        return data
    
class MemberView(generic.ListView):
    template_name = "zhaolabsinfo/pages/members.html"
    model = LabMember
    context_object_name = "pageData"

    def get_queryset(self):
        data = {}
        data["pageTitle"] = "Lab Members"
        data["current"] = LabMember.objects.filter(current=True)
        data["past"] = LabMember.objects.filter(current=False)
        return data
    
class ContactView(generic.ListView):
    template_name = "zhaolabsinfo/pages/contact.html"
    model = ContactInfo
    context_object_name = "pageData"

    def get_queryset(self):
        data = {}
        data["pageTitle"] = "Contact"
        return data
    
class UsefulLinksView(generic.ListView):
    template_name = "zhaolabsinfo/pages/useful_links.html"
    model = UsefulLink
    context_object_name = "pageData"

    def get_queryset(self):
        data = {}
        data["pageTitle"] = "Useful Links"
        return data