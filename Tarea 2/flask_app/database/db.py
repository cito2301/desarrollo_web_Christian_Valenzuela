from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "root"
DB_PASSWORD = "vivadbz23V" 
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)
      
class Aviso(Base):
    __tablename__ = "aviso_adopcion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_ingreso = Column(DateTime)
    comuna_id = Column(Integer)
    sector = Column(String(100))
    nombre = Column(String(200))
    email = Column(String(100))
    celular = Column(String(15))
    tipo = Column(String(10))
    cantidad = Column(Integer)
    edad = Column(Integer)
    unidad_medida = Column(String(1))
    fecha_entrega = Column(DateTime)
    descripcion = Column(String(500))

def get_all_avisos(limit=5):
    session = SessionLocal()
    avisos = session.query(Aviso).order_by(Aviso.fecha_ingreso.desc()).limit(limit).all()
    session.close()
    return avisos

def create_aviso(**kwargs):
    session = SessionLocal()
    aviso = Aviso(**kwargs)
    session.add(aviso)
    session.commit()
    session.close()

def get_regions():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["select_regiones"])
    regiones = cursor.fetchall()
    conn.close()
    return regiones

def get_comunas_by_region(region_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["select_comunas_by_region"], (region_id,))
    comunas = cursor.fetchall()
    conn.close()
    return comunas

def get_all_comunas():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, region_id FROM comuna ORDER BY nombre")
    comunas = cursor.fetchall()
    conn.close()
    return comunas