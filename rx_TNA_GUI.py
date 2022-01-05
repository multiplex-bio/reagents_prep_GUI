import streamlit as st
import subprocess
import sys

st.title("Carga de Reactivos para TNA ... ")

st.write("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Extracción de TNA con Opentrons.")


is_number = False
while not is_number:
    try:
        sample_number = int(st.text_input("Número de muestras : "))

        if sample_number >= 1 and sample_number <= 94:
            st.write("*Perfecto. Vamos a trabajar con ", sample_number, "muestras.*")
            is_number = True

    except ValueError:
        st.write("\n**Debes ingresar un número entre 1 y 94**")


# Calculamos la cantidad de volumen que vamos a usar para cada reactivo
vol_total_beads = (75 * (sample_number+5))/1000 # (uL usados para cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL
vol_total_etanol = (160 * (sample_number+5))/1000 # (uL usados para lavar cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL
vol_total_etanol_sal = (160 * (sample_number+5))/1000 # (uL usados para lavar cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL
vol_total_elution_buffer = (65 * (sample_number+5))/1000 # (uL usados para lavar cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL


# If the volume we need for a reagent is lower than 3 mL, it is automatically increased to 3 mL
list_of_vols = [vol_total_beads, vol_total_etanol, vol_total_etanol_sal, vol_total_elution_buffer]
list_of_vols = [3 if vol < 3 else vol for vol in list_of_vols]


# Output del script. Indica cuanto de cada reactivo se va a usar y donde debe ser cargado
st.write("\n\n\n\n\n")
st.write('\n\n Para llevar a cabo el protocolo de Extracción ... \n')
st.write("\n\n\n\n\n")
st.write("\tDebes agregar **{} mL de BEADS** en el carril 'A1' del reservoir\n".format(list_of_vols[0]+1)) #+1 porque se vio experimentalmente que son necesarios para mejorar la precision del pipeteo

st.write("\tDebes agregar **{} mL de ETANOL** en los carriles 'A2' y 'A3' del reservoir\n".format(list_of_vols[1]))

st.write("\tDebes agregar **{} mL de ETANOL SAL** en el carril 'A4'\n".format(list_of_vols[2]))

st.write("\tDebes agregar **{} mL de AGUA ULTRA PURA** en el carril 'A5'\n".format(list_of_vols[3]))