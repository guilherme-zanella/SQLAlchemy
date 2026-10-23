from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine('sqlite:///banco.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Tabelas:

class Usuario(Base): 
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = 'livros'

    id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)
    titulo = Column('titulo', String)
    qtd_paginas = Column('qtd_paginas', Integer)
    dono =  Column('dono', ForeignKey('usuarios.id'))

    def __init__(self, titulo, qtd_paginas, dono):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

# CRUD

# C - create
# usuario = Usuario(nome='Manuela', email='manu@gmail.com', senha='321')
# session.add(usuario)
# session.commit()

# R - read
# lista_usuarios = session.query(Usuario).all()
read_usuario = session.query(Usuario).filter_by(id=3).first()


# livro = Livro(titulo='Turma da Mônica', qtd_paginas=30, dono=read_usuario.id)
# session.add(livro)
# session.commit()

# U - update
# read_usuario.nome = 'Manuela Zanella'
# session.add(read_usuario)
# session.commit()

# D - delete
# session.delete(read_usuario)
# session.commit()
