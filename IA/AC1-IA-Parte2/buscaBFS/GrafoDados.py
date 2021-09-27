#conexoes entre pontos
conexoes = {}

conexoes["Casa"] = {"Santo Amaro"}
conexoes["Santo Amaro"] = {"Pinheiros","Santa Cruz"}
conexoes["Santa Cruz"] = {"Santo Amaro", "Sé"}
conexoes["Pinheiros"] = {"República", "Luz","Presidente Altino"}
conexoes["Presidente Altino"] = {"Barra Funda"}
conexoes["República"] = {"Barra Funda"}
conexoes["Luz"] = {"Sé"}
conexoes["Sé"] = {"Barra Funda"}
conexoes["Barra Funda"] = {"Impacta"}
conexoes["Impacta"] = {"Barra Funda"}

#localização de todos os lugares 

localizacao = {}
localizacao["Casa"] = [2,8]
localizacao["Santo Amaro"] = [7,2]
localizacao["Santa Cruz"] = [4,5]
localizacao["Presidente Altino"]=[1,4]
localizacao["Pinheiros"] = [2,6]
localizacao["República"] = [2,5]
localizacao["Luz"] = [3,5]
localizacao["Sé"] = [4,4]
localizacao["Barra Funda"] = [2,4]
localizacao["Impacta"] = [2,3]

