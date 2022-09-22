tarifas = """Tarifas de paso en un peaje:
pago por vehículo ligero: 100
pago por vehículo mediano: 200
pago por vehículo grande: 300"""
print(tarifas)
ValLig = 100
ValMed = 200
ValGra = 300
VehLig = int(input('cantidad de vehiculos ligeros que pagaron el peaje :'))
VehMed = int(input('cantidad de vehiculos medianos que pagaron el peaje :' ))
VehGra = int(input('cantidad de vehiculos grandes que pagaron el peaje :'))
Total = (ValLig * VehLig) + (ValMed * VehMed) + (ValGra * VehGra)
print('el recaudo total de los pagos del peaje fue de 'f'{Total}')
