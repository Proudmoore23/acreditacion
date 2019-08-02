from django.shortcuts import render
from django.views.generic.edit import *
from django.urls import reverse
from .forms import *
from .models import *

def index(request):
    return render(request,template_name='index.html',)

def list_profesor(request):
    profesor = DOCENTE.objects.all()
    curso = CURSO
    explaboral = experienciaLABORAL
    expdocente = experienciaDOCENTE
    group = grupoInvestigacion
    titulo = TITULO
    espec=ESPECIALIZACION
    produc=produccionCIENTFICA
    Eva= evaluacionyPerfeccionamiento
    cargo=CARGO
    return render(request,template_name='list_profesor.html',context={'profesor':profesor,'curso':curso,'explaboral':explaboral,'expdocente':expdocente,'group':group,
        'titulo':titulo,'espec':espec,'produc':produc,'Eva':Eva,'cargo':cargo})

def list_curso(request):
    curso = CURSO.objects.all()
    return render(request,template_name='list_curso.html',context={'curso':curso})

def list_expdocente(request):
    expdocente = experienciaDOCENTE.objects.all()
    return render(request,template_name='list_expdocente.html',context={'expdocente':expdocente})

def list_institucion(request):
    institucion = INSTITUCION.objects.all()
    return render(request,template_name='list_institucion.html',context={'institucion':institucion})

def list_explaboral(request):
    explaboral = experienciaLABORAL.objects.all()
    return render(request,template_name='list_explaboral.html',context={'explaboral':explaboral})

def list_entidad(request):
    entidad = ENTIDAD.objects.all()
    return render(request,template_name='list_entidad.html',context={'entidad':entidad})

def list_group(request):
    group = grupoInvestigacion.objects.all()
    return render(request,template_name='list_group.html',context={'group':group})

def list_titulo(request):
    titulo = TITULO.objects.all()
    return render(request,template_name='list_titulo.html',context={'titulo':titulo})

def list_espec(request):
    espec = ESPECIALIZACION.objects.all()
    return render(request,template_name='list_espec.html',context={'espec':espec})

def list_produc(request):
    produc = produccionCIENTFICA.objects.all()
    return render(request,template_name='list_produc.html',context={'produc':produc})

def list_resol(request):
    resol = RESOLUCION.objects.all()
    return render(request,template_name='list_resol.html',context={'resol':resol})

def list_eval(request):
    Eva = evaluacionyPerfeccionamiento.objects.all()
    return render(request,template_name='list_eval.html',context={'Eva':Eva})

def list_cargo(request):
    cargo = CARGO.objects.all()
    return render(request,template_name='list_cargo.html',context={'cargo':cargo})

#Aquí empieza el CreateView

class DocenteCreate(CreateView):
    model= DOCENTE
    form_class= DocenteForm
    template_name='add_docente.html'

    def get_success_url(self):
        return reverse('list_profesor')

class CursoCreate(CreateView):
    model = CURSO
    form_class = CursoForm
    template_name = 'add_curso.html'

    def get_success_url(self):
        return reverse('list_curso')

class InstitucionCreate(CreateView):
    model = INSTITUCION
    form_class = InstitucionForm
    template_name = 'add_institucion.html'

    def get_success_url(self):
        return reverse('list_institucion')

class EntidadCreate(CreateView):
    model = ENTIDAD
    form_class = EntidadForm
    template_name = 'add_entidad.html'

    def get_success_url(self):
        return reverse('list_entidad')

class expLaboralCreate(CreateView):
    model = experienciaLABORAL
    form_class = expLaboralForm
    template_name = 'add_explaboral.html'

    def get_success_url(self):
        return reverse('list_profesor')

class expDocenteCreate(CreateView):
    model = experienciaDOCENTE
    form_class = expDocenteForm
    template_name = 'add_expdocente.html'

    def get_success_url(self):
        return reverse('list_profesor')

class GroupCreate(CreateView):
    model = grupoInvestigacion
    form_class = GroupForm
    template_name = 'add_group.html'

    def get_success_url(self):
        return reverse('list_group')

class TituloCreate(CreateView):
    model = TITULO
    form_class = TituloForm
    template_name = 'add_titulo.html'

    def get_success_url(self):
        return reverse('list_profesor')


class EspecCreate(CreateView):
    model = ESPECIALIZACION
    form_class = EspecForm
    template_name = 'add_espec.html'

    def get_success_url(self):
        return reverse('list_profesor')

