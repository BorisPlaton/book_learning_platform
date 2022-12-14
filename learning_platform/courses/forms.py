from django.forms import inlineformset_factory

from courses.models import Module, Course


ModuleFormSet = inlineformset_factory(
    Course, Module, fields=['title', 'description'],
    extra=2, can_delete=True
)
