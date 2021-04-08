from django.db.models import Q
from django.http import HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Shop
from webapp.forms import ShopForm, CartAddForm, SimpleSearchForm


class IndexView(ListView):
    template_name = 'shop/index.html'
    context_object_name = 'shops'
    model = Shop
    ordering = ['category', 'name']
    form_class = SimpleSearchForm
    paginate_by = 5

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        data = Shop.objects.all()
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(name__icontains=search)).order_by('name')
                return data
        if not self.request.GET.get('is_admin', None):
            data = Shop.objects.all().filter(amount__gt=0)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddForm()
        return context


class ShopView(DetailView):
    template_name = 'shop/view.html'
    model = Shop

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddForm()
        return context


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop/create.html'

    def get_success_url(self):
        return reverse('shop_view', kwargs={'pk': self.object.pk})


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm
    template_name = 'shop/update.html'

    def get_success_url(self):
        return reverse('shop_view', kwargs={'pk': self.object.pk})


class ShopDeleteView(DeleteView):
    model = Shop
    template_name = 'shop/delete.html'
    context_object_name = 'shop'
    success_url = reverse_lazy('index')

