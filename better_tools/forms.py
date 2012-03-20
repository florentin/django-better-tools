from django import forms

class RequiredFormSet(forms.models.BaseInlineFormSet):
    """
    A special FormSet that makes the admin to validate the inline formsets
    """
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False
        

class AlwaysChangedModelForm(forms.ModelForm):
    """
    This makes the inline FormSets to be considered even if they are empty (unchanged)  
    """
    def has_changed(self):
        """
        Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved.
        """
        return True