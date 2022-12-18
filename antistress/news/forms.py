from .models import Test
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, CharField, ModelChoiceField, \
    MultipleChoiceField, CheckboxSelectMultiple, Form


class TestForm(ModelForm):
    class Meta:
        model = Test

        fields = ['title', 'anons', 'ans1', 'pr1', 'ans2', 'pr2', 'ans3', 'pr3']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вопроса'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
            'ans1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 1'
            }),
            'pr1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 2'
            }),
            'pr2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            }),
            'ans3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вариант ответа 3'
            }),
            'pr3': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена ответа в баллах'
            })
        }


class Testans(Form):
    model = Test
    fields = ['ans1', 'ans2']
    test = Test.objects.order_by('id')
    W = {}
    if len(test) > 20:
        for i in range(20):
            W[f'ans{i}'] = Select(
                choices=((test[i].ans1, test[i].ans1), (test[i].ans2, test[i].ans2), (test[i].ans3, test[i].ans3)),
                attrs={
                    'class': 'form-control',
                })
    else:
        for i in range(len(test)):
            W[f'ans{i}'] = Select(
                choices=((test[i].ans1, test[i].ans1), (test[i].ans2, test[i].ans2), (test[i].ans3, test[i].ans3)),
                attrs={
                    'class': 'form-control',
                })
    widgets = W
    print(widgets)

# from django import forms
#
#
#
# class GeeksForm(forms.Form):
#     def __init__(self):
#         model
#         geeks_field = forms.MultipleChoiceField(choices=DEMO_CHOICES)
