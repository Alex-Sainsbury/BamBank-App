from django import forms
from django.contrib.auth.models import User
from .models import Transaction


class CreateTransactionForm(forms.ModelForm):
    to_user = forms.HiddenInput()
    from_user = forms.HiddenInput()
    amount = forms.FloatField()

    class Meta:
        model = Transaction
        fields = ['to_user', 'amount']

    def clean_write(self):
        value = self.cleaned_data['amount']
        user_balance = self.cleaned_data['from_user.account.balance']
        if value > user_balance: 
            raise forms.ValidationError('wrong value')
        return value