from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# 장고가 제공하는 creationForm을 상속받아서
# 우리가 정의한 User모델을 사용하도록 새로 생성

class CustomCreationForm(UserCreationForm):
# 클래스 이름 마음대로 해도 됨(괄호안은 틀리면 안됨)
    nickname = forms.CharField(max_length=20, required=False, help_text="필요 시 닉네임을 지정하세요")
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # 앞으로 사용할 필드는 기존것과 위에서 정의한 닉넴필드다
        fields = UserCreationForm.Meta.fields + ('nickname', )

class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()