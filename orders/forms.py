
# Create your views here.
from cProfile import label
from django import forms
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset,Button, Submit,Field,HTML
from crispy_forms.bootstrap import FieldWithButtons,StrictButton
from home.models import Members
from orders.models import NonMemberModel, OrderModel


class OrderNonMemberForm(forms.ModelForm):              
    class Meta: 
        model = NonMemberModel
        fields = ["name","member_id","email","phone","family_count","prasad_count"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'You are registering for the event to be held on {{event_date}}',                
                'name',
                'email',
                'phone',
                'family_count',
                'prasad_count',
            ),
            Submit('submit', 'Submit', css_class='button'),
        )       
        self.fields['member_id'].label = 'Member ID'
