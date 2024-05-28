from django import forms

class VandermondeForm(forms.Form):
    x_values = forms.CharField(label='X Values', max_length=200, help_text='Ingrese los valores de X separados por comas')
    y_values = forms.CharField(label='Y Values', max_length=200, help_text='Ingrese los valores de Y separados por comas')

class NewtonForm(forms.Form):
    x_values = forms.CharField(label='X Values', max_length=100, help_text="Enter x values separated by commas, e.g., 1,2,3,4")
    y_values = forms.CharField(label='Y Values', max_length=100, help_text="Enter y values separated by commas, e.g., 1,4,9,16")
    
    
class NewtonRaphsonForm(forms.Form):
    function = forms.CharField(label='Function f', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'e.g. log(sin(x)^2 + 1)-(1/2)'}))
    derivative = forms.CharField(label='Function f\' (first derivative of f)', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'e.g. 2*(1/(sin(x)^2 + 1))*(sin(x)*cos(x))'}))
    x0 = forms.FloatField(label='Initial value (x0)', widget=forms.NumberInput(attrs={'placeholder': 'e.g. 0.5'}))
    tolerance = forms.FloatField(label='Tolerance', widget=forms.NumberInput(attrs={'placeholder': 'e.g. 1e-7'}))
    max_iterations = forms.IntegerField(label='Max iterations (max 100)', widget=forms.NumberInput(attrs={'placeholder': 'e.g. 100'}))
    
    
