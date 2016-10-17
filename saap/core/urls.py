# coding=utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (CadastroView, DeletarContatoView, ContatoView, TicketView,
                    AtualizaContato, VereadoresView, PublicarTicketView,
                    DeletarTicketView, GerarCartaView, CartasView,
<<<<<<< HEAD
                    DeletarCartaView, GerarPDFCartaView, EnviarCartaView,
                    BuscaContatosView, CriarGrupoDeContatosView, 
<<<<<<< HEAD
                    AdicionarContatoAoGrupo,GrupoDeContatosView,
                    GrupoDeContatosView, CriarGrupoDeContatosView,
                    BuscaContatosView, CriarGrupoDeContatosView)
=======
                    AdicionarContatoAoGrupo)
>>>>>>> Metodo para adicionar contatos a um grupo
=======
                    DeletarCartaView, GerarPDFCartaView, EnviarCartaView, OficioView,
                    DeletarOficioView, GerarOficioView, GerarPDFOficioView, EnviarOficioView)
>>>>>>> Enviar oficio

urlpatterns = [
    url(r'^cadastro_contato/$', login_required(CadastroView.as_view()),
        name='cadastro_contato'),
    url(r'^exclui_contato/$', login_required(DeletarContatoView.as_view()),
        name='exclui_contato'),
    url(r'^contato/$', login_required(ContatoView.as_view()),
        name='contato'),
    url(r'^atualiza_contato/$', login_required(AtualizaContato.as_view()),
        name='atualiza_contato'),
    url(r'^ticket/$', TicketView.as_view(),
        name='ticket'),
    url(r'^publicar_ticket/$', PublicarTicketView.as_view(),
        name='publicar_ticket'),
    url(r'^deletar_ticket/(?P<pk>[0-9]+)/$', DeletarTicketView.as_view(),
        name='deletar_ticket'),
    url(r'^vereadores/$', VereadoresView.as_view(),
        name='vereadores'),
    url(r'^gerar_carta/$', login_required(GerarCartaView.as_view()),
        name='gerar_carta'),
    url(r'^cartas/$', login_required(CartasView.as_view()),
        name='cartas'),
    url(r'^deletar_carta/(?P<pk>[0-9]+)/$', login_required(DeletarCartaView.as_view()),
        name='deletar_carta'),
    url(r'^gerar_pdf/(?P<pk>[0-9]+)/$', login_required(GerarPDFCartaView.as_view()),
        name='gerar_pdf'),
    url(r'^enviar_carta/(?P<pk>[0-9]+)/$', login_required(EnviarCartaView.as_view()),
        name='enviar_carta'),
    url(r'^criar_grupo/$', CriarGrupoDeContatosView.as_view(),
        name='criar_grupo'),
     url(r'^busca_contatos/$', BuscaContatosView.as_view(),
        name='busca_contatos'),
     url(r'^adicionar_contatos/$', AdicionarContatoAoGrupo.as_view(),
        name='adicionar_contatos'),
    url(r'^grupo_contatos/$', GrupoDeContatosView.as_view(),
        name='grupo_contatos'),
    url(r'^criar_grupo/$', CriarGrupoDeContatosView.as_view(),
        name='criar_grupo'),
    url(r'^gerar_oficio/$', GerarOficioView.as_view(),
        name = 'gerar_oficio'),
    url(r'^deletar_oficio/(?P<pk>[0-9]+)/$', DeletarOficioView.as_view(),
        name='deletar_oficio'),
        url(r'^gerar_oficio_pdf/(?P<pk>[0-9]+)/$', login_required(GerarPDFOficioView.as_view()),
        name='gerar_oficio_pdf'),
    url(r'^enviar_oficio/(?P<pk>[0-9]+)/$', login_required(EnviarOficioView.as_view()),
        name='enviar_oficio'),
    url(r'^oficio/$', OficioView.as_view(),
    name='oficio')
]
