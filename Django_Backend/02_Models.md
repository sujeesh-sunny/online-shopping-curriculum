# Models in Django

Models are Python classes that define the structure of your database.

## Creating Models
- Example of a simple model:
  ```python
  from django.db import models

  class Product(models.Model):
      name = models.CharField(max_length=100)
      price = models.DecimalField(max_digits=10, decimal_places=2)

