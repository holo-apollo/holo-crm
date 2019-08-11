from modeltranslation.translator import TranslationOptions, register

from .models import User


@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)
