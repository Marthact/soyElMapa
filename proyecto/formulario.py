from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'autocomplete': 'off','size':'28',}))

    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'autocomplete': 'off'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'autocomplete': 'off'}))

class IngresarForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'autocomplete': 'off'
                

            }
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'autocomplete': 'off'
               

            }
        )
    )