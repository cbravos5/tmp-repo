import os
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date, datetime  # Settings as shown in docker-compose.yml
engine = create_engine(
    'postgresql://postgres:postgres@localhost:5433/postgres')
Session = sessionmaker(bind=engine)
Base = declarative_base()
# from base import Base


class Ala(Base):
    __tablename__ = 'alas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    # relations
    setores = relationship("Setor", back_populates="ala")

    def __init__(self, nome):
        self.nome = nome


class Setor(Base):
    __tablename__ = 'setores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    # relations
    alaId = Column(Integer, ForeignKey('alas.id'))
    ala = relationship("Ala", back_populates="setores")
    unidades = relationship("Unidade", back_populates="setor")

    def __init__(self, nome, ala):
        self.nome = nome
        self.ala = ala


class TipoLeito(Base):
    __tablename__ = 'tipos_leito'

    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    # relations
    leitos = relationship("Leito", back_populates="tipo")
    unidades = relationship("Unidade", back_populates="tipo")

    def __init__(self, tipo):
        self.tipo = tipo


class Leito(Base):
    __tablename__ = 'leitos'

    id = Column(Integer, primary_key=True)
    disponibilidade = Column(String, nullable=False, default='desocupado')
    # relations
    tipoId = Column(Integer, ForeignKey('tipos_leito.id'))
    tipo = relationship("TipoLeito", back_populates="leitos")
    internacao = relationship(
        "Internacao", back_populates="leito", uselist=False)

    def __init__(self, tipo):
        self.tipo = tipo


class Unidade(Base):
    __tablename__ = 'unidades'

    id = Column(Integer, primary_key=True)
    andar = Column(Integer)
    # relations
    tipoId = Column(Integer, ForeignKey('tipos_leito.id'))
    tipo = relationship("TipoLeito", back_populates="unidades")
    setorId = Column(Integer, ForeignKey('setores.id'))
    setor = relationship("Setor", back_populates="unidades")
    solicitacoes = relationship("Solicitacao", back_populates="unidade")
    equipesMedicas = relationship("EquipeMedica", back_populates="unidade")

    def __init__(self, andar, tipo, setor):
        self.andar = andar
        self.tipo = tipo
        self.setor = setor


class Internacao(Base):
    __tablename__ = 'internacoes'

    id = Column(Integer, primary_key=True)
    dataInicio = Column(Date, default=datetime.now())
    status = Column(String, nullable=True)
    motivoEncerramento = Column(String, nullable=True)
    dataPrevistaLiberacao = Column(String, nullable=True)
    # relations
    leitoId = Column(Integer, ForeignKey('leitos.id'))
    leito = relationship("Leito", back_populates="internacao")
    acoesRecomendadas = relationship(
        "AcaoRecomendada", back_populates="internacao")
    paciente = relationship(
        "Paciente", back_populates="internacao", uselist=False)

    def __init__(self, leito):
        self.leito = leito


class AcaoRecomendada(Base):
    __tablename__ = 'acoes_recomendadas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    # relations
    internacaoId = Column(Integer, ForeignKey('internacoes.id'))
    internacao = relationship("Internacao", back_populates="acoesRecomendadas")

    def __init__(self, descricao, internacao):
        self.descricao = descricao
        self.internacao = internacao


class Urgencia(Base):
    __tablename__ = 'urgencias'

    id = Column(Integer, primary_key=True)
    urgencia = Column(String, nullable=False)
    # relations
    solicitacoes = relationship("Solicitacao", back_populates="urgencia")

    def __init__(self, urgencia):
        self.urgencia = urgencia


class Solicitacao(Base):
    __tablename__ = 'solicitacoes'

    id = Column(Integer, primary_key=True)
    # relations
    urgenciaId = Column(Integer, ForeignKey('urgencias.id'))
    urgencia = relationship("Urgencia", back_populates="solicitacoes")
    unidadeId = Column(Integer, ForeignKey('unidades.id'))
    unidade = relationship("Unidade", back_populates="solicitacoes")
    paciente = relationship(
        "Paciente", back_populates="solicitacao", uselist=False)

    def __init__(self, unidade, urgencia):
        self.unidade = unidade
        self.urgencia = urgencia


class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    contato = Column(String)
    # relations
    internacaoId = Column(Integer, ForeignKey('internacoes.id'))
    internacao = relationship("Internacao", back_populates="paciente")
    solicitacaoId = Column(Integer, ForeignKey('solicitacoes.id'))
    solicitacao = relationship("Solicitacao", back_populates="paciente")

    def __init__(self, nome, cpf, contato):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato


class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    contato = Column(String)
    cargo = Column(String)
    setorTrabalho = Column(String)
    # relations
    equipeMedicaId = Column(Integer, ForeignKey('equipes_medicas.id'))
    equipeMedica = relationship("EquipeMedica", back_populates="funcionarios")

    def __init__(self, nome, cpf, contato, cargo, setorTrabalho):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.cargo = cargo
        self.setorTrabalho = setorTrabalho


class EquipeMedica(Base):
    __tablename__ = 'equipes_medicas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    chefia = Column(String)
    # relations
    funcionarios = relationship("Funcionario", back_populates="equipeMedica")
    unidadeId = Column(Integer, ForeignKey('unidades.id'))
    unidade = relationship("Unidade", back_populates="equipesMedicas")
    turno = relationship("Turno", back_populates="equipeMedica", uselist=False)

    def __init__(self, nome, chefia, unidade, turno):
        self.nome = nome
        self.chefia = chefia
        self.unidade = unidade
        self.turno = turno


class Turno(Base):
    __tablename__ = 'turnos'

    id = Column(Integer, primary_key=True)
    horaInicio = Column(Date)
    horaTermino = Column(Date)
    escala = Column(String)
    # relations
    equipeMedicaId = Column(Integer, ForeignKey('equipes_medicas.id'))
    equipeMedica = relationship("EquipeMedica", back_populates="turno")

    def __init__(self, horaInicio, horaTermino, escala, equipeMedica):
        self.horaInicio = horaInicio
        self.horaTermino = horaTermino
        self.escala = escala
        self.equipeMedica = equipeMedica


if(os.environ.get('ENV') == 'commit'):
    Base.metadata.create_all(engine)
    print('Tables created successfully')


session = Session()
