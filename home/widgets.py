from django.forms import TextInput


class ColorPickerWidget(TextInput):
    """Custom widget for color picker input"""
    input_type = 'color'
    template_name = 'django/forms/widgets/text.html'

    def __init__(self, attrs=None):
        default_attrs = {'style': 'height: 40px; width: 100px; cursor: pointer;'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)