class ProducCreate(CreateView):
    model = produccionCIENTFICA
    form_class = ProducForm
    template_name = 'add_produc.html'

    def get_success_url(self):
        return reverse('list_produc')

class ResolCreate(CreateView):
    model = RESOLUCION
    form_class = ResolForm
    template_name = 'add_resol.html'

    def get_success_url(self):
        return reverse('list_profesor')

class EvalCreate(CreateView):
    model = evaluacionyPerfeccionamiento
    form_class = EvalForm
    template_name = 'add_eval.html'

    def get_success_url(self):
        return reverse('list_profesor')

class CargoCreate(CreateView):
    model = CARGO
    form_class = CargoForm
    template_name = 'add_cargo.html'

    def get_success_url(self):
        return reverse('list_profesor')

#Aquí empieza el UpdateView
class DocenteEdit(UpdateView):
    model = DOCENTE
    form_class = DocenteForm
    template_name = 'edit_docente.html'

    def get_success_url(self):
        return reverse('list_profesor')

class CursoEdit(UpdateView):
    model = CURSO
    form_class = CursoForm
    template_name = 'edit_curso.html'

    def get_success_url(self):
        return reverse('list_curso')

class InstitucionEdit(UpdateView):
    model = INSTITUCION
    form_class = InstitucionForm
    template_name = 'edit_institucion.html'

    def get_success_url(self):
        return reverse('list_institucion')

class EntidadEdit(UpdateView):
    model = ENTIDAD
    form_class = EntidadForm
    template_name = 'edit_entidad.html'

    def get_success_url(self):
        return reverse('list_entidad')

class ExpLaboralEdit(UpdateView):
    model = experienciaLABORAL
    form_class = expLaboralForm
    template_name = 'edit_explaboral.html'

    def get_success_url(self):
        return reverse('list_profesor')

class ExpDocenteEdit(UpdateView):
    model = experienciaDOCENTE
    form_class = expDocenteForm
    template_name = 'edit_expdocente.html'

    def get_success_url(self):
        return reverse('list_profesor')

class GroupEdit(UpdateView):
    model = grupoInvestigacion
    form_class = GroupForm
    template_name = 'edit_group.html'

    def get_success_url(self):
        return reverse('list_group')

class TituloEdit(UpdateView):
    model = TITULO
    form_class = TituloForm
    template_name = 'edit_titulo.html'

    def get_success_url(self):
        return reverse('list_titulo')

class EspecEdit(UpdateView):
    model = ESPECIALIZACION
    form_class = EspecForm
    template_name = 'edit_espec.html'

    def get_success_url(self):
        return reverse('list_espec')

class ProducEdit(UpdateView):
    model = produccionCIENTFICA
    form_class = ProducForm
    template_name = 'edit_produc.html'

    def get_success_url(self):
        return reverse('list_produc')

class ResolEdit(UpdateView):
    model = RESOLUCION
    form_class = ResolForm
    template_name = 'edit_resol.html'

    def get_success_url(self):
        return reverse('list_resol')

class EvalEdit(UpdateView):
    model = evaluacionyPerfeccionamiento
    form_class = EvalForm
    template_name = 'edit_eval.html'

    def get_success_url(self):
        return reverse('list_eval')

class CargoEdit(UpdateView):
    model = CARGO
    form_class = CargoForm
    template_name = 'edit_cargo.html'

    def get_success_url(self):
        return reverse('list_cargo')

