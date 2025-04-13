from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario

class EditarPerfilForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput,
        required=True,
        help_text='Debe contener al menos una mayúscula, una minúscula, un número y mínimo 8 caracteres.',
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        # Validación de seguridad
        import re
        if not re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password1):
            raise forms.ValidationError('La contraseña no cumple con los requisitos de seguridad.')

        return cleaned_data
