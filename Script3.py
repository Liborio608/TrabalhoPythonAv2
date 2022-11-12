def soma_imposto (taxa_imp, custo):
    return (1 + taxa_imp/100)*custo

taxa = float(input( "Digite A Taxa De Impostos: " ))
custo = float(input( "Digite O Custo Do Produto: " ))

print( "Valor Do Produto Com Imposto é R$:" , soma_imposto ( taxa, custo))