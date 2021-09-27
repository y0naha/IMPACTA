# Criar um dicionário com todos os mapeamentos

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