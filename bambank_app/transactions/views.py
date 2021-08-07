from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from .models import Transaction
from .forms import CreateTransactionForm

# View showing all transactions involving the current user
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transactions.html'
    context_object_name = 'transactions'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Transaction.objects.filter(Q(from_user=user) | Q(to_user=user)).order_by('-date_created')


# Create a new transaction
class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = CreateTransactionForm
    # fields = ['to_user', 'amount']

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        form.instance.from_username = self.request.user.username
        form.instance.to_username = form.instance.to_user.username

        messages.success(self.request, f'Your transaction has been completed!')
        return super().form_valid(form)