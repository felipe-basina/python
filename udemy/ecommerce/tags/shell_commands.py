
# Identificando como recuperar, de maneira inversa, as tags (a tag que possui referencia explicita para produto)
# Objeto Produto nao possui referencia, explicita, para objeto Tag
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> qs = Product.objects.all()
>>> qs
<ProductQuerySet [<Product: T-Shirt>, <Product: Hat>, <Product: Supercomputer>, <Product: T-Shirt>, <Product: Lorem Ipsum>]>
>>> tshirt = qs.
  File "<console>", line 1
    tshirt = qs.
               ^
SyntaxError: invalid syntax
>>> tshirt = qs.first()
>>> tshirt.title
'T-Shirt'
>>> tshirt.slug
't-shirt'
>>> tshirt.price
Decimal('39.99')
>>> tshirt.slug
't-shirt'
>>> tshirt.description
'This is an awesome shirt. But it. :)'
>>> tshirt.tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tag'
>>> tshirt.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x000001DF1F47D5F8>
>>> tshirt.tag_set.all()
<QuerySet [<Tag: T shirt>, <Tag: TShirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
>>>