times = 'Flamengo', 'Cruzeiro', 'Red Bull', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense' ,'Atlético Mineiro' ,'Botafogo' ,'Mirassol' ,'Corinthians' ,'Grêmio', 'Ceará' ,'Vasco da Gama', 'São Paulo' ,'Santos' ,'Vitória' ,'Internacional' ,'Fortaleza' ,'Juventude', 'Sport'
print(20*'-' +
    '\nPrimeiros 4 times:')
print(times[0:4])
print(20*'-' +
    '\nUltimos 4 times:')
print(times[-1:-5:-1])
print(20*'-' +
    '\nTimes em ordem:')
print(sorted(times))
print(20 *'-' +
    '\nPossiçao do Botafogo:')
print('O time',times[times.index('Botafogo')],'esta na possiçao', times.index('Botafogo'))