from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
def update_balances(sender, instance, created, **kwargs):
    if created:
        amount = instance.amount

        # Subtract from the sender
        from_account = instance.from_user.account
        from_account.balance -= amount
        from_account.save()
        print('test1')

        # Add to receiver
        to_account = instance.to_user.account
        to_account.balance += amount
        to_account.save()
        print('test2')