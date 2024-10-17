from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "Lev/base.html"


class InfoView(TemplateView):
    template_name = "Lev/info.html"


class GroupView(TemplateView):
    template_name = "Lev/group.html"


class AgeView(TemplateView):
    template_name = "Lev/age.html"
