import requests


def consulta_cep():
    cep_informado = input('Por favor, informe seu CEP: ')  # Solicitando o CEP ao usuário

    dados_cep = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_informado))
    dados_cep = dados_cep.json()

    print('\nCEP Informado: {}.\n'.format(cep_informado))  # Mostrando CEP informado

    # Mostrando dados do CEP ao usuário
    print('Rua/Av.: {}'.format(dados_cep['logradouro']))
    print('Bairro: {}'.format(dados_cep['bairro']))
    print('Cidade: {}'.format(dados_cep['localidade']))
    print('Estado: {}'.format(dados_cep['uf']))


if __name__ == '__main__':
    consulta_cep()
