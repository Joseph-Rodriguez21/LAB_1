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
    plt.hist(senal, bins=30, density=True, alpha=0.7, color='brown')
    plt.title("Histograma de la Señal")
    plt.xlabel("Amplitud")
    plt.ylabel("Frecuencia")
    plt.grid(True)
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


![image](https://github.com/user-attachments/assets/db7da50a-777f-4bba-8adf-99808f6f25ae)
![image](https://github.com/user-attachments/assets/42318341-6e23-49c5-989e-3b8bed7a910c)
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
