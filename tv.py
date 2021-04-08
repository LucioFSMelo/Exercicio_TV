"""
Criar uma classe TV, onde terá três atributos:
1) Power
2) Audio
3) Canais

O Power, será responsável por ligar e desligar a TV.

A tecla_volume + irá incrementar de uma unidade o volume.
Já a tecla_volume -, vai decrementar de uma unidade o volume.

A tecla_canal terá a mesma ação do vulome (incrementar e decrementar)

    Exemplo:
    >>> # Testando o Power
    >>> power = Power()
    >>> power.status
    'Desligado'
    >>> power.tecla_power()
    >>> power.status
    'Ligado'
    >>> power.tecla_power()
    >>> power.status
    'Desligado'
    >>> # Testando o Audio
    >>> audio = Audio()
    >>> audio.volume
    0
    >>> audio.tecla_volume_mais()
    >>> audio.volume
    1
    >>> audio.tecla_volume_mais()
    >>> audio.volume
    2
    >>> audio.tecla_volume_menos()
    >>> audio.volume
    1
    >>> audio.tecla_volume_menos()
    >>> audio.volume
    0
    >>> # Tentando Canais
    >>> canais = Canais()
    >>> canais.canal
    '2 - Sbt'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '4 - Record'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '6 - Rede TV'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '7 - Loading'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '9 - Band'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '11 - TV Universitária'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '13 - Globo'
    >>> canais.tecla_canal_mais()
    >>> canais.canal
    '2 - Sbt'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '13 - Globo'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '11 - TV Universitária'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '9 - Band'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '7 - Loading'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '6 - Rede TV'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '4 - Record'
    >>> canais.tecla_canal_menos()
    >>> canais.canal
    '2 - Sbt'
    >>> tv = Televisao(power, audio, canais)
    >>> tv.status_power()
    'Desligado'
    >>> tv.tecla_power()
    >>> tv.status_power()
    'Ligado'
    >>> tv.tecla_power()
    >>> tv.status_power()
    'Desligado'
    >>> tv.som()
    0
    >>> tv.tecla_volume_mais()
    >>> tv.som()
    1
    >>> tv.tecla_volume_mais()
    >>> tv.som()
    2
    >>> tv.tecla_volume_menos()
    >>> tv.som()
    1
    >>> tv.sintonia()
    '2 - Sbt'
    >>> tv.tecla_canal_mais()
    >>> tv.sintonia()
    '4 - Record'
    >>> tv.tecla_canal_menos()
    >>> tv.sintonia()
    '2 - Sbt'
    >>> tv.tecla_canal_menos()
    >>> tv.sintonia()
    '13 - Globo'
"""

