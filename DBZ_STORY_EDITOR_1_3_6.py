import base64
import csv
import io
import json
import math
import os
import re
import struct
import sys
import traceback
import tkinter as tk
from pathlib import Path
from tkinter import colorchooser, filedialog, messagebox, ttk

# --- DICCIONARIOS DE BT3 DE LA HERRAMIENTA 1 ---

BGMS = {
    "0": "000 - The Meteor",
    "1": "001 - Vital Burner",
    "2": "002 - Innocent World",
    "3": "003 - After The Fire",
    "4": "004 - Sweet Vibration",
    "5": "005 - Survive",
    "6": "006 - Heat Capacity",
    "7": "007 - Overture",
    "8": "008 - Shine",
    "9": "009 - Power Scale",
    "10": "010 - Edge of Spirit",
    "11": "011 - Caution!",
    "12": "012 - Menace",
    "13": "013 - Hot Soul",
    "14": "014 - High And Scream",
    "15": "015 - Shootout in Meteor",
    "16": "016 - Dynamite Battle",
    "17": "017 - Burnin' Up",
    "18": "018 - Wild Rush",
    "19": "019 - Evolution",
    "20": "020 - Super Survivor Full ver.",
    "21": "021 - Super Survivor Short ver.",
    "22": "022 - Super Survivor Instrumental Full ver.",
    "23": "023 - Super Survivor Instrumental Short ver.",
}

MAPS = {
    "0": "00 - Tierra baldía - Mediodía",
    "1": "01 - Zona rocosa - Mediodía",
    "2": "02 - Planeta Namek",
    "3": "03 - Namek moribundo",
    "4": "04 - Escenario del Torneo Mundial - Mediodía",
    "5": "05 - Torre de Karin",
    "6": "06 - Arena de los Juegos de Cell - Atardecer",
    "7": "07 - Mundo del Supremo Kai",
    "8": "08 - Sala del Tiempo",
    "9": "09 - Ruinas de la ciudad - Mediodía",
    "10": "10 - Camino montañoso - Mediodía",
    "11": "11 - Islas",
    "12": "12 - Casa Kame",
    "13": "13 - Planeta - Noche",
    "14": "14 - Glaciar",
    "15": "15 - Tierra devastada",
    "16": "16 - Espacio exterior",
    "17": "17 - Villa Pingüino",
    "18": "18 - Infierno",
    "19": "19 - Desierto - Mediodía",
    "20": "20 - Castillo del Rey",
    "21": "21 - Torre Músculo",
    "22": "22 - Monte Paozu",
    "23": "23 - Tierra baldía - Atardecer",
    "24": "24 - Tierra baldía - Noche",
    "25": "25 - Zona rocosa - Atardecer",
    "26": "26 - Zona rocosa - Noche",
    "27": "27 - Escenario del Torneo Mundial - Atardecer",
    "28": "28 - Arena de los Juegos de Cell - Mediodía",
    "29": "29 - Ruinas de la ciudad - Atardecer",
    "30": "30 - Ruinas de la ciudad - Noche",
    "31": "31 - Desierto - Atardecer",
    "32": "32 - Desierto - Noche",
    "33": "33 - Camino montañoso - Atardecer",
    "34": "34 - Planeta - Atardecer",
}

CHARACTERS_STORY = {
"0": "000 - Goku (Inicial)",
    "1": "001 - Goku (Medio)",
    "2": "002 - Goku (Medio) - Super Saiyajin",
    "3": "003 - Goku (Final)",
    "4": "004 - Goku (Final) - Super Saiyajin",
    "5": "005 - Goku (Final) - Super Saiyajin 2",
    "6": "006 - Goku (Final) - Super Saiyajin 3",
    "7": "007 - Goku (GT)",
    "8": "008 - Goku (GT) - Super Saiyajin",
    "9": "009 - Goku (GT) - Super Saiyajin 3",
    "10": "010 - Goku (GT) - Super Saiyajin 4",
    "11": "011 - Pequeño Goku",
    "12": "012 - Gran Mono",
    "13": "013 - Pequeño Gohan",
    "14": "014 - Adolescente Gohan",
    "15": "015 - Adolescente Gohan - Super Saiyajin",
    "16": "016 - Adolescente Gohan - Super Saiyajin 2",
    "17": "017 - Adulto Gohan",
    "18": "018 - Adulto Gohan - Super Saiyajin",
    "19": "019 - Adulto Gohan - Super Saiyajin 2",
    "20": "020 - Gran Saiyaman",
    "21": "021 - Gohan Definitivo",
    "22": "022 - Piccolo (Inicial)",
    "23": "023 - Piccolo (Final)",
    "24": "024 - Nail",
    "25": "025 - Krilin",
    "26": "026 - Yamcha",
    "27": "027 - Tenshinhan",
    "28": "028 - Chaoz",
    "29": "029 - Vegeta (Scouter)",
    "30": "030 - Gran Mono Vegeta",
    "31": "031 - Vegeta",
    "32": "032 - Vegeta - Super Saiyajin",
    "33": "033 - Super Vegeta",
    "34": "034 - Vegeta (segunda forma)",
    "35": "035 - Vegeta (segunda forma) - Super Saiyajin",
    "36": "036 - Vegeta (segunda forma) - Super Saiyajin 2",
    "37": "037 - Vegeta (Final) - Majin",
    "38": "038 - Vegeta (segunda forma) - Super Saiyajin 4",
    "39": "039 - Trunks (Espada)",
    "40": "040 - Trunks (Espada) - Super Saiyajin",
    "41": "041 - Trunks",
    "42": "042 - Trunks - Super Saiyajin",
    "43": "043 - Super Trunks",
    "44": "044 - Pequeño Trunks",
    "45": "045 - Pequeño Trunks - Super Saiyajin",
    "46": "046 - Goten",
    "47": "047 - Goten - Super Saiyajin",
    "48": "048 - Gotenks",
    "49": "049 - Gotenks - Super Saiyajin",
    "50": "050 - Gotenks - Super Saiyajin 3",
    "51": "051 - Vegetto",
    "52": "052 - Super Vegetto",
    "53": "053 - Super Gogeta",
    "54": "054 - Gogeta - Super Saiyajin 4",
    "55": "055 - Mr. Satán",
    "56": "056 - Videl",
    "57": "057 - Gran Saiyaman 2",
    "58": "058 - Kaio-shin",
    "59": "059 - Kibitoshin",
    "60": "060 - Yajirobe",
    "61": "061 - Paikuhan",
    "62": "062 - Tapion",
    "63": "063 - Pan",
    "64": "064 - Uub",
    "65": "065 - Majuub",
    "66": "066 - Maestro Roshi",
    "67": "067 - Maestro Roshi - Máximo Poder",
    "68": "068 - Abuelo Gohan",
    "69": "069 - Nam",
    "70": "070 - Androide #8",
    "71": "071 - Rey Vegeta",
    "72": "072 - Gran Mono Rey Vegeta",
    "73": "073 - Bardock",
    "74": "074 - Gran Mono Bardock",
    "75": "075 - Fasha",
    "76": "076 - Gran Mono Fasha",
    "77": "077 - Raditz",
    "78": "078 - Gran Mono Raditz",
    "79": "079 - Saibaman",
    "80": "080 - Nappa",
    "81": "081 - Gran Mono Nappa",
    "82": "082 - Zarbon",
    "83": "083 - Zarbon - Post-transformación",
    "84": "084 - Dodoria",
    "85": "085 - Cui",
    "86": "086 - Capitán Ginyu",
    "87": "087 - Recoome",
    "88": "088 - Burter",
    "89": "089 - Jeice",
    "90": "090 - Guldo",
    "91": "091 - Freezer - 1.ª forma",
    "92": "092 - Freezer - 2.ª forma",
    "93": "093 - Freezer - 3.ª forma",
    "94": "094 - Freezer - Forma final",
    "95": "095 - Freezer - Máximo poder",
    "96": "096 - Mecha Freezer",
    "97": "097 - King Cold",
    "98": "098 - Appule",
    "99": "099 - Soldado de Freezer",
    "100": "100 - Androide #16",
    "101": "101 - Androide #17",
    "102": "102 - Androide #18",
    "103": "103 - Androide #19",
    "104": "104 - Dr. Gero",
    "105": "105 - Cell - 1.ª forma",
    "106": "106 - Cell - 2.ª forma",
    "107": "107 - Cell - Forma perfecta",
    "108": "108 - Cell - Perfecto",
    "109": "109 - Cell Jr.",
    "110": "110 - Babidi",
    "111": "111 - Rey Demonio Dabura",
    "112": "112 - Majin Buu",
    "113": "113 - Majin Buu (Maldad pura)",
    "114": "114 - Super Buu",
    "115": "115 - Super Buu - Absorbido a Gotenks",
    "116": "116 - Super Buu - Absorbido a Gohan",
    "117": "117 - Pequeño Buu",
    "118": "118 - Garlic Jr.",
    "119": "119 - Super Garlic Jr.",
    "120": "120 - Dr. Wheelo",
    "121": "121 - Turles",
    "122": "122 - Gran Mono Turles",
    "123": "123 - Slug",
    "124": "124 - Slug - Gigante",
    "125": "125 - Salza",
    "126": "126 - Cooler",
    "127": "127 - Cooler - Forma final",
    "128": "128 - Meta-Cooler",
    "129": "129 - Androide #13",
    "130": "130 - Androide #13 - Fusión",
    "131": "131 - Broly",
    "132": "132 - Broly - Super Saiyajin",
    "133": "133 - Broly - Super Saiyajin Legendario",
    "134": "134 - Zangya",
    "135": "135 - Bojack",
    "136": "136 - Bojack - Máximo poder",
    "137": "137 - Janemba",
    "138": "138 - Super Janemba",
    "139": "139 - Hirudegarn",
    "140": "140 - Baby Vegeta",
    "141": "141 - Super Baby 1",
    "142": "142 - Super Baby 2",
    "143": "143 - Gran Mono Baby",
    "144": "144 - Super 17",
    "145": "145 - Nuova Shenron",
    "146": "146 - Syn Shenron",
    "147": "147 - Omega Shenron",
    "148": "148 - Tao Pai Pai",
    "149": "149 - Cíborg Tao",
    "150": "150 - General Blue",
    "151": "151 - Devilman",
    "152": "152 - Máquina de Pilaf",
    "153": "153 - Máquina de Pilaf - Fusión",
    "154": "154 - Tambourine",
    "155": "155 - Rey Demonio Piccolo",
    "156": "156 - Arale",
    "157": "157 - Chi-Chi",
    "158": "158 - Spopovich",
    "159": "159 - Gohan del Futuro",
    "160": "160 - Gohan del Futuro - Super Saiyajin"
}

COSTUMES = {
    "0": "Traje 1",
    "1": "Traje 2",
    "2": "Traje 3",
    "3": "Traje 4",
    "4": "Traje 5",
    "5": "Traje 6",
    "6": "Traje 7",
    "7": "Traje 8",
}

EMPTY_SLOT = "[Inactivo / Sin Personaje]"

ANIMATIONS = {
    "000": "000_suelo.canm",
    "001": "001_suelo_cansado.canm",
    "002": "002_mover_lejos_entrada.canm",
    "003": "003_mover_lejos_bucle.canm",
    "004": "004_mover_lejos_izquierda_entrada.canm",
    "005": "005_mover_lejos_izquierda_bucle.canm",
    "006": "006_mover_lejos_derecha_entrada.canm",
    "007": "007_mover_lejos_derecha_bucle.canm",
    "008": "008_mover_cerca_frente.canm",
    "009": "009_mover_cerca_atras.canm",
    "00A": "00A_mover_cerca_izquierda.canm",
    "00B": "00B_mover_cerca_derecha.canm",
    "00C": "00C_carrera_frente_entrada.canm",
    "00D": "00D_carrera_frente_bucle.canm",
    "00E": "00E_carrera_frente_salida.canm",
    "00F": "00F_carrera_izquierda_entrada.canm",
    "010": "010_carrera_izquierda_bucle.canm",
    "011": "011_carrera_izquierda_salida.canm",
    "012": "012_carrera_derecha_entrada.canm",
    "013": "013_carrera_derecha_bucle.canm",
    "014": "014_carrera_derecha_salida.canm",
    "015": "015_embestida_romper_entrada.canm",
    "016": "016_embestida_romper_bucle.canm",
    "017": "017_embestida_romper_salida.canm",
    "018": "018_doble_embestida_entrada.canm",
    "019": "019_doble_embestida_bucle.canm",
    "01A": "01A_doble_embestida_salida.canm",
    "01B": "01B_esquivar_frente.canm",
    "01C": "01C_esquivar_atras.canm",
    "01D": "01D_esquivar_izquierda.canm",
    "01E": "01E_esquivar_derecha.canm",
    "01F": "01F_esquivar_salida.canm",
    "020": "020_salto_entrada.canm",
    "021": "021_salto_subida.canm",
    "022": "022_salto_bajada.canm",
    "023": "023_salto_salida.canm",
    "024": "024_ascenso_entrada.canm",
    "025": "025_ascenso_salida.canm",
    "026": "026_volar.canm",
    "027": "027_volar_cansado.canm",
    "028": "028_volar_esquivar_atras.canm",
    "029": "029_volar_esquivar_izquierda.canm",
    "02A": "02A_volar_esquivar_derecha.canm",
    "02B": "02B_volar_arriba.canm",
    "02C": "02C_volar_abajo_entrada.canm",
    "02D": "02D_volar_abajo_bucle.canm",
    "02E": "02E_volar_subida_rapida_entrada.canm",
    "02F": "02F_volar_subida_rapida_bucle.canm",
    "030": "030_volar_subida_rapida_salida.canm",
    "031": "031_volar_bajada_rapida_entrada.canm",
    "032": "032_volar_bajada_rapida_bucle.canm",
    "033": "033_volar_bajada_rapida_salida.canm",
    "034": "034_carga_entrada.canm",
    "035": "035_carga_bucle.canm",
    "036": "036_carga_maxima.canm",
    "037": "037_golpe_01.canm",
    "038": "038_golpe_02.canm",
    "039": "039_golpe_03.canm",
    "03A": "03A_golpe_04.canm",
    "03B": "03B_golpe_05.canm",
    "03C": "03C_golpe_06.canm",
    "03D": "03D_golpe_07.canm",
    "03E": "03E_golpe_08.canm",
    "03F": "03F_golpe_09.canm",
    "040": "040_golpe_10.canm",
    "041": "041_golpe_elevado_entrada.canm",
    "042": "042_golpe_elevado_bucle.canm",
    "043": "043_golpe_elevado_salida.canm",
    "044": "044_corte_tierra_entrada.canm",
    "045": "045_corte_tierra_bucle.canm",
    "046": "046_corte_tierra_salida.canm",
    "047": "047_golpe_pesado_entrada.canm",
    "048": "048_golpe_pesado_bucle.canm",
    "049": "049_golpe_pesado_salida.canm",
    "04A": "04A_golpe_cargado_frente_entrada.canm",
    "04B": "04B_golpe_cargado_frente_bucle.canm",
    "04C": "04C_golpe_cargado_frente_salida.canm",
    "04D": "04D_combo_golpe_entrada.canm",
    "04E": "04E_combo_golpe_bucle.canm",
    "04F": "04F_combo_golpe_salida.canm",
    "050": "050_golpe_cargado_arriba_entrada.canm",
    "051": "051_golpe_cargado_arriba_bucle.canm",
    "052": "052_golpe_cargado_arriba_salida.canm",
    "053": "053_golpe_cargado_abajo_entrada.canm",
    "054": "054_golpe_cargado_abajo_bucle.canm",
    "055": "055_golpe_cargado_abajo_salida.canm",
    "056": "056_golpe_cargado_izquierda_entrada.canm",
    "057": "057_golpe_cargado_izquierda_bucle.canm",
    "058": "058_golpe_cargado_izquierda_salida.canm",
    "059": "059_golpe_cargado_derecha_entrada.canm",
    "05A": "05A_golpe_cargado_derecha_bucle.canm",
    "05B": "05B_golpe_cargado_derecha_salida.canm",
    "05C": "05C_golpe_rapido_frente_entrada.canm",
    "05D": "05D_golpe_rapido_frente_bucle.canm",
    "05E": "05E_golpe_rapido_frente_salida.canm",
    "05F": "05F_golpe_rapido_arriba_entrada.canm",
    "060": "060_golpe_rapido_arriba_bucle.canm",
    "061": "061_golpe_rapido_arriba_salida.canm",
    "062": "062_golpe_rapido_abajo_entrada.canm",
    "063": "063_golpe_rapido_abajo_bucle.canm",
    "064": "064_golpe_rapido_abajo_salida.canm",
    "065": "065_golpe_rapido_izquierda_entrada.canm",
    "066": "066_golpe_rapido_izquierda_bucle.canm",
    "067": "067_golpe_rapido_izquierda_salida.canm",
    "068": "068_golpe_rapido_derecha_entrada.canm",
    "069": "069_golpe_rapido_derecha_bucle.canm",
    "06A": "06A_golpe_rapido_derecha_salida.canm",
    "06B": "06B_golpe_embestida_entrada.canm",
    "06C": "06C_golpe_embestida_bucle.canm",
    "06D": "06D_golpe_embestida_salida.canm",
    "06E": "06E_golpe_salto_entrada.canm",
    "06F": "06F_golpe_salto_bucle.canm",
    "070": "070_golpe_salto_salida.canm",
    "071": "071_ki_frente_entrada.canm",
    "072": "072_ki_frente_bucle.canm",
    "073": "073_ki_disparo_arriba_entrada.canm",
    "074": "074_ki_disparo_arriba_bucle.canm",
    "075": "075_ki_disparo_abajo_entrada.canm",
    "076": "076_ki_disparo_abajo_bucle.canm",
    "077": "077_ki_embestida_frente.canm",
    "078": "078_ki_embestida_izquierda.canm",
    "079": "079_ki_embestida_derecha.canm",
    "07A": "07A_ki_salto_disparo.canm",
    "07B": "07B_ki_cargado_frente_entrada.canm",
    "07C": "07C_ki_cargado_frente_bucle.canm",
    "07D": "07D_ki_cargado_frente_salida.canm",
    "07E": "07E_ki_cargado_arriba_entrada.canm",
    "07F": "07F_ki_cargado_arriba_bucle.canm",
    "080": "080_ki_cargado_arriba_salida.canm",
    "081": "081_ki_cargado_abajo_entrada.canm",
    "082": "082_ki_cargado_abajo_bucle.canm",
    "083": "083_ki_cargado_abajo_salida.canm",
    "084": "084_ki_embestida_cargada_frente_entrada.canm",
    "085": "085_ki_embestida_cargada_frente_bucle.canm",
    "086": "086_ki_embestida_cargada_frente_salida.canm",
    "087": "087_ki_embestida_cargada_izquierda_entrada.canm",
    "088": "088_ki_embestida_cargada_izquierda_bucle.canm",
    "089": "089_ki_embestida_cargada_izquierda_salida.canm",
    "08A": "08A_ki_embestida_cargada_derecha_entrada.canm",
    "08B": "08B_ki_embestida_cargada_derecha_bucle.canm",
    "08C": "08C_ki_embestida_cargada_derecha_salida.canm",
    "08D": "08D_ki_salto_cargado_entrada.canm",
    "08E": "08E_ki_salto_cargado_bucle.canm",
    "08F": "08F_ki_salto_cargado_salida.canm",
    "090": "090_cañon_kiai_entrada.canm",
    "091": "091_cañon_kiai_bucle.canm",
    "092": "092_cañon_kiai_salida.canm",
    "093": "093_patada_voladora.canm",
    "094": "094_agarre_entrada.canm",
    "095": "095_agarre_bucle.canm",
    "096": "096_lanzamiento_evento.canm",
    "097": "097_lanzamiento_enemigo.canm",
    "098": "098_agarre_salida.canm",
    "099": "099_lanzamiento_abajo_entrada.canm",
    "09A": "09A_lanzamiento_abajo_bucle.canm",
    "09B": "09B_lanzamiento_abajo_salida.canm",
    "09C": "09C_bloqueo_lanzamiento_entrada.canm",
    "09D": "09D_bloqueo_lanzamiento_salida.canm",
    "09E": "09E_dano_frente.canm",
    "09F": "09F_dano_izquierda.canm",
    "0A0": "0A0_dano_derecha.canm",
    "0A1": "0A1_dano_atras.canm",
    "0A2": "0A2_dano_volando_frente.canm",
    "0A3": "0A3_dano_volando_izquierda.canm",
    "0A4": "0A4_dano_volando_derecha.canm",
    "0A5": "0A5_dano_volando_atras.canm",
    "0A6": "0A6_dano_11.canm",
    "0A7": "0A7_dano_12.canm",
    "0A8": "0A8_dano_13.canm",
    "0A9": "0A9_dano_14.canm",
    "0AA": "0AA_dano_15.canm",
    "0AB": "0AB_dano_16.canm",
    "0AC": "0AC_dano_17.canm",
    "0AD": "0AD_dano_18.canm",
    "0AE": "0AE_dano_pesado_frente.canm",
    "0AF": "0AF_dano_pesado_atras.canm",
    "0B0": "0B0_dano_21.canm",
    "0B1": "0B1_dano_22.canm",
    "0B2": "0B2_dano_23.canm",
    "0B3": "0B3_dano_24.canm",
    "0B4": "0B4_dano_25.canm",
    "0B5": "0B5_dano_26.canm",
    "0B6": "0B6_dano_27.canm",
    "0B7": "0B7_paralisis.canm",
    "0B8": "0B8_quebrantaguardia.canm",
    "0B9": "0B9_dano_tumbado_arriba.canm",
    "0BA": "0BA_dano_tumbado_abajo.canm",
    "0BB": "0BB_dano_explosion_frontal.canm",
    "0BC": "0BC_dano_explosion_trasera.canm",
    "0BD": "0BD_dano_rodar_atras_entrada.canm",
    "0BE": "0BE_dano_rodar_atras_bucle.canm",
    "0BF": "0BF_dano_rodar_atras_salida.canm",
    "0C0": "0C0_dano_rodar_entrada.canm",
    "0C1": "0C1_dano_rodar_bucle.canm",
    "0C2": "0C2_dano_rodar_salida.canm",
    "0C3": "0C3_dano_golpe_cargado_entrada.canm",
    "0C4": "0C4_dano_golpe_cargado_bucle.canm",
    "0C5": "0C5_dano_golpe_cargado_salida.canm",
    "0C6": "0C6_dano_caida_1.canm",
    "0C7": "0C7_dano_caida_2.canm",
    "0C8": "0C8_dano_caida_3.canm",
    "0C9": "0C9_dano_caida_4.canm",
    "0CA": "0CA_dano_28.canm",
    "0CB": "0CB_dano_29.canm",
    "0CC": "0CC_dano_30.canm",
    "0CD": "0CD_dano_31.canm",
    "0CE": "0CE_dano_32.canm",
    "0CF": "0CF_dano_33.canm",
    "0D0": "0D0_dano_34.canm",
    "0D1": "0D1_dano_35.canm",
    "0D2": "0D2_dano_tumbado_paralizado_entrada.canm",
    "0D3": "0D3_dano_tumbado_paralizado_bucle.canm",
    "0D4": "0D4_dano_tumbado_cansado_entrada.canm",
    "0D5": "0D5_dano_tumbado_cansado_bucle.canm",
    "0D6": "0D6_dano_tumbado_cansado_salida.canm",
    "0D7": "0D7_dano_flotar_agua_entrada.canm",
    "0D8": "0D8_dano_flotar_agua_bucle.canm",
    "0D9": "0D9_dano_caida_muerte.canm",
    "0DA": "0DA_dano_36.canm",
    "0DB": "0DB_dano_37.canm",
    "0DC": "0DC_dano_corte_tierra_entrada.canm",
    "0DD": "0DD_dano_corte_tierra_bucle.canm",
    "0DE": "0DE_dano_esquivar_sonico_1.canm",
    "0DF": "0DF_dano_esquivar_sonico_2.canm",
    "0E0": "0E0_dano_martillo_rodante_entrada.canm",
    "0E1": "0E1_dano_martillo_rodante_bucle.canm",
    "0E2": "0E2_levantarse_entrada.canm",
    "0E3": "0E3_levantarse_bucle.canm",
    "0E4": "0E4_levantarse_salida.canm",
    "0E5": "0E5_levantarse_4.canm",
    "0E6": "0E6_levantarse_5.canm",
    "0E7": "0E7_levantarse_6.canm",
    "0E8": "0E8_dano_38.canm",
    "0E9": "0E9_dano_39.canm",
    "0EA": "0EA_dano_40.canm",
    "0EB": "0EB_dano_41.canm",
    "0EC": "0EC_dano_contraz_1.canm",
    "0ED": "0ED_dano_contraz_2.canm",
    "0EE": "0EE_dano_42.canm",
    "0EF": "0EF_dano_43.canm",
    "0F0": "0F0_bloqueo_entrada.canm",
    "0F1": "0F1_bloqueo_bucle.canm",
    "0F2": "0F2_bloqueo_arriba_entrada.canm",
    "0F3": "0F3_bloqueo_arriba_bucle.canm",
    "0F4": "0F4_bloqueo_abajo_entrada.canm",
    "0F5": "0F5_bloqueo_abajo_bucle.canm",
    "0F6": "0F6_bloqueo_golpe_entrada.canm",
    "0F7": "0F7_bloqueo_golpe_bucle.canm",
    "0F8": "0F8_parry_combo_postura.canm",
    "0F9": "0F9_parry_combo_golpe.canm",
    "0FA": "0FA_parry_disparo_ki_1.canm",
    "0FB": "0FB_parry_disparo_ki_2.canm",
    "0FC": "0FC_parry_disparo_ki_3.canm",
    "0FD": "0FD_parry_disparo_ki_4.canm",
    "0FE": "0FE_parry_disparo_ki_5.canm",
    "0FF": "0FF_recuperacion_rapida_entrada.canm",
    "100": "100_recuperacion_rapida_bucle.canm",
    "101": "101_recuperacion_rapida_enemigo_entrada.canm",
    "102": "102_recuperacion_rapida_enemigo_bucle.canm",
    "103": "103_habilidad_001.canm",
    "104": "104_habilidad_002.canm",
    "105": "105_habilidad_003_entrada.canm",
    "106": "106_habilidad_003_carga.canm",
    "107": "107_habilidad_003_disparo1.canm",
    "108": "108_habilidad_003_disparo2.canm",
    "109": "109_habilidad_003_bucle1.canm",
    "10A": "10A_habilidad_003_bucle2.canm",
    "10B": "10B_habilidad_003_salida.canm",
    "10C": "10C_habilidad_003_entrada_arriba.canm",
    "10D": "10D_habilidad_003_carga_arriba.canm",
    "10E": "10E_habilidad_003_disparo1_arriba.canm",
    "10F": "10F_habilidad_003_disparo2_arriba.canm",
    "110": "110_habilidad_003_bucle3_arriba.canm",
    "111": "111_habilidad_003_bucle4_arriba.canm",
    "112": "112_habilidad_003_salida_arriba.canm",
    "113": "113_habilidad_003_entrada_abajo.canm",
    "114": "114_habilidad_003_carga_abajo.canm",
    "115": "115_habilidad_003_disparo1_abajo.canm",
    "116": "116_habilidad_003_disparo2_abajo.canm",
    "117": "117_habilidad_003_bucle3_abajo.canm",
    "118": "118_habilidad_003_bucle4_abajo.canm",
    "119": "119_habilidad_003_salida_abajo.canm",
    "11A": "11A_habilidad_003_22.canm",
    "11B": "11B_habilidad_003_23.canm",
    "11C": "11C_habilidad_003_evento_1.canm",
    "11D": "11D_habilidad_003_evento_2.canm",
    "11E": "11E_habilidad_003_evento_3.canm",
    "11F": "11F_habilidad_003_evento_4.canm",
    "120": "120_habilidad_003_evento_5.canm",
    "121": "121_habilidad_003_enemigo_1.canm",
    "122": "122_habilidad_003_enemigo_2.canm",
    "123": "123_habilidad_003_enemigo_3.canm",
    "124": "124_habilidad_003_enemigo_4.canm",
    "125": "125_habilidad_003_enemigo_5.canm",
    "126": "126_habilidad_003_34.canm",
    "127": "127_habilidad_004_entrada.canm",
    "128": "128_habilidad_004_carga.canm",
    "129": "129_habilidad_004_disparo1.canm",
    "12A": "12A_habilidad_004_disparo2.canm",
    "12B": "12B_habilidad_004_bucle1.canm",
    "12C": "12C_habilidad_004_bucle2.canm",
    "12D": "12D_habilidad_004_salida.canm",
    "12E": "12E_habilidad_004_entrada_arriba.canm",
    "12F": "12F_habilidad_004_carga_arriba.canm",
    "130": "130_habilidad_004_disparo1_arriba.canm",
    "131": "131_habilidad_004_disparo2_arriba.canm",
    "132": "132_habilidad_004_bucle3_arriba.canm",
    "133": "133_habilidad_004_bucle4_arriba.canm",
    "134": "134_habilidad_004_salida_arriba.canm",
    "135": "135_habilidad_004_entrada_abajo.canm",
    "136": "136_habilidad_004_carga_abajo.canm",
    "137": "137_habilidad_004_disparo1_abajo.canm",
    "138": "138_habilidad_004_disparo2_abajo.canm",
    "139": "139_habilidad_004_bucle3_abajo.canm",
    "13A": "13A_habilidad_004_bucle4_abajo.canm",
    "13B": "13B_habilidad_004_salida_abajo.canm",
    "13C": "13C_habilidad_004_22.canm",
    "13D": "13D_habilidad_004_23.canm",
    "13E": "13E_habilidad_004_evento_1.canm",
    "13F": "13F_habilidad_004_evento_2.canm",
    "140": "140_habilidad_004_evento_3.canm",
    "141": "141_habilidad_004_evento_4.canm",
    "142": "142_habilidad_004_evento_5.canm",
    "143": "143_habilidad_004_enemigo_1.canm",
    "144": "144_habilidad_004_enemigo_2.canm",
    "145": "145_habilidad_004_enemigo_3.canm",
    "146": "146_habilidad_004_enemigo_4.canm",
    "147": "147_habilidad_004_enemigo_5.canm",
    "148": "148_habilidad_004_34.canm",
    "149": "149_habilidad_005_entrada.canm",
    "14A": "14A_habilidad_005_carga.canm",
    "14B": "14B_habilidad_005_disparo1.canm",
    "14C": "14C_habilidad_005_disparo2.canm",
    "14D": "14D_habilidad_005_bucle1.canm",
    "14E": "14E_habilidad_005_bucle2.canm",
    "14F": "14F_habilidad_005_salida.canm",
    "150": "150_habilidad_005_entrada_arriba.canm",
    "151": "151_habilidad_005_carga_arriba.canm",
    "152": "152_habilidad_005_disparo1_arriba.canm",
    "153": "153_habilidad_005_disparo2_arriba.canm",
    "154": "154_habilidad_005_bucle3_arriba.canm",
    "155": "155_habilidad_005_bucle4_arriba.canm",
    "156": "156_habilidad_005_salida_arriba.canm",
    "157": "157_habilidad_005_entrada_abajo.canm",
    "158": "158_habilidad_005_carga_abajo.canm",
    "159": "159_habilidad_005_disparo1_abajo.canm",
    "15A": "15A_habilidad_005_disparo2_abajo.canm",
    "15B": "15B_habilidad_005_bucle3_abajo.canm",
    "15C": "15C_habilidad_005_bucle4_abajo.canm",
    "15D": "15D_habilidad_005_salida_abajo.canm",
    "15E": "15E_habilidad_005_22.canm",
    "15F": "15F_habilidad_005_23.canm",
    "160": "160_habilidad_005_evento_1.canm",
    "161": "161_habilidad_005_evento_2.canm",
    "162": "162_habilidad_005_evento_3.canm",
    "163": "163_habilidad_005_evento_4.canm",
    "164": "164_habilidad_005_evento_5.canm",
    "165": "165_habilidad_005_enemigo_1.canm",
    "166": "166_habilidad_005_enemigo_2.canm",
    "167": "167_habilidad_005_enemigo_3.canm",
    "168": "168_habilidad_005_enemigo_4.canm",
    "169": "169_habilidad_005_enemigo_5.canm",
    "16A": "16A_habilidad_005_34.canm",
    "16B": "16B_habilidad_005_inicio.canm",
    "16C": "16C_choque_poder_1.canm",
    "16D": "16D_choque_poder_2.canm",
    "16E": "16E_choque_poder_3.canm",
    "16F": "16F_choque_poder_4.canm",
    "170": "170_choque_poder_5.canm",
    "171": "171_choque_poder_6.canm",
    "172": "172_choque_poder_derrota.canm",
    "173": "173_choque_embestida_entrada.canm",
    "174": "174_choque_embestida_bucle.canm",
    "175": "175_choque_embestida_ganar.canm",
    "176": "176_choque_embestida_perder.canm",
    "177": "177_transformacion_entrada.canm",
    "178": "178_transformacion_bucle.canm",
    "179": "179_transformacion_salida.canm",
    "17A": "17A_guardia_poderosa_entrada.canm",
    "17B": "17B_guardia_poderosa_bucle.canm",
    "17C": "17C_caida_atras.canm",
    "17D": "17D_caida_frente.canm",
    "17E": "17E_buscar_ki.canm",
    "17F": "17F_buscar_scouter.canm",
    "180": "180_intro_entrada.canm",
    "181": "181_intro_bucle.canm",
    "182": "182_victoria_entrada.canm",
    "183": "183_victoria_bucle.canm",
    "184": "184_derrota.canm",
    "185": "185_burla.canm",
    "186": "186_lanzamiento_gigante_entrada.canm",
    "187": "187_lanzamiento_gigante_bucle.canm",
    "188": "188_lanzamiento_gigante_evento.canm",
    "189": "189_lanzamiento_gigante_enemigo.canm",
    "18A": "18A_lanzamiento_gigante_salida.canm",
    "18B": "18B_volar_sin_volar.canm",
    "18C": "18C_salto_sin_volar.canm",
    "18D": "18D_cancelar_soplo_entrada.canm",
    "18E": "18E_cancelar_soplo_bucle.canm",
    "18F": "18F_detransformacion_entrada.canm",
    "190": "190_detransformacion_bucle.canm",
    "191": "191_detransformacion_salida.canm",
    "192": "192_volar_rapido_subida.canm",
    "193": "193_esquivar_sonico_entrada.canm",
    "194": "194_esquivar_sonico_bucle.canm",
    "195": "195_esquivar_sonico_salida.canm",
    "196": "196_sorprendido.canm",
    "197": "197_ataque_rayo_entrada.canm",
    "198": "198_ataque_rayo_salida.canm",
    "199": "199_ki_rapido_entrada.canm",
    "19A": "19A_ki_rapido_carga.canm",
    "19B": "19B_ki_rapido_bucle.canm",
    "19C": "19C_ki_rapido_salida.canm",
    "19D": "19D_reposo_bucle.canm",
    "19E": "19E_wii_01.canm",
    "19F": "19F_wii_02.canm",
    "1A0": "1A0_wii_03.canm",
    "1A1": "1A1_wii_04.canm",
    "1A2": "1A2_wii_05.canm",
    "1A3": "1A3_wii_06.canm",
    "1A4": "1A4_wii_07.canm",
    "1A5": "1A5_wii_08.canm",
    "1A6": "1A6_wii_09.canm",
    "1A7": "1A7_wii_10.canm",
    "1A8": "1A8_wii_11.canm",
    "1A9": "1A9_wii_12.canm",
    "1AA": "1AA_wii_13.canm",
    "1AB": "1AB_wii_14.canm",
    "1AC": "1AC_wii_15.canm",
    "1AD": "1AD_wii_16.canm",
    "1AE": "1AE_wii_17.canm",
    "1AF": "1AF_wii_18.canm",
    "1B0": "1B0_wii_19.canm",
    "1B1": "1B1_blank.canm",
    "1B2": "1B2_blank.canm",
    "1B3": "1B3_blank.canm",
    "1B4": "1B4_blank.canm",
    "1B5": "1B5_blank.canm",
    "1B6": "1B6_blank.canm",
    "1B7": "1B7_blank.canm",
}

ANIMATION_LIST_LABELS = [f"{code} - {name}" for code, name in ANIMATIONS.items()]

HEX_CONDITIONS = {
    "Esperar 10 segundos": "0000",
    "Esperar 15 segundos": "0001",
    "Esperar 20 segundos": "0002",
    "Esperar 25 segundos": "0003",
    "Esperar 30 segundos": "0004",
    "Esperar 35 segundos": "0005",
    "Esperar 40 segundos": "0006",
    "Esperar 45 segundos": "0007",
    "Esperar 50 segundos": "0008",
    "Esperar 55 segundos": "0009",
    "Esperar 60 segundos": "000a",
    "Esperar 70 segundos": "000b",
    "Esperar 80 segundos": "000c",
    "Esperar 90 segundos": "000d",
    "Esperar 100 segundos": "000e",
    "Esperar 120 segundos": "000f",
    "Esperar 140 segundos": "0010",
    "Esperar 160 segundos": "0011",
    "Esperar 180 segundos": "0012",
    "Realizar Normal Clash": "0014",
    "Realizar Aéreo Clash": "0015",
    "Perder 1 Health Bar": "0016",
    "Perder 2 barras de salud": "0017",
    "Perder 3 barras de salud": "0018",
    "Perder 4 barras de salud": "0019",
    "Perder 5 barras de salud": "001a",
    "Perder 6 barras de salud": "001b",
    "Perder 7 barras de salud": "001c",
    "Llenar las barras de Ki": "001d",
    "Alcanzar el máximo de reservas de ráfaga": "001e",
    "Entrar en modo MÁXIMO PODER": "001f",
    "Transformar/Destransformar/Fusiónar": "0020",
    "Burlarse": "0021",
    "Caer al suelo/agua": "0022",
    "Realizar 1st Blast 1": "0024",
    "Realizar 2nd Blast 1": "0025",
    "Realizar 1st Blast 2": "0026",
    "Realizar 2nd Blast 2": "0027",
    "Realizar Ultimate Blast": "0028",
    "Golpear con 1st Blast 1": "0029",
    "Golpear con 2nd Blast 1": "002a",
    "Golpear con 1st Blast 2": "002b",
    "Golpear con 2nd Blast 2": "002c",
    "Golpear con Ultimate Blast": "002d",
    "Bloquear 1st Blast 2": "002e",
    "Bloquear 2nd Blast 2": "002f",
    "Bloquear Ultimate Blast": "0030",
    "Realizar Dragon Homing": "0031",
    "Realizar Vanishing Attack": "0032",
    "Realizar Throw": "0033",
    "Realizar Hyper Smash": "0034",
    "Golpear con Charged Ki Blast": "0036",
    "Realizar Fully Charged Left Smash Attack": "0037",
    "Realizar Fully Charged Right Smash Attack": "0038",
    "Realizar Fully Charged Up Smash Attack": "0039",
    "Realizar Fully Charged Down Smash Attack": "003a",
    "Realizar Fully Charged Neutral Smash Attack": "003b",
    "Realizar First Attack!": "003c",
    "Realizar Rush Attack": "003d",
    "Realizar Dragon Smash": "003e",
    "Realizar Burst Meteo Finisher": "003f",
    "Realizar Dash Smash": "0040",
    "Realizar Teleport": "0041",
    "Realizar Z-Counter": "0042",
    "Realizar Guard Crush": "0043",
    "Realizar Sonic Sway": "0044",
    "Realizar Emergency Blaster Wave": "0045",
    "Ganar Beam Struggle": "0046",
    "Ganar Normal Clash": "0047",
    "Ganar por K.O.": "0048",
    "Ganar via Ring out": "0049",
    "Realizar Misc. Melee Attack": "004b",
    "Press R3": "0050",
    "Realizar Blast 1 Finish": "0052",
    "Realizar Blast 2 Finish": "0053",
    "Defeat all teammates": "0054",
    "Recibir un golpe": "0055",
    "Inmediato": "ffff",
}

# --- Variantes CPU de las condiciones ($if) ---
# Usan el mismo código hex que la condición del jugador, pero con el primer
# dígito cambiado de "0" a "8" (ej: "0002" -> "8002"). Se generan de forma
# automática para no duplicar la lista a mano y evitar que se muestren como
# "DESCONOCIDO / Custom Condition" al leer un $if:&8XXX del CPU.
HEX_CONDITIONS.update({
    f"{label} [CPU]": "8" + hex_val[1:]
    for label, hex_val in list(HEX_CONDITIONS.items())
    if len(hex_val) == 4 and hex_val[0] == "0"
})

HEX_EVENTS = {
    "[P1] Inicio de batalla (no hace nada)": "0000",
    "[P1] Fin de batalla (no hace nada)": "0001",
    "[P1] Aéreo Clash (0002)": "0002",
    "[P1] Destrucción del mapa": "0003",
    "[P1] Normal Clash": "0004",
    "[P1] Aéreo Clash (0005)": "0005",
    "[P1] Aéreo Clash (0006)": "0006",
    "[P1] Aéreo Clash (0007)": "0007",
    "[P1] Beam Struggle (P1 1st B2 vs COM 1st B2)": "0008",
    "[P1] Beam Struggle (P1 1st B2 vs COM 2nd B2)": "0009",
    "[P1] Beam Struggle (P1 2nd B2 vs COM 1st B2)": "000a",
    "[P1] Beam Struggle (P1 2nd B2 vs COM 2nd B2)": "000b",
    "[P1] Beam Struggle (Ultimate Blasts)": "000c",
    "[P1] DESCONOCIDO (000D)": "000d",
    "[P1] DESCONOCIDO (000E)": "000e",
    "[P1] DESCONOCIDO (000F)": "000f",
    "[P1] Cambiar con compañero #1": "0010",
    "[P1] Cambiar con compañero #2": "0011",
    "[P1] Cambiar con compañero #3": "0012",
    "[P1] Cambiar con compañero #4": "0013",
    "[P1] Cambiar con compañero #5": "0014",
    "[P1] Asignar transformación": "0015",
    "[P1] Asignar destransformación": "0016",
    "[P1] Asignar fusión": "0017",
    "[P1] Go to MAX POWER Mode": "0018",
    "[P1] Activar 1st Blast 1": "0019",
    "[P1] Activar 2nd Blast 1": "001a",
    "[P1] Activar 1st Blast 2": "001b",
    "[P1] Activar 2nd Blast 2": "001c",
    "[P1] Activar Ultimate Blast": "001d",
    "[CPU] Cambiar con compañero #1": "8011",
    "[CPU] Cambiar con compañero #2": "8012",
    "[CPU] Cambiar con compañero #3": "8013",
    "[CPU] Cambiar con compañero #4": "8014",
    "[CPU] Cambiar con compañero #5": "8015",
    "[CPU] Asignar transformación": "8016",
    "[CPU] Asignar destransformación": "8017",
    "[CPU] Asignar fusión": "8018",
    "[CPU] Go to MAX POWER Mode": "8019",
    "[CPU] Activar 1st Blast 1": "801a",
    "[CPU] Activar 2nd Blast 1": "801b",
    "[CPU] Activar 1st Blast 2": "801c",
    "[CPU] Activar 2nd Blast 2": "801d",
    "[CPU] Activar Ultimate Blast": "801e",
}

CHARACTERS_EVENTS = {
    "00": "Goku (Inicial)",
    "01": "Goku (Medio)",
    "02": "Goku (Medio) - Super Saiyajin",
    "03": "Goku (Final)",
    "04": "Goku (Final) - Super Saiyajin",
    "05": "Goku (Final) - Super Saiyajin2",
    "06": "Goku (Final) - Super Saiyajin3",
    "07": "Goku (GT)",
    "08": "Goku (GT) - Super Saiyajin",
    "09": "Goku (GT) - Super Saiyajin3",
    "0A": "Goku (GT) - Super Saiyajin4",
    "0B": "Pequeño Goku",
    "0C": "Ozaru",
    "0D": "Pequeño Gohan",
    "0E": "Adolescente Gohan",
    "0F": "Adolescente Gohan - Super Saiyajin",
    "10": "Adolescente Gohan - Super Saiyajin2",
    "11": "Adulto Gohan",
    "12": "Adulto Gohan - Super Saiyajin",
    "13": "Adulto Gohan - Super Saiyajin2",
    "14": "Gran Saiyaman",
    "15": "Ultimate Gohan",
    "16": "Piccolo (Inicial)",
    "17": "Piccolo (Final)",
    "18": "Nail",
    "19": "Krillin",
    "1A": "Yamcha",
    "1B": "Tien",
    "1C": "Chiaotzu",
    "1D": "Vegeta (Scouter)",
    "1E": "Ozaru Vegeta",
    "1F": "Vegeta",
    "20": "Vegeta - Super Saiyajin",
    "21": "Super Vegeta",
    "22": "Vegeta (segunda forma)",
    "23": "Vegeta (2nd) - Super Saiyajin",
    "24": "Vegeta (2nd) - Super Saiyajin2",
    "25": "Vegeta (Final) - Majin",
    "26": "Vegeta (2nd) - Super Saiyajin4",
    "27": "Trunks (Espada)",
    "28": "Trunks (Espada) - Super Saiyajin",
    "29": "Trunks",
    "2A": "Trunks - Super Saiyajin",
    "2B": "Super Trunks",
    "2C": "Pequeño Trunks",
    "2D": "Pequeño Trunks - Super Saiyajin",
    "2E": "Goten",
    "2F": "Goten - Super Saiyajin",
    "30": "Gotenks",
    "31": "Gotenks - Super Saiyajin",
    "32": "Gotenks - Super Saiyajin3",
    "33": "Vegito",
    "34": "Super Vegito",
    "35": "Super Gogeta",
    "36": "Gogeta - Super Saiyajin4",
    "37": "Hercule",
    "38": "Videl",
    "39": "Gran Saiyaman 2",
    "3A": "Supremo Kai",
    "3B": "Kibito Kai",
    "3C": "Yajirobe",
    "3D": "Pikkon",
    "3E": "Tapion",
    "3F": "Pan",
    "40": "Uub",
    "41": "Majuub",
    "42": "Maestro Roshi",
    "43": "Maestro Roshi - MÁXIMO PODER",
    "44": "Abuelo Gohan",
    "45": "Nam",
    "46": "Androide #8",
    "47": "King Vegeta",
    "48": "Ozaru King Vegeta",
    "49": "Bardock",
    "4A": "Ozaru Bardock",
    "4B": "Fasha",
    "4C": "Ozaru Fasha",
    "4D": "Raditz",
    "4E": "Ozaru Raditz",
    "4F": "Saibamen",
    "50": "Nappa",
    "51": "Ozaru Nappa",
    "52": "Zarbon",
    "53": "Zarbon - Post-transformación",
    "54": "Dodoria",
    "55": "Cui",
    "56": "Ginyu",
    "57": "Recoome",
    "58": "Burter",
    "59": "Jeice",
    "5A": "Guldo",
    "5B": "Frieza - 1.ª forma",
    "5C": "Frieza - 2.ª forma",
    "5D": "Frieza - 3.ª forma",
    "5E": "Frieza - Forma final",
    "5F": "Frieza - Máximo poder",
    "60": "Mecha Frieza",
    "61": "King Cold",
    "62": "Appule",
    "63": "Frieza Soldado",
    "64": "Androide #16",
    "65": "Androide #18",
    "66": "Androide #18",
    "67": "Androide #19",
    "68": "Dr. Gero",
    "69": "Cell - 1.ª forma",
    "70": "Cell - 2.ª forma",
    "6B": "Cell - Forma perfecta",
    "6C": "Cell - Perfecto",
    "6D": "Cell Jr.",
    "6E": "Babidi",
    "6F": "Rey Demonio Dabura",
    "70": "Majin Buu",
    "71": "Majin Buu (Mal puro)",
    "72": "Super Buu",
    "73": "Super Buu - Gotenks Abs",
    "74": "Super Buu - Gohan Abs",
    "75": "Pequeño Buu",
    "76": "Garlic Jr.",
    "77": "Super Garlic Jr.",
    "78": "Dr. Wheelo",
    "79": "Turles",
    "7A": "Ozaru Turles",
    "7B": "Slug",
    "7C": "Slug - Gigante",
    "7D": "Salza",
    "7E": "Cooler",
    "7F": "Cooler - Forma final",
    "80": "Meta-Cooler",
    "81": "Androide #13",
    "82": "Androide #13 - Fusión",
    "83": "Broly",
    "84": "Broly - Super Saiyajin",
    "85": "Broly - LSuper Saiyajin",
    "86": "Zangya",
    "87": "Bojack",
    "88": "Bojack - Máximo poder",
    "89": "Janemba",
    "8A": "Super Janemba",
    "8B": "Hirudegarn",
    "8C": "Baby Vegeta",
    "8D": "Super Baby 1",
    "8E": "Super Baby 2",
    "8F": "Ozaru Baby",
    "90": "Super 17",
    "91": "Nuova Shenron",
    "92": "Syn Shenron",
    "93": "Omega Shenron",
    "94": "General Tao",
    "95": "Cíborg Tao",
    "96": "General Blue",
    "97": "Devilman",
    "98": "Pilaf Máquina",
    "99": "Pilaf Máquina - Fusión",
    "9A": "Tambourine",
    "9B": "Rey Demonio Piccolo",
    "9C": "Arale",
    "9D": "Chi-Chi",
    "9E": "Spopovich",
    "9F": "Future Gohan",
    "A0": "Future Gohan - Super Saiyajin",
}

HEX_TO_LABEL_COND = {v.lower(): k for k, v in HEX_CONDITIONS.items()}
HEX_TO_LABEL_EVENT = {v.lower(): k for k, v in HEX_EVENTS.items()}
CHAR_LIST_LABELS = [
    f"{hex_code} - {name}" for hex_code, name in CHARACTERS_EVENTS.items()
]

# ============================================================================
# --- PERSONAJES DLC (ISOs modificadas con soporte de DLC) ---
# Lista de personajes extra (165-252 / A5-FC) disponibles únicamente en isos
# modificadas con capacidad de DLC. Se generan de forma automática a partir
# del rango decimal/hexadecimal indicado por el usuario.
# ============================================================================

DLC_EMPTY_SLOT = "-- No aplicar (DLC) --"
DLC_KEEP_ORIGINAL = "Mantener personaje del juego original (Historia)"

DLC_CHARACTERS_STORY = {
    str(dec): f"{dec} - {format(dec, '02X')} - DLC:{dec}"
    for dec in range(165, 253)
}

DLC_CHARACTERS_EVENTS = {
    format(dec, "02X"): f"DLC:{dec}" for dec in range(165, 253)
}

DLC_CHAR_LIST_LABELS = [
    f"{hex_code} - {name}" for hex_code, name in DLC_CHARACTERS_EVENTS.items()
]


def normalize_hex(hex_str, mapping):
  clean = re.sub(r"[^0-9a-fA-F]", "", hex_str).lower()
  if len(clean) > 4:
    clean = clean[-4:]
  if clean in mapping:
    return clean
  if len(clean) == 4:
    swapped = clean[2:] + clean[:2]
    if swapped in mapping:
      return swapped
  return clean



# Solo las CABECERAS de bloque "$EV_XX:<" definen el evento padre. Las
# referencias "$to:$EV_XX" dentro de un $Link NO deben contarse como padre.
EV_HEADER_RE = re.compile(r"(\$EV_\w+)\s*:\s*<")


def ev_parent_sort_key(ev_id):
  m = re.search(r"(\d+)", str(ev_id))
  return int(m.group(1)) if m else 10 ** 9


def link_event_sort_key(item_text):
  """Clave de orden para una entrada '{$if:..., $to:$EV_XX}'."""
  m = re.search(r"\$to\s*:\s*\$EV_(\d+)", item_text, re.IGNORECASE)
  return int(m.group(1)) if m else 10 ** 9


def sort_link_events_in_text(text):
  """Ordena, dentro de cada '$event:K[ ... ]', las entradas por $EV_XX
  ascendente (00 -> XX), conservando sangria, saltos de linea, comas y el
  orden relativo de las entradas repetidas."""
  pattern = re.compile(r"(\$event\s*:\s*K\[)(.*?)(\])", re.DOTALL | re.IGNORECASE)
  entry_re = re.compile(r"\{[^{}]*\}")

  def _fix(m):
    body = m.group(2)
    entries = entry_re.findall(body)
    if len(entries) < 2:
      return m.group(0)
    sorted_entries = sorted(entries, key=link_event_sort_key)
    it = iter(sorted_entries)
    # Se reemplaza cada entrada en su misma posicion (mismo espaciado,
    # mismas comas), solo cambia cual entrada va en cada hueco.
    new_body = entry_re.sub(lambda _m: next(it), body)
    return m.group(1) + new_body + m.group(3)

  return pattern.sub(_fix, text)


MAP_LIST_LABELS = list(MAPS.values())


def is_map_event(ev_label):
  return "Destrucción del mapa" in ev_label


def is_char_event(ev_label):
  keywords = [
      "Cambiar con compañero",
      "Asignar transformación",
      "Asignar destransformación",
      "Asignar fusión",
  ]
  return any(kw in ev_label for kw in keywords)


# ============================================================================
# --- MÓDULO DE Z-ITEMS (inyectado desde DBZ_ZIT_EDITOR.py) ---
# Tabla de Z-Items, utilidades de búsqueda/parseo y gestor de líneas $zit,
# integrados aquí para dar soporte a la nueva pestaña "Z-Items" del editor.
# ============================================================================

ZITEMS_CSV_DATA = """dec,nombre
0,Ataque Arriba 1
1,Ataque Arriba 2
2,Ataque Arriba 3
3,Defensa Arriba 1
4,Defensa Arriba 2
5,Defensa Arriba 3
6,Poder Ki Arriba 1
7,Poder Ki Arriba 2
8,Poder Ki Arriba 3
9,Super Arriba 1
10,Super Arriba 2
11,Super Arriba 3
12,Ataque Arriba 2 y Defensa Abajo 1
13,Defensa Arriba 2 y Ataque Abajo 1
14,Poder Ki Arriba 2 y Super Abajo 1
15,Super Arriba 2 y Poder Abajo 1
16,Ataque Arriba 3 y Super Abajo 1
17,Defensa Arriba 3 y Ataque Abajo 2
18,Poder Ki Arriba 3 y Defensa Abajo 1
19,Super Arriba 3 y Poder Abajo 2
20,Ataque Arriba 3 y Defensa Abajo 2
21,Defensa Arriba 3 y Poder Ki Abajo 1
22,Poder Ki Arriba 3 y Super Abajo 2
23,Super Arriba 3 y Ataque Abajo 1
24,Vacío 1
25,Vacío 2
26,Vacío 3
27,Vacío 4
28,Vacío 5
29,Vacío 6
30,Vacío 7
31,Vacío 8
32,Vacío 9
33,Vacío 10
34,Vuelo
35,Liberar Poder Latente 1
36,Liberar Poder Latente 2
37,Liberar Poder Latente 3
38,Control de Ki
39,Maestría del Dragon Dash
40,Punto Alto
41,Esencia de la Vista
42,Linaje Guerrero
43,Halo
44,Sello Demoníaco
45,Golpe Satisfactorio
46,Corazón Activo
47,Espíritu de Lucha Indomable
48,Rompe Mentes
49,Poder Gigantesco
50,Espíritu de Lucha Creciente
51,Medidas Secretas
52,Prueba de Amistad
53,Habilidad Curativa de Dende
54,Vida Eterna
55,Tensión Arriba
56,Tensión Alta
57,Bendición del Agua
58,Control Espiritual
59,Amante de la Justicia
60,Ambiciones Malvadas
61,Corazón de Dragón
62,Latido de Dragón
63,Espíritu de Dragón
64,Confianza
65,Control de Batalla
66,Arte Secreto de Kibito
67,Amenaza Persistente
68,Maestro Milagroso
69,Habilidad Exquisita
70,Retorno Rápido
71,Presión Pesada
72,Liberar Ki
73,Poder de la Ira
74,Poder del Dragón
75,¡Energía Latente!
76,¡Espíritu de Lucha!
77,¡Indignación!
78,¡En Serio!
79,Odio hacia los Saiyans
80,Ráfaga de Ataques 1
81,Ráfaga de Ataques 2
82,Ráfaga de Ataques 3
83,Maestro de la Guardia
84,Espejismo
85,Voluntad del Guerrero
86,Orgullo Malvado
87,Guardia Perfecta
88,Sparking Plus
89,Estilo del Fuerte
90,Aura del Emperador
91,Sparking Milagroso
92,Salvador
93,Cuerpo Ligero
94,Cuerpo Poderoso
95,Cuerpo Definitivo
96,Aura Dracónica
97,Golpe Maestro
98,Ráfaga Maestra
99,Lanzamiento Maestro
100,Ataque Cargado
101,Ataque Rápido
102,Ruptura de Dragón
103,Aplastamiento de Dragón
104,Ruptura Evasiva
105,Embestida Evasiva
106,Maestro de Combos
107,Carga Rápida
108,Súper Sentidos
109,Anillo de Broly
110,Poder Namekiano
111,Poder de la Tierra
112,Poder Universal
113,Carga de Aura Azul
114,Carga de Aura Morada
115,Carga de Aura Amarilla
116,Carga de Aura Roja
117,Carga de Aura Verde
118,Carga de Aura Blanca
119,Carga de Aura Rosa
120,Carga de Aura Violeta
121,Carga de Aura Definitiva
122,Carga de Aura Definitiva 3
123,Carga de Aura Definitiva 4
124,Entrenamiento del Maestro Roshi
125,Entrenamiento del Rey Kai
126,Beso de #18
127,Bufanda de #17
128,Máquina Médica
129,Vacío 11
130,Vacío 12
131,Vacío 13
132,Vacío 14
133,Vacío 15
134,Vacío 16
135,Vacío 17
136,Apoyo de Launch
137,Tipo Goku
138,Tipo Vegeta
139,Tipo Gohan
140,Tipo Trunks
141,Tipo Piccolo
142,Tipo Krillin
143,Tipo Tien
144,Tipo Chiaotzu
145,Tipo Yajirobe
146,Tipo Freezer
147,Tipo Cell
148,Tipo Majin Buu
149,Tipo Broly
150,Tipo Ginyu
151,Tipo Recoome
152,Vacío 18
153,Vacío 19
154,Vacío 20
155,Vacío 21
156,Vacío 22
157,Vacío 23
158,Vacío 24
159,Vacío 25
160,Vacío 26
161,Vacío 27
162,Guerrero Definitivo 1
163,Guerrero Definitivo 2
164,Guerrero Definitivo 3
165,Guerrero Definitivo 4
166,Guerrero Definitivo 5
167,Guerrero Definitivo 6
168,Guerrero Definitivo 7
169,Guerrero Definitivo 8
170,Ataque -25
171,Ataque -24
172,Ataque -23
173,Ataque -22
174,Ataque -21
175,Ataque -20
176,Ataque -19
177,Ataque -18
178,Ataque -17
179,Ataque -16
180,Ataque -15
181,Ataque -14
182,Ataque -13
183,Ataque -12
184,Ataque -11
185,Ataque -10
186,Ataque -9
187,Ataque -8
188,Ataque -7
189,Ataque -6
190,Ataque -5
191,Ataque -4
192,Ataque -3
193,Ataque -2
194,Ataque -1
195,Ataque 0
196,Ataque +1
197,Ataque +2
198,Ataque +3
199,Ataque +4
200,Ataque +5
201,Ataque +6
202,Ataque +7
203,Ataque +8
204,Ataque +9
205,Ataque +10
206,Ataque +11
207,Ataque +12
208,Ataque +13
209,Ataque +14
210,Ataque +15
211,Ataque +16
212,Ataque +17
213,Ataque +18
214,Ataque +19
215,Ataque +20
216,Ataque +21
217,Ataque +22
218,Ataque +23
219,Ataque +24
220,Ataque +25
221,Ataque +26
222,Ataque +27
223,Ataque +28
224,Ataque +29
225,Ataque +30
226,Ataque +31
227,Ataque +32
228,Ataque +33
229,Ataque +34
230,Ataque +35
231,Ataque +32
232,Ataque +37
233,Ataque +38
234,Ataque +39
"""


def load_zitems_from_text(text):
  table = {}
  reader = csv.DictReader(io.StringIO(text))
  for row in reader:
    try:
      table[int(row["dec"])] = row["nombre"]
    except (KeyError, ValueError):
      continue
  return table


ZITEMS = load_zitems_from_text(ZITEMS_CSV_DATA)
EMPTY_ZIT_VALUE = 0x00000000

ZIT_PATTERN = re.compile(r"\$zit(\d+)\s*:\s*&([0-9A-Fa-f]+)")
ZIT_EVENT_PATTERN = re.compile(r"^\s*\$(EV_\w+)\s*:\s*<")
ZIT_ACTOR_BLOCK_PATTERN = re.compile(r"\$(?:actor|name)\s*:\s*\$(\w+)")


def lookup_zitem(value: int) -> str:
  if value == EMPTY_ZIT_VALUE:
    return "— (vacío / sin asignar)"
  if value in ZITEMS:
    return ZITEMS[value]
  return f"Desconocido (índice {value} fuera de la tabla)"


def parse_zit_value(text: str):
  t = text.strip()
  if t == "":
    raise ValueError("Valor vacío.")
  low = t.lower()
  if low in ("vacio", "vacío", "none", "-"):
    return EMPTY_ZIT_VALUE
  if t.startswith("&"):
    t = t[1:]
  if re.fullmatch(r"[0-9]+", t):
    val = int(t, 10)
  elif re.fullmatch(r"[0-9A-Fa-f]+", t):
    val = int(t, 16)
  else:
    raise ValueError(f"No se pudo interpretar el valor: {text!r}")
  if val < 0 or val > 0xFFFFFFFF:
    raise ValueError("El valor debe caber en 32 bits (0 a FFFFFFFF).")
  return val


class ZitLinesManager:
  """Gestor de campos $zit que opera sobre texto en memoria (self.file_content
  del editor de BT3), en lugar de un archivo propio como en la herramienta
  original. Permite normalizar, listar y editar los 8 $zit por bloque."""

  def __init__(self, text=""):
    self.set_text(text)

  def set_text(self, text):
    self.lines = text.splitlines(keepends=True) if text else []
    self.entries = []
    self._parse()

  def get_text(self):
    return "".join(self.lines)

  def normalize_all_lines(self):
    """Asegura que cada línea con zits tenga los 8 zits ordenados como:
    $zit8, $zit1..$zit7, rellenando con 00000000 y con 8 dígitos hex."""
    for line_idx, line in enumerate(self.lines):
      matches = list(ZIT_PATTERN.finditer(line))
      if not matches:
        continue

      zit_dict = {}
      for m in matches:
        zit_dict[int(m.group(1))] = m.group(2)

      order = [8, 1, 2, 3, 4, 5, 6, 7]
      complete_zit_data = []
      for num in order:
        val = zit_dict.get(num, "00000000")
        if len(val) < 8:
          val = val.zfill(8)
        complete_zit_data.append((num, val))

      ordered_str = " ".join(f"$zit{num}: &{val}" for num, val in complete_zit_data)

      cleaned = line
      for m in reversed(matches):
        cleaned = cleaned[:m.start()] + cleaned[m.end():]

      first_pos = matches[0].start()
      self.lines[line_idx] = cleaned[:first_pos] + " " + ordered_str + " " + cleaned[first_pos:]
      self.lines[line_idx] = re.sub(r"[ \t]+", " ", self.lines[line_idx]).replace(" }", "}").replace("{ ", "{")

    self._parse()

  def _parse(self):
    self.entries = []
    current_event = "(fuera de evento)"
    current_actor = "-"

    for line_idx, line in enumerate(self.lines):
      ev_match = ZIT_EVENT_PATTERN.match(line)
      if ev_match:
        current_event = ev_match.group(1)

      actor_matches = ZIT_ACTOR_BLOCK_PATTERN.findall(line)
      if actor_matches:
        current_actor = actor_matches[-1]

      for m in ZIT_PATTERN.finditer(line):
        field_idx = m.group(1)
        hex_val = m.group(2)
        start, end = m.span(2)
        dec_val = int(hex_val, 16)
        self.entries.append({
            "line_idx": line_idx,
            "start": start,
            "end": end,
            "width": len(hex_val),
            "evento": current_event,
            "actor": current_actor,
            "campo": f"zit{field_idx}",
            "hex": hex_val.upper(),
            "dec": dec_val,
            "nombre": lookup_zitem(dec_val),
        })

  def apply_edit(self, entry, new_dec: int):
    width = 8
    new_hex = format(new_dec, f"0{width}X")
    if len(new_hex) > width:
      width = len(new_hex)

    line_idx = entry["line_idx"]
    start, end = entry["start"], entry["end"]
    line = self.lines[line_idx]
    new_line = line[:start] + new_hex + line[end:]
    shift = len(new_hex) - (end - start)
    self.lines[line_idx] = new_line

    entry["hex"] = new_hex
    entry["dec"] = new_dec
    entry["nombre"] = lookup_zitem(new_dec)
    entry["end"] = start + len(new_hex)
    entry["width"] = width

    if shift:
      for other in self.entries:
        if other is entry:
          continue
        if other["line_idx"] == line_idx and other["start"] > start:
          other["start"] += shift
          other["end"] += shift


class ZitEditDialog(tk.Toplevel):
  """Cuadro de diálogo para editar un $zit concreto, con lista buscable de
  la tabla completa de Z-Items y campo manual para valores hex/dec."""

  def __init__(self, parent, entry, on_accept):
    super().__init__(parent)
    self.entry = entry
    self.on_accept = on_accept
    self.title(f"Editar {entry['campo']} — {entry['actor']} ({entry['evento']})")
    self.geometry("480x480")
    self.resizable(False, False)
    self.transient(parent)
    self.grab_set()

    info = (
        f"Evento: {entry['evento']}    Actor: {entry['actor']}    "
        f"Campo: {entry['campo']}\n"
        f"Valor actual: &{entry['hex']}  (dec {entry['dec']})  -> {entry['nombre']}"
    )
    ttk.Label(self, text=info, justify="left", wraplength=460).pack(
        fill="x", padx=10, pady=(10, 6)
    )

    ttk.Separator(self).pack(fill="x", padx=10, pady=4)

    ttk.Label(self, text="Buscar Z-Item en la lista:").pack(
        anchor="w", padx=10, pady=(6, 0)
    )
    self.search_var = tk.StringVar()
    self.search_var.trace_add("write", lambda *a: self._refresh_list())
    search_entry = ttk.Entry(self, textvariable=self.search_var)
    search_entry.pack(fill="x", padx=10, pady=(2, 6))

    list_frame = ttk.Frame(self)
    list_frame.pack(fill="both", expand=True, padx=10)
    self.listbox = tk.Listbox(list_frame, activestyle="dotbox")
    self.listbox.pack(side="left", fill="both", expand=True)
    sb = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
    self.listbox.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    self.listbox.bind("<<ListboxSelect>>", self._on_select)
    self.listbox.bind("<Double-Button-1>", lambda e: self._accept())

    self._all_items = sorted(ZITEMS.items())
    self._visible_items = []
    self._refresh_list()

    ttk.Separator(self).pack(fill="x", padx=10, pady=6)

    manual_frame = ttk.Frame(self)
    manual_frame.pack(fill="x", padx=10, pady=(0, 6))
    ttk.Label(
        manual_frame,
        text="Valor manual (hex, decimal, o 'vacio' para &00000000):",
    ).pack(anchor="w")
    self.manual_var = tk.StringVar(value=f"&{entry['hex']}")
    ttk.Entry(manual_frame, textvariable=self.manual_var).pack(fill="x", pady=(2, 0))
    ttk.Label(
        manual_frame,
        text="Útil para valores fuera de la tabla o correcciones directas.",
        foreground="#666666",
    ).pack(anchor="w", pady=(2, 0))

    btns = ttk.Frame(self)
    btns.pack(fill="x", padx=10, pady=10)
    ttk.Button(btns, text="Cancelar", command=self.destroy).pack(side="right")
    ttk.Button(btns, text="Aceptar", command=self._accept).pack(side="right", padx=(0, 6))

  def _refresh_list(self):
    term = self.search_var.get().strip().lower()
    self.listbox.delete(0, "end")
    self._visible_items = []
    for dec, nombre in self._all_items:
      label = f"{dec:>3} - {nombre}"
      if term and term not in label.lower():
        continue
      self.listbox.insert("end", label)
      self._visible_items.append((dec, nombre))

  def _on_select(self, _event):
    sel = self.listbox.curselection()
    if not sel:
      return
    dec, _nombre = self._visible_items[sel[0]]
    self.manual_var.set(str(dec))

  def _accept(self):
    try:
      new_dec = parse_zit_value(self.manual_var.get())
    except ValueError as e:
      messagebox.showerror("Valor inválido", str(e), parent=self)
      return
    self.on_accept(new_dec)
    self.destroy()




# --------------------------------------------------------------------------
# Editor de posición/rotación ($Set_transform) - integrado desde
# BT3_position_editor.py
# --------------------------------------------------------------------------

POS_TRANSFORM_RE = re.compile(
    r"\$Set_transform:\{\$actor:\$(?P<actor>\w+)\s+"
    r"\$loc:F\[\s*(?P<lx>-?\d+\.\d+),\s*(?P<ly>-?\d+\.\d+),\s*(?P<lz>-?\d+\.\d+)\]\s+"
    r"\$rot:F\[\s*(?P<rx>-?\d+\.\d+),\s*(?P<ry>-?\d+\.\d+),\s*(?P<rz>-?\d+\.\d+)\]\}"
)

POS_ACTOR_COLORS = {
    "pla0": "#2E86FF", "pla1": "#4FB0FF", "pla2": "#8FD3FF",
    "cpu0": "#FF3B30", "cpu1": "#FF7A6E", "cpu2": "#FFAFA6",
}


def pos_color_for(actor):
  return POS_ACTOR_COLORS.get(actor, "#8A8A8A")


# ============================================================================
# --- GESTIÓN DE BLOQUES $EV_XX (insertar / eliminar eventos completos) ---
# Un bloque de evento tiene la forma "$EV_XX:< ... $End_cutscn >" y puede
# incluir cinemática (cámara/animaciones) o ser una versión simple que solo
# enlaza desencadenadores y eventos.
# ============================================================================

EV_BLOCK_PATTERN = re.compile(
    r"(?P<full>\$EV_(?P<id>\w+)\s*:\s*<.*?\$End_cutscn\s*>)",
    re.IGNORECASE | re.DOTALL,
)


class PosTransform:
  """Representa una ocurrencia de $Set_transform en el archivo actual."""

  def __init__(self, event, actor, loc, rot, start, end):
    self.event = event
    self.actor = actor
    self.loc = list(loc)   # [x, y, z]
    self.rot = list(rot)   # [rx, ry, rz]
    self.start = start     # offset en self.file_content al momento del parseo
    self.end = end
    self.modified = False

  def label(self):
    return f"{self.event}  |  {self.actor}"

  def format(self):
    """Regenera el texto $Set_transform con los valores actuales."""
    x, y, z = self.loc
    rx, ry, rz = self.rot
    return (
        f"$Set_transform:{{$actor:${self.actor} "
        f"$loc:F[{x:.6f}, {y:.6f}, {z:.6f}] "
        f"$rot:F[{rx:.6f}, {ry:.6f}, {rz:.6f}]}}"
    )


def parse_pos_transforms(raw_text):
  """Encuentra todos los $Set_transform y a qué evento pertenece cada uno."""
  ev_matches = list(re.finditer(EV_HEADER_RE, raw_text))

  def event_for_offset(offset):
    for ev_m in reversed(ev_matches):
      if ev_m.start() < offset:
        return ev_m.group(1).replace('"', "").replace("'", "")
    return "DESCONOCIDO"

  transforms = []
  for m in POS_TRANSFORM_RE.finditer(raw_text):
    loc = (float(m.group("lx")), float(m.group("ly")), float(m.group("lz")))
    rot = (float(m.group("rx")), float(m.group("ry")), float(m.group("rz")))
    ev = event_for_offset(m.start())
    transforms.append(PosTransform(ev, m.group("actor"), loc, rot, m.start(), m.end()))
  return transforms


# --------------------------------------------------------------------------
# Sistema de temas dinámicos / personalizables
# --------------------------------------------------------------------------

APP_COPYRIGHT = "© CEDAJ,Epidarkrai-2026"
APP_CREDITS = ["RidJuampa", "Furuya Dthem", "Vras", "Vive", "Ryuji 突風", "Wesley Moretto"]


def _clamp8(v):
  return max(0, min(255, int(v)))


def _hex_to_rgb(h):
  h = h.lstrip("#")
  if len(h) == 3:
    h = "".join(c * 2 for c in h)
  return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb_to_hex(rgb):
  return "#%02x%02x%02x" % tuple(_clamp8(c) for c in rgb)


def shade_hex(h, amount):
  """amount > 0 aclara, amount < 0 oscurece."""
  r, g, b = _hex_to_rgb(h)
  return _rgb_to_hex((r + amount, g + amount, b + amount))


def mix_hex(h1, h2, t):
  """Interpola entre dos colores hex (t entre 0 y 1)."""
  r1, g1, b1 = _hex_to_rgb(h1)
  r2, g2, b2 = _hex_to_rgb(h2)
  return _rgb_to_hex((
      r1 + (r2 - r1) * t,
      g1 + (g2 - g1) * t,
      b1 + (b2 - b1) * t,
  ))


THEME_PRESETS = {
    "Azul Boreal":    {"bg": "#10141a", "frame_bg": "#1a212c", "accent": "#2f8fef"},
    "Violeta Gala":   {"bg": "#150f1e", "frame_bg": "#20182e", "accent": "#a35cff"},
    "Esmeralda Namek": {"bg": "#0d1712", "frame_bg": "#15241d", "accent": "#2ecc8f"},
    "Carmesí Saiyan": {"bg": "#190f11", "frame_bg": "#241318", "accent": "#ff4757"},
    "Ámbar Kaio":     {"bg": "#191408", "frame_bg": "#251d0f", "accent": "#f5a623"},
}

DEFAULT_THEME_NAME = "Azul Boreal"




# ============================================================
# MÓDULO INTEGRADO: BT3 GSC <-> GSCF Converter (bidireccional)
# ============================================================

# Base de datos del GSC Reader (funciones, propiedades y tablas de nombres)
DB = {'func_map': {1: 'Wait for Period of Time',
              2: 'Scenario Identifier',
              3: 'Scene Start',
              4: 'Scene End & Battle Start',
              5: 'Store Character Positions',
              6: 'Store VFX Switches',
              7: 'Store Conditional Properties',
              8: 'Post-Cutscene Event',
              9: 'Battle End',
              10: 'Battle Settings',
              11: 'Team Settings',
              12: 'Character Settings',
              13: "Store Player's Character Changes",
              14: "Store Opponent's Character Changes",
              15: 'Store Audio-Related Properties',
              16: 'Rewards',
              701: 'Load TXT PAK',
              702: 'Load LPS PAK',
              801: 'Assign Character Position & Rotation',
              802: 'Assign Character Position Only',
              803: 'Assign Character Rotation Only',
              804: 'Make Character Visible',
              805: 'Make Character Invisible',
              806: 'Enable Lingering Aura',
              807: 'Disable Lingering Aura',
              808: 'Enable Ki Charge Aura',
              809: 'Disable Ki Charge Aura',
              810: 'Enable MAX POWER Mode Explosion',
              901: 'Assign Animation',
              902: 'Enable Character Movement',
              1001: 'Trigger Fade-Out',
              1002: 'Trigger Fade-In',
              1003: 'Stop Current Fade',
              1201: 'Primary Camera Point',
              1202: 'Secondary Camera Point',
              1203: 'Reset Battle Camera',
              1204: 'Trigger Camera Shake',
              1205: 'Stop Camera Shake',
              1301: 'Load String in Memory (for debug reasons & no longer functional)',
              1302: 'Subtitle Settings',
              1501: 'Music Change',
              1502: 'Turn Down/Off Previous Music Volume',
              1601: 'Play Sound from SE_Battle.pak',
              1602: 'Play Any ADX from Scenario',
              1603: 'Play Character Voice Line',
              1701: 'Freeze Cutscene until Button Press'},
 'func_param_map': {1: ['Time (s)'],
                    2: ['GSC Name'],
                    8: ['Event ID', 'Character ID'],
                    9: ['Battle Outcome ID'],
                    10: ['Map', 'Music', 'Battle Time (s)', 'Referee', 'Enable Map Destruction'],
                    11: ['Team Index', 'Number of Teammates'],
                    12: ['Character Index', 'Character', 'Color', 'Damaged', 'COM Level', 'Z-Item #8', 'Health (%)',
                         'Z-Item #1', 'Z-Item #2', 'Z-Item #3', 'Z-Item #4', 'Z-Item #5', 'Z-Item #6', 'Z-Item #7'],
                    16: ['Z-Points (Easy)', 'Z-Points (Normal)', 'Z-Points (Hard)', 'Z-Item #1', 'Z-Item #2',
                         'Z-Item #3', 'Map #1', 'Map #2', 'Map #3', 'Character #1', 'Character #2', 'Character #3',
                         'Scenario #1', 'Scenario #2', 'Scenario #3'],
                    801: ['Character Index', 'Position (X)', 'Position (Y)', 'Position (Z)', 'Rotation (X)',
                          'Rotation (Y)', 'Rotation (Z)'],
                    802: ['Character Index', 'Position (X)', 'Position (Y)', 'Position (Z)'],
                    803: ['Character Index', 'Rotation (X)', 'Rotation (Y)', 'Rotation (Z)'],
                    804: ['Character Index'],
                    805: ['Character Index'],
                    806: ['Character Index'],
                    807: ['Character Index'],
                    808: ['Character Index'],
                    809: ['Character Index'],
                    810: ['Character Index'],
                    901: ['Character Index', 'ANM Name'],
                    1001: ['Time (s)'],
                    1002: ['Time (s)'],
                    1201: ['Position (X)', 'Position (Y)', 'Position (Z)', 'Rotation (Y)', 'Rotation (X)',
                           'Rotation (Z)'],
                    1202: ['Time (s)', 'Position (X)', 'Position (Y)', 'Position (Z)', 'Rotation (Y)', 'Rotation (X)',
                           'Rotation (Z)'],
                    1204: ['Force/Intensity'],
                    1301: ['String'],
                    1501: ['Music'],
                    1601: ['VAG ID'],
                    1602: ['ADX ID'],
                    1603: ['Character Index', 'Voice Line ID'],
                    1701: ['Button ID']},
 'prop_map': {(48, 13): 'Replace Z-Item #1',
              (48, 14): 'Replace Z-Item #1',
              (49, 13): 'Replace Z-Item #2',
              (49, 14): 'Replace Z-Item #2',
              (50, 13): 'Replace Z-Item #3',
              (50, 14): 'Replace Z-Item #3',
              (51, 13): 'Replace Z-Item #4',
              (51, 14): 'Replace Z-Item #4',
              (52, 13): 'Replace Z-Item #5',
              (52, 14): 'Replace Z-Item #5',
              (53, 13): 'Replace Z-Item #6',
              (53, 14): 'Replace Z-Item #6',
              (54, 13): 'Replace Z-Item #7',
              (54, 14): 'Replace Z-Item #7',
              (66, 13): 'Add Blast Stocks',
              (66, 14): 'Add Blast Stocks',
              (67, 13): 'Assign Properties to Character',
              (67, 14): 'Assign Properties to Character',
              (67, 1302): 'Text Outline Color',
              (70, 13): 'Add Ki',
              (70, 14): 'Add Ki',
              (72, 13): 'Add Health',
              (72, 14): 'Add Health',
              (73, 13): 'Assign Ki',
              (73, 14): 'Assign Ki',
              (79, 1302): 'Text Outline Size',
              (84, 1302): 'Symbol',
              (87, 1001): 'Change Fade-Out Color to White',
              (97, 7): 'Scene Link',
              (97, 1302): 'Text Size',
              (98, 13): 'Assign Blast Stocks',
              (98, 14): 'Assign Blast Stocks',
              (99, 1302): 'Text Color',
              (100, 1302): 'Text Position',
              (102, 13): 'Assign Ki',
              (102, 14): 'Assign Ki',
              (104, 13): 'Assign Health',
              (104, 14): 'Assign Health',
              (104, 1602): 'Play Audio Concurrently',
              (108, 901): 'Enable ANM Loop',
              (108, 1202): 'Additional Camera Point',
              (108, 1203): 'Enable Camera Shake Loop',
              (108, 1302): 'Text Region',
              (110, 1302): 'Text is Grey',
              (112, 1302): 'Text Padding',
              (115, 1302): 'Text Scale',
              (116, 901): 'ANM Speed Multiplier',
              (118, 7): 'Audio Link',
              (118, 15): 'Audio-Related Property',
              (119, 901): 'Wait until End of ANM',
              (119, 1001): 'Wait until End of Fade',
              (119, 1202): 'Wait until End of Camera',
              (119, 1302): 'Text Alignment',
              (119, 1502): 'Wait until End of Music',
              (119, 1602): 'Wait until End of ADX',
              (119, 1603): 'Wait until End of Voice Line'},
 'prop_param_map': {(48, 13): ['Z-Item #1'],
                    (48, 14): ['Z-Item #1'],
                    (49, 13): ['Z-Item #2'],
                    (49, 14): ['Z-Item #2'],
                    (50, 13): ['Z-Item #3'],
                    (50, 14): ['Z-Item #3'],
                    (51, 13): ['Z-Item #4'],
                    (51, 14): ['Z-Item #4'],
                    (52, 13): ['Z-Item #5'],
                    (52, 14): ['Z-Item #5'],
                    (53, 13): ['Z-Item #6'],
                    (53, 14): ['Z-Item #6'],
                    (54, 13): ['Z-Item #7'],
                    (54, 14): ['Z-Item #7'],
                    (66, 13): ['Blast Stock Amount'],
                    (67, 13): ['Character Index'],
                    (67, 1302): ['Red', 'Green', 'Blue', 'Opacity'],
                    (70, 13): ['Ki (%)'],
                    (70, 14): ['Ki (%)'],
                    (72, 13): ['Health (%)'],
                    (72, 14): ['Health (%)'],
                    (73, 13): ['Ki (%)'],
                    (73, 14): ['Ki (%)'],
                    (79, 1302): ['Width', 'Height'],
                    (84, 1302): ['Type'],
                    (97, 7): ['Condition', 'Scene ID'],
                    (97, 1302): ['Width', 'Height'],
                    (98, 13): ['Blast Stock Amount'],
                    (98, 14): ['Blast Stock Amount'],
                    (99, 1302): ['Red', 'Green', 'Blue', 'Opacity'],
                    (100, 1302): ['Position (X)', 'Position (Y)'],
                    (102, 13): ['Ki (%)'],
                    (102, 14): ['Ki (%)'],
                    (104, 13): ['Health (%)'],
                    (104, 14): ['Health (%)'],
                    (104, 1602): ['Audio Channel ID'],
                    (108, 1202): ['Time (s)', 'Position (X)', 'Position (Y)', 'Position (Z)', 'Rotation (Y)',
                                  'Rotation (X)', 'Rotation (Z)'],
                    (108, 1302): ['Region ID'],
                    (110, 1302): ['Enable Grey Text'],
                    (112, 1302): ['Padding (Vertical)', 'Padding (Horizontal)'],
                    (115, 1302): ['Coefficient'],
                    (116, 901): ['Coefficient'],
                    (118, 7): ['Condition', 'Voice Line ID'],
                    (118, 15): ['Voice Line ID', 'Character Index'],
                    (119, 1302): ['Alignment ID']},
 'tables': {'anm': {0: 'GROUND',
                    1: 'GROUND_TIRED',
                    2: 'MOVE_FAR_IN',
                    3: 'MOVE_FAR_LOOP',
                    4: 'MOVE_FAR_L_IN',
                    5: 'MOVE_FAR_L_LOOP',
                    6: 'MOVE_FAR_R_IN',
                    7: 'MOVE_FAR_R_LOOP',
                    8: 'MOVE_NEAR_F',
                    9: 'MOVE_NEAR_B',
                    10: 'MOVE_NEAR_L',
                    11: 'MOVE_NEAR_R',
                    12: 'DASH_F_IN',
                    13: 'DASH_F_LOOP',
                    14: 'DASH_F_OUT',
                    15: 'DASH_L_IN',
                    16: 'DASH_L_LOOP',
                    17: 'DASH_L_OUT',
                    18: 'DASH_R_IN',
                    19: 'DASH_R_LOOP',
                    20: 'DASH_R_OUT',
                    21: 'DASH_BREAK_IN',
                    22: 'DASH_BREAK_LOOP',
                    23: 'DASH_BREAK_OUT',
                    24: 'DDASH_IN',
                    25: 'DDASH_LOOP',
                    26: 'DDASH_OUT',
                    27: 'SWAY_F',
                    28: 'SWAY_B',
                    29: 'SWAY_L',
                    30: 'SWAY_R',
                    31: 'SWAY_OUT',
                    32: 'JUMP_IN',
                    33: 'JUMP_UP',
                    34: 'JUMP_DOWN',
                    35: 'JUMP_OUT',
                    36: 'RISING_IN',
                    37: 'RISING_OUT',
                    38: 'FLY',
                    39: 'FLY_TIRED',
                    40: 'FLY_SWAY_B',
                    41: 'FLY_SWAY_L',
                    42: 'FLY_SWAY_R',
                    43: 'FLYUP',
                    44: 'FLYDOWN_IN',
                    45: 'FLYDOWN_LOOP',
                    46: 'FLYUP_QUICK_IN',
                    47: 'FLYUP_QUICK_LOOP',
                    48: 'FLYUP_QUICK_OUT',
                    49: 'FLYDOWN_QUICK_IN',
                    50: 'FLYDOWN_QUICK_LOOP',
                    51: 'FLYDOWN_QUICK_OUT',
                    52: 'CHARGE_IN',
                    53: 'CHARGE_LOOP',
                    54: 'CHARGE_MAX',
                    55: 'STRIKE_01',
                    56: 'STRIKE_02',
                    57: 'STRIKE_03',
                    58: 'STRIKE_04',
                    59: 'STRIKE_05',
                    60: 'STRIKE_06',
                    61: 'STRIKE_07',
                    62: 'STRIKE_08',
                    63: 'STRIKE_09',
                    64: 'STRIKE_10',
                    65: 'LIFT_STRIKE_IN',
                    66: 'LIFT_STRIKE_LOOP',
                    67: 'LIFT_STRIKE_OUT',
                    68: 'GROUND_SLASH_IN',
                    69: 'GROUND_SLASH_LOOP',
                    70: 'GROUND_SLASH_OUT',
                    71: 'HEAVY_FINISH_IN',
                    72: 'HEAVY_FINISH_LOOP',
                    73: 'HEAVY_FINISH_OUT',
                    74: 'CHARGED_STRIKE_F_IN',
                    75: 'CHARGED_STRIKE_F_LOOP',
                    76: 'CHARGED_STRIKE_F_OUT',
                    77: 'COMBO_STRIKE_IN',
                    78: 'COMBO_STRIKE_LOOP',
                    79: 'COMBO_STRIKE_OUT',
                    80: 'CHARGED_STRIKE_U_IN',
                    81: 'CHARGED_STRIKE_LOOP_U',
                    82: 'CHARGED_STRIKE_OUT_U',
                    83: 'CHARGED_STRIKE_IN_D',
                    84: 'CHARGED_STRIKE_LOOP_D',
                    85: 'CHARGED_STRIKE_OUT_D',
                    86: 'CHARGED_STRIKE_L_IN',
                    87: 'CHARGED_STRIKE_L_LOOP',
                    88: 'CHARGED_STRIKE_L_OUT',
                    89: 'CHARGED_STRIKE_R_IN',
                    90: 'CHARGED_STRIKE_R_LOOP',
                    91: 'CHARGED_STRIKE_R_OUT',
                    92: 'RUSH_STRIKE_F_IN',
                    93: 'RUSH_STRIKE_F_LOOP',
                    94: 'RUSH_STRIKE_F_OUT',
                    95: 'RUSH_STRIKE_U_IN',
                    96: 'RUSH_STRIKE_U_LOOP',
                    97: 'RUSH_STRIKE_U_OUT',
                    98: 'RUSH_STRIKE_D_IN',
                    99: 'RUSH_STRIKE_D_LOOP',
                    100: 'RUSH_STRIKE_D_OUT',
                    101: 'RUSH_STRIKE_L_IN',
                    102: 'RUSH_STRIKE_L_LOOP',
                    103: 'RUSH_STRIKE_L_OUT',
                    104: 'RUSH_STRIKE_R_IN',
                    105: 'RUSH_STRIKE_R_LOOP',
                    106: 'RUSH_STRIKE_R_OUT',
                    107: 'DASH_STRIKE_IN',
                    108: 'DASH_STRIKE_LOOP',
                    109: 'DASH_STRIKE_OUT',
                    110: 'JUMP_STRIKE_IN',
                    111: 'JUMP_STRIKE_LOOP',
                    112: 'JUMP_STRIKE_OUT',
                    113: 'KI_BLASTS_F_IN',
                    114: 'KI_BLASTS_F_LOOP',
                    115: 'KI_BLASTS_U_IN',
                    116: 'KI_BLASTS_U_LOOP',
                    117: 'KI_BLASTS_D_IN',
                    118: 'KI_BLASTS_D_LOOP',
                    119: 'DASH_BLASTS_F',
                    120: 'DASH_BLASTS_L',
                    121: 'DASH_BLASTS_R',
                    122: 'JUMP_BLASTS',
                    123: 'CHARGED_KI_BLASTS_F_IN',
                    124: 'CHARGED_KI_BLASTS_F_LOOP',
                    125: 'CHARGED_KI_BLASTS_F_OUT',
                    126: 'CHARGED_KI_BLASTS_UP_IN',
                    127: 'CHARGED_KI_BLASTS_UP_LOOP',
                    128: 'CHARGED_KI_BLASTS_UP_OUT',
                    129: 'CHARGED_KI_BLASTS_DOWN_IN',
                    130: 'CHARGED_KI_BLASTS_DOWN_LOOP',
                    131: 'CHARGED_KI_BLASTS_DOWN_OUT',
                    132: 'CHARGED_DASH_BLASTS_F_IN',
                    133: 'CHARGED_DASH_BLASTS_F_LOOP',
                    134: 'CHARGED_DASH_BLASTS_F_OUT',
                    135: 'CHARGED_DASH_BLASTS_L_IN',
                    136: 'CHARGED_DASH_BLASTS_L_LOOP',
                    137: 'CHARGED_DASH_BLASTS_L_OUT',
                    138: 'CHARGED_DASH_BLASTS_R_IN',
                    139: 'CHARGED_DASH_BLASTS_R_LOOP',
                    140: 'CHARGED_DASH_BLASTS_R_OUT',
                    141: 'CHARGED_JUMP_BLASTS_IN',
                    142: 'CHARGED_JUMP_BLASTS_LOOP',
                    143: 'CHARGED_JUMP_BLASTS_OUT',
                    144: 'KIAI_CANNON_IN',
                    145: 'KIAI_CANNON_LOOP',
                    146: 'KIAI_CANNON_OUT',
                    147: 'FLYING_KICK',
                    148: 'THROW_IN',
                    149: 'THROW_LOOP',
                    150: 'THROW_EVENT',
                    151: 'THROW_ENEMY',
                    152: 'THROW_OUT',
                    153: 'THROW_D_IN',
                    154: 'THROW_D_LOOP',
                    155: 'THROW_D_OUT',
                    156: 'THROW_BLOCK_IN',
                    157: 'THROW_BLOCK_OUT',
                    158: 'F_DAMAGE',
                    159: 'F_DAMAGE_L',
                    160: 'F_DAMAGE_R',
                    161: 'F_DAMAGE_B',
                    162: 'B_DAMAGE',
                    163: 'B_DAMAGE_L',
                    164: 'B_DAMAGE_R',
                    165: 'B_DAMAGE_B',
                    166: 'DAMAGE_11',
                    167: 'DAMAGE_12',
                    168: 'DAMAGE_13',
                    169: 'DAMAGE_14',
                    170: 'DAMAGE_15',
                    171: 'DAMAGE_16',
                    172: 'DAMAGE_17',
                    173: 'DAMAGE_18',
                    174: 'DAMAGE_HEAVY_F',
                    175: 'DAMAGE_HEAVY_B',
                    176: 'DAMAGE_21',
                    177: 'DAMAGE_22',
                    178: 'DAMAGE_23',
                    179: 'DAMAGE_24',
                    180: 'DAMAGE_25',
                    181: 'DAMAGE_26',
                    182: 'DAMAGE_27',
                    183: 'PARALYSIS',
                    184: 'GUARDBREAK',
                    185: 'DAMAGE_LYING_UP',
                    186: 'DAMAGE_LYING_DOWN',
                    187: 'DAMAGE_EXPLOSION_FRONT',
                    188: 'DAMAGE_EXPLOSION_BACK',
                    189: 'DAMAGE_ROLLING_BACK_IN',
                    190: 'DAMAGE_ROLLING_BACK_LOOP',
                    191: 'DAMAGE_ROLLING_BACK_OUT',
                    192: 'DAMAGE_ROLLING_IN',
                    193: 'DAMAGE_ROLLING_LOOP',
                    194: 'DAMAGE_ROLLING_OUT',
                    195: 'DAMAGE_CHARGED_ATTACK_IN',
                    196: 'DAMAGE_CHARGED_ATTACK_LOOP',
                    197: 'DAMAGE_CHARGED_ATTACK_OUT',
                    198: 'DAMAGE_FALLING_DOWN_1',
                    199: 'DAMAGE_FALLING_DOWN_2',
                    200: 'DAMAGE_FALLING_DOWN_3',
                    201: 'DAMAGE_FALLING_DOWN_4',
                    202: 'DAMAGE_28',
                    203: 'DAMAGE_29',
                    204: 'DAMAGE_30',
                    205: 'DAMAGE_31',
                    206: 'DAMAGE_32',
                    207: 'DAMAGE_33',
                    208: 'DAMAGE_34',
                    209: 'DAMAGE_35',
                    210: 'DAMAGE_LYING_PARALYZED_IN',
                    211: 'DAMAGE_LYING_PARALYZED_LOOP',
                    212: 'DAMAGE_LYING_TIRED_IN',
                    213: 'DAMAGE_LYING_TIRED_LOOP',
                    214: 'DAMAGE_LYING_TIRED_OUT',
                    215: 'DAMAGE_FLOATING_ON_WATER_IN',
                    216: 'DAMAGE_FLOATING_ON_WATER_LOOP',
                    217: 'DAMAGE_FALL_AFTER_DIE',
                    218: 'DAMAGE_36',
                    219: 'DAMAGE_37',
                    220: 'DAMAGE_GROUND_SLASH_IN',
                    221: 'DAMAGE_GROUND_SLASH_LOOP',
                    222: 'DAMAGE_SONIC_SWAY_1',
                    223: 'DAMAGE_SONIC_SWAY_2',
                    224: 'DAMAGE_ROLLING_HAMMER_IN',
                    225: 'DAMAGE_ROLLING_HAMMER_LOOP',
                    226: 'GET_UP_IN',
                    227: 'GET_UP_LOOP',
                    228: 'GET_UP_OUT',
                    229: 'GET_UP_4',
                    230: 'GET_UP_5',
                    231: 'GET_UP_6',
                    232: 'DAMAGE_38',
                    233: 'DAMAGE_39',
                    234: 'DAMAGE_40',
                    235: 'DAMAGE_41',
                    236: 'DAMAGE_Z_COUNTER_1',
                    237: 'DAMAGE_Z_COUNTER_2',
                    238: 'DAMAGE_42',
                    239: 'DAMAGE_43',
                    240: 'BLOCKING_IN',
                    241: 'BLOCKING_LOOP',
                    242: 'BLOCKING_UP_IN',
                    243: 'BLOCKING_UP_LOOP',
                    244: 'BLOCKING_DOWN_IN',
                    245: 'BLOCKING_DOWN_LOOP',
                    246: 'BLOCKING_HIT_IN',
                    247: 'BLOCKING_HIT_LOOP',
                    248: 'PARRY_COMBO_POSTURE',
                    249: 'PARRY_COMBO_STRIKE',
                    250: 'PARRY_KI_BLAST_1',
                    251: 'PARRY_KI_BLAST_2',
                    252: 'PARRY_KI_BLAST_3',
                    253: 'PARRY_KI_BLAST_4',
                    254: 'PARRY_KI_BLAST_5',
                    255: 'QUICK_RECOVERY_IN',
                    256: 'QUICK_RECOVERY_LOOP',
                    257: 'QUICK_RECOVER_TO_ENEMY_IN',
                    258: 'QUICK_RECOVER_TO_ENEMY_LOOP',
                    259: 'SKILL_001',
                    260: 'SKILL_002',
                    261: 'SKILL_003_IN',
                    262: 'SKILL_003_CHARGE',
                    263: 'SKILL_003_FIRE1',
                    264: 'SKILL_003_FIRE2',
                    265: 'SKILL_003_LOOP1',
                    266: 'SKILL_003_LOOP2',
                    267: 'SKILL_003_OUT',
                    268: 'SKILL_003_IN_U',
                    269: 'SKILL_003_CHARGE_U',
                    270: 'SKILL_003_FIRE1_U',
                    271: 'SKILL_003_FIRE2_U',
                    272: 'SKILL_003_LOOP3_U',
                    273: 'SKILL_003_LOOP4_U',
                    274: 'SKILL_003_OUT_U',
                    275: 'SKILL_003_IN_D',
                    276: 'SKILL_003_CHARGE_D',
                    277: 'SKILL_003_FIRE1_D',
                    278: 'SKILL_003_FIRE2_D',
                    279: 'SKILL_003_LOOP3_D',
                    280: 'SKILL_003_LOOP4_D',
                    281: 'SKILL_003_OUT_D',
                    282: 'SKILL_003_22',
                    283: 'SKILL_003_23',
                    284: 'SKILL_003_EVENT_1',
                    285: 'SKILL_003_EVENT_2',
                    286: 'SKILL_003_EVENT_3',
                    287: 'SKILL_003_EVENT_4',
                    288: 'SKILL_003_EVENT_5',
                    289: 'SKILL_003_ENEMY_1',
                    290: 'SKILL_003_ENEMY_2',
                    291: 'SKILL_003_ENEMY_3',
                    292: 'SKILL_003_ENEMY_4',
                    293: 'SKILL_003_ENEMY_5',
                    294: 'SKILL_003_34',
                    295: 'SKILL_004_IN',
                    296: 'SKILL_004_CHARGE',
                    297: 'SKILL_004_FIRE1',
                    298: 'SKILL_004_FIRE2',
                    299: 'SKILL_004_LOOP1',
                    300: 'SKILL_004_LOOP2',
                    301: 'SKILL_004_OUT',
                    302: 'SKILL_004_IN_U',
                    303: 'SKILL_004_CHARGE_U',
                    304: 'SKILL_004_FIRE1_U',
                    305: 'SKILL_004_FIRE2_U',
                    306: 'SKILL_004_LOOP3_U',
                    307: 'SKILL_004_LOOP4_U',
                    308: 'SKILL_004_OUT_U',
                    309: 'SKILL_004_IN_D',
                    310: 'SKILL_004_CHARGE_D',
                    311: 'SKILL_004_FIRE1_D',
                    312: 'SKILL_004_FIRE2_D',
                    313: 'SKILL_004_LOOP3_D',
                    314: 'SKILL_004_LOOP4_D',
                    315: 'SKILL_004_OUT_D',
                    316: 'SKILL_004_22',
                    317: 'SKILL_004_23',
                    318: 'SKILL_004_EVENT_1',
                    319: 'SKILL_004_EVENT_2',
                    320: 'SKILL_004_EVENT_3',
                    321: 'SKILL_004_EVENT_4',
                    322: 'SKILL_004_EVENT_5',
                    323: 'SKILL_004_ENEMY_1',
                    324: 'SKILL_004_ENEMY_2',
                    325: 'SKILL_004_ENEMY_3',
                    326: 'SKILL_004_ENEMY_4',
                    327: 'SKILL_004_ENEMY_5',
                    328: 'SKILL_004_34',
                    329: 'SKILL_005_IN',
                    330: 'SKILL_005_CHARGE',
                    331: 'SKILL_005_FIRE1',
                    332: 'SKILL_005_FIRE2',
                    333: 'SKILL_005_LOOP1',
                    334: 'SKILL_005_LOOP2',
                    335: 'SKILL_005_OUT',
                    336: 'SKILL_005_IN_U',
                    337: 'SKILL_005_CHARGE_U',
                    338: 'SKILL_005_FIRE1_U',
                    339: 'SKILL_005_FIRE2_U',
                    340: 'SKILL_005_LOOP3_U',
                    341: 'SKILL_005_LOOP4_U',
                    342: 'SKILL_005_OUT_U',
                    343: 'SKILL_005_IN_D',
                    344: 'SKILL_005_CHARGE_D',
                    345: 'SKILL_005_FIRE1_D',
                    346: 'SKILL_005_FIRE2_D',
                    347: 'SKILL_005_LOOP3_D',
                    348: 'SKILL_005_LOOP4_D',
                    349: 'SKILL_005_OUT_D',
                    350: 'SKILL_005_22',
                    351: 'SKILL_005_23',
                    352: 'SKILL_005_EVENT_1',
                    353: 'SKILL_005_EVENT_2',
                    354: 'SKILL_005_EVENT_3',
                    355: 'SKILL_005_EVENT_4',
                    356: 'SKILL_005_EVENT_5',
                    357: 'SKILL_005_ENEMY_1',
                    358: 'SKILL_005_ENEMY_2',
                    359: 'SKILL_005_ENEMY_3',
                    360: 'SKILL_005_ENEMY_4',
                    361: 'SKILL_005_ENEMY_5',
                    362: 'SKILL_005_34',
                    363: 'SKILL_005_START',
                    364: 'POWER_CLASH_1',
                    365: 'POWER_CLASH_2',
                    366: 'POWER_CLASH_3',
                    367: 'POWER_CLASH_4',
                    368: 'POWER_CLASH_5',
                    369: 'POWER_CLASH_6',
                    370: 'POWER_CLASH_LOSE',
                    371: 'RUSH_CLASH_IN',
                    372: 'RUSH_CLASH_LOOP',
                    373: 'RUSH_CLASH_WIN',
                    374: 'RUSH_CLASH_LOSE',
                    375: 'TRANSFORMATION_IN',
                    376: 'TRANSFORMATION_LOOP',
                    377: 'TRANSFORMATION_OUT',
                    378: 'POWER_GUARD_IN',
                    379: 'POWER_GUARD_LOOP',
                    380: 'FALL_BACK',
                    381: 'FALL_FRONT',
                    382: 'SEARCH_KI',
                    383: 'SEARCH_SCOUTER',
                    384: 'INTRO_IN',
                    385: 'INTRO_LOOP',
                    386: 'WIN_IN',
                    387: 'WIN_LOOP',
                    388: 'LOSE',
                    389: 'TAUNT',
                    390: 'GIANT_THROW_IN',
                    391: 'GIANT_THROW_LOOP',
                    392: 'GIANT_THROW_EVENT',
                    393: 'GIANT_THROW_ENEMY',
                    394: 'GIANT_THROW_OUT',
                    395: 'FLIGHTLESS_FLY',
                    396: 'FLIGHTLESS_JUMP',
                    397: 'CANCEL_BLOWN_IN',
                    398: 'CANCEL_BLOWN_LOOP',
                    399: 'UNTRANSFORM_IN',
                    400: 'UNTRANSFORM_LOOP',
                    401: 'UNTRANSFORM_OUT',
                    402: 'FLYUP_QUICK',
                    403: 'SONIC_SWAY_IN',
                    404: 'SONIC_SWAY_LOOP',
                    405: 'SONIC_SWAY_OUT',
                    406: 'SURPRISED',
                    407: 'LIGHTNING_ATTACK_IN',
                    408: 'LIGHTNING_ATTACK_OUT',
                    409: 'KI_RUSH_IN',
                    410: 'KI_RUSH_CHARGE',
                    411: 'KI_RUSH_LOOP',
                    412: 'KI_RUSH_OUT',
                    413: 'STAND_LOOP',
                    414: 'WII_01',
                    415: 'WII_02',
                    416: 'WII_03',
                    417: 'WII_04',
                    418: 'WII_05',
                    419: 'WII_06',
                    420: 'WII_07',
                    421: 'WII_08',
                    422: 'WII_09',
                    423: 'WII_10',
                    424: 'WII_11',
                    425: 'WII_12',
                    426: 'WII_13',
                    427: 'WII_14',
                    428: 'WII_15',
                    429: 'WII_16',
                    430: 'WII_17',
                    431: 'WII_18',
                    432: 'WII_19',
                    433: 'BLANK',
                    434: 'BLANK',
                    435: 'BLANK',
                    436: 'BLANK',
                    437: 'BLANK',
                    438: 'BLANK',
                    439: 'BLANK'},
            'bgm': {0: 'The Meteor',
                    1: 'Vital Burner',
                    2: 'Innocent World',
                    3: 'After The Fire',
                    4: 'Sweet Vibration ',
                    5: 'Survive ',
                    6: 'Heat Capacity',
                    7: 'Overture ',
                    8: 'Shine ',
                    9: 'Power Scale ',
                    10: 'Edge of Spirit ',
                    11: 'Caution!',
                    12: 'Menace',
                    13: 'Hot Soul',
                    14: 'High And Scream',
                    15: 'Shootout in Meteor',
                    16: 'Dynamite Battle',
                    17: "Burnin' Up",
                    18: 'Wild Rush',
                    19: 'Evolution',
                    20: 'Super Survivor Full ver.',
                    21: 'Super Survivor Short ver.',
                    22: 'Super Survivor Instrumental Full ver.',
                    23: 'Super Survivor Instrumental Short ver.'},
            'chara': {0: 'Goku (Early)',
                      1: 'Goku (Mid)',
                      2: 'Goku (Mid) - Super Saiyan',
                      3: 'Goku (End)',
                      4: 'Goku (End) - Super Saiyan',
                      5: 'Goku (End) - Super Saiyan 2',
                      6: 'Goku (End) - Super Saiyan 3',
                      7: 'Goku (GT)',
                      8: 'Goku (GT) - Super Saiyan',
                      9: 'Goku (GT) - Super Saiyan 3',
                      10: 'Goku (GT) - Super Saiyan 4',
                      11: 'Kid Goku',
                      12: 'Great Ape',
                      13: 'Kid Gohan',
                      14: 'Teen Gohan',
                      15: 'Teen Gohan - Super Saiyan',
                      16: 'Teen Gohan - Super Saiyan 2',
                      17: 'Adult Gohan',
                      18: 'Adult Gohan - Super Saiyan',
                      19: 'Adult Gohan - Super Saiyan 2',
                      20: 'Great Saiyaman',
                      21: 'Ultimate Gohan',
                      22: 'Piccolo (Early)',
                      23: 'Piccolo (End)',
                      24: 'Nail',
                      25: 'Krillin',
                      26: 'Yamcha',
                      27: 'Tien',
                      28: 'Chiaotzu',
                      29: 'Vegeta (Scouter)',
                      30: 'Great Ape Vegeta',
                      31: 'Vegeta',
                      32: 'Vegeta - Super Saiyan',
                      33: 'Super Vegeta',
                      34: 'Vegeta (second form)',
                      35: 'Vegeta (second form) - Super Saiyan',
                      36: 'Vegeta (second form) - Super Saiyan 2',
                      37: 'Vegeta (End) - Majin',
                      38: 'Vegeta (second form) - Super Saiyan 4',
                      39: 'Trunks (Sword)',
                      40: 'Trunks (Sword) - Super Saiyan',
                      41: 'Trunks',
                      42: 'Trunks - Super Saiyan',
                      43: 'Super Trunks',
                      44: 'Kid Trunks',
                      45: 'Kid Trunks - Super Saiyan',
                      46: 'Goten',
                      47: 'Goten - Super Saiyan',
                      48: 'Gotenks',
                      49: 'Gotenks - Super Saiyan',
                      50: 'Gotenks - Super Saiyan 3',
                      51: 'Vegito',
                      52: 'Super Vegito',
                      53: 'Super Gogeta',
                      54: 'Gogeta - Super Saiyan 4',
                      55: 'Hercule',
                      56: 'Videl',
                      57: 'Great Saiyaman 2',
                      58: 'Supreme Kai',
                      59: 'Kibito Kai',
                      60: 'Yajirobe',
                      61: 'Pikkon',
                      62: 'Tapion',
                      63: 'Pan',
                      64: 'Uub',
                      65: 'Majuub',
                      66: 'Master Roshi',
                      67: 'Master Roshi - MAX Power',
                      68: 'Grandpa Gohan',
                      69: 'Nam',
                      70: 'Android #8',
                      71: 'King Vegeta ',
                      72: 'Great Ape King Vegeta',
                      73: 'Bardock',
                      74: 'Great Ape Bardock',
                      75: 'Fasha',
                      76: 'Great Ape Fasha',
                      77: 'Raditz',
                      78: 'Great Ape Raditz',
                      79: 'Saibamen',
                      80: 'Nappa',
                      81: 'Great Ape Nappa',
                      82: 'Zarbon',
                      83: 'Zarbon - Post-Transformation',
                      84: 'Dodoria',
                      85: 'Cui',
                      86: 'Ginyu',
                      87: 'Recoome',
                      88: 'Burter',
                      89: 'Jeice',
                      90: 'Guldo',
                      91: 'Frieza - 1st Form',
                      92: 'Frieza - 2nd Form',
                      93: 'Frieza - 3rd Form',
                      94: 'Frieza - Final Form',
                      95: 'Frieza - Full Power',
                      96: 'Mecha Frieza',
                      97: 'King Cold',
                      98: 'Appule',
                      99: 'Frieza Soldier',
                      100: 'Android #16',
                      101: 'Android #17',
                      102: 'Android #18',
                      103: 'Android #19',
                      104: 'Dr. Gero',
                      105: 'Cell - 1st Form',
                      106: 'Cell - 2nd Form',
                      107: 'Cell - Perfect Form',
                      108: 'Cell - Perfect',
                      109: 'Cell Jr.',
                      110: 'Babidi',
                      111: 'Demon King Dabura',
                      112: 'Majin Buu',
                      113: 'Majin Buu (Pure Evil)',
                      114: 'Super Buu',
                      115: 'Super Buu - Gotenks Absorbed',
                      116: 'Super Buu - Gohan Absorbed',
                      117: 'Kid Buu',
                      118: 'Garlic Jr.',
                      119: 'Super Garlic Jr.',
                      120: 'Dr. Wheelo',
                      121: 'Turles',
                      122: 'Great Ape Turles',
                      123: 'Slug',
                      124: 'Slug - Giant',
                      125: 'Salza',
                      126: 'Cooler',
                      127: 'Cooler - Final Form',
                      128: 'Meta-Cooler',
                      129: 'Android #13',
                      130: 'Android #13 - Fusion',
                      131: 'Broly',
                      132: 'Broly - Super Saiyan',
                      133: 'Broly - Legendary Super Saiyan',
                      134: 'Zangya',
                      135: 'Bojack',
                      136: 'Bojack - Full Power',
                      137: 'Janemba',
                      138: 'Super Janemba',
                      139: 'Hirudegarn',
                      140: 'Baby Vegeta',
                      141: 'Super Baby 1',
                      142: 'Super Baby 2',
                      143: 'Great Ape Baby',
                      144: 'Super 17',
                      145: 'Nuova Shenron',
                      146: 'Syn Shenron',
                      147: 'Omega Shenron',
                      148: 'General Tao',
                      149: 'Cyborg Tao',
                      150: 'General Blue',
                      151: 'Devilman',
                      152: 'Pilaf Machine',
                      153: 'Pilaf Machine - Fusion',
                      154: 'Tambourine',
                      155: 'Demon King Piccolo',
                      156: 'Arale',
                      157: 'Chi-Chi',
                      158: 'Spopovich',
                      159: 'Future Gohan',
                      160: 'Future Gohan - Super Saiyan'},
            'cond': {0: 'Wait 10 seconds',
                     1: 'Wait 15 seconds',
                     2: 'Wait 20 seconds',
                     3: 'Wait 25 seconds',
                     4: 'Wait 30 seconds',
                     5: 'Wait 35 seconds',
                     6: 'Wait 40 seconds',
                     7: 'Wait 45 seconds',
                     8: 'Wait 50 seconds',
                     9: 'Wait 55 seconds',
                     10: 'Wait 60 seconds',
                     11: 'Wait 70 seconds',
                     12: 'Wait 80 seconds',
                     13: 'Wait 90 seconds',
                     14: 'Wait 100 seconds',
                     15: 'Wait 120 seconds',
                     16: 'Wait 140 seconds',
                     17: 'Wait 160 seconds',
                     18: 'Wait 180 seconds',
                     19: 'UNKNOWN',
                     20: 'Perform Normal Clash',
                     21: 'Perform Aerial Clash',
                     22: 'Lose 1 Health Bar',
                     23: 'Lose 2 Health Bars',
                     24: 'Lose 3 Health Bars',
                     25: 'Lose 4 Health Bars',
                     26: 'Lose 5 Health Bars',
                     27: 'Lose 6 Health Bars',
                     28: 'Lose 7 Health Bars',
                     29: 'Reach Full Ki Bars',
                     30: 'Reach Max Amount of Blast Stocks',
                     31: 'Go in MAX POWER Mode',
                     32: 'Transform',
                     33: 'Taunt',
                     34: 'Fall into ground/water',
                     35: 'UNKNOWN',
                     36: 'Perform 1st Blast 1',
                     37: 'Perform 2nd Blast 1',
                     38: 'Perform 1st Blast 2',
                     39: 'Perform 2nd Blast 2',
                     40: 'Perform Ultimate Blast',
                     41: 'Hit with 1st Blast 1',
                     42: 'Hit with 2nd Blast 1',
                     43: 'Hit with 1st Blast 2',
                     44: 'Hit with 2nd Blast 2',
                     45: 'Hit with Ultimate Blast',
                     46: 'Block 1st Blast 2',
                     47: 'Block 2nd Blast 2',
                     48: 'Block Ultimate Blast',
                     49: 'Perform Dragon Homing',
                     50: 'Perform Vanishing Attack',
                     51: 'Perform Throw',
                     52: 'Perform Hyper Smash',
                     53: 'UNKNOWN',
                     54: 'Hit with Charged Ki Blast',
                     55: 'Perform Fully Charged Left Smash Attack',
                     56: 'Perform Fully Charged Right Smash Attack',
                     57: 'Perform Fully Charged Up Smash Attack',
                     58: 'Perform Fully Charged Down Smash Attack',
                     59: 'Perform Fully Charged Neutral Smash Attack',
                     60: 'Perform First Attack!',
                     61: 'Perform Rush Attack',
                     62: 'Perform Dragon Smash',
                     63: 'Perform Burst Meteo Finisher',
                     64: 'Perform Dash Smash',
                     65: 'Perform Teleport',
                     66: 'Perform Z-Counter',
                     67: 'Perform Guard Crush',
                     68: 'Perform Sonic Sway',
                     69: 'Perform Emergency Blaster Wave',
                     70: 'Win Beam Struggle',
                     71: 'Win Normal Clash',
                     72: 'Win via K.O.',
                     73: 'Win via Ringout',
                     74: 'UNKNOWN',
                     75: 'Perform Misc. Melee Attack',
                     76: 'Resume Control (?)',
                     77: 'UNKNOWN',
                     78: 'UNKNOWN',
                     79: 'Reset Camera (?)',
                     80: 'Press R3',
                     81: 'UNKNOWN',
                     82: 'Perform Blast 1 Finish',
                     83: 'Perform Blast 2 Finish',
                     84: 'Defeat all teammates',
                     85: 'Get Hit',
                     86: 'UNKNOWN',
                     87: 'UNKNOWN',
                     88: 'UNKNOWN',
                     89: 'UNKNOWN',
                     90: 'NULL',
                     91: 'NULL'},
            'event': {0: 'Battle Start',
                      1: 'Battle Finish',
                      2: 'Aerial Clash',
                      3: 'Map Destruction',
                      4: 'Normal Clash',
                      5: 'Aerial Clash',
                      6: 'Aerial Clash',
                      7: 'Aerial Clash',
                      8: "Beam Struggle between Player 1's 1st Blast 2 and COM's 1st Blast 2",
                      9: "Beam Struggle between Player 1's 1st Blast 2 and COM's 2nd Blast 2",
                      10: "Beam Struggle between Player 1's 2nd Blast 2 and COM's 1st Blast 2",
                      11: "Beam Struggle between Player 1's 2nd Blast 2 and COM's 2nd Blast 2",
                      12: "Beam Struggle between Player 1 and the COM's Ultimate Blasts",
                      13: 'UNKNOWN',
                      14: 'UNKNOWN',
                      15: 'UNKNOWN',
                      16: 'Switch with Teammate #1',
                      17: 'Switch with Teammate #2',
                      18: 'Switch with Teammate #3',
                      19: 'Switch with Teammate #4',
                      20: 'Switch with Teammate #5',
                      21: 'Assign Transformation',
                      22: 'Assign Transformation',
                      23: 'Assign Fusion',
                      24: 'Go to MAX POWER Mode',
                      25: 'Trigger 1st Blast 1',
                      26: 'Trigger 2nd Blast 1',
                      27: 'Trigger 1st Blast 2',
                      28: 'Trigger 2nd Blast 2',
                      29: 'Trigger Ultimate Blast'},
            'gsc': {0: 'Common Enemy',
                    1: "Goku's Quiet Rage",
                    2: 'Ultimate Decisive Battle',
                    3: 'Super Saiyan?!',
                    4: "Frieza's Ultimate Transformation!",
                    5: 'Defeat Frieza!',
                    6: 'Legendary Super Saiyan',
                    7: 'Enraged Android',
                    8: "Vegeta's Curiosity",
                    9: 'Perfect Body',
                    10: 'Cell Games Begin',
                    11: 'Gohan Explodes!',
                    12: 'Final Battle',
                    13: 'Future Peace',
                    14: 'Destined Battle: Goku Vs. Vegeta',
                    15: 'Farewell to the Proud Warrior',
                    16: 'Final Fusion',
                    17: 'Battle for the Universe',
                    18: 'Conclusion',
                    19: 'Alone for the Final Battle',
                    20: 'Destroy the Makyo Star',
                    21: 'Final Battle For Earth',
                    22: 'Super Saiyan Goku',
                    23: 'Strongest in the World',
                    24: 'Strongest Vs. Strongest',
                    25: 'Clash of the Ultimate Warriors',
                    26: 'Ultimate Battle! Three Super Saiyans',
                    27: 'Legendary Super Saiyan',
                    28: 'Blaze! Ultimate Burning Battle',
                    29: 'Galactic Crisis',
                    30: 'I Will Protect the Earth!',
                    31: "Dangerous Duo! The Ultimate Warrior Doesn't Sleep",
                    32: 'Innocent Monster',
                    33: 'Fusion Reborn! Goku and Vegeta',
                    34: '"Dragon Fist Explosion! If Goku Doesn\'t Who Will?"',
                    35: 'Immortal Monster',
                    36: 'Ultimate Android',
                    37: 'Solar Warrior 6000 Degrees of Power!',
                    38: 'Ultimate Super Gogeta',
                    39: 'A Miracle Saves The Day!',
                    40: 'Ceiling Vs. Ground',
                    41: 'Battle in Korin Tower',
                    42: 'Goku Strikes Back',
                    43: 'Penguin Village',
                    44: 'Dream Match: Goku Vs. Arale',
                    45: 'Affectionate Android',
                    46: 'Galaxy Battle',
                    47: 'Unexpected Help'},
            'item': {0: 'Attack Up 1',
                     1: 'Attack Up 2',
                     2: 'Attack Up 3',
                     3: 'Defense Up 1',
                     4: 'Defense Up 2',
                     5: 'Defense Up 3',
                     6: 'Ki Power Up 1',
                     7: 'Ki Power Up 2',
                     8: 'Ki Power Up 3',
                     9: 'Super Up 1',
                     10: 'Super Up 2',
                     11: 'Super Up 3',
                     12: 'Attack Up 2 & Defense Down 1',
                     13: 'Defense Up 2 & Attack Down 1',
                     14: 'Ki Power Up 2 & Super Down 1',
                     15: 'Super Up 2 & Power Down 1',
                     16: 'Attack Up 3 & Super Down 1',
                     17: 'Defense Up 3 & Attack Down 2',
                     18: 'Ki Power Up 3 & Defense Down 1',
                     19: 'Super Up 3 & Power Down 2',
                     20: 'Attack Up 3 & Defense Down 2',
                     21: 'Defense Up 3 & Ki Power Down 1',
                     22: 'Ki Power Up 3 & Super Down 2',
                     23: 'Super Up 3 & Attack Down 1',
                     24: 'Blank 1',
                     25: 'Blank 2',
                     26: 'Blank 3',
                     27: 'Blank 4',
                     28: 'Blank 5',
                     29: 'Blank 6',
                     30: 'Blank 7',
                     31: 'Blank 8 ',
                     32: 'Blank 9',
                     33: 'Blank 10',
                     34: 'Flight',
                     35: 'Unleash Latent Power 1',
                     36: 'Unleash Latent Power 2',
                     37: 'Unleash Latent Power 3',
                     38: 'Ki Control',
                     39: 'Dragon Dash Mastery',
                     40: 'High Spot',
                     41: 'Essence of Sight',
                     42: 'Warrior Lineage',
                     43: 'Halo',
                     44: 'Demon Seal',
                     45: 'Satisfying Blow',
                     46: 'Active Heart',
                     47: 'Indomitable Fighting Spirit',
                     48: 'Mind Breaker',
                     49: 'Gigantic Power',
                     50: 'Rising Fighting Spirit',
                     51: 'Secret Measures',
                     52: 'Proof of Friendship',
                     53: "Dende's Healing Ability",
                     54: 'Eternal Life',
                     55: 'Tension Up',
                     56: 'High Tension',
                     57: 'Water Blessing',
                     58: 'Spiritual Control',
                     59: 'Lover of Justice',
                     60: 'Evil Ambitions',
                     61: 'Dragon Heart',
                     62: 'Dragon Beat',
                     63: 'Dragon Spirit',
                     64: 'Confidence',
                     65: 'Battle Control',
                     66: "Kibito's Secret Art",
                     67: 'Persistent Threat',
                     68: 'Miracle Master',
                     69: 'Exquisite Skill',
                     70: 'Quick Return',
                     71: 'Heavy Pressure',
                     72: 'Unleash Ki',
                     73: 'Power of Rage',
                     74: 'Dragon Power',
                     75: 'Latent Energy!',
                     76: 'Fighting Spirit!',
                     77: 'Indignation!',
                     78: 'Serious!',
                     79: 'Hatred of Saiyans',
                     80: 'Rush Blast 1',
                     81: 'Rush Blast 2',
                     82: 'Rush Blast 3',
                     83: 'Guard Master',
                     84: 'Mirage',
                     85: "Warrior's Will",
                     86: 'Evil Pride',
                     87: 'Perfect Guard',
                     88: 'Sparking Plus',
                     89: 'Style of the Strong',
                     90: "Emperor's Aura",
                     91: 'Miracle Sparking',
                     92: 'Savior',
                     93: 'Light Body',
                     94: 'Power Body',
                     95: 'Ultimate Body',
                     96: 'Draconic Aura',
                     97: 'Master Strike',
                     98: 'Master Blast',
                     99: 'Master Throw',
                     100: 'Charged Attack',
                     101: 'Quick Fast Attack',
                     102: 'Dragon Break',
                     103: 'Dragon Crush',
                     104: 'Vanishing Break',
                     105: 'Vanishing Rush',
                     106: 'Combo Master',
                     107: 'Quick Charge',
                     108: 'Super Senses',
                     109: "Broly's Ring",
                     110: 'Namek Power',
                     111: 'Earth Power',
                     112: 'Universal Power',
                     113: 'Aura Charge Blue',
                     114: 'Aura Charge Purple',
                     115: 'Aura Charge Yellow',
                     116: 'Aura Charge Red',
                     117: 'Aura Charge Green',
                     118: 'Aura Charge White',
                     119: 'Aura Charge Pink',
                     120: 'Aura Charge Violet',
                     121: 'Aura Charge Ultimate',
                     122: 'Aura Charge Ultimate 3',
                     123: 'Aura Charge Ultimate 4',
                     124: "Master Roshi's Training",
                     125: "King Kai's Training",
                     126: "#18's Kiss",
                     127: "#17's Scarf",
                     128: 'Medical Machine',
                     129: 'Blank 11',
                     130: 'Blank 12',
                     131: 'Blank 13',
                     132: 'Blank 14',
                     133: 'Blank 15',
                     134: 'Blank 16',
                     135: 'Blank 17',
                     136: "Launch's Support",
                     137: 'Goku Type',
                     138: 'Vegeta Type',
                     139: 'Gohan Type',
                     140: 'Trunks Type',
                     141: 'Piccolo Type',
                     142: 'Krillin Type',
                     143: 'Tien Type',
                     144: 'Chiaotzu Type',
                     145: 'Yajirobe Type',
                     146: 'Frieza Type',
                     147: 'Cell Type',
                     148: 'Majin Buu Type',
                     149: 'Broly Type',
                     150: 'Ginyu Type',
                     151: 'Recoome Type',
                     152: 'Blank 18',
                     153: 'Blank 19',
                     154: 'Blank 20',
                     155: 'Blank 21',
                     156: 'Blank 22',
                     157: 'Blank 23',
                     158: 'Blank 24',
                     159: 'Blank 25',
                     160: 'Blank 26',
                     161: 'Blank 27',
                     162: 'Ultimate Warrior 1',
                     163: 'Ultimate Warrior 2',
                     164: 'Ultimate Warrior 3',
                     165: 'Ultimate Warrior 4',
                     166: 'Ultimate Warrior 5',
                     167: 'Ultimate Warrior 6',
                     168: 'Ultimate Warrior 7',
                     169: 'Ultimate Warrior 8',
                     170: 'Attack -25',
                     171: 'Attack -24',
                     172: 'Attack -23',
                     173: 'Attack -22',
                     174: 'Attack -21',
                     175: 'Attack -20',
                     176: 'Attack -19',
                     177: 'Attack -18',
                     178: 'Attack -17',
                     179: 'Attack -16',
                     180: 'Attack -15',
                     181: 'Attack -14',
                     182: 'Attack -13',
                     183: 'Attack -12',
                     184: 'Attack -11',
                     185: 'Attack -10',
                     186: 'Attack -9',
                     187: 'Attack -8',
                     188: 'Attack -7',
                     189: 'Attack -6',
                     190: 'Attack -5',
                     191: 'Attack -4',
                     192: 'Attack -3',
                     193: 'Attack -2',
                     194: 'Attack -1',
                     195: 'Attack 0',
                     196: 'Attack +1',
                     197: 'Attack +2',
                     198: 'Attack +3',
                     199: 'Attack +4',
                     200: 'Attack +5',
                     201: 'Attack +6',
                     202: 'Attack +7',
                     203: 'Attack +8',
                     204: 'Attack +9',
                     205: 'Attack +10',
                     206: 'Attack +11',
                     207: 'Attack +12',
                     208: 'Attack +13',
                     209: 'Attack +14',
                     210: 'Attack +15',
                     211: 'Attack +16',
                     212: 'Attack +17',
                     213: 'Attack +18',
                     214: 'Attack +19',
                     215: 'Attack +20',
                     216: 'Attack +21',
                     217: 'Attack +22',
                     218: 'Attack +23',
                     219: 'Attack +24',
                     220: 'Attack +25',
                     221: 'Attack +26',
                     222: 'Attack +27',
                     223: 'Attack +28',
                     224: 'Attack +29',
                     225: 'Attack +30',
                     226: 'Attack +31',
                     227: 'Attack +32',
                     228: 'Attack +33',
                     229: 'Attack +34',
                     230: 'Attack +35',
                     231: 'Attack +36',
                     232: 'Attack +37',
                     233: 'Attack +38',
                     234: 'Attack +39',
                     235: 'Attack +40',
                     236: 'Attack +41',
                     237: 'Attack +42',
                     238: 'Attack +43',
                     239: 'Attack +44',
                     240: 'Attack +45',
                     241: 'Attack +46',
                     242: 'Attack +47',
                     243: 'Attack +48',
                     244: 'Attack +49',
                     245: 'Attack +50',
                     246: 'Defense -25',
                     247: 'Defense -24',
                     248: 'Defense -23',
                     249: 'Defense -22',
                     250: 'Defense -21',
                     251: 'Defense -20',
                     252: 'Defense -19',
                     253: 'Defense -18',
                     254: 'Defense -17',
                     255: 'Defense -16',
                     256: 'Defense -15',
                     257: 'Defense -14',
                     258: 'Defense -13',
                     259: 'Defense -12',
                     260: 'Defense -11',
                     261: 'Defense -10',
                     262: 'Defense -9',
                     263: 'Defense -8',
                     264: 'Defense -7',
                     265: 'Defense -6',
                     266: 'Defense -5',
                     267: 'Defense -4',
                     268: 'Defense -3',
                     269: 'Defense -2',
                     270: 'Defense -1',
                     271: 'Defense 0',
                     272: 'Defense +1',
                     273: 'Defense +2',
                     274: 'Defense +3',
                     275: 'Defense +4',
                     276: 'Defense +5',
                     277: 'Defense +6',
                     278: 'Defense +7',
                     279: 'Defense +8',
                     280: 'Defense +9',
                     281: 'Defense +10',
                     282: 'Defense +11',
                     283: 'Defense +12',
                     284: 'Defense +13',
                     285: 'Defense +14',
                     286: 'Defense +15',
                     287: 'Defense +16',
                     288: 'Defense +17',
                     289: 'Defense +18',
                     290: 'Defense +19',
                     291: 'Defense +20',
                     292: 'Defense +21',
                     293: 'Defense +22',
                     294: 'Defense +23',
                     295: 'Defense +24',
                     296: 'Defense +25',
                     297: 'Defense +26',
                     298: 'Defense +27',
                     299: 'Defense +28',
                     300: 'Defense +29',
                     301: 'Defense +30',
                     302: 'Defense +31',
                     303: 'Defense +32',
                     304: 'Defense +33',
                     305: 'Defense +34',
                     306: 'Defense +35',
                     307: 'Defense +36',
                     308: 'Defense +37',
                     309: 'Defense +38',
                     310: 'Defense +39',
                     311: 'Defense +40',
                     312: 'Defense +41',
                     313: 'Defense +42',
                     314: 'Defense +43',
                     315: 'Defense +44',
                     316: 'Defense +45',
                     317: 'Defense +46',
                     318: 'Defense +47',
                     319: 'Defense +48',
                     320: 'Defense +49',
                     321: 'Defense +50',
                     322: 'Strength Enhancement',
                     323: 'Strength Reduction (-30k)',
                     324: 'Blast Clash Weakened (Small)',
                     325: 'Blast Clash Weakened (Medium)',
                     326: 'Blast Clash Weakened (Large)',
                     327: 'Absolutely Invincible Body',
                     328: 'Go To Hell',
                     329: 'Super Mode',
                     330: 'Extreme Hand to Hand',
                     331: 'Extreme Energy Blast',
                     332: 'Extreme Blast',
                     333: 'Extreme Defense',
                     334: 'Resistor',
                     335: 'Super Regeneration Cells',
                     336: 'Complete Ki Control',
                     337: 'God of Battle',
                     338: 'Fierce God',
                     339: 'Strength Reduction (-10k)',
                     340: 'Strength Reduction (-20k)',
                     341: 'Limitbreaker',
                     342: 'Inherited Power',
                     343: 'Blank 28',
                     344: 'Blank 29',
                     345: 'Blank 30',
                     346: 'Blank 31',
                     347: 'Blank 32',
                     348: 'Blank 33',
                     349: 'Blank 34'},
            'map': {0: 'Wasteland - Noon',
                    1: 'Rocky Area - Noon',
                    2: 'Planet Namek',
                    3: 'Dying Namek',
                    4: 'World Tournament Stage  - Noon',
                    5: "Kami's Lookout",
                    6: 'Cell Games Arena - Evening',
                    7: "Supreme Kai's World",
                    8: 'Hyperbolic Time Chamber',
                    9: 'City Ruins - Noon',
                    10: 'Mountain Road - Noon',
                    11: 'Islands',
                    12: 'Kame House',
                    13: 'Planet - Night',
                    14: 'Glacier',
                    15: 'Ruined Earth',
                    16: 'Outer Space',
                    17: 'Penguin Village',
                    18: 'Hell',
                    19: 'Desert - Noon',
                    20: "King's Castle",
                    21: 'Muscle Tower',
                    22: 'Mount Paozu',
                    23: 'Wasteland - Evening',
                    24: 'Wasteland - Night',
                    25: 'Rocky Area - Evening',
                    26: 'Rocky Area - Night',
                    27: 'World Tournament Stage - Evening',
                    28: 'Cell Games Arena - Noon',
                    29: 'City Ruins - Evening',
                    30: 'City Ruins - Night',
                    31: 'Desert - Evening',
                    32: 'Desert - Night',
                    33: 'Mountain Road - Evening',
                    34: 'Planet - Evening'},
            'ref': {0: 'Ox King',
                    1: 'Videl',
                    2: 'Supreme Kai',
                    3: 'Shenron',
                    4: 'Announcer 1',
                    5: 'Announcer 2',
                    6: 'Announcer 3',
                    7: 'Videl (used for Battle Training only)'}}}
GSCF = b'GSCF'
GSHD = b'GSHD'
GSCD = b'GSCD'
GSAC = b'GSAC'
GSDT = b'GSDT'
EOFC = b'EOFC'
def u16(b, off):
    return struct.unpack_from('<H', b, off)[0]
def s16(b, off):
    return struct.unpack_from('<h', b, off)[0]
def u32(b, off):
    return struct.unpack_from('<I', b, off)[0]
def i32(b, off):
    return struct.unpack_from('<i', b, off)[0]
def f32(b, off):
    return struct.unpack_from('<f', b, off)[0]
def hx(v, width=4):
    return '&' + format(v & (1 << width * 4) - 1, '0%dx' % width).upper()
def fmt_float(v):
    if v == 0.0:
        v = 0.0
    return f'{v:12.6f}'
def fmt_vec(prefix, vals, commas=False):
    if commas:
        return prefix + '[' + ', '.join((f'{v:.6f}' for v in vals)) + ']'
    else:
        return prefix + '[' + ' '.join((f'{v:.6f}' for v in vals)) + ']'
def sanitize_keyword(name):
    aliases = {
        'Wait for Period of Time': 'Wait',
        'Scene Start': 'Scene_Start',
        'Scene End & Battle Start': 'End_cutscn',
        'Load TXT PAK': 'Load_TXT',
        'Load LPS PAK': 'Load_LPS',
        'Assign Character Position & Rotation': 'Set_transform',
        'Assign Character Position Only': 'Set_position',
        'Assign Character Rotation Only': 'Set_rotation',
        'Make Character Visible': 'Visible',
        'Make Character Invisible': 'Invisible',
        'Enable Lingering Aura': 'Enable_Aura',
        'Disable Lingering Aura': 'Disable_Aura',
        'Enable Ki Charge Aura': 'Enable_ChargeAura',
        'Disable Ki Charge Aura': 'Disable_ChargeAura',
        'Enable MAX POWER Mode Explosion': 'Enable_MaxMode',
        'Assign Animation': 'Load_Anim',
        'Enable Character Movement': 'Move',
        'Trigger Fade-Out': 'Fade_out',
        'Trigger Fade-In': 'Fade_in',
        'Stop Current Fade': 'Fade_stop',
        'Primary Camera Point': 'Camera_Start',
        'Secondary Camera Point': 'CS_Camera',
        'Reset Battle Camera': 'Camera_Reset',
        'Trigger Camera Shake': 'Shake_on',
        'Stop Camera Shake': 'Shake_off',
        'Music Change': 'Music',
        'Turn Down/Off Previous Music Volume': 'Music_off',
        'Play Sound from SE_Battle.pak': 'Play_SE',
        'Play Any ADX from Scenario': 'Play_ADX',
        'Play Character Voice Line': 'Play_ADX',
        'Freeze Cutscene until Button Press': 'Button_wait',
        'Store Character Positions': 'Store_positions',
        'Store VFX Switches': 'Store_VFX',
        'Store Conditional Properties': 'Link',
        'Post-Cutscene Event': 'Event',
        'Battle End': 'End_event',
        'Battle Settings': 'Setting',
        'Team Settings': 'Role',
        'Character Settings': 'Actor',
        "Store Player's Character Changes": 'Set_plafield',
        "Store Opponent's Character Changes": 'Set_cpufield',
        'Store Audio-Related Properties': 'Dialogs',
        'Rewards': 'Rewards',
        'Scenario Identifier': 'ID',
        'Subtitle Settings': 'Subtittle',
        'Load String in Memory (for debug reasons & no longer functional)': 'Load_String',
        'Load String in Memory': 'Load_String',
    }
    if name in aliases:
        return aliases[name]
    else:
        x = re.sub('[^A-Za-z0-9]+', '_', name).strip('_')
        return x or 'FUNCTION'
def table_name_for_type(t):
    return DB['tables'].get(t, {})
def resolve_value(raw, ptype):
    if ptype == 'bool':
        return '1' if raw else '0'
    else:
        if ptype in ['num', '', None]:
            return str(raw)
        else:
            if raw == (-1) or raw & 4294967295 == 4294967295:
                return '&FFFFFFFF'
            else:
                if ptype in DB['tables']:
                    return hx(raw)
                else:
                    return str(raw)
def name_for_id(raw, ptype):
    if ptype not in DB['tables']:
        return
    else:
        val = raw & 65535 if ptype != 'gsc' else raw & 65535
        return DB['tables'][ptype].get(val)
class GSCReader:
    def __init__(self, path):
        self.path = Path(path)
        self.data = self.path.read_bytes()
        self.size = len(self.data)
        self.game = 'unknown'
        self.gsdt_pos = None
        self.gsdt = b''
        self.records = []
        self.raw_header = self.data[:112]
        self._detect_game()
        self._locate_gsdt()
        self._parse_records()
    def _detect_game(self):
        if len(self.data) >= 40:
            a = u32(self.data, 32)
            b = u32(self.data, 36)
            if a == 3 and 1 <= b <= 3:
                self.game = ['bt2', 'bt3', 'rb1'][b - 1]
                return
            if a == 2 and b == 0:
                self.game = 'bt2'
                return
    def _locate_gsdt(self):
        p = self.data.find(GSDT)
        if p < 0:
            raise ValueError('GSDT não encontrado.')
        else:
            self.gsdt_pos = p + 16
            if p < 8:
                raise ValueError('Cabeçalho GSDT inválido.')
            else:
                size = u32(self.data, p + 8)
                if self.gsdt_pos + size > self.size:
                    size = max(0, self.size - self.gsdt_pos)
                self.gsdt = self.data[self.gsdt_pos:self.gsdt_pos + size]
    def gsdt_int(self, offset):
        addr = (offset & 65535) * 4
        if addr + 4 > len(self.gsdt):
            return
        else:
            return i32(self.gsdt, addr)
    def gsdt_float(self, offset):
        addr = (offset & 65535) * 4
        if addr + 4 > len(self.gsdt):
            return
        else:
            return f32(self.gsdt, addr)
    def _parse_records(self):
        first_gsac = self.data.find(GSAC)
        if first_gsac < 0 or first_gsac >= self.gsdt_pos:
            raise ValueError('GSAC não encontrado.')
        pos = max(0, first_gsac - 28)
        scene = None
        curr_func = 0
        while pos + 4 <= self.gsdt_pos:
            inp = self.data[pos:pos + 4]
            if inp == GSAC and pos + 16 <= self.gsdt_pos:
                sid = u32(self.data, pos + 12)
                self.records.append({'kind': 'scene', 'id': sid, 'offset': pos})
                scene = sid
                pos += 16
                continue
            if inp == EOFC:
                pos += 16
                continue
            if inp[0] == 1 and pos + 4 <= self.gsdt_pos:
                n = inp[1]
                fid = u16(inp, 2)
                rec = {'kind': 'func', 'scene': scene, 'id': fid, 'n': n, 'offset': pos, 'params': []}
                p = pos + 4
                for i in range(n):
                    if p + 4 > self.gsdt_pos:
                        break
                    pd = self.data[p:p + 4]
                    typ = pd[0]
                    off = u16(pd, 1)
                    rec['params'].append(self._param(typ, off))
                    p += 4
                self.records.append(rec)
                curr_func = fid
                pos = p
                continue
            if inp[0] == 8:
                n = inp[2]
                pid = inp[1]
                rec = {'kind': 'prop', 'scene': scene, 'id': pid, 'n': n, 'func': curr_func, 'offset': pos, 'params': []}
                p = pos + 4
                for i in range(n):
                    if p + 4 > self.gsdt_pos:
                        break
                    pd = self.data[p:p + 4]
                    typ = pd[0]
                    off = u16(pd, 1)
                    rec['params'].append(self._param(typ, off))
                    p += 4
                self.records.append(rec)
                pos = p
                continue
            self.records.append({'kind': 'raw', 'scene': scene, 'offset': pos, 'bytes': inp.hex(' ').upper()})
            pos += 4
    def _param(self, typ, off):
        if typ == 10:
            val = self.gsdt_int(off)
            return {'type': 'int', 'type_code': 10, 'offset': off, 'value': val if val is not None else 0}
        else:
            if typ == 26:
                val = self.gsdt_float(off)
                return {'type': 'float', 'type_code': 26, 'offset': off, 'value': val if val is not None else 0.0}
            else:
                return {'type': 'unknown', 'type_code': typ, 'offset': off, 'value': None}
    def func_name(self, fid):
        return DB['func_map'].get(fid, f'FUNCTION_{fid:04X}')
    def prop_name(self, pid, fid):
        return DB['prop_map'].get((pid, fid), DB['prop_map'].get((pid, 0), f'PROPERTY_{pid:02X}'))
    def ptypes(self, fid, prop=False, pid=None):
        if prop:
            return DB['prop_param_map'].get((pid, fid), [])
        else:
            return DB['func_param_map'].get(fid, [])
    def param_text(self, param, ptype):
        if param['type'] == 'float':
            return f"{param['value']:12.6f}"
        else:
            raw = param['value']
            if raw is None:
                return 'null'
            else:
                if ptype == 'bool':
                    return 'True' if raw else 'False'
                else:
                    if ptype == 'anm':
                        return hx(raw, 3)
                    else:
                        if ptype in DB['tables']:
                            return hx(raw)
                        else:
                            if raw == (-1):
                                return '-1'
                            else:
                                return str(raw)
class GSCFWriter:
    def __init__(self, reader):
        self.r = reader
        self.out = []
        self.indent = 0
    def line(self, s=''):
        self.out.append('   ' * self.indent + s)
    def block_start(self, s):
        self.line(s + '<')
        self.indent += 1
    def block_end(self):
        self.indent = max(0, self.indent - 1)
        self.line('>')
    def compact(self, keyword, fields):
        parts = []
        for k, v in fields:
            parts.append(f'${k}:{v}')
        self.line('$' + keyword + ':{' + ' '.join(parts) + '}')
    def actor_ref(self, raw):
        if raw is None:
            return '$null'
        else:
            u = raw & 4294967295
            if u & 32768:
                return '$cpu' + str(u & 32767)
            else:
                return '$pla' + str(u & 32767)
    def pval(self, p, ptype):
        return self.r.param_text(p, ptype)
    def write_header(self):
        d = self.r.data
        flg = u32(d, 12) if len(d) >= 16 else 1
        self.line('$GSCF:{ $flg:' + hx(flg) + ',')
        self.indent += 1
        gshd = d[32:48] if len(d) >= 48 else b''
        if len(gshd) >= 8:
            packed = bytes([gshd[0], gshd[4], 0, 0])
            self.line('$GSHD:<&0000, I&[%s,]>' % ' '.join((f'{x:02X}' for x in packed)))
        else:
            self.line('$GSHD:<&0000, I&[00 00 00 00,]>')
        self.line('$GSCD:<&0001,')
        self.indent += 1
    def close_header(self):
        self.indent -= 1
        self.line('>')
        self.indent -= 1
        self.line('}')
    def write(self):
        self.write_header()
        self.write_metadata_sections()
        scene_groups = []
        current = None
        for rec in self.r.records:
            if rec['kind'] == 'scene':
                current = {'id': rec['id'], 'records': []}
                scene_groups.append(current)
            else:
                if current is not None:
                    current['records'].append(rec)
        for g in scene_groups:
            sid = g['id']
            if sid in [4294967295, 1000, 4294967294, 4294967293, 4294967292, 4294967291]:
                continue
            else:
                self.write_scene(g)
        self.close_header()
        return '\n'.join(self.out) + '\n'
    def write_metadata_sections(self):
        self.block_start('$Init:')
        self.line('$EV_00,')
        self.block_end()
        self.block_start('$Setup:')
        self.line('$Set_subtittles,')
        self.line('$Set_scene,')
        self.line('$Set_dialogs,')
        self.line('$Load_files,')
        self.block_end()
        groups = {}
        cur = None
        for rec in self.r.records:
            if rec['kind'] == 'scene':
                cur = rec['id']
                groups[cur] = []
                continue
            if cur is not None:
                groups[cur].append(rec)
        if 4294967294 in groups:
            self.block_start('$Load_files:')
            for rec in groups[4294967294]:
                if rec['kind'] == 'func':
                    if rec['id'] == 701:
                        self.line('$Load_TXT')
                        continue
                    if rec['id'] == 702:
                        self.line('$Load_LPS')
                        continue
                    self.write_generic_func(rec)
            self.block_end()
        if 4294967293 in groups:
            self.write_subtitles_section(groups[4294967293])
        if 4294967292 in groups:
            self.block_start('$Set_scene:')
            for rec in groups[4294967292]:
                if rec['kind'] != 'func':
                    continue
                if rec['id'] == 10:
                    self.write_setting(rec)
                    continue
                if rec['id'] == 11:
                    self.write_role(rec)
                    continue
                if rec['id'] == 12:
                    self.write_actor(rec)
                    continue
                self.write_generic_func(rec)
            self.block_end()
        if 4294967291 in groups:
            self.block_start('$Set_dialogs:')
            self.line('$Dialogs:K[')
            self.indent += 1
            recs = groups[4294967291]
            for rec in recs:
                if rec['kind'] == 'prop' and rec['id'] == 118:
                    vals = rec['params']
                    if len(vals) >= 2:
                        self.line('{$adx:' + hx(vals[0]['value']) + ', $actor:' + self.actor_ref(vals[1]['value']) + '}')
            self.indent -= 1
            self.line(']')
            self.block_end()
    def write_subtitles_section(self, recs):
        self.block_start('$Set_subtittles:')
        for rec in recs:
            if rec['kind'] == 'func' and rec['id'] == 2 and rec['params']:
                self.line('$ID: ' + str(rec['params'][0]['value']))
            else:
                if rec['kind'] == 'func' and rec['id'] == 16:
                        names = ['moneyEasy', 'moneyMid', 'moneyHard', 'item1', 'item2', 'item3', 'map1', 'map2', 'map3', 'chr1', 'chr2', 'chr3', 'next1', 'next2', 'next3']
                        vals = []
                        for k, pv in enumerate(rec['params']):
                            if k < 3 or k >= 12:
                                v = str(pv['value'])
                            else:
                                v = hx(pv['value'], 8)
                            vals.append((names[k] if k < len(names) else f'p{k}', v))
                        self.line('$Rewards:{' + ' '.join((f'${k}: {v}' for k, v in vals)) + ' }')
        i = 0
        while i < len(recs):
            if recs[i]['kind'] == 'func' and recs[i]['id'] == 1302:
                self.line('$Subtittle:<')
                self.indent += 1
                j = i + 1
                while j < len(recs) and recs[j]['kind'] == 'prop':
                        pr = recs[j]
                        pid = pr['id']
                        vals = pr['params']
                        if pid == 108 and vals:
                            self.line('$l:' + self.pval(vals[0], 'num'))
                        else:
                            if pid == 110 and vals:
                                self.line('$n:' + self.pval(vals[0], 'num'))
                            else:
                                if pid == 100:
                                    self.line('$loc:I[' + ' '.join((self.pval(x, 'num') for x in vals)) + ']')
                                else:
                                    if pid == 97:
                                        self.line('$size:F[' + ' '.join((f"{x['value']:12.6f}" for x in vals)) + ']')
                                    else:
                                        if pid == 115 and vals:
                                            self.line('$scale:' + f"{vals[0]['value']:12.6f}")
                                        else:
                                            if pid == 99:
                                                self.line('$fcolor:I[' + ', '.join((self.pval(x, 'num') for x in vals)) + ']')
                                            else:
                                                if pid == 112 and len(vals) >= 2:
                                                    self.line('$sep:{$char:' + self.pval(vals[0], 'num') + ', $line:' + self.pval(vals[1], 'num') + '}')
                                                else:
                                                    if pid == 119 and vals:
                                                        aid = vals[0]['value']
                                                        align_name = {0: '$left', 1: '$center', 2: '$right'}.get(aid, hx(aid))
                                                        self.line('$align:' + align_name + ',')
                                                    else:
                                                        if pid == 84 and vals:
                                                            self.line('$style:' + self.pval(vals[0], 'num') + ',')
                                                        else:
                                                            if pid == 79:
                                                                self.line('$border:I[' + ' '.join((self.pval(x, 'num') for x in vals)) + ']')
                                                            else:
                                                                if pid == 67:
                                                                    self.line('$bcolor:I[' + ', '.join((f"{int(x['value']):3d}" for x in vals)) + ']')
                        j += 1
                self.indent -= 1
                self.line('>')
                i = j
            else:
                i += 1
        self.block_end()
    def write_scene(self, g):
        sid = g['id']
        if sid == 4294967295:
            return
        else:
            if sid == 1000:
                return
            else:
                if sid == 4294967294:
                    self.write_metadata(g)
                    return
                else:
                    normal = [x for x in g['records'] if x['kind'] in ['func', 'prop']]
                    if not normal:
                        return
                    else:
                        ev = self.event_name_from_scene(sid)
                        self.block_start('$' + ev + ':')
                        self.write_event_records(g['records'])
                        self.block_end()
    def event_name_from_scene(self, sid):
        if 10000 <= sid <= 10099:
                return f'EV_{sid - 10000:02d}'
        return f'SCENE_{sid:08X}'
    def write_metadata(self, g):
        self.block_start('$GSCD:')
        recs = g['records']
        for rec in recs:
            if rec['kind'] == 'func':
                fid = rec['id']
                name = self.r.func_name(fid)
                if fid == 2:
                    self.line('$ID: ' + self.pval(rec['params'][0], 'gsc'))
                else:
                    if fid == 16:
                        self.write_rewards(rec)
                    else:
                        if fid == 1302:
                            self.write_subtitle(recs, rec)
                        else:
                            if fid == 10:
                                self.write_setting(rec)
                            else:
                                if fid == 11:
                                    self.write_role(rec)
                                else:
                                    if fid == 12:
                                        self.write_actor(rec)
                                    else:
                                        if fid == 15:
                                            self.write_dialogs(recs, rec)
                                        else:
                                            if fid in (701, 702):
                                                self.line('$' + sanitize_keyword(name))
                                            else:
                                                self.write_generic_func(rec)
            else:
                if rec['kind'] == 'prop':
                    continue
        self.block_end()
    def write_rewards(self, rec):
        names = ['moneyEasy', 'moneyMid', 'moneyHard', 'item1', 'item2', 'item3', 'map1', 'map2', 'map3', 'chr1', 'chr2', 'chr3', 'next1', 'next2', 'next3']
        pts = self.r.ptypes(16)
        fields = []
        for i, p in enumerate(rec['params']):
            key = names[i] if i < len(names) else f'p{i}'
            v = self.pval(p, pts[i] if i < len(pts) else 'num')
            fields.append(f'${key}: {v}')
        self.line('$Rewards:{' + ' '.join(fields) + ' }')
    def write_subtitle(self, recs, func):
        self.block_start('$Set_subtittles:')
        self.line('$Subtittle:<')
        self.indent += 1
        props = []
        idx = recs.index(func) if func in recs else -1
        j = idx + 1
        while j < len(recs) and recs[j]['kind'] == 'prop':
            props.append(recs[j])
            j += 1
        for pr in props:
            pid = pr['id']
            key = self.r.prop_name(pid, 1302)
            vals = pr['params']
            pts = self.r.ptypes(1302, True, pid)
            if pid == 108:
                self.line('$l:' + self.pval(vals[0], pts[0] if pts else 'num'))
                continue
            if pid == 110:
                self.line('$n:' + self.pval(vals[0], 'num'))
                continue
            if pid == 100:
                self.line('$loc:I[' + ' '.join((self.pval(x, 'num') for x in vals)) + ']')
                continue
            if pid == 97:
                self.line('$size:F[' + ' '.join((f"{x['value']:12.6f}" for x in vals)) + ']')
                continue
            if pid == 115:
                self.line('$scale:' + self.pval(vals[0], 'num'))
                continue
            if pid == 99:
                self.line('$fcolor:I[' + ', '.join((self.pval(x, 'num') for x in vals)) + ']')
                continue
            if pid == 112:
                self.line('$sep:{$char:' + self.pval(vals[0], 'num') + ', $line:' + self.pval(vals[1], 'num') + '}')
                continue
            if pid == 119:
                self.line('$align:$center,')
                continue
            if pid == 84:
                self.line('$style:' + self.pval(vals[0], 'num') + ',')
                continue
            if pid == 79:
                self.line('$border:I[' + ' '.join((self.pval(x, 'num') for x in vals)) + ']')
                continue
            if pid == 67:
                self.line('$bcolor:I[' + ', '.join((f"{int(x['value']):3d}" for x in vals)) + ']')
                continue
            self.line('$' + sanitize_keyword(key) + ':' + self.pval(vals[0], 'num') + ',')
        self.indent -= 1
        self.line('>')
        self.indent -= 1
    def write_setting(self, rec):
        pts = self.r.ptypes(10)
        names = ['map', 'bgm', 'time', 'st', 'mflg']
        fields = []
        for i, p in enumerate(rec['params']):
            fields.append(f"${(names[i] if i < len(names) else f'p{i}')}: {self.pval(p, pts[i] if i < len(pts) else 'num')}")
        self.line('$Setting:{' + ' '.join(fields) + '}')
    def write_role(self, rec):
        if len(rec['params']) >= 2:
            self.line('$Role:{$type: ' + self.pval(rec['params'][0], 'num') + ', $count: ' + self.pval(rec['params'][1], 'num') + '}')
        else:
            self.line('$Role:{}')
    def write_actor(self, rec):
        names = ['name', 'chr', 'ctm', 'dmg', 'ia', 'zit8', 'hp', 'zit1', 'zit2', 'zit3', 'zit4', 'zit5', 'zit6', 'zit7']
        pts = self.r.ptypes(12)
        vals = []
        for i, p in enumerate(rec['params']):
            key = names[i] if i < len(names) else f'p{i}'
            if key == 'name':
                v = self.actor_ref(p['value'])
            else:
                if key == 'chr':
                    v = hx(p['value'], 4)
                else:
                    if key in ['zit1', 'zit2', 'zit3', 'zit4', 'zit5', 'zit6', 'zit7', 'zit8']:
                        v = hx(p['value'], 8)
                    else:
                        if key == 'dmg':
                            v = str(p['value'])
                        else:
                            v = self.pval(p, pts[i] if i < len(pts) else 'num')
            vals.append((key, v))
        self.line('$Actor:{' + ' '.join((f'${k}:{v}' if k == 'name' else f'${k}: {v}' for k, v in vals)) + '}')
    def write_dialogs(self, recs, func):
        self.line('$Dialogs:K[')
        self.indent += 1
        idx = recs.index(func)
        j = idx + 1
        while j < len(recs) and recs[j]['kind'] == 'prop' and (recs[j]['id'] == 118):
            pr = recs[j]
            vals = pr['params']
            self.line('{$adx:' + hx(vals[0]['value']) + ', $actor:' + self.actor_ref(vals[1]['value']) + '}')
            j += 1
        self.indent -= 1
        self.line(']')
    def write_generic_func(self, rec):
        fid = rec['id']
        name = self.r.func_name(fid)
        key = sanitize_keyword(name)
        pts = self.r.ptypes(fid)
        if not rec['params']:
            self.line('$' + key)
            return
        else:
            fields = []
            pnames = pts if pts else [f'p{i}' for i in range(len(rec['params']))]
            for i, p in enumerate(rec['params']):
                pname = pnames[i] if i < len(pnames) else f'p{i}'
                if pname == 'Character Index':
                    v = self.actor_ref(p['value'])
                else:
                    v = self.pval(p, pts[i] if i < len(pts) else 'num')
                compact_name = {'Time (s)': 'time', 'Position (X)': 'x', 'Position (Y)': 'y', 'Position (Z)': 'z', 'Rotation (X)': 'rx', 'Rotation (Y)': 'ry', 'Rotation (Z)': 'rz', 'ANM Name': 'anm', 'Music': 'bgm', 'Character Index': 'actor', 'Voice Line ID': 'adx', 'ADX ID': 'adx', 'Button ID': 'id', 'Battle Outcome ID': 'outcome', 'Scene ID': 'scene'}.get(pname, re.sub('[^A-Za-z0-9]+', '_', pname).strip('_').lower())
                fields.append((compact_name, v))
            self.compact(key, fields)
    def write_event_records(self, recs):
        current_func = None
        i = 0
        while i < len(recs):
            rec = recs[i]
            if rec['kind'] == 'func':
                fid = rec['id']
                current_func = fid
                aliases = {3: 'Unk3', 4: 'End_cutscn', 5: 'Reset_transform', 6: 'End_effects', 15: 'Dialogs', 17: 'Button_wait'}
                if fid == 1 and rec['params']:
                    self.line('$CS_time:' + f"{rec['params'][0]['value']:12.6f}")
                elif fid == 1 and (not rec['params']):
                    self.line('$Wait')
                elif fid in (13, 14):
                    j = self.write_field_group(recs, i, fid)
                    i = j - 1
                elif fid in aliases and (not rec['params']):
                    self.line('$' + aliases[fid])
                elif fid == 9:
                    if rec['params']:
                        ev = self.pval(rec['params'][0], 'num')
                        self.line('$End_event:' + ev if ev.startswith('-') else '$End_event: ' + ev)
                    else:
                        self.line('$End_event')
                elif fid == 8:
                    vals = rec['params']
                    evt = hx(vals[0]['value']) if vals else '&0000'
                    flag = hx(vals[1]['value'], 8) if len(vals) > 1 else '&00000000'
                    self.line('$Event:{$evt: ' + evt + ' $flag: ' + flag + '}')
                elif fid == 7:
                    j = self.write_link_group(recs, i)
                    i = j - 1
                elif fid == 1201:
                    self.write_camera_start(rec)
                elif fid == 1202:
                    j = self.write_secondary_camera(recs, i)
                    i = j - 1
                elif fid == 801:
                    self.write_transform(rec)
                elif fid == 901:
                    j = self.write_anim(recs, i)
                    i = j - 1
                elif fid == 1603:
                    self.compact('Play_ADX', [('actor', self.actor_ref(rec['params'][0]['value'])), ('adx', hx(rec['params'][1]['value']))])
                    if i + 1 < len(recs) and recs[i + 1]['kind'] == 'prop' and (recs[i + 1]['id'] == 119):
                        self.line('$Wait')
                        i += 1
                elif fid in (804, 805, 806, 807, 808, 809, 810):
                    names = {804: 'Visible', 805: 'Invisible', 806: 'Enable_Aura', 807: 'Disable_Aura', 808: 'Enable_ChargeAura', 809: 'Disable_ChargeAura', 810: 'Enable_MaxMode'}
                    actor = self.actor_ref(rec['params'][0]['value']) if rec['params'] else '$null'
                    self.line('$' + names[fid] + ':' + actor)
                elif fid in (1001, 1002):
                    key = 'Fade_out' if fid == 1001 else 'Fade_in'
                    if rec['params']:
                        self.line('$' + key + ':' + f"{rec['params'][0]['value']:12.6f}")
                    else:
                        self.line('$' + key)
                elif fid == 1204:
                    if rec['params']:
                        self.compact('Shake_on', [('time', f"{rec['params'][0]['value']:12.6f}")])
                    else:
                        self.line('$Shake_on')
                elif fid == 1205:
                    self.line('$Shake_off')
                elif fid == 1501:
                    self.line('$BGM:' + (str(rec['params'][0]['value']) if rec['params'] else '0'))
                elif fid == 1502:
                    self.line('$BGM_vol')
                    if i + 1 < len(recs) and recs[i + 1]['kind'] == 'prop' and (recs[i + 1]['id'] == 119):
                        i += 1
                elif fid == 1701:
                    self.compact('Button_wait', [('id', self.pval(rec['params'][0], 'num'))] if rec['params'] else [])
                elif fid == 1302:
                    self.write_generic_func(rec)
                else:
                    self.write_generic_func(rec)
            elif rec['kind'] == 'prop':
                if current_func in (7, 13, 14, 901, 1202, 1603):
                    pass
                else:
                    self.write_property(rec, current_func)
            i += 1
    def write_transform(self, rec):
        vals = rec['params']
        actor = self.actor_ref(vals[0]['value'])
        loc = vals[1:4]
        rot = vals[4:7]
        self.compact('Set_transform', [('actor', actor), ('loc', 'F[' + ', '.join((f"{p['value']:12.6f}" for p in loc)) + ']'), ('rot', 'F[' + ', '.join((f"{p['value']:12.6f}" for p in rot)) + ']')])
    def write_camera_start(self, rec):
        v = rec['params']
        self.compact('Camera_Start', [('loc', 'F[' + ', '.join((f"{p['value']:12.6f}" for p in v[0:3])) + ']'), ('rot', 'F[' + ', '.join((f"{p['value']:12.6f}" for p in v[3:6])) + ']')])
    def write_secondary_camera(self, recs, i):
        j = i + 1
        camera_props = []
        while j < len(recs) and recs[j]['kind'] == 'prop' and (recs[j]['id'] == 108):
            camera_props.append(recs[j])
            j += 1
        if not camera_props:
            self.line('$CS_Camera:K[]')
            return j
        self.line('$CS_Camera:K[')
        self.indent += 1
        for pr in camera_props:
            vals = pr['params']
            if len(vals) < 7:
                continue
            self.line('{$time:' + f"{vals[0]['value']:12.6f}" + ', $loc:F[' + ', '.join((f"{p['value']:12.6f}" for p in vals[1:4])) + '] $rot:F[' + ', '.join((f"{p['value']:12.6f}" for p in vals[4:7])) + ']}')
        self.indent -= 1
        self.line(']')
        if j < len(recs) and recs[j]['kind'] == 'prop' and (recs[j]['id'] == 119):
            self.line('$Wait')
            j += 1
        return j
    def write_anim(self, recs, i):
        rec = recs[i]
        vals = rec['params']
        self.compact('Load_Anim', [('actor', self.actor_ref(vals[0]['value'])), ('anm', hx(vals[1]['value'], 3))])
        if i + 1 < len(recs) and recs[i + 1]['kind'] == 'prop' and (recs[i + 1]['id'] == 108):
                    self.line('$Loop')
        if i + 1 < len(recs) and recs[i + 1]['kind'] == 'prop' and (recs[i + 1]['id'] == 119):
                    self.line('$Wait')
        return i + 2 if i + 1 < len(recs) and recs[i + 1]['kind'] in ['prop'] and (recs[i + 1]['id'] in [108, 119]) else i + 1
    def write_link_group(self, recs, i):
        event_items = []
        audio_items = []
        j = i + 1
        while j < len(recs) and recs[j]['kind'] == 'prop' and (recs[j]['id'] == 97):
                    p = recs[j]['params']
                    if len(p) >= 2:
                        target = p[1]['value']
                        evnum = target - 10000 if target >= 10000 else target
                        event_items.append('{$if:' + hx(p[0]['value']) + ', $to:$EV_' + format(evnum, '02d') + '}')
                    j += 1
        while j < len(recs) and recs[j]['kind'] == 'prop' and (recs[j]['id'] == 118):
                    p = recs[j]['params']
                    if len(p) >= 2:
                        audio_items.append('{$if:' + hx(p[0]['value']) + ', $adx:' + hx(p[1]['value']) + '}')
                    j += 1
        self.line('$Link:{')
        self.indent += 1
        if event_items:
            self.line('$event:K[')
            self.indent += 1
            # Siempre en orden ascendente $EV_00 -> $EV_XX (orden estable:
            # las condiciones repetidas hacia un mismo EV conservan su orden).
            event_items.sort(key=link_event_sort_key)
            for x in event_items:
                self.line(x)
            self.indent -= 1
            self.line('],')
        else:
            self.line('$event:null,')
        if audio_items:
            self.line('$audio:K[')
            self.indent += 1
            for x in audio_items:
                self.line(x)
            self.indent -= 1
            self.line(']')
        else:
            self.line('$audio:null,')
        self.indent -= 1
        self.line('}')
        return j
    def write_field_group(self, recs, i, fid):
        key = 'Set_plafield' if fid == 13 else 'Set_cpufield'
        j = i + 1
        fields = []
        while j < len(recs) and recs[j]['kind'] == 'prop':
                pr = recs[j]
                pts = self.r.ptypes(fid, True, pr['id'])
                pnames = DB['prop_param_map'].get((pr['id'], fid), [])
                for k, v in enumerate(pr['params']):
                    pn = pnames[k] if k < len(pnames) else f'p{k}'
                    field_names = {48: 'zit1', 49: 'zit2', 50: 'zit3', 51: 'zit4', 52: 'zit5', 53: 'zit6', 54: 'zit7', 66: 'addBlast', 67: 'actor', 70: 'addKi', 72: 'addHp', 73: 'ki', 98: 'blast', 102: 'ki', 104: 'hp'}
                    ck = field_names.get(pr['id'], {'Character Index': 'actor'}.get(pn, re.sub('[^A-Za-z0-9]+', '_', pn).strip('_').lower()))
                    if pr['id'] == 67 or pn == 'Character Index':
                        if pr['id'] == 67:
                            vv = '$pla' + str(v['value'] & 32767)
                        else:
                            vv = self.actor_ref(v['value'])
                    else:
                        if pr['id'] in [48, 49, 50, 51, 52, 53, 54]:
                            vv = hx(v['value'], 8)
                        else:
                            vv = self.pval(v, pts[k] if k < len(pts) else 'num')
                    fields.append((ck, vv))
                j += 1
        if not fields:
            self.line('$' + key + ':null')
        else:
            self.line('$' + key + ':<' + ' '.join(('$' + k + ':' + v for k, v in fields)) + ' >')
        return j
    def write_property(self, rec, current_func):
        pid = rec['id']
        fid = rec.get('func', current_func or 0)
        name = self.r.prop_name(pid, fid)
        vals = rec['params']
        if pid == 108:
            if fid == 901:
                self.line('$Loop')
            else:
                if fid == 1202:
                    pass
                else:
                    self.line('$' + sanitize_keyword(name))
            return None
        else:
            if pid == 119:
                if fid in [901, 1603, 1602, 1001, 1202, 1502]:
                    self.line('$Wait')
                else:
                    self.line('$' + sanitize_keyword(name))
                return None
            else:
                if pid in [48, 49, 50, 51, 52, 53, 54, 66, 67, 70, 72, 73, 98, 102, 104]:
                    if fid == 13:
                        key = 'Set_plafield'
                    else:
                        if fid == 14:
                            key = 'Set_cpufield'
                        else:
                            key = sanitize_keyword(name)
                    if len(vals) == 1:
                        field_names = {48: 'zit1', 49: 'zit2', 50: 'zit3', 51: 'zit4', 52: 'zit5', 53: 'zit6', 54: 'zit7', 66: 'addBlast', 67: 'actor', 70: 'addKi', 72: 'addHp', 73: 'ki', 98: 'blast', 102: 'ki', 104: 'hp'}
                        fk = field_names.get(pid, re.sub('[^A-Za-z0-9]+', '_', DB['prop_param_map'].get((pid, fid), [name])[0]).strip('_').lower())
                        if pid == 67:
                            vv = '$pla' + str(vals[0]['value'] & 32767)
                        else:
                            vv = self.pval(vals[0], 'item' if pid in range(48, 85) else 'num')
                        self.compact(key, [(fk, vv)])
                    else:
                        self.compact(key, [(f'p{k}', self.pval(v, 'num')) for k, v in enumerate(vals)])
                    return None
                else:
                    pts = self.r.ptypes(fid, True, pid)
                    fields = []
                    for k, v in enumerate(vals):
                        pn = pts[k] if k < len(pts) else f'p{k}'
                        fields.append((re.sub('[^A-Za-z0-9]+', '_', pn).strip('_').lower(), self.pval(v, pts[k] if k < len(pts) else 'num')))
                    self.compact(sanitize_keyword(name), fields)
class GSCFParseError(Exception):
    # return None
    pass
class GSCFCompiler:
    """Compiler for the textual GSCF dialect emitted by this application.

    The binary layout follows the supplied BT3 gsc-reader implementation:
    GSCF/GSHD/GSCD/GSAC/GSDT sectors, little-endian 32-bit GSDT values, and
    4-byte parameter references whose low 16 bits index GSDT values.
    """
    FUNC = {
        'Wait': 1,
        'CS_time': 1,
        'ID': 2,
        'Unk3': 3,
        'End_cutscn': 4,
        'Reset_transform': 5,
        'End_effects': 6,
        'Link': 7,
        'Event': 8,
        'End_event': 9,
        'Setting': 10,
        'Role': 11,
        'Actor': 12,
        'Set_plafield': 13,
        'Set_cpufield': 14,
        'Dialogs': 15,
        'Rewards': 16,
        'Load_TXT': 701,
        'Load_LPS': 702,
        'Set_transform': 801,
        'Set_position': 802,
        'Set_rotation': 803,
        'Visible': 804,
        'Invisible': 805,
        'Enable_Aura': 806,
        'Disable_Aura': 807,
        'Enable_ChargeAura': 808,
        'Disable_ChargeAura': 809,
        'Enable_MaxMode': 810,
        'Load_Anim': 901,
        'Move': 902,
        'Fade_out': 1001,
        'Fade_in': 1002,
        'Fade_stop': 1003,
        'Camera_Start': 1201,
        'CS_Camera': 1202,
        'Camera_Reset': 1203,
        'Shake_on': 1204,
        'Shake_off': 1205,
        'Load_String': 1301,
        'Subtittle': 1302,
        'BGM': 1501,
        'BGM_vol': 1502,
        'Music': 1501,
        'Music_off': 1502,
        'Play_SE': 1601,
        'Play_ADX': 1603,
        'Button_wait': 1701,
    }
    PROP = {
        ('Set_plafield', 'zit1'): (48, 13),
        ('Set_cpufield', 'zit1'): (48, 14),
        ('Set_plafield', 'zit2'): (49, 13),
        ('Set_cpufield', 'zit2'): (49, 14),
        ('Set_plafield', 'zit3'): (50, 13),
        ('Set_cpufield', 'zit3'): (50, 14),
        ('Set_plafield', 'zit4'): (51, 13),
        ('Set_cpufield', 'zit4'): (51, 14),
        ('Set_plafield', 'zit5'): (52, 13),
        ('Set_cpufield', 'zit5'): (52, 14),
        ('Set_plafield', 'zit6'): (53, 13),
        ('Set_cpufield', 'zit6'): (53, 14),
        ('Set_plafield', 'zit7'): (54, 13),
        ('Set_cpufield', 'zit7'): (54, 14),
        ('Set_plafield', 'addBlast'): (66, 13),
        ('Set_cpufield', 'addBlast'): (66, 14),
        ('Set_plafield', 'actor'): (67, 13),
        ('Set_cpufield', 'actor'): (67, 14),
        ('Set_plafield', 'addKi'): (70, 13),
        ('Set_cpufield', 'addKi'): (70, 14),
        ('Set_plafield', 'addHp'): (72, 13),
        ('Set_cpufield', 'addHp'): (72, 14),
        ('Set_plafield', 'ki'): (73, 13),
        ('Set_cpufield', 'ki'): (73, 14),
        ('Set_plafield', 'blast'): (98, 13),
        ('Set_cpufield', 'blast'): (98, 14),
        ('Set_plafield', 'hp'): (104, 13),
        ('Set_cpufield', 'hp'): (104, 14),
        ('Set_plafield', 'health'): (104, 13),
        ('Set_cpufield', 'health'): (104, 14),
    }
    SUBPROPS = {'l': 108, 'n': 110, 'loc': 100, 'size': 97, 'scale': 115, 'fcolor': 99, 'sep': 112, 'align': 119, 'style': 84, 'border': 79, 'bcolor': 67}
    FIELD_IDS = {'zit1': 48, 'zit2': 49, 'zit3': 50, 'zit4': 51, 'zit5': 52, 'zit6': 53, 'zit7': 54, 'addBlast': 66, 'actor': 67, 'addKi': 70, 'addHp': 72, 'ki': 73, 'blast': 98, 'hp': 104, 'health': 104}
    def __init__(self, text):
        self.text = text.replace('\r\n', '\n').replace('\r', '\n')
        self.gsdt = []
        self.gsdt_map = {}
        self.scenes = []
        self.warnings = []
        self._parse()
    @staticmethod
    def _balanced(text, start, op, cl):
        depth = 0
        for i in range(start, len(text)):
            c = text[i]
            if c == op:
                depth += 1
            else:
                if c == cl:
                    depth -= 1
                    if depth == 0:
                        return (text[start + 1:i], i + 1)
        raise GSCFParseError(f'Bloco {op}{cl} não fechado na posição {start}')
    @classmethod
    def _blocks(cls, text, name_pattern):
        pat = re.compile(name_pattern, re.M)
        out = []
        for m in pat.finditer(text):
            i = m.end()
            while i < len(text) and text[i].isspace():
                i += 1
            if i >= len(text) or text[i] != ':':
                continue
            i += 1
            while i < len(text) and text[i].isspace():
                i += 1
            if i >= len(text):
                continue
            op = text[i]
            if op == '<':
                content, end = cls._balanced(text, i, '<', '>')
            elif op == '{':
                content, end = cls._balanced(text, i, '{', '}')
            elif op == '[':
                content, end = cls._balanced(text, i, '[', ']')
            else:
                continue
            out.append((m.group(0), content, end))
        return out
    @classmethod
    def commands(cls, text):
        out = []
        i = 0
        n = len(text)
        while i < n:
            while i < n and (text[i].isspace() or text[i] == ','):
                i += 1
            if i >= n:
                break
            if text[i] != '$':
                j = text.find('$', i)
                if j < 0:
                    break
                i = j
            m = re.match('\\$([A-Za-z0-9_]+)', text[i:])
            if not m:
                raise GSCFParseError(f'Comando inválido perto de: {text[i:i + 60]!r}')
            name = m.group(1)
            i += m.end()
            while i < n and text[i].isspace():
                i += 1
            value = None
            delim = None
            if i < n and text[i] == ':':
                i += 1
                while i < n and text[i].isspace():
                    i += 1
                if i < n and text[i] in '<{[':
                    op = text[i]
                    cl = {'<': '>', '{': '}', '[': ']'}[op]
                    content, end = cls._balanced(text, i, op, cl)
                    value = content
                    delim = op
                    i = end
                elif text.startswith('K[', i):
                    content, end = cls._balanced(text, i + 1, '[', ']')
                    value = content
                    delim = '['
                    i = end
                else:
                    j = i
                    while j < n and text[j] not in '\n,':
                        j += 1
                    value = text[i:j].strip()
                    i = j
            out.append((name, value, delim))
        return out
    @staticmethod
    def fields(body):
        res = []
        i = 0
        n = len(body)
        while i < n:
            while i < n and (body[i].isspace() or body[i] == ','):
                i += 1
            if i < n and body[i] == '>':
                i += 1
                continue
            if i >= n:
                break
            if body[i] != '$':
                j = body.find('$', i)
                if j < 0:
                    break
                i = j
            m = re.match('\\$([A-Za-z0-9_]+)\\s*:', body[i:])
            if not m:
                raise GSCFParseError(f'Campo inválido: {body[i:i + 60]!r}')
            key = m.group(1)
            i += m.end()
            while i < n and body[i].isspace():
                i += 1
            if i < n and (body[i] in 'IFK' and i + 1 < n and (body[i + 1] == '[') or body[i] in '[{<'):
                if body[i] in 'IFK' and i + 1 < n and (body[i + 1] == '['):
                    prefix = body[i]
                    op = '['
                    cl = ']'
                    start = i + 1
                    val, end = GSCFCompiler._balanced(body, start, op, cl)
                    i = end
                    res.append((key, prefix + op + val + cl))
                else:
                    op = body[i]
                    cl = {'[': ']', '{': '}', '<': '>'}[op]
                    val, end = GSCFCompiler._balanced(body, i, op, cl)
                    i = end
                    res.append((key, op + val + cl))
            else:
                mm = re.search('\\s+\\$[A-Za-z0-9_]+\\s*:', body[i:])
                if mm:
                    j = i + mm.start()
                else:
                    j = i
                    while j < n and body[j] not in '\n,':
                        j += 1
                res.append((key, body[i:j].strip().rstrip(',')))
                i = j
        return res
    @staticmethod
    def scalar(v):
        if v is None:
            return 0
        else:
            v = v.strip().rstrip(',')
            if v.startswith('$pla'):
                return int(v[4:])
            else:
                if v.startswith('$cpu'):
                    return 32768 | int(v[4:])
                else:
                    if v.lower() in ['true', 'false']:
                        return 1 if v.lower() == 'true' else 0
                    else:
                        if v.startswith('&'):
                            x = int(v[1:], 16)
                            return x if x < 2147483648 else x - 4294967296
                        else:
                            try:
                                if re.search('[.eE]', v):
                                    return float(v)
                                else:
                                    return int(v, 10)
                            except ValueError:
                                raise GSCFParseError(f'Valor não numérico: {v!r}')
    @classmethod
    def array(cls, v):
        v = v.strip()
        if len(v) >= 2 and v[0] in 'IF' and (v[1] == '['):
            return [cls.scalar(x) for x in re.split('[\\s,]+', v[2:(-1)].strip()) if x]
        else:
            raise GSCFParseError(f'Array inválido: {v!r}')
    def ref(self, val, is_float=False):
        if is_float:
            raw = struct.pack('<f', float(val))
        else:
            raw = struct.pack('<i', int(val))
        key = ('float' if is_float else 'int', raw)
        if key not in self.gsdt_map:
            idx = len(self.gsdt)
            self.gsdt.append(raw)
            self.gsdt_map[key] = idx
        return self.gsdt_map[key]
    def func(self, fid, vals, types=None):
        types = types or ['int'] * len(vals)
        b = bytearray(struct.pack('<BBH', 1, len(vals), fid))
        for v, t in zip(vals, types):
            b += bytes([26 if t == 'float' else 10]) + struct.pack('<H', self.ref(v, t == 'float')) + b'\x00'
        return bytes(b)
    def prop(self, pid, fid, vals, types=None):
        types = types or ['int'] * len(vals)
        b = bytearray(bytes([8, pid, len(vals), 0]))
        for v, t in zip(vals, types):
            b += bytes([26 if t == 'float' else 10]) + struct.pack('<H', self.ref(v, t == 'float')) + b'\x00'
        return bytes(b)
    def compact_fields(self, body):
        return dict(self.fields(body))
    def event_records(self, body):
        records = []
        last_name = None
        for name, val, delim in self.commands(body):
            prior_name = last_name
            last_name = name
            if name in ['Wait', 'CS_time']:
                if name == 'Wait':
                    if prior_name in ['Load_Anim', 'Fade_out', 'Fade_in', 'CS_Camera', 'BGM_vol', 'Music_off', 'Play_ADX']:
                        pfid = {'Load_Anim': 901, 'Fade_out': 1001, 'Fade_in': 1002, 'CS_Camera': 1202, 'BGM_vol': 1502, 'Music_off': 1502, 'Play_ADX': 1603}[prior_name]
                        records.append(self.prop(119, pfid, []))
                    else:
                        records.append(self.func(1, []))
                else:
                    records.append(self.func(1, [self.scalar(val)], ['float']))
                continue
            if name in ['Unk3', 'End_cutscn', 'Reset_transform', 'End_effects', 'Camera_Reset', 'Shake_off', 'Fade_stop']:
                records.append(self.func(self.FUNC[name], []))
                continue
            if name == 'End_event':
                records.append(self.func(9, [self.scalar(val or '0')]))
                continue
            if name == 'Event':
                f = self.compact_fields(val or '')
                records.append(self.func(8, [self.scalar(f.get('evt', '0')), self.scalar(f.get('flag', '0'))]))
                continue
            if name == 'Set_transform':
                f = self.compact_fields(val)
                loc = self.array(f['loc'])[0:3]
                rot = self.array(f['rot'])[0:3]
                records.append(self.func(801, [self.scalar(f['actor'])] + loc + rot, ['int'] + ['float'] * 6))
                continue
            if name in ['Set_position', 'Set_rotation']:
                f = self.compact_fields(val)
                arr = self.array(f.get('loc') or f.get('rot'))
                records.append(self.func(self.FUNC[name], [self.scalar(f['actor'])] + arr, ['int'] + ['float'] * 3))
                continue
            if name in ['Visible', 'Invisible', 'Enable_Aura', 'Disable_Aura', 'Enable_ChargeAura', 'Disable_ChargeAura', 'Enable_MaxMode']:
                records.append(self.func(self.FUNC[name], [self.scalar(val)]))
                continue
            if name == 'Load_Anim':
                f = self.compact_fields(val)
                records.append(self.func(901, [self.scalar(f['actor']), self.scalar(f['anm'])]))
                continue
            if name == 'Loop':
                records.append(self.prop(108, 901, []))
                continue
            if name == 'Move':
                f = self.compact_fields(val)
                records.append(self.func(902, [self.scalar(f.get('actor', '0'))]))
                continue
            if name in ['Fade_out', 'Fade_in']:
                records.append(self.func(self.FUNC[name], [self.scalar(val)] if val else [], ['float'] if val else []))
                continue
            if name == 'Camera_Start':
                f = self.compact_fields(val)
                loc = self.array(f['loc'])
                rot = self.array(f['rot'])
                records.append(self.func(1201, loc + rot, ['float'] * 6))
                continue
            if name == 'CS_Camera':
                points = []
                if delim == '[':
                    q = 0
                    while q < len(val):
                        while q < len(val) and val[q].isspace():
                            q += 1
                        if q < len(val) and val[q] == ',':
                            q += 1
                            continue
                        if q >= len(val):
                            break
                        if val[q] != '{':
                            q += 1
                            continue
                        item, end = self._balanced(val, q, '{', '}')
                        f = self.compact_fields(item)
                        points.append([self.scalar(f['time'])] + self.array(f['loc']) + self.array(f['rot']))
                        q = end
                records.append(self.func(1202, []))
                for p in points:
                    records.append(self.prop(108, 1202, p, ['float'] * 7))
                continue
            if name == 'Play_ADX':
                f = self.compact_fields(val)
                records.append(self.func(1603, [self.scalar(f['actor']), self.scalar(f['adx'])]))
                continue
            if name == 'Play_SE':
                records.append(self.func(1601, [self.scalar(val)]))
                continue
            if name in ['BGM', 'Music']:
                records.append(self.func(1501, [self.scalar(val)]))
                continue
            if name in ['BGM_vol', 'Music_off']:
                records.append(self.func(1502, []))
                continue
            if name == 'Button_wait':
                f = self.compact_fields(val) if val else {}
                records.append(self.func(1701, [self.scalar(f.get('id', '0'))]))
                continue
            if name == 'Shake_on':
                f = self.compact_fields(val) if val else {}
                records.append(self.func(1204, [self.scalar(f.get('time', '0'))], ['float']))
                continue
            if name == 'Link':
                records.append(self.func(7, []))
                ftext = val or ''
                for sec, pid in [('event', 97), ('audio', 118)]:
                    mm = re.search('\\$' + sec + '\\s*:\\s*K\\[(.*?)\\]', ftext, re.S)
                    if mm:
                        for item in re.finditer('\\{(.*?)\\}', mm.group(1), re.S):
                            ff = self.compact_fields(item.group(1))
                            if sec == 'event':
                                records.append(self.prop(97, 7, [self.scalar(ff.get('if', '0')), self.event_id(ff.get('to', '0'))]))
                            else:
                                records.append(self.prop(118, 7, [self.scalar(ff.get('if', '0')), self.scalar(ff.get('adx', '0'))]))
                continue
            if name in ['Set_plafield', 'Set_cpufield']:
                fid = 13 if name == 'Set_plafield' else 14
                records.append(self.func(fid, []))
                if delim == '<' and val and (val.strip().lower() != 'null'):
                    for k, v in self.fields(val):
                        pid = self.FIELD_IDS.get(k)
                        if pid is None:
                            self.warnings.append(f'Campo desconhecido {name}:{k}')
                            continue
                        if pid == 67:
                            records.append(self.prop(pid, fid, [self.scalar(v)]))
                            continue
                        if pid in [48, 49, 50, 51, 52, 53, 54]:
                            records.append(self.prop(pid, fid, [self.scalar(v)]))
                            continue
                        records.append(self.prop(pid, fid, [self.scalar(v)]))
                continue
            if name not in ['Set_scene', 'Set_dialogs', 'Set_subtittles', 'ID', 'Rewards', 'Actor', 'Role', 'Dialogs', 'Subtittle', 'Load_files']:
                self.warnings.append(f'Comando não suportado no evento: ${name}')
        return b''.join(records)
    @staticmethod
    def event_id(v):
        v = v.strip()
        if v.startswith('$EV_'):
            return 10000 + int(v[4:])
        else:
            return GSCFCompiler.scalar(v)
    def subtitle_records(self, body):
        out = []
        for name, val, delim in self.commands(body):
            if name == 'ID':
                out.append(self.func(2, [self.scalar(val)]))
            else:
                if name == 'Rewards':
                    f = self.compact_fields(val)
                    keys = ['moneyEasy', 'moneyMid', 'moneyHard', 'item1', 'item2', 'item3', 'map1', 'map2', 'map3', 'chr1', 'chr2', 'chr3', 'next1', 'next2', 'next3']
                    out.append(self.func(16, [self.scalar(f.get(k, '0')) for k in keys]))
                else:
                    if name == 'Subtittle':
                        out.append(self.func(1302, []))
                        for k, v in self.fields(val):
                            pid = self.SUBPROPS.get(k)
                            if pid is None:
                                continue
                            else:
                                if pid == 100:
                                    arr = self.array(v)
                                    out.append(self.prop(pid, 1302, arr))
                                else:
                                    if pid == 112:
                                        sf = self.compact_fields(v[1:(-1)] if v.startswith('{') else v)
                                        out.append(self.prop(pid, 1302, [self.scalar(sf.get('char', '0')), self.scalar(sf.get('line', '0'))]))
                                    else:
                                        if pid in [97, 99, 79, 67]:
                                            arr = self.array(v)
                                            types = ['float'] * len(arr) if pid == 97 else ['int'] * len(arr)
                                            out.append(self.prop(pid, 1302, arr, types))
                                        else:
                                            if pid == 119:
                                                out.append(self.prop(pid, 1302, [1]))
                                            else:
                                                if pid == 115:
                                                    out.append(self.prop(pid, 1302, [self.scalar(v)], ['float']))
                                                else:
                                                    out.append(self.prop(pid, 1302, [self.scalar(v)]))
        return b''.join(out)
    def scene_setup_records(self, body):
        out = []
        for name, val, delim in self.commands(body):
            if name == 'Setting':
                f = self.compact_fields(val)
                out.append(self.func(10, [self.scalar(f.get(k, '0')) for k in ['map', 'bgm', 'time', 'st', 'mflg']]))
            else:
                if name == 'Role':
                    f = self.compact_fields(val)
                    out.append(self.func(11, [self.scalar(f.get('type', '0')), self.scalar(f.get('count', '0'))]))
                else:
                    if name == 'Actor':
                        f = self.compact_fields(val)
                        keys = ['name', 'chr', 'ctm', 'dmg', 'ia', 'zit8', 'hp', 'zit1', 'zit2', 'zit3', 'zit4', 'zit5', 'zit6', 'zit7']
                        types = ['int'] * 14
                        out.append(self.func(12, [self.scalar(f.get(k, '0')) for k in keys], types))
        return b''.join(out)
    def dialogs_records(self, body):
        out = [self.func(15, [])]
        for name, val, delim in self.commands(body):
            if name == 'Dialogs' and delim == '[':
                    for item in re.finditer('\\{(.*?)\\}', val, re.S):
                        f = self.compact_fields(item.group(1))
                        out.append(self.prop(118, 15, [self.scalar(f.get('adx', '0')), self.scalar(f.get('actor', '0'))]))
        return b''.join(out)
    def load_records(self, body):
        out = []
        for name, val, delim in self.commands(body):
            if name == 'Load_TXT':
                out.append(self.func(701, []))
            else:
                if name == 'Load_LPS':
                    out.append(self.func(702, []))
        return b''.join(out)
    def build_scene(self, sid, body):
        if sid in [(-1)]:
            return struct.pack('<IIII', 1196638531, 16, 16, 4294967295) + struct.pack('<I', 10000) + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + b''
        else:
            return None
    def _parse(self):
        text = self.text
        evs = []
        for m in re.finditer('\\$EV_(\\d+)\\s*:', text):
            i = m.end()
            while i < len(text) and text[i].isspace():
                i += 1
            if i < len(text) and text[i] == '<':
                body, end = self._balanced(text, i, '<', '>')
                evs.append((int(m.group(1)), body))
        self.events = evs
        blocks = {}
        for name in ('Load_files', 'Set_subtittles', 'Set_scene', 'Set_dialogs'):
            bs = self._blocks(text, f'\\${name}')
            if bs:
                blocks[name] = bs[0][1]
        self.blocks = blocks
    def compile(self):
        scenes = []
        body = bytearray(struct.pack('<HH', 2, 10000) + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        scenes.append(((-1), bytes(body)))
        body = bytearray()
        for sid in [(-3), (-4), (-5), (-2)]:
            body += struct.pack('<HH', 2, sid & 65535)
        scenes.append((1000, bytes(body)))
        mapping = [((-2), 'Load_files', self.load_records), ((-3), 'Set_subtittles', self.subtitle_records), ((-4), 'Set_scene', self.scene_setup_records), ((-5), 'Set_dialogs', self.dialogs_records)]
        for sid, key, fn in mapping:
            if key in self.blocks:
                scenes.append((sid, fn(self.blocks[key])))
        for n, body in self.events:
            scenes.append((10000 + n, self.event_records(body)))
        gsac = bytearray()
        for sid, content in scenes:
            if sid in ((-1), 4294967295):
                pad = 0
            else:
                pad = 16 - len(content) % 16
            content_padded = content + b'\x00' * pad
            gsac += b'GSAC' + struct.pack('<III', 16, len(content_padded), sid & 4294967295) + content_padded + b'EOFC' + struct.pack('<I', 16) + b'\x00\x00\x00\x00\x00\x00\x00\x00'
        gsac += b'EOFC' + struct.pack('<I', 16) + b'\x00\x00\x00\x00\x00\x00\x00\x00'
        gsdt = b''.join(self.gsdt)
        header = bytearray()
        header += b'GSCF' + struct.pack('<III', 16, 0, 1)
        header += b'GSHD' + struct.pack('<I', 16) + struct.pack('<IIIIII', 16, 0, 3, 2, 0, 0)
        header += b'EOFC' + struct.pack('<I', 16) + b'\x00\x00\x00\x00\x00\x00\x00\x00'
        gscd_size = max(0, len(gsac) - 16)
        header += b'GSCD' + struct.pack('<III', 16, gscd_size, 1)
        header += gsac
        header += b'GSDT' + struct.pack('<III', 16, len(gsdt), 0) + gsdt
        header += b'EOFC' + struct.pack('<I', 16) + b'\x00\x00\x00\x00\x00\x00\x00\x00' + b'EOFC' + struct.pack('<I', 16) + b'\x00\x00\x00\x00\x00\x00\x00\x00'
        file_size = len(header)
        struct.pack_into('<I', header, 8, file_size - 32)
        return bytes(header)
def compile_gscf_text(text):
    c = GSCFCompiler(text)
    return (c.compile(), c.warnings)
def compile_gscf_file(path, out=None):
    p = Path(path)
    data = p.read_text(encoding='utf-8-sig')
    b, w = compile_gscf_text(data)
    if out is None:
        out = p.with_suffix('.unk')
    Path(out).write_bytes(b)
    return (Path(out), w)
def convert(path):
    r = GSCReader(path)
    return GSCFWriter(r).write()


class GSCConverterFrame(ttk.Frame):
    """Pestaña embebida: Conversor GSC <-> GSCF (bidireccional).

    Sigue el tema visual general de la app (self.theme del editor principal)
    a través del método retheme(theme), que el editor llama cada vez que el
    usuario cambia de tema, color de acento o color de fondo.
    """
    def __init__(self, parent, theme=None):
        super().__init__(parent)
        self.theme = dict(theme) if theme else {
            "bg": "#101722", "frame_bg": "#172231", "accent": "#20a4f3",
        }
        self.src = tk.StringVar()
        self.dst = tk.StringVar()
        self.status = tk.StringVar(value='Listo.')
        self._ui()
        self.retheme(self.theme)

    # ------------------------------------------------------------- UI --
    def _ui(self):
        self.header = tk.Frame(self, height=86)
        self.header.pack(fill='x')
        self.header.pack_propagate(False)

        self.title_frame = tk.Frame(self.header)
        self.title_frame.pack(side='left', fill='y', padx=24)
        self.title_lbl = tk.Label(
            self.title_frame, text='CONVERSOR GSC ⇄ GSCF',
            font=('Segoe UI', 20, 'bold'),
        )
        self.title_lbl.pack(anchor='w', pady=(12, 0))
        self.subtitle_lbl = tk.Label(
            self.title_frame,
            text='Convierte escenarios BT3 entre formato binario (.unk/.gsc) y texto editable (GSCF)',
            font=('Segoe UI', 9),
        )
        self.subtitle_lbl.pack(anchor='w', pady=(1, 10))
        self.badge_lbl = tk.Label(self.header, text='GSCF', font=('Segoe UI', 11, 'bold'))
        self.badge_lbl.pack(side='right', padx=24)

        self.info_bar = tk.Frame(self, highlightthickness=1)
        self.info_bar.pack(fill='x', padx=24, pady=(14, 0))
        self.info_lbl = tk.Label(
            self.info_bar,
            text=('Esta pestaña permite convertir un archivo de escena binario (.unk / .gsc) a '
                  'texto editable GSCF y viceversa, comparar un binario compilado contra el '
                  'original byte a byte, y analizar un GSCF antes de compilarlo.'),
            font=('Segoe UI', 9), justify='left', wraplength=1100,
        )
        self.info_lbl.pack(anchor='w', padx=14, pady=8)

        self.workspace = tk.Frame(self)
        self.workspace.pack(fill='both', expand=True, padx=24, pady=18)

        self.source_card = tk.Frame(self.workspace, highlightthickness=1)
        self.source_card.pack(fill='x', pady=(0, 14))
        self.source_title_lbl = tk.Label(
            self.source_card, text='ARCHIVO DE ENTRADA', font=('Segoe UI', 9, 'bold'),
        )
        self.source_title_lbl.pack(anchor='w', padx=16, pady=(12, 4))
        self.row = tk.Frame(self.source_card)
        self.row.pack(fill='x', padx=16, pady=(0, 14))
        self.row_label = tk.Label(self.row, text='Origen', font=('Segoe UI', 9))
        self.row_label.pack(side='left', padx=(0, 10))
        ttk.Entry(self.row, textvariable=self.src, style='GSCInput.TEntry').pack(
            side='left', fill='x', expand=True, padx=(0, 10), ipady=4
        )
        ttk.Button(self.row, text='ABRIR ARCHIVO', style='GSC.TButton', command=self.open_src).pack(side='left')

        self.action_bar = tk.Frame(self.workspace, highlightthickness=1)
        self.action_bar.pack(fill='x', pady=(0, 14))
        self.action_label = tk.Label(self.action_bar, text='ACCIONES', font=('Segoe UI', 9, 'bold'))
        self.action_label.pack(side='left', padx=(16, 10), pady=12)
        self.controls = tk.Frame(self.action_bar)
        self.controls.pack(side='left', pady=7)
        ttk.Button(self.controls, text='UNK → GSCF', style='GSC.TButton', command=self.do_forward).pack(side='left', padx=3)
        ttk.Button(self.controls, text='GSCF → UNK', style='GSC.TButton', command=self.do_reverse).pack(side='left', padx=3)
        ttk.Button(self.controls, text='COMPARAR BINARIO', style='GSC.TButton', command=self.compare_binary).pack(side='left', padx=3)
        ttk.Button(self.controls, text='ANALIZAR GSCF', style='GSC.TButton', command=self.analyze_gscf).pack(side='left', padx=3)
        ttk.Button(self.controls, text='LIMPIAR', style='GSC.TButton', command=self.clear).pack(side='left', padx=3)

        self.output_card = tk.Frame(self.workspace, highlightthickness=1)
        self.output_card.pack(fill='both', expand=True)
        self.output_title_lbl = tk.Label(
            self.output_card, text='SALIDA Y DIAGNÓSTICO', font=('Segoe UI', 9, 'bold'),
        )
        self.output_title_lbl.pack(anchor='w', padx=16, pady=(12, 6))
        self.main = tk.Frame(self.output_card)
        self.main.pack(fill='both', expand=True, padx=16, pady=(0, 16))
        self.text = tk.Text(
            self.main, wrap='none', font=('Consolas', 10),
            insertbackground='white', relief='flat', padx=12, pady=10,
        )
        ys = ttk.Scrollbar(self.main, orient='vertical', command=self.text.yview)
        xs = ttk.Scrollbar(self.main, orient='horizontal', command=self.text.xview)
        self.text.configure(yscrollcommand=ys.set, xscrollcommand=xs.set)
        self.text.grid(row=0, column=0, sticky='nsew')
        ys.grid(row=0, column=1, sticky='ns')
        xs.grid(row=1, column=0, sticky='ew')
        self.main.rowconfigure(0, weight=1)
        self.main.columnconfigure(0, weight=1)

        self.footer = tk.Frame(self, height=32)
        self.footer.pack(fill='x')
        self.footer.pack_propagate(False)
        self.status_lbl = ttk.Label(self.footer, textvariable=self.status, style='GSCInfo.TLabel')
        self.status_lbl.pack(side='left', padx=24, pady=7)
        self.footer_label = tk.Label(self.footer, text='BT3 TOOLSET', font=('Segoe UI', 8, 'bold'))
        self.footer_label.pack(side='right', padx=24)

    # --------------------------------------------------------- tema --
    def retheme(self, theme):
        """Recolorea toda la pestaña siguiendo el tema activo del editor."""
        self.theme = dict(theme)
        bg = self.theme.get("bg", "#101722")
        frame_bg = self.theme.get("frame_bg", "#172231")
        accent = self.theme.get("accent", "#20a4f3")
        fg = "#f4f7fb"
        muted = shade_hex(bg, 120)
        border = shade_hex(frame_bg, 30)
        header_bg = shade_hex(frame_bg, -10)
        bar_bg = shade_hex(frame_bg, -4)
        field_bg = shade_hex(frame_bg, 12)
        text_bg = shade_hex(bg, -8)
        hover = shade_hex(accent, 22)
        pressed = shade_hex(accent, -22)

        st = ttk.Style(self)
        try:
            st.theme_use('clam')
        except Exception:
            pass
        st.configure('GSC.TButton', padding=(12, 8), font=('Segoe UI', 9, 'bold'), background=field_bg, foreground=fg)
        st.map('GSC.TButton', background=[('active', hover), ('pressed', pressed)], foreground=[('active', '#ffffff')])
        st.configure('GSCInput.TEntry', fieldbackground=field_bg, foreground=fg, insertcolor=fg)
        st.configure('GSCInfo.TLabel', font=('Segoe UI', 9), foreground=muted, background=header_bg)

        self.configure(style='TFrame')

        self.header.configure(bg=header_bg)
        self.title_frame.configure(bg=header_bg)
        self.title_lbl.configure(bg=header_bg, fg='#ffffff')
        self.subtitle_lbl.configure(bg=header_bg, fg=muted)
        self.badge_lbl.configure(bg=header_bg, fg=accent)

        self.info_bar.configure(bg=frame_bg, highlightbackground=border, highlightcolor=border)
        self.info_lbl.configure(bg=frame_bg, fg=muted)

        self.workspace.configure(bg=bg)

        self.source_card.configure(bg=frame_bg, highlightbackground=border, highlightcolor=border)
        self.source_title_lbl.configure(bg=frame_bg, fg=accent)
        self.row.configure(bg=frame_bg)
        self.row_label.configure(bg=frame_bg, fg=muted)

        self.action_bar.configure(bg=bar_bg, highlightbackground=border, highlightcolor=border)
        self.action_label.configure(bg=bar_bg, fg=muted)
        self.controls.configure(bg=bar_bg)

        self.output_card.configure(bg=frame_bg, highlightbackground=border, highlightcolor=border)
        self.output_title_lbl.configure(bg=frame_bg, fg=accent)
        self.main.configure(bg=frame_bg)
        self.text.configure(bg=text_bg, fg='#e8eaf0', insertbackground='#ffffff', selectbackground=shade_hex(accent, -10))

        self.footer.configure(bg=header_bg)
        self.footer_label.configure(bg=header_bg, fg=shade_hex(muted, -20))
        try:
            self.status_lbl.configure(background=header_bg)
        except tk.TclError:
            pass

    # ------------------------------------------------------- acciones --
    def open_src(self):
        p = filedialog.askopenfilename(
            title='Abrir GSC / GSCF',
            filetypes=[('GSC/UNK/GSCF', '*.gsc *.unk *.json *.gscf *.txt'), ('Todos', '*.*')],
        )
        if p:
            self.src.set(p)

    def do_forward(self):
        try:
            p = self.src.get().strip() or filedialog.askopenfilename(filetypes=[('UNK/GSC', '*.unk *.gsc')])
            if not p:
                return
            sugerido = str(Path(p).with_suffix('')) + '.GSCF.json'
            out_path = filedialog.asksaveasfilename(
                title='Guardar GSCF como...',
                defaultextension='.json',
                initialfile=Path(sugerido).name,
                initialdir=str(Path(p).parent),
                filetypes=[('GSCF (JSON)', '*.json'), ('Todos', '*.*')],
            )
            if not out_path:
                return
            out = Path(out_path)
            out.write_text(convert(p), encoding='utf-8')
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', f'✓ UNK → GSCF\n\n{out}\n\n{out.stat().st_size:,} bytes')
            self.status.set('Conversión completada.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def do_reverse(self):
        try:
            p = self.src.get().strip() or filedialog.askopenfilename(filetypes=[('GSCF', '*.json *.gscf *.txt'), ('Todos', '*.*')])
            if not p:
                return
            text = Path(p).read_text(encoding='utf-8-sig')
            c = GSCFCompiler(text)
            b = c.compile()
            sugerido = str(Path(p).with_suffix('')) + '.unk'
            out_path = filedialog.asksaveasfilename(
                title='Guardar UNK como...',
                defaultextension='.unk',
                initialfile=Path(sugerido).name,
                initialdir=str(Path(p).parent),
                filetypes=[('UNK', '*.unk'), ('Todos', '*.*')],
            )
            if not out_path:
                return
            out = Path(out_path)
            out.write_bytes(b)
            check = 'VALIDACIÓN: OK'
            try:
                rr = GSCReader(out)
                if rr.gsdt_pos is None:
                    check = 'VALIDACIÓN: GSDT no localizado'
            except Exception as ve:
                check = 'VALIDACIÓN: FALLÓ — ' + str(ve)
                c.warnings.append(str(ve))
            msg = f'✓ GSCF → UNK\n\n{out}\n\nTamaño: {len(b):,} bytes\nGSDT: {len(c.gsdt):,} valores\nEventos: {len(c.events)}\n{check}'
            if c.warnings:
                msg += '\n\nAvisos:\n' + '\n'.join(c.warnings)
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', msg)
            self.status.set('Compilación binaria completada y validada.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def compare_binary(self):
        try:
            original = filedialog.askopenfilename(title='UNK original', filetypes=[('UNK', '*.unk'), ('Todos', '*.*')])
            if not original:
                return
            gscf = filedialog.askopenfilename(title='GSCF correspondiente', filetypes=[('GSCF', '*.json *.gscf *.txt'), ('Todos', '*.*')])
            if not gscf:
                return
            b, w = compile_gscf_text(Path(gscf).read_text(encoding='utf-8-sig'))
            a = Path(original).read_bytes()
            n = min(len(a), len(b))
            first = next((i for i in range(n) if a[i] != b[i]), n)
            if first == n and len(a) == len(b):
                msg = f'✓ BYTE IDÉNTICO — 100%\n\n{len(a):,} bytes idénticos.'
                self.status.set('BINARIO 100% idéntico.')
            else:
                msg = f"✗ DIFERENTE\n\nOriginal: {len(a):,} bytes\nGenerado: {len(b):,} bytes\nPrimera diferencia: 0x{first:X}\nOriginal: {a[first:first + 32].hex(' ')}\nGenerado: {b[first:first + 32].hex(' ')}"
                self.status.set('Existen diferencias en el binario.')
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', msg)
            messagebox.showinfo('Comparación binaria', msg)
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def analyze_gscf(self):
        try:
            p = self.src.get().strip() or filedialog.askopenfilename(filetypes=[('GSCF', '*.json *.gscf *.txt'), ('Todos', '*.*')])
            if not p:
                return
            text = Path(p).read_text(encoding='utf-8-sig')
            c = GSCFCompiler(text)
            b = c.compile()
            self.text.delete('1.0', 'end')
            self.text.insert(
                '1.0',
                f'GSCF analizado\n\nEventos: {len(c.events)}\nValores GSDT: {len(c.gsdt)}\n'
                f'UNK compilable: {len(b):,} bytes\nAvisos: {len(c.warnings)}\n\n' + '\n'.join(c.warnings),
            )
            self.status.set('Análisis completado.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def clear(self):
        self.src.set('')
        self.text.delete('1.0', 'end')
        self.status.set('Listo.')

class BT3CombinedEditor:

  def __init__(self, root):
    self.root = root
    self.root.title("Sparking! Story Builder")
    self.root.geometry("1280x720")

    self.file_path = None
    self.file_content = ""

    # Guarda el $chr original (decimal) de cada actor (pla0-4 / cpu0-4) tal
    # como venía en el archivo modo historia al momento de cargarlo, para la
    # opción "Mantener personaje del juego original" de la pestaña DLC.
    self.original_actor_char = {}

    self.triggers_list = []
    self.events_list = []
    self.anims_list = []
    self.selected_trig_idx = None
    self.selected_ev_idx = None
    self.selected_anim_idx = None

    # --- estado del editor de posición/rotación ($Set_transform) ---
    self.pos_transforms = []
    self.pos_selected = None
    self.pos_clipboard = None
    self.pos_updating_fields = False

    # --- estado del tema visual (personalizable) ---
    self.theme_name = DEFAULT_THEME_NAME
    self.theme = dict(THEME_PRESETS[DEFAULT_THEME_NAME])

    self.setup_dark_theme()
    self.setup_background_image()

    self.menubar = tk.Menu(root)
    self.file_menu = tk.Menu(self.menubar, tearoff=0)
    self.file_menu.add_command(label="📁 Cargar Archivo", command=self.load_file)
    self.file_menu.add_command(label="💾 Guardar", command=self.save_file)
    self.file_menu.add_command(label="💾 Guardar como...", command=self.save_file_as)
    self.menubar.add_cascade(label="Archivo", menu=self.file_menu)

    self.appearance_menu = tk.Menu(self.menubar, tearoff=0)
    self.theme_preset_menu = tk.Menu(self.appearance_menu, tearoff=0)
    for preset_name in THEME_PRESETS:
      self.theme_preset_menu.add_command(
          label=preset_name,
          command=lambda n=preset_name: self.set_preset_theme(n),
      )
    self.appearance_menu.add_cascade(label="🎨 Temas predefinidos", menu=self.theme_preset_menu)
    self.appearance_menu.add_separator()
    self.appearance_menu.add_command(
        label="🖌 Color de acento personalizado...", command=self.choose_custom_accent
    )
    self.appearance_menu.add_command(
        label="🌑 Color de fondo personalizado...", command=self.choose_custom_background
    )
    self.appearance_menu.add_separator()
    self.appearance_menu.add_command(
        label="↺ Restablecer tema", command=self.reset_theme
    )
    self.menubar.add_cascade(label="Apariencia", menu=self.appearance_menu)

    self.help_menu = tk.Menu(self.menubar, tearoff=0)
    self.help_menu.add_command(label="ℹ️ Créditos", command=self.show_credits)
    self.menubar.add_cascade(label="Ayuda", menu=self.help_menu)

    root.config(menu=self.menubar)
    self.apply_theme_to_menus()

    # ---- barra superior: título de la app + acciones rápidas ----
    self.topbar = ttk.Frame(root, padding=(12, 8, 12, 4))
    self.topbar.pack(side="top", fill="x")

    self.app_title_label = ttk.Label(
        self.topbar, text="Sparking! Story Builder",
        font=("Segoe UI", 13, "bold"),
    )
    self.app_title_label.pack(side="left")

    self.lbl_file = ttk.Label(
        self.topbar, text="Sin archivo cargado",
        font=("Segoe UI", 9, "italic"), style="Muted.TLabel",
    )
    self.lbl_file.pack(side="left", padx=(16, 0))

    self.btn_credits = ttk.Button(
        self.topbar, text="ℹ️ Créditos", command=self.show_credits
    )
    self.btn_credits.pack(side="right")

    self.btn_theme = ttk.Button(
        self.topbar, text="🎨 Personalizar tema", command=self.open_theme_picker
    )
    self.btn_theme.pack(side="right", padx=(0, 6))

    # ---- barra inferior: copyright ----
    self.footer = ttk.Frame(root, padding=(12, 4, 12, 6))
    self.footer.pack(side="bottom", fill="x")

    self.lbl_copyright = ttk.Label(
        self.footer, text=APP_COPYRIGHT, style="Muted.TLabel", font=("Segoe UI", 8, "italic")
    )
    self.lbl_copyright.pack(side="right")

    self.main_notebook = ttk.Notebook(root)
    self.main_notebook.pack(fill="both", expand=True, padx=10, pady=5)

    self.zit_manager = ZitLinesManager("")
    self.zit_row_to_entry = {}

    self.tab_main_editor = ttk.Frame(self.main_notebook)
    self.tab_dlc_editor = ttk.Frame(self.main_notebook)
    self.tab_stats_editor = ttk.Frame(self.main_notebook)
    self.tab_events_editor = ttk.Frame(self.main_notebook)
    self.tab_anim_editor = ttk.Frame(self.main_notebook)
    self.tab_zit_editor = ttk.Frame(self.main_notebook)
    self.tab_position_editor = ttk.Frame(self.main_notebook)
    self.tab_gsc_converter = GSCConverterFrame(self.main_notebook, self.theme)

    self.main_notebook.add(
        self.tab_main_editor, text=" Personajes y Ajustes "
    )
    self.main_notebook.add(
        self.tab_dlc_editor, text=" DLC "
    )
    self.main_notebook.add(self.tab_stats_editor, text=" Salud e IA ")
    self.main_notebook.add(
        self.tab_events_editor, text=" Eventos y Condicionales "
    )
    self.main_notebook.add(
        self.tab_anim_editor, text=" Anim "
    )
    self.main_notebook.add(
        self.tab_zit_editor, text=" Z-Items "
    )
    self.main_notebook.add(
        self.tab_position_editor, text=" Posición/Rotación "
    )
    self.main_notebook.add(
        self.tab_gsc_converter, text=" Conversor GSC ↔ GSCF "
    )

    self.setup_story_editor_ui(self.tab_main_editor)
    self.setup_dlc_editor_ui(self.tab_dlc_editor)
    self.setup_stats_editor_ui(self.tab_stats_editor)
    self.setup_events_editor_ui(self.tab_events_editor)
    self.setup_anim_editor_ui(self.tab_anim_editor)
    self.setup_zit_editor_ui(self.tab_zit_editor)
    self.setup_position_editor_ui(self.tab_position_editor)

  def setup_dark_theme(self):
    self.apply_theme()

  def apply_theme(self):
    """(Re)aplica el tema actual (self.theme) a todos los estilos ttk
    y a los widgets tk "crudos" que no siguen ttk.Style automáticamente."""
    th = self.theme
    bg_color = th["bg"]
    frame_bg = th["frame_bg"]
    accent_color = th["accent"]
    fg_color = "#f3f3f3"
    muted_fg = shade_hex(bg_color, 120)
    field_bg = shade_hex(frame_bg, 12)
    hover = shade_hex(accent_color, 22)
    pressed = shade_hex(accent_color, -22)
    header_bg = shade_hex(frame_bg, -8)

    style = ttk.Style()
    style.theme_use("clam")

    self.root.configure(bg=bg_color)

    style.configure(".", background=bg_color, foreground=fg_color, font=("Segoe UI", 10))
    style.configure("TLabel", background=bg_color, foreground=fg_color)
    style.configure("Muted.TLabel", background=bg_color, foreground=muted_fg)
    style.configure(
        "TLabelframe", background=frame_bg, foreground=fg_color, borderwidth=1
    )
    style.configure(
        "TLabelframe.Label", background=frame_bg, foreground=accent_color,
        font=("Segoe UI", 10, "bold"),
    )
    style.configure("TFrame", background=bg_color)
    style.configure(
        "TButton", background=field_bg, foreground=fg_color, borderwidth=1,
        padding=6, focuscolor=accent_color,
    )
    style.map(
        "TButton",
        background=[("active", hover), ("pressed", pressed)],
        foreground=[("active", "#ffffff"), ("pressed", "#ffffff")],
    )
    style.configure(
        "TCheckbutton", background=bg_color, foreground=fg_color,
    )
    style.map(
        "TCheckbutton",
        background=[("active", bg_color)],
        indicatorbackground=[("selected", accent_color)],
    )
    style.configure(
        "TCombobox", fieldbackground=field_bg, background=field_bg, foreground=fg_color,
        arrowcolor=accent_color,
    )
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", field_bg)],
        selectbackground=[("readonly", accent_color)],
        selectforeground=[("readonly", "#ffffff")],
    )
    style.configure(
        "TEntry", fieldbackground=field_bg, foreground=fg_color, insertcolor=accent_color,
    )
    style.configure(
        "Horizontal.TScale", background=bg_color, troughcolor=field_bg,
    )
    style.configure(
        "TScrollbar", background=field_bg, troughcolor=bg_color, arrowcolor=accent_color,
    )
    style.configure("TNotebook", background=bg_color, borderwidth=0)
    style.configure(
        "TNotebook.Tab", background=header_bg, foreground=muted_fg,
        padding=[12, 6], font=("Segoe UI", 9, "bold"),
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", accent_color), ("active", hover)],
        foreground=[("selected", "#ffffff"), ("active", "#ffffff")],
    )
    style.configure(
        "Treeview",
        background=frame_bg,
        foreground=fg_color,
        fieldbackground=frame_bg,
        rowheight=25,
    )
    style.configure(
        "Treeview.Heading", background=header_bg, foreground=accent_color, borderwidth=1
    )
    style.map(
        "Treeview",
        background=[("selected", accent_color)],
        foreground=[("selected", "#ffffff")],
    )

    # widgets tk "crudos" que no se pintan solos con ttk.Style
    if hasattr(self, "pos_canvas"):
      self.pos_canvas.configure(bg=shade_hex(bg_color, -6))
    if hasattr(self, "pos_listbox"):
      self.pos_listbox.configure(
          bg=field_bg, fg=fg_color, selectbackground=accent_color,
          selectforeground="#ffffff", highlightthickness=0, relief="flat",
      )
    if hasattr(self, "canvas"):
      self.canvas.configure(bg=shade_hex(bg_color, -6))
    if hasattr(self, "tab_gsc_converter"):
      self.tab_gsc_converter.retheme(self.theme)

    self.apply_theme_to_menus()

  def apply_theme_to_menus(self):
    """Colorea los tk.Menu (Archivo/Apariencia/Ayuda), que no siguen ttk.Style."""
    th = self.theme
    menu_bg = shade_hex(th["frame_bg"], -6)
    menu_fg = "#f3f3f3"
    menu_active = th["accent"]
    for m in (
        getattr(self, "menubar", None),
        getattr(self, "file_menu", None),
        getattr(self, "appearance_menu", None),
        getattr(self, "theme_preset_menu", None),
        getattr(self, "help_menu", None),
    ):
      if m is None:
        continue
      try:
        m.configure(
            bg=menu_bg, fg=menu_fg,
            activebackground=menu_active, activeforeground="#ffffff",
        )
      except tk.TclError:
        pass

  # ------------------------------------------------------- personalización --
  def set_preset_theme(self, name):
    if name not in THEME_PRESETS:
      return
    self.theme_name = name
    self.theme = dict(THEME_PRESETS[name])
    self.apply_theme()

  def choose_custom_accent(self):
    _, hex_color = colorchooser.askcolor(
        color=self.theme["accent"], title="Elige el color de acento",
        parent=self.root,
    )
    if hex_color:
      self.theme["accent"] = hex_color
      self.theme_name = "Personalizado"
      self.apply_theme()

  def choose_custom_background(self):
    _, hex_color = colorchooser.askcolor(
        color=self.theme["bg"], title="Elige el color de fondo",
        parent=self.root,
    )
    if hex_color:
      self.theme["bg"] = hex_color
      self.theme["frame_bg"] = shade_hex(hex_color, 12)
      self.theme_name = "Personalizado"
      self.apply_theme()

  def reset_theme(self):
    self.set_preset_theme(DEFAULT_THEME_NAME)

  def open_theme_picker(self):
    win = tk.Toplevel(self.root)
    win.title("Personalizar tema")
    win.resizable(False, False)
    win.transient(self.root)
    win.configure(bg=self.theme["bg"])

    pad = ttk.Frame(win, padding=16)
    pad.pack(fill="both", expand=True)

    ttk.Label(
        pad, text="Elige un tema o personaliza tus propios colores",
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w", pady=(0, 10))

    presets_frame = ttk.Frame(pad)
    presets_frame.pack(fill="x")
    for name, colors in THEME_PRESETS.items():
      swatch = tk.Button(
          presets_frame, text=name, bg=colors["accent"], fg="#ffffff",
          activebackground=shade_hex(colors["accent"], 20), relief="flat",
          borderwidth=0, padx=10, pady=6,
          command=lambda n=name: (self.set_preset_theme(n), win.destroy()),
      )
      swatch.pack(fill="x", pady=3)

    ttk.Separator(pad, orient="horizontal").pack(fill="x", pady=10)

    ttk.Button(
        pad, text="🖌 Color de acento personalizado...",
        command=lambda: (self.choose_custom_accent(), win.destroy()),
    ).pack(fill="x", pady=3)
    ttk.Button(
        pad, text="🌑 Color de fondo personalizado...",
        command=lambda: (self.choose_custom_background(), win.destroy()),
    ).pack(fill="x", pady=3)
    ttk.Button(
        pad, text="↺ Restablecer tema por defecto",
        command=lambda: (self.reset_theme(), win.destroy()),
    ).pack(fill="x", pady=(10, 0))

    ttk.Button(pad, text="Cerrar", command=win.destroy).pack(fill="x", pady=(14, 0))

    win.update_idletasks()
    rx, ry = self.root.winfo_rootx(), self.root.winfo_rooty()
    rw, rh = self.root.winfo_width(), self.root.winfo_height()
    ww, wh = win.winfo_width(), win.winfo_height()
    win.geometry(f"+{rx + (rw - ww) // 2}+{ry + (rh - wh) // 2}")

  # ------------------------------------------------------------ créditos --
  def show_credits(self):
    win = tk.Toplevel(self.root)
    win.title("Créditos")
    win.resizable(False, False)
    win.transient(self.root)
    win.configure(bg=self.theme["bg"])
    win.grab_set()

    pad = ttk.Frame(win, padding=(24, 20, 24, 16))
    pad.pack(fill="both", expand=True)

    ttk.Label(pad, text="Créditos:", font=("Segoe UI", 12, "bold")).pack(anchor="w")

    names_frame = ttk.Frame(pad, padding=(4, 8, 4, 4))
    names_frame.pack(fill="x")
    for name in APP_CREDITS:
      ttk.Label(names_frame, text=name, font=("Segoe UI", 10)).pack(anchor="w", pady=1)

    ttk.Separator(pad, orient="horizontal").pack(fill="x", pady=(10, 8))
    ttk.Label(pad, text=APP_COPYRIGHT, style="Muted.TLabel", font=("Segoe UI", 8, "italic")).pack(anchor="e")

    ttk.Button(pad, text="Cerrar", command=win.destroy).pack(fill="x", pady=(14, 0))

    win.update_idletasks()
    rx, ry = self.root.winfo_rootx(), self.root.winfo_rooty()
    rw, rh = self.root.winfo_width(), self.root.winfo_height()
    ww, wh = win.winfo_width(), win.winfo_height()
    win.geometry(f"+{rx + (rw - ww) // 2}+{ry + (rh - wh) // 2}")

  def setup_background_image(self):
    image_name = "background.png"
    if os.path.exists(image_name):
      try:
        self.bg_image = tk.PhotoImage(file=image_name)
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()
      except Exception as e:
        print(f"No se pudo cargar la imagen PNG: {e}")

  def setup_story_editor_ui(self, parent):
    frame_settings = ttk.LabelFrame(parent, text=" Escenario y Música ")
    frame_settings.pack(fill="x", padx=10, pady=5)

    ttk.Label(frame_settings, text="Mapa ($map):").grid(
        row=0, column=0, sticky="w", padx=5, pady=5
    )
    self.cmb_map = ttk.Combobox(
        frame_settings, values=list(MAPS.values()), state="readonly", width=50
    )
    self.cmb_map.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_settings, text="Música ($bgm):").grid(
        row=1, column=0, sticky="w", padx=5, pady=5
    )
    self.cmb_bgm = ttk.Combobox(
        frame_settings, values=list(BGMS.values()), state="readonly", width=50
    )
    self.cmb_bgm.grid(row=1, column=1, padx=5, pady=5)

    self.notebook_teams = ttk.Notebook(parent)
    self.notebook_teams.pack(fill="both", expand=True, padx=10, pady=5)

    self.tab_players = ttk.Frame(self.notebook_teams)
    self.tab_cpus = ttk.Frame(self.notebook_teams)

    self.notebook_teams.add(self.tab_players, text=" Equipo Jugador ")
    self.notebook_teams.add(self.tab_cpus, text=" Equipo Rival CPU ")

    self.init_characters_tabs()

  def init_characters_tabs(self):
    self.cmb_players, self.cmb_player_costumes, self.chk_player_dmg = [], [], []
    self.cmb_cpus, self.cmb_cpu_costumes, self.chk_cpu_dmg = [], [], []

    for i in range(5):
      lbl_text = "Líder (pla0):" if i == 0 else f"Compañero {i} (pla{i}):"
      ttk.Label(self.tab_players, text=lbl_text).grid(
          row=i, column=0, sticky="w", padx=10, pady=8
      )
      vals = (
          list(CHARACTERS_STORY.values())
          if i == 0
          else [EMPTY_SLOT] + list(CHARACTERS_STORY.values())
      )
      cmb_char = ttk.Combobox(
          self.tab_players, values=vals, state="readonly", width=32
      )
      cmb_char.grid(row=i, column=1, padx=5, pady=8)
      cmb_char.set(vals[0])
      self.cmb_players.append(cmb_char)

      cmb_cost = ttk.Combobox(
          self.tab_players,
          values=list(COSTUMES.values()),
          state="readonly",
          width=12,
      )
      cmb_cost.grid(row=i, column=2, padx=5, pady=8)
      cmb_cost.set(COSTUMES["0"])
      self.cmb_player_costumes.append(cmb_cost)

      var_dmg = tk.IntVar(value=0)
      chk_dmg = ttk.Checkbutton(
          self.tab_players, text="Dañado ($dmg)", variable=var_dmg
      )
      chk_dmg.grid(row=i, column=3, padx=5, pady=8)
      self.chk_player_dmg.append(var_dmg)

    for i in range(5):
      lbl_text = "Líder CPU (cpu0):" if i == 0 else f"Compañero {i} (cpu{i}):"
      ttk.Label(self.tab_cpus, text=lbl_text).grid(
          row=i, column=0, sticky="w", padx=10, pady=8
      )
      vals = (
          list(CHARACTERS_STORY.values())
          if i == 0
          else [EMPTY_SLOT] + list(CHARACTERS_STORY.values())
      )
      cmb_char = ttk.Combobox(
          self.tab_cpus, values=vals, state="readonly", width=32
      )
      cmb_char.grid(row=i, column=1, padx=5, pady=8)
      cmb_char.set(vals[0])
      self.cmb_cpus.append(cmb_char)

      cmb_cost = ttk.Combobox(
          self.tab_cpus,
          values=list(COSTUMES.values()),
          state="readonly",
          width=12,
      )
      cmb_cost.grid(row=i, column=2, padx=5, pady=8)
      cmb_cost.set(COSTUMES["0"])
      self.cmb_cpu_costumes.append(cmb_cost)

      var_dmg = tk.IntVar(value=0)
      chk_dmg = ttk.Checkbutton(
          self.tab_cpus, text="Dañado ($dmg)", variable=var_dmg
      )
      chk_dmg.grid(row=i, column=3, padx=5, pady=8)
      self.chk_cpu_dmg.append(var_dmg)

  def setup_dlc_editor_ui(self, parent):
    info = ttk.Label(
        parent,
        text=(
            "Selecciona un personaje DLC (165-252 / A5-FC) para reemplazar a un "
            "jugador (pla) o a un rival CPU (cpu) que ya esté activo (con un "
            "personaje asignado) en la pestaña \"Personajes y Ajustes\".\n"
            "Requiere una ISO modificada con capacidad de DLC. La selección se "
            "aplica al guardar (Archivo > Guardar), o de inmediato con el botón "
            "de abajo. Deja los slots que no quieras cambiar en \""
            + DLC_EMPTY_SLOT
            + "\"."
        ),
        style="Muted.TLabel",
        justify="left",
        wraplength=760,
    )
    info.pack(fill="x", padx=10, pady=(10, 5))

    notebook_dlc = ttk.Notebook(parent)
    notebook_dlc.pack(fill="both", expand=True, padx=10, pady=5)

    tab_dlc_players = ttk.Frame(notebook_dlc)
    tab_dlc_cpus = ttk.Frame(notebook_dlc)
    notebook_dlc.add(tab_dlc_players, text=" Equipo Jugador (DLC) ")
    notebook_dlc.add(tab_dlc_cpus, text=" Equipo Rival CPU (DLC) ")

    dlc_vals = [DLC_EMPTY_SLOT, DLC_KEEP_ORIGINAL] + list(
        DLC_CHARACTERS_STORY.values()
    )

    self.cmb_dlc_players = []
    for i in range(5):
      lbl_text = "Líder (pla0):" if i == 0 else f"Compañero {i} (pla{i}):"
      ttk.Label(tab_dlc_players, text=lbl_text).grid(
          row=i, column=0, sticky="w", padx=10, pady=8
      )
      cmb_char = ttk.Combobox(
          tab_dlc_players, values=dlc_vals, state="readonly", width=32
      )
      cmb_char.grid(row=i, column=1, padx=5, pady=8)
      cmb_char.set(DLC_EMPTY_SLOT)
      self.cmb_dlc_players.append(cmb_char)

    self.cmb_dlc_cpus = []
    for i in range(5):
      lbl_text = "Líder CPU (cpu0):" if i == 0 else f"Compañero {i} (cpu{i}):"
      ttk.Label(tab_dlc_cpus, text=lbl_text).grid(
          row=i, column=0, sticky="w", padx=10, pady=8
      )
      cmb_char = ttk.Combobox(
          tab_dlc_cpus, values=dlc_vals, state="readonly", width=32
      )
      cmb_char.grid(row=i, column=1, padx=5, pady=8)
      cmb_char.set(DLC_EMPTY_SLOT)
      self.cmb_dlc_cpus.append(cmb_char)

    ttk.Button(
        parent,
        text="🔄 Aplicar Cambios de Personaje DLC",
        command=self.apply_dlc_selection,
    ).pack(pady=10)

  def apply_dlc_character_to_slot(self, slot_name, new_chr_hex):
    """Reemplaza el $chr de un $Actor existente (pla/cpu) por un valor DLC."""
    pattern = re.compile(
        r"(\$Actor:\s*\{[^}]*\$name:\s*\$?"
        + re.escape(slot_name)
        + r"\b[^}]*?\$chr:\s*&)[0-9A-Fa-f]+",
        re.IGNORECASE,
    )
    if not pattern.search(self.file_content):
      return False
    self.file_content = pattern.sub(
        lambda m: m.group(1) + new_chr_hex, self.file_content, count=1
    )
    return True

  def apply_dlc_selection(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return

    slots = [(f"pla{i}", self.cmb_dlc_players[i]) for i in range(5)] + [
        (f"cpu{i}", self.cmb_dlc_cpus[i]) for i in range(5)
    ]

    changes = 0
    for slot_name, combo in slots:
      val = combo.get()
      if not val or val == DLC_EMPTY_SLOT:
        continue
      if val == DLC_KEEP_ORIGINAL:
        orig_dec = self.original_actor_char.get(slot_name)
        if orig_dec is None:
          continue
        char_hex = f"{int(orig_dec):04X}"
      else:
        matches = [k for k, v in DLC_CHARACTERS_STORY.items() if v == val]
        if not matches:
          continue
        char_hex = f"{int(matches[0]):04X}"
      if self.apply_dlc_character_to_slot(slot_name, char_hex):
        changes += 1

    if changes:
      self.parse_events_file()
      self.parse_animations_file()
      self.refresh_tables()
      messagebox.showinfo(
          "Éxito",
          f"Se aplicaron {changes} cambio(s) de personaje DLC correctamente.",
      )
    else:
      messagebox.showwarning(
          "Atención",
          "No se aplicó ningún cambio. Verifica que hayas seleccionado al menos "
          "un personaje DLC y que el actor (pla/cpu) ya exista en el archivo "
          "cargado.",
      )

  def setup_stats_editor_ui(self, parent):
    frame_info = ttk.LabelFrame(
        parent, text=" Configuración de Salud e Inteligencia Artificial "
    )
    frame_info.pack(fill="both", expand=True, padx=10, pady=10)

    notebook_stats = ttk.Notebook(frame_info)
    notebook_stats.pack(fill="both", expand=True, padx=5, pady=5)

    tab_p_stats = ttk.Frame(notebook_stats)
    tab_c_stats = ttk.Frame(notebook_stats)

    notebook_stats.add(tab_p_stats, text=" Jugadores  ")
    notebook_stats.add(tab_c_stats, text=" CPU  ")

    self.ent_player_hp, self.ent_player_ia = [], []
    self.ent_cpu_hp, self.ent_cpu_ia = [], []

    for i in range(5):
      lbl = "Líder (pla0):" if i == 0 else f"Compañero {i} (pla{i}):"
      ttk.Label(tab_p_stats, text=lbl).grid(
          row=i, column=0, sticky="w", padx=10, pady=10
      )
      ttk.Label(tab_p_stats, text="Salud ($hp):").grid(
          row=i, column=1, padx=5, pady=10
      )
      ent_hp = ttk.Entry(tab_p_stats, width=12)
      ent_hp.insert(0, "30000")
      ent_hp.grid(row=i, column=2, padx=5, pady=10)
      self.ent_player_hp.append(ent_hp)

      ttk.Label(tab_p_stats, text="Nivel IA ($ia):").grid(
          row=i, column=3, padx=5, pady=10
      )
      ent_ia = ttk.Entry(tab_p_stats, width=12)
      ent_ia.insert(0, "0")
      ent_ia.grid(row=i, column=4, padx=5, pady=10)
      self.ent_player_ia.append(ent_ia)

    for i in range(5):
      lbl = "Líder CPU (cpu0):" if i == 0 else f"Compañero {i} (cpu{i}):"
      ttk.Label(tab_c_stats, text=lbl).grid(
          row=i, column=0, sticky="w", padx=10, pady=10
      )
      ttk.Label(tab_c_stats, text="Salud ($hp):").grid(
          row=i, column=1, padx=5, pady=10
      )
      ent_hp = ttk.Entry(tab_c_stats, width=12)
      ent_hp.insert(0, "30000")
      ent_hp.grid(row=i, column=2, padx=5, pady=10)
      self.ent_cpu_hp.append(ent_hp)

      ttk.Label(tab_c_stats, text="Nivel IA ($ia):").grid(
          row=i, column=3, padx=5, pady=10
      )
      ent_ia = ttk.Entry(tab_c_stats, width=12)
      ent_ia.insert(0, "9")
      ent_ia.grid(row=i, column=4, padx=5, pady=10)
      self.ent_cpu_ia.append(ent_ia)

  def setup_events_editor_ui(self, parent):
    self.notebook_events = ttk.Notebook(parent)
    self.notebook_events.pack(fill="both", expand=True, padx=5, pady=5)

    self.tab_triggers = ttk.Frame(self.notebook_events)
    self.tab_events = ttk.Frame(self.notebook_events)

    self.notebook_events.add(
        self.tab_triggers, text=" Desencadenadores  "
    )
    self.notebook_events.add(self.tab_events, text=" Lista de Eventos  ")

    self.setup_triggers_tab()
    self.setup_events_tab()

  def setup_triggers_tab(self):
    frame_top = ttk.LabelFrame(
        self.tab_triggers, text=" Modificar Desencadenador Seleccionado "
    )
    frame_top.pack(fill="x", padx=5, pady=5)

    ttk.Label(frame_top, text="Evento Padre:").grid(
        row=0, column=0, padx=5, pady=5
    )
    self.ent_trig_id = ttk.Entry(frame_top, width=15, state="readonly")
    self.ent_trig_id.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_top, text="Nueva Condición ($if):").grid(
        row=0, column=2, padx=5, pady=5
    )
    self.cmb_trig_cond = ttk.Combobox(
        frame_top, values=list(HEX_CONDITIONS.keys()), width=35
    )
    self.cmb_trig_cond.current(0)
    self.cmb_trig_cond.grid(row=0, column=3, padx=5, pady=5)

    ttk.Label(frame_top, text="Nuevo Ir a ($to):").grid(
        row=1, column=0, padx=5, pady=5
    )
    self.ent_trig_target = ttk.Entry(frame_top, width=15)
    self.ent_trig_target.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(
        frame_top,
        text="🔄 Aplicar Cambio a Desencadenador",
        command=self.replace_trigger,
    ).grid(row=1, column=2, columnspan=2, pady=5)

    ttk.Label(frame_top, text="Renombrar $to:$EV_ a:").grid(
        row=2, column=0, padx=5, pady=5
    )
    self.ent_trig_rename_to = ttk.Entry(frame_top, width=15)
    self.ent_trig_rename_to.grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(
        frame_top,
        text="🔁 Renombrar $to en Todos los Desencadenadores",
        command=self.rename_trigger_target,
    ).grid(row=2, column=2, columnspan=2, pady=5)

    self.tree_triggers = ttk.Treeview(
        self.tab_triggers,
        columns=("ID", "Condicion_Hex", "Descripcion", "Destino"),
        show="headings",
    )
    self.tree_triggers.heading("ID", text="Evento Padre")
    self.tree_triggers.heading("Condicion_Hex", text="Hex ($if)")
    self.tree_triggers.heading("Descripcion", text="Desencadenador / Condición")
    self.tree_triggers.heading("Destino", text="Siguiente Evento ($to)")

    self.tree_triggers.column("ID", width=120)
    self.tree_triggers.column("Condicion_Hex", width=100)
    self.tree_triggers.column("Descripcion", width=360)
    self.tree_triggers.column("Destino", width=140)

    self.tree_triggers.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_triggers.bind("<<TreeviewSelect>>", self.on_trig_select)

  def setup_events_tab(self):
    frame_top = ttk.LabelFrame(
        self.tab_events, text=" Modificar Evento Seleccionado "
    )
    frame_top.pack(fill="x", padx=5, pady=5)

    ttk.Label(frame_top, text="Evento Padre:").grid(
        row=0, column=0, padx=2, pady=5
    )
    self.ent_ev_id = ttk.Entry(frame_top, width=12, state="readonly")
    self.ent_ev_id.grid(row=0, column=1, padx=2, pady=5)

    ttk.Label(frame_top, text="Evento ($evt):").grid(
        row=0, column=2, padx=2, pady=5
    )
    self.cmb_ev_select = ttk.Combobox(
        frame_top, values=list(HEX_EVENTS.keys()), width=42
    )
    self.cmb_ev_select.current(0)
    self.cmb_ev_select.grid(row=0, column=3, padx=2, pady=5)
    self.cmb_ev_select.bind("<<ComboboxSelected>>", self.on_evt_combo_change)

    ttk.Label(frame_top, text="Personaje ($flag):").grid(
        row=0, column=4, padx=2, pady=5
    )
    self.cmb_char_select = ttk.Combobox(
        frame_top, values=CHAR_LIST_LABELS, width=32, state="disabled"
    )
    self.cmb_char_select.current(0)
    self.cmb_char_select.grid(row=0, column=5, padx=2, pady=5)

    # --- Lista aparte de personajes DLC ---
    # Aplica a los eventos de Transformación, Destransformación, Fusión y
    # Cambio de equipo (mismos eventos cubiertos por is_char_event()).
    self.var_use_dlc_char = tk.BooleanVar(value=False)
    self.chk_use_dlc_char = ttk.Checkbutton(
        frame_top,
        text="Usar personaje DLC",
        variable=self.var_use_dlc_char,
        state="disabled",
        command=self.on_toggle_dlc_char,
    )
    self.chk_use_dlc_char.grid(row=1, column=4, padx=2, pady=5, sticky="w")

    self.cmb_char_select_dlc = ttk.Combobox(
        frame_top, values=DLC_CHAR_LIST_LABELS, width=32, state="disabled"
    )
    self.cmb_char_select_dlc.current(0)
    self.cmb_char_select_dlc.grid(row=1, column=5, padx=2, pady=5)

    # --- Selector de mapa (solo para "Destrucción del mapa") ---
    ttk.Label(frame_top, text="Mapa ($flag):").grid(
        row=1, column=2, padx=2, pady=5, sticky="e"
    )
    self.cmb_map_select = ttk.Combobox(
        frame_top, values=MAP_LIST_LABELS, width=42, state="disabled"
    )
    self.cmb_map_select.current(0)
    self.cmb_map_select.grid(row=1, column=3, padx=2, pady=5)

    ttk.Button(
        frame_top,
        text="🔄 Aplicar Cambio a Evento",
        command=self.replace_event,
    ).grid(row=2, column=0, columnspan=6, pady=5)

    self.tree_events = ttk.Treeview(
        self.tab_events,
        columns=("Padre", "Hex_Actual", "Descripcion", "Flag_Hex", "Personaje"),
        show="headings",
    )
    self.tree_events.heading("Padre", text="Evento Padre")
    self.tree_events.heading("Hex_Actual", text="Hex ($evt)")
    self.tree_events.heading("Descripcion", text="Evento Ejecutado")
    self.tree_events.heading("Flag_Hex", text="Hex ($flag)")
    self.tree_events.heading("Personaje", text="Personaje Seleccionado")

    self.tree_events.column("Padre", width=110)
    self.tree_events.column("Hex_Actual", width=80)
    self.tree_events.column("Descripcion", width=340)
    self.tree_events.column("Flag_Hex", width=100)
    self.tree_events.column("Personaje", width=220)

    self.tree_events.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_events.bind("<<TreeviewSelect>>", self.on_ev_select)

  def setup_ev_manage_tab(self):
    self.new_ev_audio_entries = []
    self.new_ev_trigger_entries = []

    # --- Contenedor con scroll: el formulario de inserción tiene varias
    # secciones y puede no caber completo en la altura visible de la
    # pestaña, así que envolvemos todo en un Canvas desplazable para que
    # el botón "Insertar" siempre quede alcanzable.
    outer_canvas = tk.Canvas(self.tab_ev_manage, highlightthickness=0)
    outer_scroll = ttk.Scrollbar(
        self.tab_ev_manage, orient="vertical", command=outer_canvas.yview
    )
    outer_canvas.configure(yscrollcommand=outer_scroll.set)
    outer_canvas.pack(side="left", fill="both", expand=True)
    outer_scroll.pack(side="right", fill="y")

    content = ttk.Frame(outer_canvas)
    content_id = outer_canvas.create_window((0, 0), window=content, anchor="nw")

    def _on_content_configure(event=None):
      outer_canvas.configure(scrollregion=outer_canvas.bbox("all"))

    content.bind("<Configure>", _on_content_configure)

    def _on_canvas_configure(event):
      outer_canvas.itemconfig(content_id, width=event.width)

    outer_canvas.bind("<Configure>", _on_canvas_configure)

    def _on_mousewheel(event):
      outer_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_wheel(event=None):
      outer_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def _unbind_wheel(event=None):
      outer_canvas.unbind_all("<MouseWheel>")

    outer_canvas.bind("<Enter>", _bind_wheel)
    outer_canvas.bind("<Leave>", _unbind_wheel)

    frame_list = ttk.LabelFrame(
        content, text=" Eventos Existentes ($EV_XX) "
    )
    frame_list.pack(fill="x", padx=5, pady=5)

    self.tree_ev_blocks = ttk.Treeview(
        frame_list,
        columns=("ID", "Tipo", "Triggers", "Eventos"),
        show="headings",
        height=6,
    )
    self.tree_ev_blocks.heading("ID", text="Evento ($EV_XX)")
    self.tree_ev_blocks.heading("Tipo", text="Tipo")
    self.tree_ev_blocks.heading("Triggers", text="Nº Desencadenadores")
    self.tree_ev_blocks.heading("Eventos", text="Nº Eventos ($Event)")
    self.tree_ev_blocks.column("ID", width=140)
    self.tree_ev_blocks.column("Tipo", width=200)
    self.tree_ev_blocks.column("Triggers", width=160)
    self.tree_ev_blocks.column("Eventos", width=160)
    self.tree_ev_blocks.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_ev_blocks.bind(
        "<<TreeviewSelect>>", self.on_ev_block_select
    )

    ttk.Button(
        frame_list,
        text="🗑️ Eliminar Evento Seleccionado",
        command=self.delete_ev_block,
    ).pack(pady=5)

    frame_new = ttk.LabelFrame(
        content, text=" Insertar Nuevo Evento ($EV_XX) "
    )
    frame_new.pack(fill="x", padx=5, pady=5)

    self.lbl_insert_after_target = ttk.Label(
        frame_new,
        text=(
            "Se insertará al final de la lista. Selecciona un evento en la "
            "tabla de arriba para insertar justo después de él."
        ),
        style="Muted.TLabel",
        wraplength=760,
        justify="left",
    )
    self.lbl_insert_after_target.grid(
        row=0, column=0, columnspan=4, padx=5, pady=(5, 8), sticky="w"
    )

    ttk.Label(frame_new, text="Número/ID de nuevo EV (ej: 42):").grid(
        row=1, column=0, padx=5, pady=5, sticky="w"
    )
    self.ent_new_ev_id = ttk.Entry(frame_new, width=10)
    self.ent_new_ev_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(frame_new, text="Plantilla:").grid(
        row=1, column=2, padx=5, pady=5, sticky="w"
    )
    self.cmb_new_ev_type = ttk.Combobox(
        frame_new,
        values=[
            "Simple (sin cámara ni animaciones)",
            "Completo (con cámara y animaciones)",
        ],
        state="readonly",
        width=36,
    )
    self.cmb_new_ev_type.current(0)
    self.cmb_new_ev_type.grid(row=1, column=3, padx=5, pady=5, sticky="w")
    self.cmb_new_ev_type.bind(
        "<<ComboboxSelected>>", self.on_new_ev_type_change
    )

    ttk.Label(frame_new, text="Evento ($evt) a ejecutar:").grid(
        row=2, column=0, padx=5, pady=5, sticky="w"
    )
    self.cmb_new_ev_evt = ttk.Combobox(
        frame_new, values=list(HEX_EVENTS.keys()), width=36
    )
    self.cmb_new_ev_evt.current(0)
    self.cmb_new_ev_evt.grid(
        row=2, column=1, columnspan=3, padx=5, pady=5, sticky="w"
    )

    # --- Desencadenadores iniciales ($if -> $to), hasta 3 ---
    ttk.Label(
        frame_new,
        text="Desencadenadores iniciales ($if -> $to), máximo 3:",
    ).grid(row=3, column=0, columnspan=4, padx=5, pady=(10, 2), sticky="w")

    self.frame_new_ev_trigger_list = ttk.Frame(frame_new)
    self.frame_new_ev_trigger_list.grid(
        row=4, column=0, columnspan=4, padx=5, pady=2, sticky="we"
    )

    ttk.Label(self.frame_new_ev_trigger_list, text="$if (hex):").grid(
        row=0, column=0, padx=2
    )
    self.ent_trig_new_if = ttk.Entry(
        self.frame_new_ev_trigger_list, width=10
    )
    self.ent_trig_new_if.insert(0, "0048")
    self.ent_trig_new_if.grid(row=0, column=1, padx=2)

    ttk.Label(self.frame_new_ev_trigger_list, text="Ir a ($to) - Nº EV:").grid(
        row=0, column=2, padx=2
    )
    self.ent_trig_new_to = ttk.Entry(
        self.frame_new_ev_trigger_list, width=10
    )
    self.ent_trig_new_to.grid(row=0, column=3, padx=2)

    self.btn_add_new_ev_trigger = ttk.Button(
        self.frame_new_ev_trigger_list,
        text="➕ Agregar condición",
        command=self.add_new_ev_trigger_entry,
    )
    self.btn_add_new_ev_trigger.grid(row=0, column=4, padx=5)
    ttk.Button(
        self.frame_new_ev_trigger_list,
        text="➖ Quitar seleccionada",
        command=self.remove_new_ev_trigger_entry,
    ).grid(row=0, column=5, padx=5)

    self.list_new_ev_triggers = tk.Listbox(
        self.frame_new_ev_trigger_list, height=3, width=50
    )
    self.list_new_ev_triggers.grid(
        row=1, column=0, columnspan=6, padx=2, pady=4, sticky="we"
    )

    self.var_new_ev_audio = tk.BooleanVar(value=False)
    self.chk_new_ev_audio = ttk.Checkbutton(
        frame_new,
        text="Agregar audios en $Link ($audio:K[...]) — solo plantilla Simple",
        variable=self.var_new_ev_audio,
        command=self.on_toggle_new_ev_audio,
    )
    self.chk_new_ev_audio.grid(
        row=5, column=0, columnspan=4, padx=5, pady=(10, 2), sticky="w"
    )

    self.frame_new_ev_audio_list = ttk.Frame(frame_new)
    self.frame_new_ev_audio_list.grid(
        row=6, column=0, columnspan=4, padx=5, pady=2, sticky="we"
    )

    ttk.Label(self.frame_new_ev_audio_list, text="$if (hex):").grid(
        row=0, column=0, padx=2
    )
    self.ent_audio_if = ttk.Entry(self.frame_new_ev_audio_list, width=10)
    self.ent_audio_if.insert(0, "FFFF")
    self.ent_audio_if.grid(row=0, column=1, padx=2)

    ttk.Label(self.frame_new_ev_audio_list, text="$adx (hex):").grid(
        row=0, column=2, padx=2
    )
    self.ent_audio_adx = ttk.Entry(self.frame_new_ev_audio_list, width=10)
    self.ent_audio_adx.grid(row=0, column=3, padx=2)

    ttk.Button(
        self.frame_new_ev_audio_list,
        text="➕ Agregar audio",
        command=self.add_new_ev_audio_entry,
    ).grid(row=0, column=4, padx=5)
    ttk.Button(
        self.frame_new_ev_audio_list,
        text="➖ Quitar seleccionado",
        command=self.remove_new_ev_audio_entry,
    ).grid(row=0, column=5, padx=5)

    self.list_new_ev_audio = tk.Listbox(
        self.frame_new_ev_audio_list, height=4, width=50
    )
    self.list_new_ev_audio.grid(
        row=1, column=0, columnspan=6, padx=2, pady=4, sticky="we"
    )

    ttk.Button(
        frame_new,
        text="➕ Insertar Nuevo Evento ($EV_XX)",
        command=self.insert_ev_block,
    ).grid(row=7, column=0, columnspan=4, pady=10)

    self.on_new_ev_type_change()
    self.on_toggle_new_ev_audio()

  def on_ev_block_select(self, event=None):
    sel = self.tree_ev_blocks.selection()
    if not sel:
      self.lbl_insert_after_target.config(
          text=(
              "Se insertará al final de la lista. Selecciona un evento en "
              "la tabla de arriba para insertar justo después de él."
          )
      )
      return
    ev_label = self.tree_ev_blocks.item(sel[0], "values")[0]
    self.lbl_insert_after_target.config(
        text=f"El nuevo evento se insertará justo después de {ev_label}."
    )

  def add_new_ev_trigger_entry(self):
    if len(self.new_ev_trigger_entries) >= 3:
      messagebox.showwarning(
          "Atención",
          "Solo se permiten hasta 3 desencadenadores iniciales por evento.",
      )
      return
    if_hex = self.ent_trig_new_if.get().strip().upper().lstrip("&")
    to_raw = self.ent_trig_new_to.get().strip()
    if not if_hex:
      messagebox.showwarning("Atención", "Ingresa el valor hex de $if.")
      return
    if not to_raw:
      messagebox.showwarning(
          "Atención", "Ingresa a qué evento ($to) apunta esta condición."
      )
      return
    to_id = to_raw.zfill(2) if to_raw.isdigit() else to_raw.upper()
    self.new_ev_trigger_entries.append((if_hex, to_id))
    self.list_new_ev_triggers.insert(
        tk.END, f"$if:&{if_hex}   $to:$EV_{to_id}"
    )
    if len(self.new_ev_trigger_entries) >= 3:
      self.btn_add_new_ev_trigger.config(state="disabled")

  def remove_new_ev_trigger_entry(self):
    sel = self.list_new_ev_triggers.curselection()
    if not sel:
      return
    idx = sel[0]
    self.list_new_ev_triggers.delete(idx)
    del self.new_ev_trigger_entries[idx]
    self.btn_add_new_ev_trigger.config(state="normal")

  def on_new_ev_type_change(self, event=None):
    is_simple = self.cmb_new_ev_type.get().startswith("Simple")
    self.chk_new_ev_audio.config(
        state="normal" if is_simple else "disabled"
    )
    if not is_simple and self.var_new_ev_audio.get():
      self.var_new_ev_audio.set(False)
    self.on_toggle_new_ev_audio()

  def on_toggle_new_ev_audio(self):
    is_simple = self.cmb_new_ev_type.get().startswith("Simple")
    state = "normal" if (is_simple and self.var_new_ev_audio.get()) else "disabled"
    for child in self.frame_new_ev_audio_list.winfo_children():
      try:
        child.config(state=state)
      except tk.TclError:
        pass

  def add_new_ev_audio_entry(self):
    if_hex = self.ent_audio_if.get().strip().upper().lstrip("&") or "FFFF"
    adx_hex = self.ent_audio_adx.get().strip().upper().lstrip("&")
    if not adx_hex:
      messagebox.showwarning("Atención", "Ingresa el valor hex de $adx.")
      return
    self.new_ev_audio_entries.append((if_hex, adx_hex))
    self.list_new_ev_audio.insert(
        tk.END, f"$if:&{if_hex}   $adx:&{adx_hex}"
    )
    self.ent_audio_adx.delete(0, tk.END)

  def remove_new_ev_audio_entry(self):
    sel = self.list_new_ev_audio.curselection()
    if not sel:
      return
    idx = sel[0]
    self.list_new_ev_audio.delete(idx)
    del self.new_ev_audio_entries[idx]

  def get_ev_blocks(self):
    blocks = []
    for m in EV_BLOCK_PATTERN.finditer(self.file_content):
      full = m.group("full")
      blocks.append({
          "id": m.group("id"),
          "full": full,
          "start": m.start(),
          "end": m.end(),
          "has_camera": bool(
              re.search(
                  r"\$Camera_Start|\$CS_Camera|\$Load_Anim",
                  full,
                  re.IGNORECASE,
              )
          ),
          "n_triggers": len(re.findall(r"\$if\s*:\s*&", full, re.IGNORECASE)),
          "n_events": len(
              re.findall(r"\$Event\s*:\s*\{", full, re.IGNORECASE)
          ),
      })
    return blocks

  def refresh_ev_manage_table(self):
    if not hasattr(self, "tree_ev_blocks"):
      return
    for row in self.tree_ev_blocks.get_children():
      self.tree_ev_blocks.delete(row)
    for b in self.get_ev_blocks():
      tipo = "Con cinemática" if b["has_camera"] else "Simple"
      self.tree_ev_blocks.insert(
          "",
          "end",
          values=(f"$EV_{b['id']}", tipo, b["n_triggers"], b["n_events"]),
      )

  def delete_ev_block(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return

    sel = self.tree_ev_blocks.selection()
    if not sel:
      messagebox.showwarning(
          "Atención", "Selecciona un evento de la lista para eliminar."
      )
      return

    ev_label = self.tree_ev_blocks.item(sel[0], "values")[0]
    ev_id = str(ev_label).replace("$EV_", "")

    if not messagebox.askyesno(
        "Confirmar eliminación",
        f"¿Seguro que deseas eliminar por completo el evento {ev_label}?\n\n"
        "Esto borrará toda su cinemática, desencadenadores y eventos "
        "asociados a él. Verifica antes que ningún otro evento apunte a "
        "él mediante $to.",
    ):
      return

    target = next(
        (b for b in self.get_ev_blocks() if b["id"] == ev_id), None
    )
    if not target:
      messagebox.showerror(
          "Error", f"No se encontró el evento {ev_label} en el archivo."
      )
      return

    start, end = target["start"], target["end"]

    # Consumir la sangría (espacios/tabs) que precede a "$EV_XX" en su
    # propia línea, para que no quede una indentación huérfana que se
    # sume a la del siguiente bloque.
    while start > 0 and self.file_content[start - 1] in (" ", "\t"):
      start -= 1

    after = self.file_content[end:end + 2]
    if after.startswith("\r\n"):
      end += 2
    elif after[:1] in ("\n", "\r"):
      end += 1

    self.file_content = self.file_content[:start] + self.file_content[end:]

    self.parse_events_file()
    self.parse_animations_file()
    self.parse_position_transforms()
    self.refresh_tables()
    self.refresh_zit_table()
    messagebox.showinfo("Éxito", f"Se eliminó el evento {ev_label} correctamente.")

  def insert_ev_block(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return

    raw_id = self.ent_new_ev_id.get().strip()
    if not raw_id:
      messagebox.showwarning(
          "Atención", "Ingresa un número/ID para el nuevo evento."
      )
      return
    new_id = raw_id.zfill(2) if raw_id.isdigit() else raw_id.upper()

    blocks = self.get_ev_blocks()
    if any(b["id"].upper() == new_id.upper() for b in blocks):
      messagebox.showerror(
          "Error", f"Ya existe un evento $EV_{new_id} en el archivo."
      )
      return

    if not self.new_ev_trigger_entries:
      messagebox.showwarning(
          "Atención",
          "Agrega al menos un desencadenador inicial ($if -> $to) antes de "
          "insertar el evento.",
      )
      return

    evt_label = self.cmb_new_ev_evt.get()
    evt_hex = HEX_EVENTS.get(evt_label, "0000")
    flag_hex = "FFFFFFFF"

    # --- Determinar dónde insertar: justo después del evento seleccionado
    # en la tabla, o al final de la lista si no hay ninguno seleccionado.
    ref_block = None
    sel = self.tree_ev_blocks.selection()
    if sel:
      ref_label = self.tree_ev_blocks.item(sel[0], "values")[0]
      ref_id = str(ref_label).replace("$EV_", "")
      ref_block = next((b for b in blocks if b["id"] == ref_id), None)

    if ref_block is None and blocks:
      ref_block = blocks[-1]

    indent = ""
    if ref_block:
      indent_match = re.search(
          r"([ \t]*)\$EV_" + re.escape(ref_block["id"]) + r"\s*:\s*<",
          self.file_content,
      )
      if indent_match:
        indent = indent_match.group(1)

    is_simple = self.cmb_new_ev_type.get().startswith("Simple")

    trigger_lines = "\n".join(
        f"{indent}            {{$if:&{ih}, $to:$EV_{tid}}}"
        for ih, tid in self.new_ev_trigger_entries
    )
    trigger_block = f"K[\n{trigger_lines}\n{indent}        ],"

    if is_simple and self.var_new_ev_audio.get() and self.new_ev_audio_entries:
      audio_lines = "\n".join(
          f"{indent}            {{$if:&{ih}, $adx:&{ah}}}"
          for ih, ah in self.new_ev_audio_entries
      )
      audio_part = f"K[\n{audio_lines}\n{indent}        ],"
    else:
      audio_part = "null,"

    if is_simple:
      new_block = (
          f"{indent}$EV_{new_id}:<\n"
          f"{indent}    $Unk3\n"
          f"{indent}    $End_event:-1\n"
          f"{indent}    $Reset_transform\n"
          f"{indent}    $End_effects\n"
          f"{indent}    $Link:{{\n"
          f"{indent}        $event:{trigger_block}\n"
          f"{indent}        $audio:{audio_part}\n"
          f"{indent}    }}\n"
          f"{indent}    $Set_plafield:null\n"
          f"{indent}    $Set_cpufield:null\n"
          f"{indent}    $Event:{{$evt: &{evt_hex} $flag: &{flag_hex}}}\n"
          f"{indent}    $End_cutscn\n"
          f"{indent}>"
      )
    else:
      new_block = (
          f"{indent}$EV_{new_id}:<\n"
          f"{indent}    $Unk3\n"
          f"{indent}    $End_event:-1\n"
          f"{indent}    $Reset_transform\n"
          f"{indent}    $Set_transform:{{$actor:$pla0 $loc:F[    0.000000,    0.000000,    0.000000] $rot:F[    0.000000,    0.000000,    0.000000]}}\n"
          f"{indent}    $Set_transform:{{$actor:$cpu0 $loc:F[    0.000000,    0.000000,    0.000000] $rot:F[    0.000000,    0.000000,    0.000000]}}\n"
          f"{indent}    $Camera_Start:{{$loc:F[    0.000000,    0.000000,    0.000000] $rot:F[    0.000000,    0.000000,    0.000000]}}\n"
          f"{indent}    $CS_Camera:K[\n"
          f"{indent}        {{time:    2.000000, $loc:F[    0.000000,    0.000000,    0.000000] $rot:F[    0.000000,    0.000000,    0.000000]}}\n"
          f"{indent}    ]\n"
          f"{indent}    $Load_Anim:{{$actor:$pla0 $anm:&0001}}\n"
          f"{indent}    $Loop\n"
          f"{indent}    $Load_Anim:{{$actor:$cpu0 $anm:&0180}}\n"
          f"{indent}    $Wait\n"
          f"{indent}    $CS_time:    2.500000\n"
          f"{indent}    $End_effects\n"
          f"{indent}    $Link:{{\n"
          f"{indent}        $event:{trigger_block}\n"
          f"{indent}        $audio:null,\n"
          f"{indent}    }}\n"
          f"{indent}    $Set_plafield:null\n"
          f"{indent}    $Set_cpufield:null\n"
          f"{indent}    $Event:{{$evt: &{evt_hex} $flag: &{flag_hex}}}\n"
          f"{indent}    $End_cutscn\n"
          f"{indent}>"
      )

    if ref_block:
      insert_pos = ref_block["end"]
      self.file_content = (
          self.file_content[:insert_pos]
          + "\n"
          + new_block
          + self.file_content[insert_pos:]
      )
    else:
      self.file_content = self.file_content.rstrip("\n") + "\n" + new_block + "\n"

    self.parse_events_file()
    self.parse_animations_file()
    self.parse_position_transforms()
    self.refresh_tables()
    self.refresh_zit_table()

    self.new_ev_audio_entries = []
    self.list_new_ev_audio.delete(0, tk.END)
    self.new_ev_trigger_entries = []
    self.list_new_ev_triggers.delete(0, tk.END)
    self.btn_add_new_ev_trigger.config(state="normal")
    self.ent_new_ev_id.delete(0, tk.END)

    messagebox.showinfo(
        "Éxito",
        f"Se insertó el nuevo evento $EV_{new_id} correctamente.\n"
        "Puedes afinar sus desencadenadores, eventos y (en la plantilla "
        "completa) cámara/animaciones desde las demás pestañas de esta "
        "sección.",
    )

  def setup_anim_editor_ui(self, parent):
    frame_top = ttk.LabelFrame(
        parent, text=" Modificar Animación Seleccionada ($Load_Anim) "
    )
    frame_top.pack(fill="x", padx=5, pady=5)

    ttk.Label(frame_top, text="Evento Padre:").grid(
        row=0, column=0, padx=5, pady=5, sticky="w"
    )
    self.ent_anim_id = ttk.Entry(frame_top, width=15, state="readonly")
    self.ent_anim_id.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_top, text="Actor ($actor):").grid(
        row=0, column=2, padx=5, pady=5, sticky="w"
    )
    self.ent_anim_actor = ttk.Entry(frame_top, width=15, state="readonly")
    self.ent_anim_actor.grid(row=0, column=3, padx=5, pady=5)

    ttk.Label(frame_top, text="Nueva Animación ($anm):").grid(
        row=1, column=0, padx=5, pady=5, sticky="w"
    )
    self.cmb_anim_select = ttk.Combobox(
        frame_top, values=ANIMATION_LIST_LABELS, width=45, state="readonly"
    )
    self.cmb_anim_select.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

    ttk.Label(frame_top, text="Ejecución ($Loop/$Wait):").grid(
        row=2, column=0, padx=5, pady=5, sticky="w"
    )
    self.cmb_anim_mode = ttk.Combobox(
        frame_top, values=["", "$Loop", "$Wait"], width=15, state="readonly"
    )
    self.cmb_anim_mode.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    ttk.Button(
        frame_top,
        text="🔄 Aplicar Cambio a Animación",
        command=self.replace_animation,
    ).grid(row=3, column=0, columnspan=4, pady=8)

    self.tree_anims = ttk.Treeview(
        parent,
        columns=("Padre", "Actor", "Anm_Hex", "Tipo_Animacion", "Modo"),
        show="headings",
    )
    self.tree_anims.heading("Padre", text="Evento Padre")
    self.tree_anims.heading("Actor", text="Actor ($actor)")
    self.tree_anims.heading("Anm_Hex", text="Hex ($anm)")
    self.tree_anims.heading("Tipo_Animacion", text="Nombre / Tipo de Animación")
    self.tree_anims.heading("Modo", text="Modo ($Loop/$Wait)")

    self.tree_anims.column("Padre", width=110)
    self.tree_anims.column("Actor", width=110)
    self.tree_anims.column("Anm_Hex", width=80)
    self.tree_anims.column("Tipo_Animacion", width=340)
    self.tree_anims.column("Modo", width=110)

    self.tree_anims.pack(fill="both", expand=True, padx=5, pady=5)
    self.tree_anims.bind("<<TreeviewSelect>>", self.on_anim_select)

  def setup_zit_editor_ui(self, parent):
    sub_notebook = ttk.Notebook(parent)
    sub_notebook.pack(fill="both", expand=True, padx=5, pady=5)

    self.zit_tab = ttk.Frame(sub_notebook)
    self.zit_comp_tab = ttk.Frame(sub_notebook)
    sub_notebook.add(self.zit_tab, text=" Editor de Z-Items ")
    sub_notebook.add(self.zit_comp_tab, text=" Comparar Archivos ")

    top_bar = ttk.Frame(self.zit_tab)
    top_bar.pack(fill="x", padx=8, pady=(8, 2))

    ttk.Label(
        top_bar,
        text="Los Z-Items se leen y se guardan junto con el resto del archivo cargado en 'Archivo'.",
        anchor="w",
    ).pack(side="left", fill="x", expand=True)

    ttk.Button(
        top_bar, text="Normalizar Z-Items", command=self.normalize_zits
    ).pack(side="right")
    ttk.Button(
        top_bar, text="Actualizar tabla", command=self.refresh_zit_table
    ).pack(side="right", padx=(0, 6))

    filter_bar = ttk.Frame(self.zit_tab)
    filter_bar.pack(fill="x", padx=8, pady=(0, 4))
    ttk.Label(filter_bar, text="Filtrar:").pack(side="left")
    self.zit_filter_var = tk.StringVar()
    self.zit_filter_var.trace_add("write", lambda *a: self.apply_zit_filter())
    ttk.Entry(filter_bar, textvariable=self.zit_filter_var).pack(
        side="left", fill="x", expand=True, padx=(4, 0)
    )

    hint = ttk.Label(
        self.zit_tab,
        text="Doble clic sobre una fila para cambiar su Z-Item. Orden al normalizar: $zit8, $zit1..$zit7 (Vacíos: &00000000).",
        foreground="#999999",
    )
    hint.pack(anchor="w", padx=8)

    columns = ("evento", "actor", "campo", "hex", "dec", "nombre")
    headers = {
        "evento": "Evento", "actor": "Actor", "campo": "Campo",
        "hex": "Valor (hex)", "dec": "Valor (dec)", "nombre": "Z-Item",
    }
    widths = {"evento": 100, "actor": 80, "campo": 60, "hex": 110, "dec": 90, "nombre": 380}

    table_frame = ttk.Frame(self.zit_tab)
    table_frame.pack(fill="both", expand=True, padx=8, pady=4)

    self.zit_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
    for c in columns:
      self.zit_tree.heading(c, text=headers[c], command=lambda col=c: self.sort_zit_by(col))
      self.zit_tree.column(c, width=widths[c], anchor="w")
    self.zit_tree.pack(side="left", fill="both", expand=True)
    self.zit_tree.bind("<Double-1>", lambda e: self.edit_selected_zit())

    zit_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.zit_tree.yview)
    self.zit_tree.configure(yscroll=zit_scrollbar.set)
    zit_scrollbar.pack(side="right", fill="y")

    bottom_bar = ttk.Frame(self.zit_tab)
    bottom_bar.pack(fill="x", padx=8, pady=(0, 8))
    ttk.Button(bottom_bar, text="Editar seleccionado...", command=self.edit_selected_zit).pack(
        side="left"
    )

    self._setup_zit_comparator_ui(self.zit_comp_tab)

  def _setup_zit_comparator_ui(self, parent):
    file_frame = ttk.LabelFrame(parent, text=" Archivos a Comparar ")
    file_frame.pack(fill="x", padx=8, pady=8)

    row_a = ttk.Frame(file_frame)
    row_a.pack(fill="x", padx=6, pady=4)
    ttk.Label(row_a, text="Archivo ANTES (Original):", width=22).pack(side="left")
    self.zit_comp_path_a = tk.StringVar()
    ttk.Entry(row_a, textvariable=self.zit_comp_path_a).pack(side="left", fill="x", expand=True, padx=4)
    ttk.Button(row_a, text="Examinar...", command=lambda: self._browse_zit_comp_file(self.zit_comp_path_a)).pack(side="right")

    row_b = ttk.Frame(file_frame)
    row_b.pack(fill="x", padx=6, pady=(4, 8))
    ttk.Label(row_b, text="Archivo DESPUÉS (Nuevo):", width=22).pack(side="left")
    self.zit_comp_path_b = tk.StringVar()
    ttk.Entry(row_b, textvariable=self.zit_comp_path_b).pack(side="left", fill="x", expand=True, padx=4)
    ttk.Button(row_b, text="Examinar...", command=lambda: self._browse_zit_comp_file(self.zit_comp_path_b)).pack(side="right")

    btn_row = ttk.Frame(file_frame)
    btn_row.pack(fill="x", padx=6, pady=(0, 6))
    ttk.Button(btn_row, text="Ejecutar Comparación", command=self.run_zit_comparison).pack(side="left")
    ttk.Button(btn_row, text="Usar archivo abierto actual como 'DESPUÉS'", command=self.set_current_as_zit_comp_b).pack(side="left", padx=8)

    comp_cols = ("linea", "tipo", "detalle", "antes", "despues")
    comp_headers = {
        "linea": "Línea", "tipo": "Elemento", "detalle": "Cambio / Campo",
        "antes": "Valor ANTES", "despues": "Valor DESPUÉS"
    }
    comp_widths = {"linea": 60, "tipo": 90, "detalle": 180, "antes": 240, "despues": 240}

    comp_table_frame = ttk.Frame(parent)
    comp_table_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

    self.zit_comp_tree = ttk.Treeview(comp_table_frame, columns=comp_cols, show="headings")
    for c in comp_cols:
      self.zit_comp_tree.heading(c, text=comp_headers[c])
      self.zit_comp_tree.column(c, width=comp_widths[c], anchor="w")
    self.zit_comp_tree.pack(side="left", fill="both", expand=True)

    comp_sb = ttk.Scrollbar(comp_table_frame, orient="vertical", command=self.zit_comp_tree.yview)
    self.zit_comp_tree.configure(yscroll=comp_sb.set)
    comp_sb.pack(side="right", fill="y")

  def _browse_zit_comp_file(self, string_var):
    path = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=[("Archivos de Modo Historia", "*.json *.gscf *.GSCF *.gsc *.txt"), ("Todos los archivos", "*.*")]
    )
    if path:
      string_var.set(path)

  def set_current_as_zit_comp_b(self):
    if self.file_path:
      self.zit_comp_path_b.set(self.file_path)
      messagebox.showinfo("Copiado", f"Se asignó el archivo actual como 'DESPUÉS':\n{os.path.basename(self.file_path)}")
    else:
      messagebox.showwarning("Aviso", "No hay ningún archivo abierto actualmente en el editor.")

  def run_zit_comparison(self):
    path_a = self.zit_comp_path_a.get().strip()
    path_b = self.zit_comp_path_b.get().strip()

    if not path_a or not path_b:
      messagebox.showwarning("Faltan rutas", "Por favor selecciona ambos archivos para comparar.")
      return

    if not os.path.exists(path_a) or not os.path.exists(path_b):
      messagebox.showerror("Error", "Uno de los archivos especificados no existe.")
      return

    try:
      with open(path_a, "r", encoding="utf-8", errors="replace") as f:
        lines_a = f.readlines()
      with open(path_b, "r", encoding="utf-8", errors="replace") as f:
        lines_b = f.readlines()
    except Exception as e:
      messagebox.showerror("Error de lectura", str(e))
      return

    self.zit_comp_tree.delete(*self.zit_comp_tree.get_children())

    n = min(len(lines_a), len(lines_b))
    total_line_diffs = 0
    total_zit_diffs = 0

    for i in range(n):
      la, lb = lines_a[i], lines_b[i]
      if la == lb:
        continue
      total_line_diffs += 1

      self.zit_comp_tree.insert("", "end", values=(i + 1, "Línea distinta", "Cambio en contenido de línea", la.strip(), lb.strip()))

      zits_a = {f"zit{m.group(1)}": m.group(2).upper() for m in ZIT_PATTERN.finditer(la)}
      zits_b = {f"zit{m.group(1)}": m.group(2).upper() for m in ZIT_PATTERN.finditer(lb)}

      all_fields = set(zits_a) | set(zits_b)
      for field in sorted(all_fields, key=lambda x: int(x[3:])):
        va = zits_a.get(field, "(no existe)")
        vb = zits_b.get(field, "(no existe)")
        if va != vb:
          total_zit_diffs += 1

          try:
            dec_a = int(va, 16) if va != "(no existe)" else None
            name_a = f" ({lookup_zitem(dec_a)})" if dec_a is not None else ""
          except ValueError:
            name_a = ""

          try:
            dec_b = int(vb, 16) if vb != "(no existe)" else None
            name_b = f" ({lookup_zitem(dec_b)})" if dec_b is not None else ""
          except ValueError:
            name_b = ""

          val_a_str = f"&{va}{name_a}" if va != "(no existe)" else va
          val_b_str = f"&{vb}{name_b}" if vb != "(no existe)" else vb

          self.zit_comp_tree.insert("", "end", values=("", f"Z-Item ({field})", f"Modificación de {field}", val_a_str, val_b_str))

    summary_msg = f"Comparación finalizada. Líneas distintas: {total_line_diffs} | Campos $zit distintos: {total_zit_diffs}"
    if total_line_diffs == 0:
      messagebox.showinfo("Resultado", "¡Los archivos son idénticos línea por línea!")
    else:
      messagebox.showinfo("Resultado", summary_msg)

  def refresh_zit_table(self):
    self.zit_manager.set_text(self.file_content)
    self.render_zit_rows(self.zit_manager.entries)

  def normalize_zits(self):
    if not self.file_content:
      messagebox.showinfo("Nada que normalizar", "Primero carga un archivo de Modo Historia.")
      return
    self.zit_manager.set_text(self.file_content)
    self.zit_manager.normalize_all_lines()
    self.file_content = self.zit_manager.get_text()
    self.render_zit_rows(self.zit_manager.entries)
    messagebox.showinfo(
        "Z-Items normalizados",
        "Los campos $zit del archivo cargado fueron ordenados y completados "
        "($zit8, $zit1..$zit7). Usa 'Guardar' para escribir los cambios en disco."
    )

  def render_zit_rows(self, entries):
    self.zit_tree.delete(*self.zit_tree.get_children())
    self.zit_row_to_entry.clear()
    for entry in entries:
      row_id = self.zit_tree.insert(
          "", "end",
          values=(
              entry["evento"], entry["actor"], entry["campo"],
              f"&{entry['hex']}", entry["dec"], entry["nombre"],
          ),
      )
      self.zit_row_to_entry[row_id] = entry

  def apply_zit_filter(self):
    term = self.zit_filter_var.get().strip().lower()
    if not term:
      self.render_zit_rows(self.zit_manager.entries)
      return
    filtered = [
        e for e in self.zit_manager.entries
        if term in str(e["evento"]).lower()
        or term in str(e["actor"]).lower()
        or term in str(e["campo"]).lower()
        or term in str(e["hex"]).lower()
        or term in str(e["dec"]).lower()
        or term in str(e["nombre"]).lower()
    ]
    self.render_zit_rows(filtered)

  def sort_zit_by(self, col):
    data = [(self.zit_tree.set(k, col), k) for k in self.zit_tree.get_children("")]
    try:
      data.sort(key=lambda t: int(t[0]))
    except ValueError:
      data.sort(key=lambda t: t[0].lower())
    for index, (_, k) in enumerate(data):
      self.zit_tree.move(k, "", index)

  def edit_selected_zit(self):
    if not self.file_content:
      messagebox.showinfo("Nada que editar", "Primero carga un archivo de Modo Historia.")
      return
    sel = self.zit_tree.selection()
    if not sel:
      messagebox.showinfo("Selecciona una fila", "Elige un campo $zit de la tabla primero.")
      return
    row_id = sel[0]
    entry = self.zit_row_to_entry.get(row_id)
    if entry is None:
      return

    def on_accept(new_dec):
      self.zit_manager.apply_edit(entry, new_dec)
      self.file_content = self.zit_manager.get_text()
      self.zit_tree.item(
          row_id,
          values=(
              entry["evento"], entry["actor"], entry["campo"],
              f"&{entry['hex']}", entry["dec"], entry["nombre"],
          ),
      )
      messagebox.showinfo(
          "Actualizado",
          f"{entry['campo']} de {entry['actor']} ({entry['evento']}) "
          f"actualizado a &{entry['hex']} -> {entry['nombre']}\n"
          "Usa 'Guardar' para escribir los cambios en disco."
      )

    ZitEditDialog(self.root, entry, on_accept)

  # ======================================================================
  # EDITOR DE POSICIÓN / ROTACIÓN ($Set_transform)
  # (integrado desde BT3_position_editor.py)
  # ======================================================================

  POS_SCALE = 2.2
  POS_COS_A = math.cos(math.radians(30)) * POS_SCALE
  POS_SIN_A = math.sin(math.radians(30)) * POS_SCALE
  POS_GRID_RANGE = 100
  POS_GRID_STEP = 20

  def setup_position_editor_ui(self, parent):
    top = ttk.Frame(parent, padding=6)
    top.pack(side="top", fill="x")
    ttk.Button(
        top, text="🔄 Recargar desde el archivo actual",
        command=self.parse_position_transforms,
    ).pack(side="left")
    ttk.Button(
        top, text="💾 Aplicar cambios de posición al archivo",
        command=self.save_position_changes,
    ).pack(side="left", padx=6)
    ttk.Label(
        top,
        text="(esto actualiza el contenido en memoria; usa Archivo > Guardar "
             "para escribirlo en disco)",
        foreground="#888888",
    ).pack(side="left", padx=6)

    body = ttk.Frame(parent)
    body.pack(side="top", fill="both", expand=True)

    # ---- panel izquierdo: lista de transforms ----
    left = ttk.Frame(body, padding=6)
    left.pack(side="left", fill="y")

    ttk.Label(left, text="Eventos / Actores ($Set_transform)", font=("", 10, "bold")).pack(anchor="w")

    list_frame = ttk.Frame(left)
    list_frame.pack(side="top", fill="y")
    self.pos_listbox = tk.Listbox(list_frame, width=28, height=28, exportselection=False)
    self.pos_listbox.pack(side="left", fill="y")
    pos_scroll = ttk.Scrollbar(list_frame, orient="vertical", command=self.pos_listbox.yview)
    pos_scroll.pack(side="left", fill="y")
    self.pos_listbox.config(yscrollcommand=pos_scroll.set)
    self.pos_listbox.bind("<<ListboxSelect>>", self.on_position_select)
    self.pos_listbox.bind("<Control-c>", lambda e: self.copy_position_current())
    self.pos_listbox.bind("<Control-v>", lambda e: self.paste_position_current())

    cp_row = ttk.Frame(left)
    cp_row.pack(fill="x", pady=(6, 0))
    ttk.Button(cp_row, text="Copiar (Ctrl+C)", command=self.copy_position_current).pack(side="left", fill="x", expand=True)
    ttk.Button(cp_row, text="Pegar (Ctrl+V)", command=self.paste_position_current).pack(side="left", fill="x", expand=True, padx=(4, 0))

    self.pos_clipboard_label = ttk.Label(left, text="Portapapeles: (vacío)", wraplength=210, foreground="#888888")
    self.pos_clipboard_label.pack(anchor="w", pady=(4, 0))

    # ---- panel central: canvas isométrico ----
    center = ttk.Frame(body, padding=6)
    center.pack(side="left", fill="both", expand=True)

    ttk.Label(
        center,
        text="Vista de referencia (suelo = X/Z, altura = Y). "
             "Clic o arrastra sobre el suelo para mover al actor seleccionado.",
        wraplength=520,
    ).pack(anchor="w")

    self.pos_canvas = tk.Canvas(center, width=620, height=520, bg="#101418", highlightthickness=0)
    self.pos_canvas.pack(pady=6)
    self.pos_canvas.bind("<Button-1>", self.on_position_canvas_click)
    self.pos_canvas.bind("<B1-Motion>", self.on_position_canvas_click)
    self.pos_canvas.bind("<Control-c>", lambda e: self.copy_position_current())
    self.pos_canvas.bind("<Control-v>", lambda e: self.paste_position_current())

    self.pos_legend = ttk.Label(center, text="")
    self.pos_legend.pack(anchor="w")

    # ---- panel derecho: controles numéricos ----
    right = ttk.Frame(body, padding=6)
    right.pack(side="left", fill="y")

    ttk.Label(right, text="Editar transform seleccionado", font=("", 10, "bold")).pack(anchor="w", pady=(0, 6))

    self.pos_actor_label = ttk.Label(right, text="Actor: -", font=("", 10, "bold"))
    self.pos_actor_label.pack(anchor="w")
    self.pos_event_label = ttk.Label(right, text="Evento: -")
    self.pos_event_label.pack(anchor="w", pady=(0, 10))

    self.pos_sliders = {}
    self.pos_entries = {}
    specs = [
        ("loc", 0, "Posición X", -150, 150),
        ("loc", 1, "Posición Y (altura)", -50, 50),
        ("loc", 2, "Posición Z (profundidad)", -150, 150),
        ("rot", 0, "Rotación X (pitch)", -180, 180),
        ("rot", 1, "Rotación Y (yaw)", -180, 180),
        ("rot", 2, "Rotación Z (roll)", -180, 180),
    ]
    for group, idx, label, lo, hi in specs:
      frame = ttk.Frame(right)
      frame.pack(fill="x", pady=4)
      ttk.Label(frame, text=label, width=22).pack(anchor="w")

      row = ttk.Frame(frame)
      row.pack(fill="x")

      var = tk.DoubleVar(value=0.0)
      scale = ttk.Scale(
          row, from_=lo, to=hi, orient="horizontal", variable=var,
          command=lambda v, g=group, i=idx: self.on_position_slider_change(g, i),
      )
      scale.pack(side="left", fill="x", expand=True)

      entry = ttk.Entry(row, width=9)
      entry.pack(side="left", padx=4)
      entry.bind("<Return>", lambda e, g=group, i=idx: self.on_position_entry_change(g, i))

      self.pos_sliders[(group, idx)] = var
      self.pos_entries[(group, idx)] = entry

    ttk.Button(right, text="Aplicar a este transform", command=self.apply_position_current).pack(fill="x", pady=(14, 4))
    ttk.Label(
        right,
        text="(los cambios se aplican en memoria;\nusa 'Aplicar cambios de posición\nal archivo' para escribirlos\nal contenido del archivo)",
        foreground="#888888",
    ).pack(anchor="w")

    self.pos_status = ttk.Label(parent, text="Carga un archivo para ver los $Set_transform.", anchor="w", relief="sunken")
    self.pos_status.pack(side="bottom", fill="x")

  # -------------------------------------------------------- parseo/carga --
  def parse_position_transforms(self):
    if not self.file_content:
      self.pos_transforms = []
      self.pos_selected = None
      if hasattr(self, "pos_listbox"):
        self.pos_listbox.delete(0, "end")
        self.draw_position_scene()
        self.pos_status.config(text="Carga un archivo para ver los $Set_transform.")
      return

    self.pos_transforms = parse_pos_transforms(self.file_content)
    self.pos_selected = None
    self.refresh_position_listbox()

    self.pos_status.config(
        text=f"{len(self.pos_transforms)} bloques $Set_transform encontrados."
    )
    if self.pos_transforms:
      self.pos_listbox.selection_set(0)
      self.on_position_select()
    else:
      self.draw_position_scene()

  def refresh_position_listbox(self):
    self.pos_listbox.delete(0, "end")
    for t in self.pos_transforms:
      label = t.label() + ("  *" if t.modified else "")
      self.pos_listbox.insert("end", label)

  # --------------------------------------------------------- selección --
  def on_position_select(self, event=None):
    sel = self.pos_listbox.curselection()
    if not sel:
      return
    self.pos_selected = self.pos_transforms[sel[0]]
    self.sync_position_fields()
    self.draw_position_scene()

  def sync_position_fields(self):
    t = self.pos_selected
    if not t:
      return
    self.pos_updating_fields = True
    self.pos_actor_label.config(text=f"Actor: {t.actor}")
    self.pos_event_label.config(text=f"Evento: {t.event}")
    for i in range(3):
      self.pos_sliders[("loc", i)].set(t.loc[i])
      self.pos_entries[("loc", i)].delete(0, "end")
      self.pos_entries[("loc", i)].insert(0, f"{t.loc[i]:.2f}")
      self.pos_sliders[("rot", i)].set(t.rot[i])
      self.pos_entries[("rot", i)].delete(0, "end")
      self.pos_entries[("rot", i)].insert(0, f"{t.rot[i]:.2f}")
    self.pos_updating_fields = False

  # ------------------------------------------------------------ edición --
  def on_position_slider_change(self, group, idx):
    if self.pos_updating_fields or not self.pos_selected:
      return
    value = self.pos_sliders[(group, idx)].get()
    getattr(self.pos_selected, group)[idx] = value
    self.pos_selected.modified = True
    entry = self.pos_entries[(group, idx)]
    entry.delete(0, "end")
    entry.insert(0, f"{value:.2f}")
    self.draw_position_scene()

  def on_position_entry_change(self, group, idx):
    if not self.pos_selected:
      return
    try:
      value = float(self.pos_entries[(group, idx)].get())
    except ValueError:
      return
    getattr(self.pos_selected, group)[idx] = value
    self.pos_selected.modified = True
    self.pos_sliders[(group, idx)].set(value)
    self.draw_position_scene()

  def apply_position_current(self):
    if not self.pos_selected:
      return
    self.pos_selected.modified = True
    idx = self.pos_transforms.index(self.pos_selected)
    self.refresh_position_listbox()
    self.pos_listbox.selection_set(idx)
    self.pos_status.config(
        text=f"Cambios aplicados en memoria a {self.pos_selected.actor} ({self.pos_selected.event})."
    )
    self.draw_position_scene()

  # ----------------------------------------------------- copiar/pegar --
  def copy_position_current(self):
    if not self.pos_selected:
      return
    self.pos_clipboard = (list(self.pos_selected.loc), list(self.pos_selected.rot))

    try:
      self.root.clipboard_clear()
      self.root.clipboard_append(self.pos_selected.format())
    except tk.TclError:
      pass

    self.pos_clipboard_label.config(
        text=f"Portapapeles: {self.pos_selected.actor} ({self.pos_selected.event})\n"
             f"loc={tuple(round(v, 2) for v in self.pos_selected.loc)}\n"
             f"rot={tuple(round(v, 2) for v in self.pos_selected.rot)}"
    )
    self.pos_status.config(text=f"Copiado: {self.pos_selected.actor} ({self.pos_selected.event}).")

  def paste_position_current(self):
    if not self.pos_selected:
      return

    loc, rot = None, None

    if self.pos_clipboard is not None:
      loc, rot = self.pos_clipboard
    else:
      try:
        text = self.root.clipboard_get()
      except tk.TclError:
        text = ""
      m = POS_TRANSFORM_RE.search(text)
      if m:
        loc = (float(m.group("lx")), float(m.group("ly")), float(m.group("lz")))
        rot = (float(m.group("rx")), float(m.group("ry")), float(m.group("rz")))

    if loc is None:
      messagebox.showinfo(
          "Nada para pegar",
          "Primero copia un $Set_transform (Ctrl+C), o pega un texto\n"
          "de la forma $Set_transform:{$actor:$X $loc:F[...] $rot:F[...]}\n"
          "en el portapapeles del sistema.",
      )
      return

    self.pos_selected.loc = list(loc)
    self.pos_selected.rot = list(rot)
    self.pos_selected.modified = True
    self.sync_position_fields()

    idx = self.pos_transforms.index(self.pos_selected)
    self.refresh_position_listbox()
    self.pos_listbox.selection_set(idx)

    self.draw_position_scene()
    self.pos_status.config(text=f"Pegado en: {self.pos_selected.actor} ({self.pos_selected.event}).")

  # ------------------------------------------------------- canvas iso --
  def pos_world_to_screen(self, x, y, z):
    cx, cy = 310, 280
    sx = cx + (x - z) * self.POS_COS_A
    sy = cy + (x + z) * self.POS_SIN_A - y * self.POS_SCALE
    return sx, sy

  def pos_screen_to_world_floor(self, sx, sy):
    cx, cy = 310, 280
    dx = sx - cx
    dy = sy - cy
    a = dx / self.POS_COS_A
    b = dy / self.POS_SIN_A
    x = (a + b) / 2
    z = (b - a) / 2
    return x, z

  def draw_position_scene(self):
    if not hasattr(self, "pos_canvas"):
      return
    c = self.pos_canvas
    c.delete("all")

    rng = self.POS_GRID_RANGE
    step = self.POS_GRID_STEP
    for v in range(-rng, rng + 1, step):
      p1 = self.pos_world_to_screen(v, 0, -rng)
      p2 = self.pos_world_to_screen(v, 0, rng)
      c.create_line(*p1, *p2, fill="#233042")
      p3 = self.pos_world_to_screen(-rng, 0, v)
      p4 = self.pos_world_to_screen(rng, 0, v)
      c.create_line(*p3, *p4, fill="#233042")

    ox = self.pos_world_to_screen(-rng, 0, 0)
    oxe = self.pos_world_to_screen(rng, 0, 0)
    c.create_line(*ox, *oxe, fill="#3d5a80", width=2)
    c.create_text(*self.pos_world_to_screen(rng + 8, 0, 0), text="X", fill="#3d5a80")

    oz = self.pos_world_to_screen(0, 0, -rng)
    oze = self.pos_world_to_screen(0, 0, rng)
    c.create_line(*oz, *oze, fill="#5a3d80", width=2)
    c.create_text(*self.pos_world_to_screen(0, 0, rng + 8), text="Z (profundidad)", fill="#5a3d80")

    oy = self.pos_world_to_screen(0, 0, 0)
    oye = self.pos_world_to_screen(0, 40, 0)
    c.create_line(*oy, *oye, fill="#808080", dash=(3, 2))
    c.create_text(*self.pos_world_to_screen(0, 44, 0), text="Y (altura)", fill="#808080")

    if not self.pos_selected:
      return

    same_event = [t for t in self.pos_transforms if t.event == self.pos_selected.event]
    for t in same_event:
      x, y, z = t.loc
      sx, sy = self.pos_world_to_screen(x, y, z)
      is_sel = (t is self.pos_selected)
      r = 10 if is_sel else 7
      color = pos_color_for(t.actor)
      outline = "#FFFFFF" if is_sel else color

      floor_sx, floor_sy = self.pos_world_to_screen(x, 0, z)
      if abs(y) > 0.01:
        c.create_line(sx, sy, floor_sx, floor_sy, fill="#555", dash=(2, 2))

      c.create_oval(sx - r, sy - r, sx + r, sy + r, fill=color, outline=outline, width=2)
      c.create_text(sx, sy - r - 10, text=t.actor, fill="white", font=("", 9, "bold" if is_sel else "normal"))

      yaw = math.radians(t.rot[1])
      arrow_len = 16
      ax = x + arrow_len * math.sin(yaw)
      az = z + arrow_len * math.cos(yaw)
      asx, asy = self.pos_world_to_screen(ax, y, az)
      c.create_line(sx, sy, asx, asy, fill=outline, width=2, arrow="last")

    self.pos_legend.config(
        text=f"Editando: {self.pos_selected.actor}  en  {self.pos_selected.event}   "
             f"|  loc=({self.pos_selected.loc[0]:.2f}, {self.pos_selected.loc[1]:.2f}, {self.pos_selected.loc[2]:.2f})  "
             f"rot=({self.pos_selected.rot[0]:.2f}, {self.pos_selected.rot[1]:.2f}, {self.pos_selected.rot[2]:.2f})"
    )

  def on_position_canvas_click(self, event):
    if not self.pos_selected:
      return
    x, z = self.pos_screen_to_world_floor(event.x, event.y)
    self.pos_selected.loc[0] = x
    self.pos_selected.loc[2] = z
    self.pos_selected.modified = True
    self.sync_position_fields()
    self.draw_position_scene()

  # ------------------------------------------------------------- guardar --
  def save_position_changes(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return

    modified = [t for t in self.pos_transforms if t.modified]
    if not modified:
      messagebox.showinfo("Nada que guardar", "No hay cambios de posición pendientes.")
      return

    text = self.file_content
    for t in sorted(modified, key=lambda t: t.start, reverse=True):
      text = text[:t.start] + t.format() + text[t.end:]

    self.file_content = text
    self.parse_position_transforms()

    self.pos_status.config(
        text=f"{len(modified)} transform(s) aplicados al contenido del archivo (en memoria)."
    )
    messagebox.showinfo(
        "Aplicado",
        f"{len(modified)} bloque(s) $Set_transform actualizados en el archivo.\n"
        "Usa Archivo > Guardar (o Guardar como...) para escribirlo en disco.",
    )

  def load_file(self):
    path = filedialog.askopenfilename(
        filetypes=[
            ("Archivos GSCF / JSON", "*.json *.GSCF *.gsc"),
            ("Todos los Archivos", "*.*"),
        ]
    )
    if not path:
      return

    try:
      with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
        self.file_content = f.read()

      # Los $event de cada $Link siempre en orden $EV_00 -> $EV_XX
      self.file_content = sort_link_events_in_text(self.file_content)

      self.file_path = path
      self.lbl_file.config(text=f"Archivo cargado: {os.path.basename(path)}")

      self.parse_json_data()
      self.parse_events_file()
      self.parse_animations_file()
      self.refresh_tables()
      self.refresh_zit_table()
      self.parse_position_transforms()

    except Exception as e:
      messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

  def parse_json_data(self):
    match_map = re.search(r"\$map:\s*(\d+)", self.file_content)
    if match_map:
      self.cmb_map.set(MAPS.get(match_map.group(1), MAPS["0"]))

    match_bgm = re.search(r"\$bgm:\s*(\d+)", self.file_content)
    if match_bgm:
      self.cmb_bgm.set(BGMS.get(match_bgm.group(1), BGMS["0"]))

    for i in range(5):
      self.read_actor_info(
          f"pla{i}",
          self.cmb_players[i],
          self.cmb_player_costumes[i],
          self.chk_player_dmg[i],
          self.ent_player_hp[i],
          self.ent_player_ia[i],
          i,
      )
      self.read_actor_info(
          f"cpu{i}",
          self.cmb_cpus[i],
          self.cmb_cpu_costumes[i],
          self.chk_cpu_dmg[i],
          self.ent_cpu_hp[i],
          self.ent_cpu_ia[i],
          i,
          default_ia="9",
      )

  def read_actor_info(
      self,
      actor_tag,
      cmb_char,
      cmb_cost,
      var_dmg,
      ent_hp,
      ent_ia,
      index,
      default_ia="0",
  ):
    pattern = (
        rf"\$Actor:\s*\{{[^}}]*?\$name:\s*[\"\']?\${actor_tag}\b[\"\']?[^}}]*?\}}"
    )
    match = re.search(pattern, self.file_content, re.IGNORECASE)

    if match:
      line_text = match.group(0)

      match_chr = re.search(r"\$chr:\s*&([0-9A-Fa-f]+)", line_text)
      if match_chr:
        char_dec = str(int(match_chr.group(1), 16))
        cmb_char.set(CHARACTERS_STORY.get(char_dec, CHARACTERS_STORY["0"]))
        self.original_actor_char[actor_tag] = char_dec

        # --- Detección automática de personaje DLC -----------------------
        # Si el $chr del actor coincide con uno de la lista de personajes
        # DLC (165-252), lo reflejamos de una vez en la pestaña "Cambiar
        # Personaje a DLC" para que el usuario vea que ese slot ya tiene
        # un personaje DLC asignado, en lugar de dejarlo en "No aplicar".
        dlc_combo_list = None
        if actor_tag.startswith("pla") and hasattr(self, "cmb_dlc_players"):
          dlc_combo_list = self.cmb_dlc_players
        elif actor_tag.startswith("cpu") and hasattr(self, "cmb_dlc_cpus"):
          dlc_combo_list = self.cmb_dlc_cpus

        if dlc_combo_list is not None and index < len(dlc_combo_list):
          if char_dec in DLC_CHARACTERS_STORY:
            dlc_combo_list[index].set(DLC_CHARACTERS_STORY[char_dec])
          else:
            dlc_combo_list[index].set(DLC_EMPTY_SLOT)

      match_cost = re.search(r"\$ctm:\s*(\d+)", line_text)
      if match_cost:
        cmb_cost.set(COSTUMES.get(match_cost.group(1), COSTUMES["0"]))

      match_dmg = re.search(r"\$dmg:\s*(\d+)", line_text)
      if match_dmg:
        var_dmg.set(int(match_dmg.group(1)))
      else:
        var_dmg.set(0)

      match_hp = re.search(r"\$hp:\s*(\d+)", line_text)
      ent_hp.delete(0, tk.END)
      ent_hp.insert(0, match_hp.group(1) if match_hp else "30000")

      match_ia = re.search(r"\$ia:\s*(\d+)", line_text)
      ent_ia.delete(0, tk.END)
      ent_ia.insert(0, match_ia.group(1) if match_ia else default_ia)
    else:
      self.original_actor_char.pop(actor_tag, None)
      if index > 0:
        cmb_char.set(EMPTY_SLOT)
      var_dmg.set(0)
      ent_hp.delete(0, tk.END)
      ent_hp.insert(0, "30000")
      ent_ia.delete(0, tk.END)
      ent_ia.insert(0, default_ia)

      # Actor inexistente: no hay personaje DLC que detectar, así que
      # dejamos su combo de la pestaña DLC en el valor por defecto.
      dlc_combo_list = None
      if actor_tag.startswith("pla") and hasattr(self, "cmb_dlc_players"):
        dlc_combo_list = self.cmb_dlc_players
      elif actor_tag.startswith("cpu") and hasattr(self, "cmb_dlc_cpus"):
        dlc_combo_list = self.cmb_dlc_cpus
      if dlc_combo_list is not None and index < len(dlc_combo_list):
        dlc_combo_list[index].set(DLC_EMPTY_SLOT)

  def parse_events_file(self):
    self.triggers_list = []
    self.events_list = []

    ev_matches = list(
        re.finditer(EV_HEADER_RE, self.file_content)
    )

    trig_pattern = re.compile(
        r'\{\s*\$if\s*:\s*&([0-9a-fA-F]+)[\s,]+\$to\s*:\s*(\$EV_\w+|\w+)\s*\}',
        re.IGNORECASE,
    )

    for match in trig_pattern.finditer(self.file_content):
      if_pos = match.start()
      parent_ev = "DESCONOCIDO"
      for ev_m in reversed(ev_matches):
        if ev_m.start() < if_pos:
          parent_ev = ev_m.group(1).replace('"', "").replace("'", "")
          break

      self.triggers_list.append({
          "ev_id": parent_ev,
          "block_raw": match.group(0),
          "if_raw": match.group(1),
          "to_raw": match.group(2),
      })

    full_event_pattern = re.compile(
        r'(\$Set_plafield:[^\n\r]*[\r\n]+\s*\$Set_cpufield:[^\n\r]*[\r\n]+\s*\$Event:\s*\{[^\}]*?\$evt:\s*&?([0-9a-fA-F]{4})\s+\$flag:\s*&?([0-9a-fA-F]{8})[^\}]*\})',
        re.IGNORECASE,
    )

    for match in full_event_pattern.finditer(self.file_content):
      full_block = match.group(1)
      evt_hex = match.group(2)
      flag_hex = match.group(3)
      cmd_pos = match.start()

      parent_ev = "DESCONOCIDO"
      for ev_m in reversed(ev_matches):
        if ev_m.start() < cmd_pos:
          parent_ev = ev_m.group(1).replace('"', "").replace("'", "")
          break

      self.events_list.append({
          "ev_id": parent_ev,
          "block_raw": full_block,
          "evt_hex": evt_hex,
          "flag_hex": flag_hex,
      })

    # Orden por bloque $EV_00 -> $EV_XX (estable: respeta el orden interno)
    self.triggers_list.sort(key=lambda d: ev_parent_sort_key(d["ev_id"]))
    self.events_list.sort(key=lambda d: ev_parent_sort_key(d["ev_id"]))

  def parse_animations_file(self):
    self.anims_list = []
    ev_matches = list(
        re.finditer(EV_HEADER_RE, self.file_content)
    )

    anim_pattern = re.compile(
        r'(\$Load_Anim\s*:\s*\{[^}]*?\$actor\s*:\s*(\$[\w\d]+)[^}]*?\$anm\s*:\s*&([0-9a-fA-F]+)[^}]*\})(?:\s*[\r\n]*\s*(\$Loop|\$Wait))?',
        re.IGNORECASE,
    )

    for match in anim_pattern.finditer(self.file_content):
      full_block = match.group(0)
      anim_block_only = match.group(1)
      actor_name = match.group(2)
      anm_hex = match.group(3).upper()
      mode = match.group(4) if match.group(4) else ""
      pos = match.start()

      parent_ev = "DESCONOCIDO"
      for ev_m in reversed(ev_matches):
        if ev_m.start() < pos:
          parent_ev = ev_m.group(1).replace('"', "").replace("'", "")
          break

      self.anims_list.append({
          "ev_id": parent_ev,
          "full_block_raw": full_block,
          "anim_block_only": anim_block_only,
          "actor": actor_name,
          "anm_hex": anm_hex,
          "mode": mode,
      })

    self.anims_list.sort(key=lambda d: ev_parent_sort_key(d["ev_id"]))

  def refresh_tables(self):
    for item in self.tree_triggers.get_children():
      self.tree_triggers.delete(item)
    for item in self.tree_events.get_children():
      self.tree_events.delete(item)
    for item in self.tree_anims.get_children():
      self.tree_anims.delete(item)

    self.refresh_ev_manage_table()

    for idx, item in enumerate(self.triggers_list):
      norm_hex = normalize_hex(item["if_raw"], HEX_TO_LABEL_COND)
      desc = HEX_TO_LABEL_COND.get(norm_hex, "DESCONOCIDO / Custom Condition")
      self.tree_triggers.insert(
          "",
          "end",
          iid=str(idx),
          values=(item["ev_id"], item["if_raw"], desc, item["to_raw"]),
      )

    for idx, item in enumerate(self.events_list):
      norm_hex = normalize_hex(item["evt_hex"], HEX_TO_LABEL_EVENT)
      desc = HEX_TO_LABEL_EVENT.get(norm_hex, "DESCONOCIDO / Custom Event")

      if is_char_event(desc):
        char_hex_code = item["flag_hex"][-2:].upper()
        char_name = CHARACTERS_EVENTS.get(char_hex_code, "Desconocido")
        char_display = f"{char_hex_code} - {char_name}"
      elif is_map_event(desc):
        map_id = self._map_id_from_flag(item["flag_hex"])
        char_display = MAPS.get(str(map_id), "Mapa desconocido")
      else:
        char_display = "N/A"

      self.tree_events.insert(
          "",
          "end",
          iid=str(idx),
          values=(
              item["ev_id"],
              item["evt_hex"],
              desc,
              item["flag_hex"],
              char_display,
          ),
      )

    for idx, item in enumerate(self.anims_list):
      clean_hex = item["anm_hex"].lstrip("0") or "000"
      if len(clean_hex) == 1:
        clean_hex = "00" + clean_hex
      elif len(clean_hex) == 2:
        clean_hex = "0" + clean_hex

      anim_name = ANIMATIONS.get(
          clean_hex,
          ANIMATIONS.get(
              item["anm_hex"], "Animación Personalizada / Desconocida"
          ),
      )
      self.tree_anims.insert(
          "",
          "end",
          iid=str(idx),
          values=(
              item["ev_id"],
              item["actor"],
              item["anm_hex"],
              anim_name,
              item.get("mode", ""),
          ),
      )

  def on_trig_select(self, event):
    sel = self.tree_triggers.selection()
    if not sel:
      return
    self.selected_trig_idx = int(sel[0])
    item = self.triggers_list[self.selected_trig_idx]

    self.ent_trig_id.config(state="normal")
    self.ent_trig_id.delete(0, tk.END)
    self.ent_trig_id.insert(0, item["ev_id"])
    self.ent_trig_id.config(state="readonly")

    norm_hex = normalize_hex(item["if_raw"], HEX_TO_LABEL_COND)
    desc = HEX_TO_LABEL_COND.get(norm_hex, None)
    if desc in HEX_CONDITIONS:
      self.cmb_trig_cond.set(desc)
    else:
      self.cmb_trig_cond.set(item["if_raw"])

    self.ent_trig_target.delete(0, tk.END)
    self.ent_trig_target.insert(0, item["to_raw"])

    self.ent_trig_rename_to.delete(0, tk.END)
    self.ent_trig_rename_to.insert(0, item["to_raw"])

  def on_ev_select(self, event):
    sel = self.tree_events.selection()
    if not sel:
      return
    self.selected_ev_idx = int(sel[0])
    item = self.events_list[self.selected_ev_idx]

    self.ent_ev_id.config(state="normal")
    self.ent_ev_id.delete(0, tk.END)
    self.ent_ev_id.insert(0, item["ev_id"])
    self.ent_ev_id.config(state="readonly")

    norm_hex = normalize_hex(item["evt_hex"], HEX_TO_LABEL_EVENT)
    desc = HEX_TO_LABEL_EVENT.get(norm_hex, None)
    if desc in HEX_EVENTS:
      self.cmb_ev_select.set(desc)
    else:
      self.cmb_ev_select.set(item["evt_hex"])

    if is_char_event(desc or ""):
      self.chk_use_dlc_char.config(state="normal")
      char_hex_code = item["flag_hex"][-2:].upper()
      if char_hex_code in DLC_CHARACTERS_EVENTS:
        self.var_use_dlc_char.set(True)
        self.cmb_char_select_dlc.set(
            f"{char_hex_code} - {DLC_CHARACTERS_EVENTS[char_hex_code]}"
        )
      elif char_hex_code in CHARACTERS_EVENTS:
        self.var_use_dlc_char.set(False)
        self.cmb_char_select.set(
            f"{char_hex_code} - {CHARACTERS_EVENTS[char_hex_code]}"
        )
      else:
        self.var_use_dlc_char.set(False)
      self.on_toggle_dlc_char()
    else:
      self.cmb_char_select.config(state="disabled")
      self.chk_use_dlc_char.config(state="disabled")
      self.cmb_char_select_dlc.config(state="disabled")

    if is_map_event(desc or ""):
      map_id = self._map_id_from_flag(item["flag_hex"])
      label = MAPS.get(str(map_id)) if map_id is not None else None
      if label:
        self.cmb_map_select.set(label)
      self.cmb_map_select.config(state="readonly")
    else:
      self.cmb_map_select.config(state="disabled")

  @staticmethod
  def _map_id_from_flag(flag_hex):
    try:
      return int(flag_hex[-2:], 16)
    except (ValueError, TypeError):
      return None

  def on_anim_select(self, event):
    sel = self.tree_anims.selection()
    if not sel:
      return
    self.selected_anim_idx = int(sel[0])
    item = self.anims_list[self.selected_anim_idx]

    self.ent_anim_id.config(state="normal")
    self.ent_anim_id.delete(0, tk.END)
    self.ent_anim_id.insert(0, item["ev_id"])
    self.ent_anim_id.config(state="readonly")

    self.ent_anim_actor.config(state="normal")
    self.ent_anim_actor.delete(0, tk.END)
    self.ent_anim_actor.insert(0, item["actor"])
    self.ent_anim_actor.config(state="readonly")

    mode_val = item.get("mode", "").strip()
    if mode_val.lower() == "$loop":
      self.cmb_anim_mode.set("$Loop")
    elif mode_val.lower() == "$wait":
      self.cmb_anim_mode.set("$Wait")
    else:
      self.cmb_anim_mode.set("")

    clean_hex = item["anm_hex"].lstrip("0") or "000"
    if len(clean_hex) == 1:
      clean_hex = "00" + clean_hex
    elif len(clean_hex) == 2:
      clean_hex = "0" + clean_hex

    for val in ANIMATION_LIST_LABELS:
      if val.startswith(clean_hex + " ") or val.startswith(
          item["anm_hex"] + " "
      ):
        self.cmb_anim_select.set(val)
        break

  def on_evt_combo_change(self, event=None):
    ev_label = self.cmb_ev_select.get()
    if is_char_event(ev_label):
      self.chk_use_dlc_char.config(state="normal")
      self.on_toggle_dlc_char()
    else:
      self.cmb_char_select.config(state="disabled")
      self.chk_use_dlc_char.config(state="disabled")
      self.cmb_char_select_dlc.config(state="disabled")

    if is_map_event(ev_label):
      self.cmb_map_select.config(state="readonly")
    else:
      self.cmb_map_select.config(state="disabled")

  def on_toggle_dlc_char(self):
    if self.var_use_dlc_char.get():
      self.cmb_char_select.config(state="disabled")
      self.cmb_char_select_dlc.config(state="readonly")
    else:
      self.cmb_char_select.config(state="readonly")
      self.cmb_char_select_dlc.config(state="disabled")

  def replace_trigger(self):
    if self.selected_trig_idx is None:
      messagebox.showwarning(
          "Atención",
          "Selecciona una fila en la tabla de Desencadenadores primero.",
      )
      return

    cond_label = self.cmb_trig_cond.get()
    new_hex = HEX_CONDITIONS.get(cond_label, cond_label)
    new_to = self.ent_trig_target.get().strip()

    item = self.triggers_list[self.selected_trig_idx]
    old_block = item["block_raw"]
    new_block = f"{{$if:&{new_hex}, $to:{new_to}}}"

    if old_block in self.file_content:
      self.file_content = self.file_content.replace(old_block, new_block, 1)
      self.parse_events_file()
      self.parse_animations_file()
      self.refresh_tables()
      messagebox.showinfo(
          "Éxito", f"Desencadenador modificado correctamente:\n{new_block}"
      )
    else:
      messagebox.showerror(
          "Error", "No se encontró el desencadenador original en el archivo."
      )

  def rename_trigger_target(self):
    """Renombra el $to:$EV_XX del desencadenador seleccionado en TODAS las
    apariciones del archivo (todos los $if -> $to que apunten a ese mismo
    evento), a diferencia de "Aplicar Cambio a Desencadenador" que solo
    modifica el desencadenador seleccionado."""
    if self.selected_trig_idx is None:
      messagebox.showwarning(
          "Atención",
          "Selecciona una fila en la tabla de Desencadenadores primero.",
      )
      return

    old_to = self.triggers_list[self.selected_trig_idx]["to_raw"].strip()
    new_to = self.ent_trig_rename_to.get().strip()

    if not new_to:
      messagebox.showwarning(
          "Atención", "Escribe el nuevo nombre para $to (por ej. $EV_30)."
      )
      return

    if new_to == old_to:
      messagebox.showinfo(
          "Sin cambios", "El nuevo nombre es igual al actual; no hay nada que renombrar."
      )
      return

    pattern = re.compile(
        r"(\$to\s*:\s*)" + re.escape(old_to) + r"\b", re.IGNORECASE
    )
    self.file_content, count = pattern.subn(
        lambda m: m.group(1) + new_to, self.file_content
    )

    if count:
      self.parse_events_file()
      self.parse_animations_file()
      self.refresh_tables()
      messagebox.showinfo(
          "Éxito",
          f"Se renombró '{old_to}' a '{new_to}' en {count} desencadenador(es).",
      )
    else:
      messagebox.showerror(
          "Error",
          f"No se encontró ningún '$to:{old_to}' en el archivo.",
      )

  def replace_event(self):
        if self.selected_ev_idx is None:
            messagebox.showwarning(
                "Atención", "Selecciona una fila en la tabla de Eventos primero."
            )
            return

        ev_label = self.cmb_ev_select.get()
        new_evt_hex = HEX_EVENTS.get(ev_label, ev_label)

        if is_char_event(ev_label):
            if self.var_use_dlc_char.get():
                char_label = self.cmb_char_select_dlc.get()
            else:
                char_label = self.cmb_char_select.get()
            char_hex_code = char_label.split(" - ")[0].strip()
            new_flag_hex = f"000000{char_hex_code}"
        elif is_map_event(ev_label):
            map_label = self.cmb_map_select.get()
            map_num = map_label.split(" - ")[0].strip()
            try:
                new_flag_hex = f"000000{int(map_num):02X}"
            except ValueError:
                new_flag_hex = "FFFFFFFF"
        else:
            new_flag_hex = "FFFFFFFF"

        item = self.events_list[self.selected_ev_idx]
        old_block = item["block_raw"]

        sangria = "         "  # 9 espacios de sangría exacta

        if "[CPU]" in ev_label:
            # Mapeo según el evento de CPU seleccionado (de 8011 a 8015)
            if new_evt_hex == "8011":
                cpufield = "<$actor:$cpu0 >"
            elif new_evt_hex == "8012":
                cpufield = "<$actor:$cpu1 >"
            elif new_evt_hex == "8013":
                cpufield = "<$actor:$cpu2 >"
            elif new_evt_hex == "8014":
                cpufield = "<$actor:$cpu3 >"
            elif new_evt_hex == "8015":
                cpufield = "<$actor:$cpu4 >"
            else:
                cpufield = "<$actor:$cpu0 >"

            plafield = "<$addHp:100 >"
        else:
            plafield = "<$actor:$pla1 >"
            cpufield = "null"

        new_block = (
            f"$Set_plafield:{plafield}\n"
            f"{sangria}$Set_cpufield:{cpufield}\n"
            f"{sangria}$Event:{{$evt: &{new_evt_hex} $flag: &{new_flag_hex}}}"
        )

        sangria = "         "  # 9 espacios de sangría exacta

        new_block = (
            f"$Set_plafield:{plafield}\n"
            f"{sangria}$Set_cpufield:{cpufield}\n"
            f"{sangria}$Event:{{$evt: &{new_evt_hex} $flag: &{new_flag_hex}}}"
        )

        if old_block in self.file_content:
            self.file_content = self.file_content.replace(old_block, new_block, 1)
            self.parse_events_file()
            self.parse_animations_file()
            self.refresh_tables()
            messagebox.showinfo(
                "Éxito",
                f"Evento y Personaje de {item['ev_id']} modificado correctamente.",
            )
        else:
            messagebox.showerror(
                "Error", "No se encontró el evento original en el archivo."
      )

  def replace_animation(self):
    if self.selected_anim_idx is None:
      messagebox.showwarning(
          "Atención", "Selecciona una fila en la pestaña de Animaciones primero."
      )
      return

    selected_anim_text = self.cmb_anim_select.get()
    if not selected_anim_text:
      return

    new_anm_hex = selected_anim_text.split(" - ")[0].strip()
    new_mode = self.cmb_anim_mode.get().strip()

    item = self.anims_list[self.selected_anim_idx]
    old_full_block = item["full_block_raw"]
    old_anim_block = item["anim_block_only"]

    new_anim_block = re.sub(
        r"(\$anm\s*:\s*&?)[0-9a-fA-F]+",
        rf"\g<1>{new_anm_hex}",
        old_anim_block,
        flags=re.IGNORECASE,
    )

    line_start_idx = self.file_content.rfind('\n', 0, self.file_content.find(old_anim_block))
    if line_start_idx == -1:
      line_start_idx = 0
    else:
      line_start_idx += 1
    
    current_line = self.file_content[line_start_idx:self.file_content.find(old_anim_block) + len(old_anim_block)]
    indent_match = re.match(r"^([ \t]*)", current_line)
    indent = indent_match.group(1) if indent_match else "        "

    if new_mode:
      new_full_block = f"{new_anim_block}\n{indent}{new_mode}"
    else:
      new_full_block = new_anim_block

    if old_full_block in self.file_content:
      self.file_content = self.file_content.replace(
          old_full_block, new_full_block, 1
      )
    elif old_anim_block in self.file_content:
      self.file_content = self.file_content.replace(
          old_anim_block, new_full_block, 1
      )
    else:
      messagebox.showerror(
          "Error", "No se encontró el bloque de animación original en el archivo."
      )
      return

    self.parse_events_file()
    self.parse_animations_file()
    self.refresh_tables()

    modo_msg = new_mode if new_mode else "Ninguno"
    messagebox.showinfo(
        "Éxito",
        f"Animación y ejecución actualizadas correctamente.\nModo: {modo_msg}",
    )

  def process_updated_content(self):
    if not self.file_content:
      messagebox.showwarning("Atención", "Carga un archivo primero.")
      return None

    content = self.file_content
    map_key = [k for k, v in MAPS.items() if v == self.cmb_map.get()][0]
    bgm_key = [k for k, v in BGMS.items() if v == self.cmb_bgm.get()][0]

    content = re.sub(r"(\$map:\s*)\d+", r"\g<1>" + str(map_key), content)
    content = re.sub(r"(\$bgm:\s*)\d+", r"\g<1>" + str(bgm_key), content)

    # 0. Conservar los campos $zit ya existentes de cada actor (por si fueron
    #    editados en la pestaña "Z-Items") antes de reconstruir los bloques $Actor.
    existing_actor_zits = {}
    for m in re.finditer(r"\$Actor:\s*\{([^}]*)\}", content):
      block = m.group(1)
      name_m = re.search(r"\$name:\s*\$?(\w+)", block)
      if not name_m:
        continue
      zit_fields = re.findall(r"\$zit\d+\s*:\s*&[0-9A-Fa-f]+", block)
      if zit_fields:
        existing_actor_zits[name_m.group(1)] = " ".join(zit_fields)

    # 1. Eliminar todos los bloques de actores existentes para evitar duplicados o desorden
    content = re.sub(r"\$Actor:\s*\{[^}]*?\}\s*", "", content)

    # 2. Generar la lista ordenada de nuevos actores con sangría fija de 9 espacios
    new_actors_lines = []
    sangria = "         "  # 9 espacios de indentación exacta

    # Recopilar jugadores activos
    active_players = 0
    for i in range(5):
      val = self.cmb_players[i].get()
      if val != EMPTY_SLOT:
        active_players = i + 1
        char_id = [k for k, v in CHARACTERS_STORY.items() if v == val][0]
        char_hex = f"{int(char_id):04X}"

        # Si en la pestaña "Cambiar Personaje a DLC" hay un personaje DLC
        # seleccionado para este slot, tiene prioridad sobre la lista normal.
        if hasattr(self, "cmb_dlc_players"):
          dlc_val = self.cmb_dlc_players[i].get()
          if dlc_val == DLC_KEEP_ORIGINAL:
            orig_dec = self.original_actor_char.get(f"pla{i}")
            if orig_dec is not None:
              char_hex = f"{int(orig_dec):04X}"
          elif dlc_val and dlc_val != DLC_EMPTY_SLOT:
            dlc_matches = [
                k for k, v in DLC_CHARACTERS_STORY.items() if v == dlc_val
            ]
            if dlc_matches:
              char_hex = f"{int(dlc_matches[0]):04X}"

        cost_val = self.cmb_player_costumes[i].get()
        cost_id = [k for k, v in COSTUMES.items() if v == cost_val][0]
        dmg_val = self.chk_player_dmg[i].get()
        hp_val = self.ent_player_hp[i].get().strip() or "30000"
        ia_val = self.ent_player_ia[i].get().strip() or "0"
        zit_block = existing_actor_zits.get(f"pla{i}", "$zit8: &00000089")

        actor_str = f"{sangria}$Actor:{{$name:$pla{i} $chr: &{char_hex} $ctm: {cost_id} $dmg: {dmg_val} $ia: {ia_val} {zit_block} $hp: {hp_val}}}"
        new_actors_lines.append(actor_str)

    # Recopilar rivales CPU activos
    active_cpus = 0
    for i in range(5):
      val = self.cmb_cpus[i].get()
      if val != EMPTY_SLOT:
        active_cpus = i + 1
        char_id = [k for k, v in CHARACTERS_STORY.items() if v == val][0]
        char_hex = f"{int(char_id):04X}"

        # Igual que en jugadores: la selección DLC tiene prioridad.
        if hasattr(self, "cmb_dlc_cpus"):
          dlc_val = self.cmb_dlc_cpus[i].get()
          if dlc_val == DLC_KEEP_ORIGINAL:
            orig_dec = self.original_actor_char.get(f"cpu{i}")
            if orig_dec is not None:
              char_hex = f"{int(orig_dec):04X}"
          elif dlc_val and dlc_val != DLC_EMPTY_SLOT:
            dlc_matches = [
                k for k, v in DLC_CHARACTERS_STORY.items() if v == dlc_val
            ]
            if dlc_matches:
              char_hex = f"{int(dlc_matches[0]):04X}"

        cost_val = self.cmb_cpu_costumes[i].get()
        cost_id = [k for k, v in COSTUMES.items() if v == cost_val][0]
        dmg_val = self.chk_cpu_dmg[i].get()
        hp_val = self.ent_cpu_hp[i].get().strip() or "30000"
        ia_val = self.ent_cpu_ia[i].get().strip() or "9"
        zit_block = existing_actor_zits.get(f"cpu{i}", "$zit8: &00000089")

        actor_str = f"{sangria}$Actor:{{$name:$cpu{i} $chr: &{char_hex} $ctm: {cost_id} $dmg: {dmg_val} $ia: {ia_val} {zit_block} $hp: {hp_val}}}"
        new_actors_lines.append(actor_str)

    # Actualizar los conteos en las líneas de $Role si existen
    content = re.sub(r"(\$Role:\s*\{\s*\$type:\s*0,\s*\$count:\s*)\d+", rf"\g<1>{active_players}", content)
    content = re.sub(r"(\$Role:\s*\{\s*\$type:\s*1,\s*\$count:\s*)\d+", rf"\g<1>{active_cpus}", content)

    # 3. Insertar los actores ordenados justo después de la última línea de $Role o de $Setting
    actors_block = "\n" + "\n".join(new_actors_lines) + "\n"
    
    role_matches = list(re.finditer(r"\$Role:\s*\{[^}]*\}", content))
    if role_matches:
      last_role_end = role_matches[-1].end()
      content = content[:last_role_end] + actors_block + content[last_role_end:]
    else:
      setting_match = re.search(r"\$Setting:\s*\{[^}]*\}", content)
      if setting_match:
        pos = setting_match.end()
        content = content[:pos] + actors_block + content[pos:]

    return content

  def save_file(self):
    content = self.process_updated_content()
    if content is None:
      return

    if self.file_path:
      try:
        with open(self.file_path, "w", encoding="utf-8", newline="") as f:
          f.write(content)
        self.file_content = content
        self.refresh_zit_table()
        messagebox.showinfo(
            "Éxito", "Los cambios han sido guardados correctamente."
        )
      except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    else:
      self.save_file_as()

  def save_file_as(self):
    content = self.process_updated_content()
    if content is None:
      return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[
            ("Archivos JSON", "*.json"),
            ("Archivos GSCF", "*.GSCF"),
            ("Todos los Archivos", "*.GSCF *.gsc"),
        ],
    )

    if save_path:
      try:
        with open(save_path, "w", encoding="utf-8", newline="") as f:
          f.write(content)
        self.file_path = save_path
        self.file_content = content
        self.lbl_file.config(
            text=f"Archivo cargado: {os.path.basename(save_path)}"
        )
        self.refresh_zit_table()
        messagebox.showinfo(
            "Éxito", "El archivo se guardó en la ubicación elegida."
        )
      except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")


# ============================================================================
# ICONO EMBEBIDO (BT3_no_green.ico)
# El icono vive DENTRO de este script (multi-tamaño 16-256 px, en base64).
# No depende de ningún .ico externo, ni al ejecutar el .py ni en el .exe
# compilado con PyInstaller / GitHub Actions.
# ============================================================================
APP_ICON_ICO_B64 = """
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
qy8EUkrAm2jelQm3vz4J56XvqW/144SUKGLC45AqAoWQFmN251yWnnQ6c2bNY9eubrZv30kykWT2rJl0TZlKOBZCM1RQPKR0kNLF
Ew6WV6FYHWVwYJhKtUiyszTsh/MXDoz0b6nUbH1obw7Pr85Q3OhxumKeghWZE5aNzWEloZVl1i/pe36SmeZf49f0oVy2wn8tX/Wm
5DZS2EDFKpKOtOM6Pvt2jXLE0ckkTEpUGTp6fLh81O4tvQs2bdi+dPVjz8cGesZoTkyiq20mCbMR6aqoik4qk6DECE+vX83SY5cx
fUYnv175c6bOy5T++eoPXORa3FtyBulI/uVjAt7WBuAlDjVD8Hp8/ttnYytjplntuj6hdP7PTCaGFpJs27knO5DbfV4haz329B2j
LPucmdyxrjivMMjpXsk4TbeT85JmezIdaSMSSoIQVGs1xkvjjJWyFCpjlJ0ijletz0H/o4a+3sJLIamnfaj7/lIIkD5SutR9CWVi
3MHL7sLLAcD6H359fp4UCClAquCDgoaphjmsYzZ/v3gph8+dz9h4ju69e8H3iUdjaIZKNB2iaVKcREZF6jZSsfD0Ep5WoFq1GNxT
ZHjfmFsqlYZ8xfGkBK+qEFJDmagZi+qqgYKBK13Gvb0jOXZ/w2nZuzxhTS7nB2vc+ct1b4mMsvIxvFIGlwIxvQlDiTCwb5iurs5Y
0elZOpZ1Ttq2qfusVQ892/X809tM1Yowr+tImpOTEa5BLBlh1O5j++6tnHL8aXihMr9bcxdf+fYV9045TFw0UqiWpiT/smDg67n/
gQF4m/Kl//M+qlVJyclnYnbnL1vj00/LtOuUqxW2bN21Olvo/UhUb9gTbXJY+/gm9jyps/QTZrJ7c26eWwgtKY44R5uycWFca2pN
mZPMeKiZkBEHBapOiVxphFxpjHKthGVXsJwKnudi+w6OdKhrfr1r4FP//dKmyHoHoN4jqI8HgHq3QCJQhYYqNAw9hKEZxMIpwmaE
aChKLJQgrEfRVZ1MSwOz584kFokzNDzE+HiWSEqloTVKvFFHj9gIzQbNw1ccpGIhVRtfOpRGXfK9YOU1pK3j2wLhCvAlnmpT8AcZ
d7tXlZT+a81b168Sn5yPQOfn33/ubyq34dx6XFkjGkqQCM3FZ1N72VJO2r5p8ENPPvrcKY899HSsmpMsmnMSzYkOQhGDgeIeevb2
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
"""


def get_app_icon_bytes():
  """Bytes del archivo .ico embebido."""
  return base64.b64decode("".join(APP_ICON_ICO_B64.split()))


def export_app_icon(path):
  """Escribe el .ico embebido en 'path' (util para el build: --export-icon)."""
  with open(path, "wb") as f:
    f.write(get_app_icon_bytes())
  return path


def _largest_png_from_ico(ico_bytes):
  """Devuelve los bytes PNG del frame mas grande del .ico (para iconphoto)."""
  try:
    count = struct.unpack("<H", ico_bytes[4:6])[0]
    best = None
    for i in range(count):
      w, h, _c, _r, _p, _b, size, off = struct.unpack(
          "<BBBBHHII", ico_bytes[6 + 16 * i: 22 + 16 * i]
      )
      w = w or 256
      chunk = ico_bytes[off: off + size]
      if chunk[:8] == b"\x89PNG\r\n\x1a\n" and (best is None or w > best[0]):
        best = (w, chunk)
    return best[1] if best else None
  except Exception:
    return None


def apply_embedded_icon(root):
  """Aplica el icono embebido a la ventana principal y a las secundarias."""
  ico_bytes = get_app_icon_bytes()

  # Windows: que la barra de tareas use NUESTRO icono y no el de python.exe
  try:
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "CEDAJ.SparkingStoryBuilder"
    )
  except Exception:
    pass

  # 1) .ico multi-tamano (titulo, barra de tareas, Alt+Tab) -> nitido en
  #    todos los tamanos. Tk necesita un archivo, se escribe uno temporal.
  try:
    import tempfile
    tmp_dir = tempfile.mkdtemp(prefix="sparkingsb_")
    ico_path = os.path.join(tmp_dir, "app_icon.ico")
    with open(ico_path, "wb") as f:
      f.write(ico_bytes)
    root.iconbitmap(default=ico_path)
    root._app_icon_path = ico_path
  except Exception:
    pass

  # 2) Respaldo / otros sistemas: PhotoImage del frame mas grande (256 px)
  try:
    png = _largest_png_from_ico(ico_bytes)
    if png:
      img = tk.PhotoImage(data=base64.b64encode(png))
      root.iconphoto(True, img)
      root._app_icon_ref = img  # evita que el GC lo elimine
  except Exception:
    pass


if __name__ == "__main__":
  # Uso en el build:  python script.py --export-icon BT3_no_green.ico
  if len(sys.argv) >= 3 and sys.argv[1] == "--export-icon":
    export_app_icon(sys.argv[2])
    print("Icono exportado en:", sys.argv[2])
    sys.exit(0)
  try:
    root = tk.Tk()
    apply_embedded_icon(root)
    app = BT3CombinedEditor(root)
    root.mainloop()
  except Exception as e:
    import traceback

    print("Error crítico al iniciar la aplicación:")
    traceback.print_exc()
    input("Presiona Enter para salir...")