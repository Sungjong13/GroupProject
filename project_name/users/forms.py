from django import forms
from .models import User


class CreateAccountForm(forms.ModelForm):
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="비밀번호 재확인",
                                       widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "nickname")

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        return password2
