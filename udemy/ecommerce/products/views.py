from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
    
    '''
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    '''
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)
    
class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        instance = Product.objects.get_by_id(id=pk)
        print("instance - <from get_object>", instance)
        if instance is None:
            raise Http404("Product %d doesn't exist" % int(pk))
        return instance
    
    '''
    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        print("id from get_queryset", pk)
        return Product.objects.filter(pk=pk)
    '''
    
def product_detail_view(request, pk):
    #instance = Product.objects.get(pk=pk)
    #instance = get_object_or_404(Product, pk=pk)
    instance = Product.objects.get_by_id(id=pk)
    print("instance:", instance)
    if instance is None:
        raise Http404("Product %d doesn't exist" % int(pk))
    '''
    try:
        instance = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        print("no product here")
        raise Http404("Product %d doesn't exist" % int(pk))
    except:
        print("huh?")
   
    qs = Product.objects.filter(id=pk)
    print(qs)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product %d doesn't exist" % int(pk))
    '''
    context = {
        "object": instance
    }
    print("context", context)
    return render(request, "products/detail.html", context)