#Aquí empieza el DeleteView
class DocenteDelete(DeleteView):
    model = DOCENTE
    form_class = DocenteForm
    template_name = 'delete_profesor.html'

    def get_context_data(self, **kwargs):
        context_data = super(DocenteDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        docente = DOCENTE.objects.get(id=int(pk))
        context_data.update({'docente': docente})
        return context_data

    def get_success_url(self):
        return reverse('list_profesor')

class CursoDelete(DeleteView):
    model = CURSO
    form_class = CursoForm
    template_name = 'delete_curso.html'

    def get_context_data(self, **kwargs):
        context_data = super(CursoDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        curso = CURSO.objects.get(id=int(pk))
        context_data.update({'curso': curso})
        return context_data

    def get_success_url(self):
        return reverse('list_curso')

class EntidadDelete(DeleteView):
    model = ENTIDAD
    form_class = EntidadForm
    template_name = 'delete_entidad.html'

    def get_context_data(self, **kwargs):
        context_data = super(EntidadDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        entidad = ENTIDAD.objects.get(id=int(pk))
        context_data.update({'entidad': entidad})
        return context_data

    def get_success_url(self):
        return reverse('list_entidad')

class EspecDelete(DeleteView):
    model = ESPECIALIZACION
    form_class = EspecForm
    template_name = 'delete_espec.html'

    def get_context_data(self, **kwargs):
        context_data = super(EspecDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        espec = ESPECIALIZACION.objects.get(id=int(pk))
        context_data.update({'espec': espec})
        return context_data

    def get_success_url(self):
        return reverse('list_espec')

class InstitucionDelete(DeleteView):
    model = INSTITUCION
    form_class = InstitucionForm
    template_name = 'delete_institucion.html'

    def get_context_data(self, **kwargs):
        context_data = super(InstitucionDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        institucion = INSTITUCION.objects.get(id=int(pk))
        context_data.update({'institucion': institucion})
        return context_data

    def get_success_url(self):
        return reverse('list_institucion')

class ExpDocenteDelete(DeleteView):
    model = experienciaDOCENTE
    form_class = expDocenteForm
    template_name = 'delete_expdocente.html'

    def get_context_data(self, **kwargs):
        context_data = super(ExpDocenteDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        expdocente = experienciaDOCENTE.objects.get(id=int(pk))
        context_data.update({'expdocente': expdocente})
        return context_data

    def get_success_url(self):
        return reverse('list_expdocente')

class ExpLaboralDelete(DeleteView):
    model = experienciaLABORAL
    form_class = expLaboralForm
    template_name = 'delete_explaboral.html'

    def get_context_data(self, **kwargs):
        context_data = super(ExpLaboralDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        explaboral = experienciaLABORAL.objects.get(id=int(pk))
        context_data.update({'explaboral': explaboral})
        return context_data

    def get_success_url(self):
        return reverse('list_explaboral')

class GroupDelete(DeleteView):
    model = grupoInvestigacion
    form_class = GroupForm
    template_name = 'delete_group.html'

    def get_context_data(self, **kwargs):
        context_data = super(GroupDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        group = grupoInvestigacion.objects.get(id=int(pk))
        context_data.update({'group': group})
        return context_data

    def get_success_url(self):
        return reverse('list_group')

class TituloDelete(DeleteView):
    model = TITULO
    form_class = TituloForm
    template_name = 'delete_titulo.html'

    def get_context_data(self, **kwargs):
        context_data = super(TituloDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        titulo = TITULO.objects.get(id=int(pk))
        context_data.update({'titulo': titulo})
        return context_data

    def get_success_url(self):
        return reverse('list_titulo')

class ProducDelete(DeleteView):
    model = produccionCIENTFICA
    form_class = ProducForm
    template_name = 'delete_produc.html'

    def get_context_data(self, **kwargs):
        context_data = super(ProducDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        produc = produccionCIENTFICA.objects.get(id=int(pk))
        context_data.update({'produc': produc})
        return context_data

    def get_success_url(self):
        return reverse('list_produc')

class ResolDelete(DeleteView):
    model = RESOLUCION
    form_class = ResolForm
    template_name = 'delete_resol.html'

    def get_context_data(self, **kwargs):
        context_data = super(ResolDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        resol = RESOLUCION.objects.get(id=int(pk))
        context_data.update({'resol': resol})
        return context_data

    def get_success_url(self):
        return reverse('list_resol')

class EvalDelete(DeleteView):
    model = evaluacionyPerfeccionamiento
    form_class = EvalForm
    template_name = 'delete_eval.html'

    def get_context_data(self, **kwargs):
        context_data = super(EvalDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        eva = evaluacionyPerfeccionamiento.objects.get(id=int(pk))
        context_data.update({'eva': eva})
        return context_data

    def get_success_url(self):
        return reverse('list_eval')

class CargoDelete(DeleteView):
    model = CARGO
    form_class = CargoForm
    template_name = 'delete_cargo.html'

    def get_context_data(self, **kwargs):
        context_data = super(CargoDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        cargo = CARGO.objects.get(id=int(pk))
        context_data.update({'cargo': cargo})
        return context_data

    def get_success_url(self):
        return reverse('list_cargo')