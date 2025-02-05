import numpy as np
import matplotlib.pyplot as plt
import wfdb
import scipy.stats as stats
import scipy.signal as signal

def descargar_senal_desde_archivo(datos):
    record = wfdb.rdrecord(datos)
    senal = record.p_signal[:, 0]  # Tomar el primer canal
    return senal, record

def graficar_senal(senal, inicio=0, duracion=2000, titulo="Señal Fisiológica", color="purple"):
    plt.figure(figsize=(10, 4))
    plt.plot(senal[inicio:inicio+duracion], color=color, label=titulo)
    plt.xlabel("Muestras")
    plt.ylabel("Amplitud")
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    plt.show()

def estadisticos_manual(senal):
    media = np.sum(senal) / len(senal)
    desviacion = np.sqrt(np.sum((senal - media)**2) / len(senal))
    coef_variacion = desviacion / media
    return media, desviacion, coef_variacion
                  
def estadisticos_numpy(senal):
    media = np.mean(senal)
    desviacion = np.std(senal)
    coef_variacion = desviacion / media
    return media, desviacion, coef_variacion

def graficar_histograma(senal):
    plt.figure(figsize=(10, 6))
    
    # Histograma normalizado
    count, bins, _ = plt.hist(senal, bins='auto', density=True, alpha=0.7, color='brown', label='Histograma')
    # Calcular media y desviación estándar de la señal
    media, desviacion = np.mean(senal), np.std(senal)
    # Estimar densidad con KDE (mejor ajuste en lugar de distribución normal)
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

def calcular_snr(senal, ruido):
    potencia_senal = np.mean(senal**2)
    potencia_ruido = np.mean(ruido**2)
    return 10 * np.log10(potencia_senal / potencia_ruido)

def contaminar_con_ruido(senal, tipo="gaussiano", nivel=0.1):
    if tipo == "gaussiano":
        ruido = np.random.normal(0, nivel * np.std(senal), len(senal))
    elif tipo == "impulso":
        ruido = np.zeros_like(senal)
        indices = np.random.choice(len(senal), int(0.05 * len(senal)), replace=False)
        ruido[indices] = np.random.choice([-1, 1], size=len(indices)) * np.max(senal)
    elif tipo == "artefacto":
        ruido = np.sin(2 * np.pi * 100 * np.linspace(0, 1, len(senal))) * nivel * np.std(senal)
    else:
        raise ValueError("Tipo de ruido no soportado")
    
    senal_ruidosa = senal + ruido
    snr = calcular_snr(senal, ruido)
    return senal_ruidosa, snr



# Código principal
nombre_base = "rec_1"  # Nombre del archivo sin extensión
senal, record = descargar_senal_desde_archivo(nombre_base)
graficar_senal(senal)

media_manual, desv_manual, coef_var_manual = estadisticos_manual(senal)
media_numpy, desv_numpy, coef_var_numpy = estadisticos_numpy(senal)

print(f"Media: {media_manual} (manual) vs {media_numpy} (numpy)")
print(f"Desviación estándar: {desv_manual} (manual) vs {desv_numpy} (numpy)")
print(f"Coef. Variación: {coef_var_manual} (manual) vs {coef_var_numpy} (numpy)")

graficar_histograma(senal)
colores = {"gaussiano": "red", "impulso": "blue", "artefacto": "orange"}

for tipo in ["gaussiano", "impulso", "artefacto"]:
    senal_ruidosa, snr = contaminar_con_ruido(senal, tipo)
    graficar_senal(senal_ruidosa, inicio=0, duracion=2000,titulo=f"Señal con Ruido {tipo.capitalize()}", color=colores[tipo])
    print(f"SNR con ruido {tipo}: {snr} dB")
    
import pandas as pd
resultados = {
    "Media Manual": media_manual,
    "Desviación Manual": desv_manual,
    "Coeficiente de Variación Manual": coef_var_manual,
    "Media Numpy": media_numpy,
    "Desviación Numpy": desv_numpy,
    "Coeficiente de Variación Numpy": coef_var_numpy,
    "SNR Ruido Gaussiano": snr
}

df_resultados = pd.DataFrame([resultados])
df_resultados.to_csv("resultados_laboratorio.csv", index=False)

print("Resultados guardados en 'resultados_laboratorio.csv'.")

   
    
