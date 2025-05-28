# community_board_app/context_processors.py
from .models import Category

def categories(request):
    """
    Adds the list of categories to the context of every template
    """
    categories = Category.objects.all()
    return {'categories': categories}
