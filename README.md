
![image](https://github.com/user-attachments/assets/80df962c-52ca-496f-84d6-1f1db3b9e9f3)

Se añaden librerias con el fin de poder realizar de manera más sencilla cálculos matemáticos, también para graficar señales, procesarlas y se utiliza una libreria aparte 'wfdb', la cual nos ayuda a leer los archivos de la señal fisiologica descargada previamente en physionet, por úlimo la libreria 'pandas' para manejar datos en formato tabla y guardarlos en archivo CSV.

![image](https://github.com/user-attachments/assets/3f1330c3-ec44-40e0-bd02-b84bbfb3351e)

Utilizando la función wfdb.rdrecord(datos). Lo que hace es abrir el archivo especificado por el nombre que se le pasa como argumento (datos) y devuelve un objeto llamado record. Dentro de este objeto, record.p_signal contiene los datos de la señal; al poner [:, 0], estamos seleccionando solo el primer canal de la señal, con esto nos retorna la señal (senal) y el objeto (record), los cuales traen la información para poder usarse.


![image](https://github.com/user-attachments/assets/48347ca2-b573-47c0-b1fd-9dc1cf113237)

Se define una función que recibe varios parámetros como el 'inicio' desde donde se comenzará a graficar la señal hasta la 'duración' de estos puntos, con esto podemos analizar diferentes segmentos de la señal y modificarlo a nuestro interés. De igual manera se nombran ejes, cuadricula y colores. Esta misma es utilizada para graficar las demás señales contaminadas lo cual facilita su comparación.

![image](https://github.com/user-attachments/assets/8d61e777-8ece-400e-9d36-c3e420274c4f)

Primero, se obtiene la media sumando todos los valores de la señal '(np.sum(senal))' y dividiéndolos por el número total de muestras '(len(senal))'. Luego, para la desviación estándar, se calcula cuánto se desvían los valores individuales de la media: se resta la media de cada valor, se eleva al cuadrado, se promedia y finalmente se saca la raíz cuadrada para obtener la medida de dispersión. Por último, el coeficiente de variación nos muestra qué tan grande es la desviación en relación con la media.

![image](https://github.com/user-attachments/assets/e3aeca58-7603-401e-aa71-ebb33ecb4864)

Se ingresan los datos numéricos que representa la señal fisiológica, para calcular el valor promedio de la señal y su 'desviación estándar' en la cual se mide cuanto varían los datos respecto a la 'media' en donde valor alto indica que los datos están muy dispersos, mientras que un valor bajo indica que los datos están más agrupados cerca de la media para luego calcular el 'coeficiente de variación' que mide la variabilidad de la señal en relación con su medio para poder comparar y analizar estos tres valores


![image](https://github.com/user-attachments/assets/94dded00-71dc-4035-b789-73eeb26d1b14)

Se utiliza una función mas precisa para la PDF (probabilidad de función)  para la grafica del histograma con la cual se calcula la media y desviación de la señal con una variable alta para que su tiempo de muestreo sea mas preciso   

![image](https://github.com/user-attachments/assets/5a10f00b-6482-48e8-ba35-89eae386f996) 

El SNR mide qué tan fuerte es la señal en comparación con el ruido. Por lo cual se calcula la potencia de la señal (energía total de la señal) y la potencia del ruido, siendo estos la media de los valores al cuadrado '(np.mean(senal**2))','(np.mean(ruido**2))'. Luego, aplicamos la fórmula '10 * np.log10(potencia_senal / potencia_ruido)', que convierte esta relación en decibeles (dB) para medir la calidad de la señal. De acuerdo a su valor se puede deducir que tan clara o fuerte es la señal correspondiente.

![image](https://github.com/user-attachments/assets/95a662cc-6067-4450-a5c2-bf1a6c8802ac)
blablablablablabla

![image](https://github.com/user-attachments/assets/654df77f-6517-4641-bcc2-1501dbdc783d)
blablablablablablablablabla

![image](https://github.com/user-attachments/assets/fef9fa80-d53a-4580-b02c-089b3913f4b7)

En este apartado primero definimos 'colores', para asignarle un color diferente a cada tipo de ruido. El (for) recorre los tres tipos de ruido y los agrega a la señal usando la función ya antes definida 'contaminar_con_ruido(senal, tipo)'. Luego la nueva señal ruidosa se grafica llamando a la función ya antes definida de 'graficar_senal(...)' (recordando que usamos la misma función para poder compararlas y acortar codigo) en la cual tambien podemos seleccionar que tamaño de datos queremos para su analisís, y se imprime el valor de SNR en decibeles.

![image](https://github.com/user-attachments/assets/812736fe-152b-43be-b89b-b4d6b22e0f61)
blablablabla

![image](https://github.com/user-attachments/assets/db7da50a-777f-4bba-8adf-99808f6f25ae)
![image](https://github.com/user-attachments/assets/fd143544-41c7-4997-a5bc-2cc71cafb474)
![image](https://github.com/user-attachments/assets/f4621f06-1587-4de0-b1eb-c4ee30340df7)
![image](https://github.com/user-attachments/assets/dab18c8b-66c0-4b67-9a35-9175a8c24ea8)
![image](https://github.com/user-attachments/assets/986c9b20-fd1a-46cf-b510-c37318d71ba8)


Media: -0.024002000000000002 (manual) vs -0.024002000000000002 (numpy)
Desviación estándar: 0.12935114609465198 (manual) vs 0.12935114609465198 (numpy)
Coef. Variación: -5.3891819887781 (manual) vs -5.3891819887781 (numpy)
SNR con ruido gaussiano: 20.104351664394343 dB
SNR con ruido impulso: -3.5950777316690354 dB
SNR con ruido artefacto: 23.157751096132063 dB
Resultados guardados en 'resultados_laboratorio.csv'.
