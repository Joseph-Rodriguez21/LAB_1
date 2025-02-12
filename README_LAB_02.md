                                                    INFORME LABORATORIO 2 CONVOLUCIÓN Y CORRELACIÓN 
                                                             FELIPE TORRES 5600825
                                                             YADER ORTIZ   5600782
                                                             JOSEPH RODRIGUEZ 5600835

                 PRIMERA PARTE (A)
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/f3c8b298-402a-4acb-800c-add117427036)

Para empezar a definir el codigo de este laboratorio, vamos a llamar estas librerias ya vistas en la anterior práctica para poder graficar y realizar las diferentes operaciones que nos exige el ejercicio, en este caso la convolución.
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/5695277b-239f-4baa-9879-96ae51555c8c)

Ahora de acuerdo al ejercicio vamos a definir dos arreglos, en este caso 'j' y 'r' representando señales discretas respectivamente y en las cuales agregamos primero el código del primer estudiante (Joseph Rodriguez) (5600835) y su cédula en el otro arreglo (1076242362), el objetivo de esto es realizar la convolución entre estos dos arreglos mediando la función 'np.convolve(j, r)' el cual calcula la convolución discreta entre 'j' y 'r'.
Por otro lado se genera un arreglo 'y_nj' con valores desde 0 hasta 'len(y1)-1', que representa el eje n para graficar. Y por último se imprime el resultado de esta convolución 'y1' para que se refleje en la consola al ejecutar el código.
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/e16c8f89-7a2a-40b5-982a-8c7599fd0132)

Se genera un gráfico de stem plot (de tipo palos), el cual es el más ideal para representar las señales discretas presentes en la práctica. De igual manera agregamos ejes, titulos y una cuadricula para su mejor analisís.
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/fe7c727b-4e84-4da9-afcd-f61013be1ee9)

Ahora aplicamos lo explicado anteriormente con los demás datos de los integrantes del grupo, en este caso (Felipe Torres) y (Yader Ortiz) con sus datos respectivos, mismo concepto del uso de la función y misma forma para graficar, de tal manera obtenemos las siguientes gráficas y su convolución impresa en la consola:
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/af537f3a-0bca-4d95-98ff-e73d377c7060)

Resultado gráfica convolución Joseph Rodriguez 
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/a523b097-cc1a-43f9-872d-ac0a7393f496)

Resultado gráfica convolución Felipe Torres 
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/db8f4cd3-ea31-4a1e-a3d5-a5354bf7d15d)

Resultado gráfica convolución Yader Ortiz
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/9533c770-1cff-4833-b514-3244af135ac2)

Resultado datos convolución reflejados en la consola de py.

___________________________________________________________________________________________________________________________

Ahora comparamos con las convoluciones realizadas manualmente, en este orden de ideas obtenemos la siguiente tabla por cada estudiante y su respectiva gráfica hecha a mano:
___________________________________________________________________________________________________________________________

Joseph Rodriguez 

