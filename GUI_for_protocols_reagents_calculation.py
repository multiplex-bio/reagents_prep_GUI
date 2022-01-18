import streamlit as st

st.title("Selecciona el protocolo que quieres ejecutar")
protocol = st.selectbox(label = "",
             options = ["TNA", "RT", "qPCR"])

st.write("you selected : ", protocol)


# SELECCIONAMOS TNA COMO EL PROTOCOLO QUE QUEREMOS EJECUTAR
if protocol == "TNA":

    st.title("Carga de Reactivos para TNA ... ")
    st.write("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Extracción de TNA con Opentrons.")


    sample_number = st.number_input("Número de muestras a procesar *(incluye los controles)*: ",
                                    min_value= 1,
                                    max_value= 92,
                                    value = 1,
                                    )

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



elif protocol == "RT":

    st.title("Carga de Reactivos para RT ... ")
    st.write("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar la preparación de muestras para el RT con Opentrons.")

    st.write("\n1. Correr el protocolo '00_RT_prep' en la mantis")
    st.write("2. Colocar los tubos eppendorf con los controles negativos y positivos de RT:")
    st.write("\t 2.1 El control positivo se debe colocar en la posición A1 del 'eppendorf_rack' ubicado en el slot 11")
    st.write("\t 2.2 El control negativo se debe colocar en la posición D6 del 'eppendorf_rack' ubicado en el slot 11")
    st.write("Correr el protocolo 'rt_samples_distribution' en el OT-2. Debes seguir las instrucciones que la App del robot entregará")



elif protocol == "qPCR":

    st.title("Carga de Reactivos para qPCR ... ")
    st.write("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar la preparación de muestras para el RT con Opentrons.")

    st.write("Usar el programa '00_qPCR_prep_2X' en la mantis")

    st.write("\n*OJO: en la mantis sólo se deben seleccionar los wells que corresponden a la primera mitad de las replicas totales, ya que el mastermix preparado por la mantis está a una concentración de 2X.*")
    st.write("**El robot separará el mastermix 2x en las dos réplicas 1x**")

    st.write("2. Colocar los tubos eppendorf con los controles negativos y positivos de qPCR:")
    st.write("\t2.1 El control positivo se debe colocar en la posición A1 del 'eppendorf_rack' ubicado en el slot 9")
    st.write("\t 2.2 El control negativo se debe colocar en la posición D1 del 'eppendorf_rack' ubicado en el slot 9")
    st.write("Correr el protocolo 'qPCR_samples_distribution' en el OT-2. Debes seguir las instrucciones que la App del robot entregará")