def calculo (basemaior,basemenor,alt):
    area = (basemaior+basemenor)*alt/2
    
    return area

basemaior = float (input ("Digite Quantos m² Tem A Base Maior Do Trapézio: " ))
basemenor = float (input ("Digite Quantos m² Tem A Base Menor Do Trapézio: " ))
alt = float (input ("Digite Quantos m² Tem A Altura Do Trapézio: " ))

print (f"Área: {calculo (basemaior,basemenor,alt) } m²")
