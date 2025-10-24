from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql
import json
from datetime import datetime
import os

DB_NAME = "tarea2"
DB_USERNAME = "root"
DB_PASSWORD = "vivadbz23V" 
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'querys.json'), 'r', encoding='utf-8') as f:
    QUERY_DICT = json.load(f)

def get_conn():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        db=DB_NAME,
        port=DB_PORT,
        charset=DB_CHARSET,
        cursorclass=pymysql.cursors.Cursor,
        autocommit=False
    )
    return conn

def insert_aviso(fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["insert_aviso"], (fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion))
    aviso_id = cur.lastrowid
    conn.commit()
    cur.close()
    conn.close()
    return aviso_id

def insert_foto(ruta, nombre_arch, aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["insert_foto"], (ruta, nombre_arch, aviso_id))
    conn.commit()
    cur.close()
    conn.close()

def insert_contactar(nombre, identificador, aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["insert_contactar_por"], (nombre, identificador, aviso_id))
    conn.commit()
    cur.close()
    conn.close()

def get_last_avisos(limit=5):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_last_avisos"], (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_avisos_paginated(limit, offset):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_avisos_paginated"], (limit, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_aviso_by_id(aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_aviso_by_id"], (aviso_id,))
    aviso = cur.fetchone()
    cur.close()
    conn.close()
    return aviso

def get_fotos(aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_fotos_by_aviso"], (aviso_id,))
    fotos = cur.fetchall()
    cur.close()
    conn.close()
    return fotos

def get_contactos(aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_contactos_by_aviso"], (aviso_id,))
    contacts = cur.fetchall()
    cur.close()
    conn.close()
    return contacts

def insert_comment(nombre, texto, fecha, aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["insert_comment"], (nombre, texto, fecha, aviso_id))
    conn.commit()
    cur.close()
    conn.close()

def get_comments(aviso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_comments_by_aviso"], (aviso_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_regions():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_regions"])
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_comunas():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["get_comunas"])
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def stats_avisos_por_dia():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["stats_avisos_por_dia"])
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def stats_por_tipo():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["stats_por_tipo"])
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def stats_por_mes_tipo():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(QUERY_DICT["stats_por_mes_tipo"])
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows