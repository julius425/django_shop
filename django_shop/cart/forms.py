from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.fields_required:
            self.fields[field].required = True

    class Meta:

        model = Order
        fields = ('order_name', 'order_email', 'order_phone', 'order_address', 'order_date')
        fields_required = ('order_email', 'order_phone')
        labels = {'order_name': 'ФИО',
                  'order_email': 'Электронная почта',
                  'order_phone': 'Номер телефона',
                  'order_address': 'Адрес доставки',
                  'order_date': 'Дата доставки'}



