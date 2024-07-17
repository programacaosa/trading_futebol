import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime, date
from io import BytesIO

def drop_reset_index(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    df.index += 1
    return df

def ajustar_id_mercado(id_mercado, comprimento_decimal_desejado=9):
    id_mercado_str = str(id_mercado)
    partes = id_mercado_str.split('.')
    if len(partes) == 1:
        return id_mercado_str + '.' + '0' * comprimento_decimal_desejado
    parte_inteira, parte_decimal = partes
    zeros_para_adicionar = comprimento_decimal_desejado - len(parte_decimal)
    if zeros_para_adicionar > 0:
        parte_decimal += '0' * zeros_para_adicionar
    id_mercado_ajustado = parte_inteira + '.' + parte_decimal
    return id_mercado_ajustado