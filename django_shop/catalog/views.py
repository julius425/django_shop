from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def categories_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'catalog/categories_list.html', context)


def product_list(request, slug):
    import pprint
    pprint.pprint(request.META)
    category = get_object_or_404(Category, slug=slug)
    products_list = category.products.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(products_list, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, category_slug, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)