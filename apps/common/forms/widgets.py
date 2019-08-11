from django import forms
from django.utils.safestring import mark_safe


class ImageUrlWidget(forms.URLInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value:
            output.append(
                f'<a target="_blank" href="{value}">'
                f'<img src="{value}" style="height: 90px;" /></a><br />'
            )
        output.append(super().render(name, value, attrs, renderer))
        return mark_safe(''.join(output))
