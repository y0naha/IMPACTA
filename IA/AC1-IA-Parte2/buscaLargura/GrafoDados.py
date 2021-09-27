# Criar um dicionário com todos os mapeamentos

conexoes = {}

conexoes["Casa"] = {"Santo Amaro"}
conexoes["Santo Amaro"] = {"Casa", "Pinheiros","Santa Cruz"}
conexoes["Santa Cruz"] = {"Santo Amaro", "Sé"}
conexoes["Pinheiros"] = {"Santo Amaro", "República", "Luz"}
conexoes["Presidente Altino"] = ["Barra Funda","Pinheiros"]
conexoes["República"] = {"Pinheiros", "Barra Funda"}
conexoes["Luz"] = {"Pinheiros", "Sé"}
conexoes["Sé"] = {"Luz", "Barra Funda"}
conexoes["Barra Funda"] = {"República", "Sé", "Impacta"}
conexoes["Impacta"] = {"Barra Funda"}
