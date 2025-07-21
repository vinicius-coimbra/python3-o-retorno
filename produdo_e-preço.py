produdo_e_preço = ('alho', 2.21 , "notbook", 1000.500 ,
    'labis' , 32 , 'estojo' , 3.50 , 'mochila' , 32.32 ,
    'livro' , 56.70 , 'rtx4050' , 4000.60 , 'xbox' , 1800,
    'enden ring' , 400 )
lugar_do_VALO = 1
lugar_do_PRODUTO = 0 
print('-' * 40)
print(f'{'produtos': ^40}')
print('-' * 40)

for lista in range(9):
    print(f"{produdo_e_preço[lugar_do_PRODUTO]:.<40} R$ {produdo_e_preço[lugar_do_VALO]:.2f}")
    lugar_do_PRODUTO += 2
    lugar_do_VALO += 2
print('-' * 40)