![Imagen de WhatsApp 2025-02-11 a las 20 47 23_66dc3fff](https://github.com/user-attachments/assets/51b9521e-2943-4889-a0a0-47826662b21b)
![Imagen de WhatsApp 2025-02-11 a las 21 02 49_dd65efd8](https://github.com/user-attachments/assets/8bf23f20-e8e8-473d-a794-0744e6f35d6a)
___________________________________________________________________________________________________________________________

Yader Ortiz 

![Imagen de WhatsApp 2025-02-11 a las 21 27 00_60fc6128](https://github.com/user-attachments/assets/33098a0a-db66-4da6-a60e-2a2cc8f86be2)
![Imagen de WhatsApp 2025-02-11 a las 21 27 09_3c3c1ca7](https://github.com/user-attachments/assets/3d4ee2a7-5fb6-48e0-a84b-b119e329405f)
___________________________________________________________________________________________________________________________
Felipe Torres 

![image](https://github.com/user-attachments/assets/d870b71e-2c4c-44ea-8624-2bbea483c921)
![image](https://github.com/user-attachments/assets/12b210db-683f-4e3e-a36b-6aeadb66eff0)

___________________________________________________________________________________________________________________________


                                                                           SEGUNDA PARTE (B) 
                                                                           
![image](https://github.com/user-attachments/assets/8e3f2a6b-0170-41cc-a86b-4dd8ccef8073)

Ahora para el desarrollo de esta segunda de la práctica vamos a definir el periodo de muestreo 'Ts=1,25 ms' el cual ya esta previamente establecido en la guia de laboratorio, luego por medio de 'n = np.arange(9)' se crea un vector de tiempo discreto con valores de 0 a 8, representando los instantes en los que se evalúan las señales, de igual manera ya previamente establecido en la guia de laboratorio como "𝑝𝑎𝑟𝑎 0 ≤ 𝑛 < 9".

___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/10110a3a-e8ff-4f2e-b633-f2718cb201da)

Ahora definimos las señales establecidas en la guia de laboratorio, tales como "x1 = cos(2𝜋100𝑛𝑇𝑠)" y "x2 = sin(2𝜋100𝑛𝑇𝑠)", las cuales son señales que poseen una misma frecuencia de 100 Hz y estan evaluadas en los instantes 'n * Ts'

Luego por medio de la función 'np.correlate(x1, x2, mode='full')' Se calcula la correlación cruzada entre x1 y x2. (definidos anteriormente) esta correlación nos ayuda a medir la similitud entre estas dos señales a diferentes desplazamientos. Y por medio de la función 'lag = np.arange(-len(x1) + 1, len(x1))' Se crea un vector que representa los desplazamientos posibles en la correlación. Esto es sencillo pues si encontramos algo similar en los desplazamientos de x1 y x2, entonces la correlación tendra un valor alto en ese punto, pero de lo contrario (como en este caso), estas dos señales estan desfasadas 90°, entonces la correlación mostrara este desfase.
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/3209bd9b-e7a6-48e0-b021-27a4ff0c7b7d)

Ahora creamos una figura para incluir las tres gráficas, siendo estas la de las señales por separado y la última su correlacióm. 
Allí utilizamos 'stem()' para graficar la señal como una secuencia discreta de puntos, tambien se cambia el color de sus puntos y lineas corrientes, por último ejes y una cuadricula, esto en ambas gráficas.

___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/2fda55b1-ba33-40f0-a523-bbebcc4cfa36)

Acá añadimos el tercer subgráfico para representar y reflejar la correlación de las dos señales previas. Se llama a 'lag' el cuañ ya definimos anteriormente como aquel que representa el desplazamiento de una señal con la otra, al igual que con 'correlation' que muestra la similitud entre ambas señales y su desplazamiento. Ya por último declaramos los ejes, titulos y se muestra la figuro con estos tres subgraficos, de la siguiente manera:

![image](https://github.com/user-attachments/assets/3c3db6b0-73bd-43fe-a290-1a1eb4e97829)

___________________________________________________________________________________________________________________________

                                     TERCERA PARTE (C)
                                     
![image](https://github.com/user-attachments/assets/836aa702-8cc1-45e4-a647-10bbe5f00892)

Para desarrollar el punto C, se incorporan diversas librerías usadas anteriormente en el laboratorio 1, ya que facilitan los cálculos matemáticos, la visualización y el procesamiento de señales. Además, se emplea la librería 'wfdb', que permite leer los archivos de la señal fisiológica previamente descargada desde PhysioNet.

___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/ce75fe83-2a0b-4707-99f2-491367ef0149)

Los datos de la señal fisiológica provienen de una base de datos de EMG. Para acceder a ellos se utiliza la función wfdb.rdrecord(datos) que abre el archivo cuyo nombre se proporciona como argumento (datos) y devuelve un objeto denominado record, Dentro de este objeto record.p_signal almacena los valores de la señal y al seleccionar [:, 0] se extrae únicamente el primer canal de la misma. Además record.fs contiene la frecuencia de muestreo que indica cuántas muestras por segundo se han tomado. Como resultado la función devuelve la señal (senal) y su frecuencia de muestreo (fs), brindando la información necesaria para su procesamiento.
___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/b8b69978-70ba-4e6c-af25-7ee37d919825)

Esta función calcula y devuelve los resultados de la señal que son 
Media que es el (valor promedio de la señal)
Desviación estándar muestra (qué tanto varían los valores)
Mediana (valor central de la señal)
Duración de la señal en segundos y su frecuencia de muestreo.

___________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/b4df0bbb-2ccb-4c43-a489-2cb515eadd48)

Esta función la usamos para que nos muestre una descripción de la señal que se va a usar
___________________________________________________________________________________________________________________________
![image](https://github.com/user-attachments/assets/65f48595-441e-4e57-9e9d-b0629bb9105b)

Calcula la Transformada Rápida de Fourier (FFT) de la señal para analizar su contenido en el dominio de la frecuencia donde N representa el número total de puntos en la señal luego se divide por N para normalizar los valores y evitar escalamiento en la magnitud generando el eje de frecuencias en función del número de muestras y la frecuencia de muestreo, además se toman los valores positivos ya que los negativos no aportan información nueva 
___________________________________________________________________________________________________________________________
![image](https://github.com/user-attachments/assets/99980d53-b8c7-4002-bf4d-2f615adc273c)

Esta función se encarga de representar gráficamente la señal en función del tiempo en donde se obtiene el numero total de las muestras y se obtiene el tiempo en (s) para cada muestra, configurando el tamaño de la grafica y agregándole etiquetas como color y nombre del eje X y Y
___________________________________________________________________________________________________________________________
