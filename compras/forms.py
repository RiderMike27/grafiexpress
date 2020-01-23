from dal import autocomplete
from django import forms
from compras.models import *
from produccion.models import OrdenDeTrabajo 


class OrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenDeCompra
        fields = ('__all__')
        widgets = { 
            "proveedor": autocomplete.ModelSelect2(url='/admin/proveedores/proveedor/proveedorautocomplete/'),
            "creado_por": forms.HiddenInput()
        }
    total = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),required=False)

    def __init__(self, *args, **kwargs):
        super(OrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['total'] = instance.get_total()
        self.fields['total'].widget.attrs['readonly'] = True


class PapelOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = PapelOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/papelcostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
            "precio_unitario": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto subtotal_iterable', 'data-a-sep': '.', 'data-a-dec': ','}), label='SubTotal', required=False)

    def __init__(self, *args, **kwargs):
        super(PapelOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class PreprensaOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = PreprensaOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/preprensacostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(PreprensaOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class TroquelOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = TroquelOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/troquelcostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(TroquelOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class PosprensaServicioOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = PosprensaServicioOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/posprensaserviciocostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(PosprensaServicioOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class PosprensaMaterialOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = PosprensaMaterialOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/posprensamaterialcostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(PosprensaMaterialOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class PosprensaOtroServicioOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = PosprensaOtroServicioOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/posprensaotroserviciocostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),                "precio_unitario":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(PosprensaOtroServicioOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class DatosDeBolsaOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = DatosDeBolsaOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/datosdebolsacostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(DatosDeBolsaOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class RevistaOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = RevistaOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/revistacostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(RevistaOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class CompuestoOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = CompuestoOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/compuestocostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(CompuestoOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class PlastificadoOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = PlastificadoOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/plastificadocostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(PlastificadoOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class OtroGastoOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = OtroGastoOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/produccion/otrogastocostoautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(OtroGastoOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class InsumoOrdenDeCompraForm(forms.ModelForm):
    class Meta:
        model = InsumoOrdenDeCompra
        fields = '__all__'
        widgets = { 
            "descripcion": autocomplete.ModelSelect2(url='/admin/materiales/materialautocomplete/'),
            "cantidad": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
            "precio_unitario": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }
    subtotal = forms.CharField(widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto subtotal_iterable','data-a-sep':'.','data-a-dec':','}),label='SubTotal',required=False)

    def __init__(self, *args, **kwargs):
        super(InsumoOrdenDeCompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['subtotal'] = instance.get_subtotal()
        self.fields['subtotal'].widget.attrs['readonly'] = True


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        exclude = ['codigo_de_establecimiento', 'punto_de_expedicion', 'numero_de_factura', 'pagado', 'saldo']
        widgets = { 
            "proveedor": autocomplete.ModelSelect2(url="proveedor-autocomplete"),
            "empresa": autocomplete.ModelSelect2(url='empresa-autocomplete'),
            "sucursal": autocomplete.ModelSelect2(url='sucursal-autocomplete', forward=['empresa']),
            "orden_de_compra": autocomplete.ModelSelect2Multiple(url='ordendecompra-autocomplete',forward=['proveedor']),
            #"timbrado": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12'}),
            "total": forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
        }

    numero_de_factura = forms.CharField(widget=forms.TextInput(attrs={'size': '12', 'placeholder': '000-000-0000000'}), required=True)

    def clean(self):
        cleaned_data = super(CompraForm, self).clean()

        condicion = cleaned_data.get("condicion")
        fecha_de_vencimiento = cleaned_data.get("fecha_de_vencimiento")
        fecha_de_emision = cleaned_data.get("fecha")

        if (condicion == CREDITO) and (fecha_de_vencimiento == fecha_de_emision):
            msg = "Factura es CREDITO, la fecha de vencimiento no puede ser igual a la fecha de emision"
            self.add_error('fecha_de_vencimiento', msg)

        if (condicion == CONTADO) and (fecha_de_vencimiento != fecha_de_emision):
            msg = "Factura es CONTADO, la fecha de vencimiento no puede ser distinta a la fecha de emision"
            self.add_error('fecha_de_vencimiento', msg)

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.initial['numero_de_factura'] = instance.get_numero_de_factura()
        self.fields['total'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        compra = super(CompraForm, self).save(commit=False)

        numero_de_factura = self.cleaned_data.get('numero_de_factura')
        vector = numero_de_factura.split("-")

        compra.codigo_de_establecimiento = vector[0]
        compra.punto_de_expedicion = vector[1]
        compra.numero_de_factura = vector[2]

        if commit:
            compra.save()
        return compra


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = '__all__'
        widgets = { 
            "material": autocomplete.ModelSelect2(url="material-autocomplete"),
            "cantidad": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
            "precio_unitario": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
            "subtotal": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
        }


class DetalleCompra2Form(forms.ModelForm):
    class Meta:
        model = DetalleCompra2
        fields = '__all__'
        widgets = { 
            "cantidad": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
            "precio_unitario": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
            "subtotal": forms.TextInput(attrs={'style': 'text-align:right', 'size': '12', 'class': 'auto', 'data-a-sep': '.', 'data-a-dec': ','}),
        }