palavra_correta = input('Informe uma palavra: ')
letra_acertada = ''
numero_tentativas = 0

while True:
    print('Adivinhe a palavra?')

    palpite = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(palpite) > 1:
        print('Digite apenas uma letra por vez!')
        continue    
    
    if palpite in palavra_correta: 
        letra_acertada += palpite
 
    palavra_formada = ''
    for letra_secreta in palavra_correta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta            
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_correta:
        print('ACERTOOOOOOOOUUU!!')
        print('A palavra é', palavra_correta) 
        print('Tentativas: ', numero_tentativas)
        letra_acertada = ''
        numero_tentativas = 0
        break