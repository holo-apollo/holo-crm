import factory

from apps.customers.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('name')
    email = factory.Faker('email')
    phone = factory.Sequence(lambda n: f'+38099{n:07d}')
