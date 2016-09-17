from get_urls.model.Proyecto import *

unProyecto = Proyecto()
unaConsulta = []
unaConsulta.append(raw_input('Consulta: '))
unProyecto.generarUrl(unaConsulta)
data = unProyecto.generarMensajeJsonUrls()
for buscador in data['buscadores']:
    print buscador['buscador']
    for index,url in enumerate(buscador['urls']):
        if index < 20:
            print url['url']
