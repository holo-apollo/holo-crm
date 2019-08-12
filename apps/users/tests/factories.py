import factory

from apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('word')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone = factory.Sequence(lambda n: f'+38099{n:07d}')
