# Views and URLs

Views are Python functions or classes that receive web requests and return web responses.

## Creating a View
- Example of a simple view:
  ```python
  from django.http import HttpResponse

  def home(request):
      return HttpResponse("Welcome to the online shop!")

