import factory
from product.models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    title = factory.Faker('pystr')

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Adiciona as categorias passadas como argumento
            self.categories.set(extracted)
        else:
            # Cria uma categoria padrão se nenhuma for fornecida
            default_category = CategoryFactory()
            self.categories.add(default_category)

    class Meta:
        model = Product