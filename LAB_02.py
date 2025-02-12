import numpy as np
import matplotlib.pyplot as plt

#DATOS JOSEPH RODRIGUEZ
j = np.array([5,6,0,0,8,3,5])
r = np.array([1,0,7,6,2,4,2,3,6,2])

y1 = np.convolve(j, r)
y_nj = np.arange(len(y1))
print("JOSEPH y[n] =", y1)

plt.stem(y_nj, y1)
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Convolución de j[n] y r[n] (JOSEPH RODRIGUEZ)")
plt.grid()
plt.show()

#DATOS FELIPE TORRES 
f = np.array([5,6,0,0,8,2,5])
t = np.array([1,0,1,2,3,4,1,6,6,7])

y2 = np.convolve(f, t)
y_nf = np.arange(len(y2))
print("FELIPE y[n] =", y2)

plt.stem(y_nf, y2)
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Convolución de f[n] y t[n] (FELIPE TORRES)")
plt.grid()
plt.show()

#DATOS EEEE YEEEIDER ORTIZ
y = np.array([5,6,0,0,7,8,2])
o = np.array([1,0,6,9,2,8,2,0,4,8])

y3 = np.convolve(y, o)
y_ny = np.arange(len(y3))
print("YADER  y[n] =", y3)

plt.stem(y_ny, y3)
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Convolución de y[n] y o[n] (YADER ORTIZ)")
plt.grid()
plt.show()


#SEGUNDA PARTE LABORATORIO 


# Parámetros
fs = 1000  # Frecuencia de muestreo (Hz)
Ts = 1.25e-3  # Período de muestreo (s)
n = np.arange(9)  # Vector de tiempo discreto

# Señales
x1 = np.cos(2 * np.pi * 100 * n * Ts)
x2 = np.sin(2 * np.pi * 100 * n * Ts)

# Cálculo de la correlación
correlation = np.correlate(x1, x2, mode='full')
lag = np.arange(-len(x1) + 1, len(x1))

# Crear figura con tres subgráficos
plt.figure(figsize=(10, 7))

# Gráfica de x1[n]
plt.subplot(3, 1, 1)
plt.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.title('Señal x1[n] = cos(2π100nTs)')
plt.grid()

# Gráfica de x2[n]
plt.subplot(3, 1, 2)
plt.stem(n, x2, linefmt='g-', markerfmt='go', basefmt='k-')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.title('Señal x2[n] = sin(2π100nTs)')
plt.grid()

# Gráfica de la correlación
plt.subplot(3, 1, 3)
plt.stem(lag, correlation, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.xlabel('Desplazamiento')
plt.ylabel('Correlación')
plt.title('Correlación entre x1[n] y x2[n]')
plt.grid()

# Mostrar la figura
plt.tight_layout()
plt.show()

# TERCERA PARTE LABORATORIO (C)

import numpy as np
import matplotlib.pyplot as plt
import wfdb
import scipy.stats as stats
import scipy.signal as signal

def descargar_senal_desde_archivo(datos):
    record = wfdb.rdrecord(datos)
    senal = record.p_signal[:, 0]  # Tomar el primer canal
    fs = record.fs  # Frecuencia de muestreo
    return senal, fs

def caracterizar_senal(senal, fs):
    media = np.mean(senal)
    desviacion = np.std(senal)
    mediana = np.median(senal)
    duracion = len(senal) / fs
    return media, desviacion, mediana, duracion

def describir_clasificacion():
    return "La señal es una señal electromiográfica (EMG), utilizada para medir la actividad eléctrica de los músculos."

def aplicar_transformada_fourier(senal, fs):
    
    N = len(senal)
    espectro = np.fft.fft(senal) / N  # Normalizar
    freqs = np.fft.fftfreq(N, d=1/fs)
    return freqs[:N//2], np.abs(espectro[:N//2])  # Solo valores positivos

def graficar_senal(senal, fs, alpha=0.7, titulo="Señal Fisiológica", color="purple"):
    tiempo = np.arange(len(senal)) / fs
    plt.figure(figsize=(10, 4))
    plt.plot(tiempo, senal, color=color, label=titulo)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    plt.show()

def graficar_transformada(freqs, espectro):
    plt.figure(figsize=(10, 4))
    plt.plot(freqs, espectro, color='red', label='Espectro de Fourier')
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Magnitud")
    plt.yscale("log")  # Escala logarítmica para mejor visualización
    plt.title("Transformada de Fourier de la Señal EMG")
    plt.grid(True)
    plt.legend()
    plt.show()

def graficar_densidad_espectral(senal, fs):
    freqs, psd = signal.welch(senal, fs, nperseg=1024)
    plt.figure(figsize=(10, 4))
    plt.semilogy(freqs, psd, color='blue', label='Densidad Espectral de Potencia')
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Densidad de Potencia [V²/Hz]")
    plt.title("Densidad Espectral de Potencia de la Señal EMG")
    plt.grid(True)
    plt.legend()
    plt.show()
    return freqs, psd

def graficar_histograma(senal):
    plt.figure(figsize=(10, 6))
    
    count, bins, _ = plt.hist(senal, bins='auto', density=True, alpha=0.7, color='brown', label='Histograma')

    # Calcular media y desviación estándar de la señal
    media, desviacion = np.mean(senal), np.std(senal)

    # Estimar densidad con KDE
    kde = stats.gaussian_kde(senal)
    x_vals = np.linspace(min(senal), max(senal), 1000)
    pdf_kde = kde(x_vals)  # Densidad estimada

    # Graficar la densidad estimada
    plt.plot(x_vals, pdf_kde, 'r-', label='PDF Estimada (KDE)', linewidth=2)


    plt.title("Histograma de la Señal con Función de Probabilidad")
    plt.xlabel("Amplitud")
    plt.ylabel("Densidad de Probabilidad")
    plt.grid(True)
    plt.legend()
    plt.show()

# Código principal
nombre_base = "session1_participant1_gesture10_trial1"
senal, fs = descargar_senal_desde_archivo(nombre_base)

graficar_senal(senal, fs)

media, desviacion, mediana, duracion = caracterizar_senal(senal, fs)
print(f"Media: {media}")
print(f"Desviación estándar: {desviacion}")
print(f"Mediana: {mediana}")
print(f"Duración de la señal: {duracion} segundos")
print(describir_clasificacion())

freqs, espectro = aplicar_transformada_fourier(senal, fs)
graficar_transformada(freqs, espectro)
graficar_densidad_espectral(senal, fs)  # Se agrega la gráfica de densidad espectral
graficar_histograma(senal)
