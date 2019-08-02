from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('index',views.index,name='index'),
    path('list_profesor',views.list_profesor,name='list_profesor'),
    path('list_curso',views.list_curso,name='list_curso'),
    path('list_expdocente',views.list_expdocente,name='list_expdocente'),
    path('list_institucion',views.list_institucion,name='list_institucion'),
    path('list_explaboral',views.list_explaboral,name='list_explaboral'),
    path('list_entidad',views.list_entidad,name='list_entidad'),
    path('list_group',views.list_group,name='list_group'),
    path('list_titulo',views.list_titulo,name='list_titulo'),
    path('list_espec',views.list_espec,name='list_espec'),
    path('list_produc',views.list_produc,name='list_produc'),
    path('list_resol',views.list_resol,name='list_resol'),
    path('list_eval',views.list_eval,name='list_eval'),
    path('list_cargo',views.list_cargo,name='list_cargo'),
    #CreateView
    path('add_docente',views.DocenteCreate.as_view(),name='add_docente'),
    path('add_curso',views.CursoCreate.as_view(),name='add_curso'),
    path('add_institucion',views.InstitucionCreate.as_view(),name='add_institucion'),
    path('add_entidad',views.EntidadCreate.as_view(),name='add_entidad'),
    path('add_explaboral',views.expLaboralCreate.as_view(),name='add_explaboral'),
    path('add_expdocente',views.expDocenteCreate.as_view(),name='add_expdocente'),
    path('add_group',views.GroupCreate.as_view(),name='add_group'),
    path('add_titulo',views.TituloCreate.as_view(),name='add_titulo'),
    path('add_espec', views.EspecCreate.as_view(), name='add_espec'),
    path('add_produc', views.ProducCreate.as_view(), name='add_produc'),
    path('add_resol', views.ResolCreate.as_view(), name='add_resol'),
    path('add_eval', views.EvalCreate.as_view(), name='add_eval'),
    path('add_cargo', views.CargoCreate.as_view(), name='add_cargo'),
    #UpdateView
    url(r'edit_profesor/(?P<pk>\d+)/$',views.DocenteEdit.as_view(),name='edit_profesor') ,
    url(r'edit_curso/(?P<pk>\d+)/$',views.CursoEdit.as_view(),name='edit_curso') ,
    url(r'edit_institucion/(?P<pk>\d+)/$',views.InstitucionEdit.as_view(),name='edit_institucion') ,
    url(r'edit_entidad/(?P<pk>\d+)/$',views.EntidadEdit.as_view(),name='edit_entidad') ,
    url(r'edit_explaboral/(?P<pk>\d+)/$',views.ExpLaboralEdit.as_view(),name='edit_explaboral'),
    url(r'edit_expdocente/(?P<pk>\d+)/$',views.ExpDocenteEdit.as_view(),name='edit_expdocente'),
    url(r'edit_group/(?P<pk>\d+)/$',views.GroupEdit.as_view(),name='edit_group'),
    url(r'edit_titulo/(?P<pk>\d+)/$',views.TituloEdit.as_view(),name='edit_titulo'),
    url(r'edit_espec/(?P<pk>\d+)/$',views.EspecEdit.as_view(),name='edit_espec'),
    url(r'edit_produc/(?P<pk>\d+)/$',views.ProducEdit.as_view(),name='edit_produc'),
    url(r'edit_resol/(?P<pk>\d+)/$',views.ResolEdit.as_view(),name='edit_resol'),
    url(r'edit_eval/(?P<pk>\d+)/$',views.EvalEdit.as_view(),name='edit_eval'),
    url(r'edit_cargo/(?P<pk>\d+)/$',views.CargoEdit.as_view(),name='edit_cargo'),
    #DeleteView
    url(r'delete_profesor/(?P<pk>\d+)/$',views.DocenteDelete.as_view(),name='delete_profesor'),
    url(r'delete_curso/(?P<pk>\d+)/$',views.CursoDelete.as_view(),name='delete_curso'),
    url(r'delete_entidad/(?P<pk>\d+)/$',views.EntidadDelete.as_view(),name='delete_entidad'),
    url(r'delete_espec/(?P<pk>\d+)/$',views.EspecDelete.as_view(),name='delete_espec'),
    url(r'delete_institucion/(?P<pk>\d+)/$',views.InstitucionDelete.as_view(),name='delete_institucion'),
    url(r'delete_expdocente/(?P<pk>\d+)/$',views.ExpDocenteDelete.as_view(),name='delete_expdocente'),
    url(r'delete_explaboral/(?P<pk>\d+)/$',views.ExpLaboralDelete.as_view(),name='delete_explaboral'),
    url(r'delete_group/(?P<pk>\d+)/$',views.GroupDelete.as_view(),name='delete_group'),
    url(r'delete_titulo/(?P<pk>\d+)/$',views.TituloDelete.as_view(),name='delete_titulo'),
    url(r'delete_produc/(?P<pk>\d+)/$',views.ProducDelete.as_view(),name='delete_produc'),
    url(r'delete_resol/(?P<pk>\d+)/$',views.ResolDelete.as_view(),name='delete_resol'),
    url(r'delete_eval/(?P<pk>\d+)/$',views.EvalDelete.as_view(),name='delete_eval'),
    url(r'delete_cargo/(?P<pk>\d+)/$',views.CargoDelete.as_view(),name='delete_cargo'),

]