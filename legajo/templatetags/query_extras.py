from django import template
from legajo.models import * 

register = template.Library()

@register.filter
def docentes(value,arg): 
	return CURSO.objects.filter(docentes__id=arg) 
@register.filter
def explaboral(value,arg): 
	return experienciaLABORAL.objects.filter(docentes__id=arg) 
@register.filter
def expdocente(value,arg): 
	return experienciaDOCENTE.objects.filter(docente__id=arg) 
@register.filter
def group(value,arg): 
	return grupoInvestigacion.objects.filter(docentes__id=arg) 
@register.filter
def titulo(value,arg): 
	return TITULO.objects.filter(docente__id=arg) 
@register.filter
def espec(value,arg): 
	return ESPECIALIZACION.objects.filter(docente__id=arg) 
@register.filter
def produc(value,arg): 
	return produccionCIENTFICA.objects.filter(docentes__id=arg) 
@register.filter
def eval(value,arg): 
	return evaluacionyPerfeccionamiento.objects.filter(docentes__id=arg)
@register.filter
def cargo(value,arg): 
	return CARGO.objects.filter(docente__id=arg)  