from sqlalchemy import select

session = Session(engine)

stmt = select(Game).where(Game.name.in_([name]))

for Game in session.scalars(stmt):
    print(Game)