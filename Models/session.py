from sqlalchemy.orm import Session

with Session(engine) as session:

    DEAD SPACE REMAKE = Game(
        id = '1',
        nome = 'DEAD SPACE REMAKE',
        plataforma = 'PS5',
        preco = 'R$350,00',
        quantidade = '10'
    )
    FORSPOKEN = Game(
        id = '2',
        nome = 'FORSPOKEN',
        plataforma = 'PC',
        preco = 'R$299,00',
        quantidade = '8'
    )
    DEAD ISLAND 2  = Game(
        id = '3',
        nome = 'DEAD ISLAND 2 ',
        plataforma = 'PS5',
        preco = 'R$350,00',
        quantidade = '10'
    )
    HOGWARTS LEGACY = Game(
        id = '4',
        nome = 'HOGWARTS LEGACY',
        plataforma = 'PC',
        preco = 'R$219,00',
        quantidade = '7'
    )
    WILD HEARTS = Game(
        id = '5',
        nome = 'WILD HEARTS',
        plataforma = 'XBox Series',
        preco = 'R$350,00',
        quantidade = '7'
    )
    RESIDENT EVIL 4  = Game(
        id = '6',
        nome = 'RESIDENT EVIL 4 ', 
        plataforma = 'PC',
        preco = 'R$289,00',
        quantidade = '10'
    )
    THE LEGEND OF ZELDA: TEARS OF THE KINGDOM = Game(
        id = '7',
        nome = 'THE LEGEND OF ZELDA: TEARS OF THE KINGDOM',
        plataforma = 'PS5',
        preco = 'R$289,00',
        quantidade = '10'
    )

session.add_all([DEAD SPACE REMAKE, FORSPOKEN, DEAD ISLAND 2, HOGWARTS LEGACY, WILD HEARTS,  RESIDENT EVIL 4, THE LEGEND OF ZELDA: TEARS OF THE KINGDOM])
session.commit()