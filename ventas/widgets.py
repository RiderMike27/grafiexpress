import re
from django.forms.widgets import SelectMultiple
from django.utils.safestring import mark_safe


class ChosenWidget(SelectMultiple):

    def render(self, name, value, attrs=None, choices=()):
        value = [] if value is None else value

        multiselect = """
            <select id=id_{nombre} name={nombre} multiple class="chosen-select " >
                {options}
            </select>
            """.format(**{
            'nombre': name,
            'options': re.sub('selected="selected"',
                              '',
                              '\n'.join([option for option in self.render_options(choices, value).splitlines()
                                         if 'selected="selected"' in option
                                         ])),
        })

        return mark_safe(multiselect)
