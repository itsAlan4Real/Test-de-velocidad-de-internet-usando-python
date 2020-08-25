#Instalar previamente speedtest-cli
## Ya sea de esta manera: pip install speedtest-cli o desde settings.
#Codigo
from speedtest import Speedtest
st=Speedtest()
bajada=st.download()/1024**2
subida=st.upload()/1024**2
#La velociad por defecto estara en bytes/seg, por lo que para cambiarla a mb/s solo dividimos entre 1024 al cuadrado.
print("La velocidad de descarga de tu conexion es: ", bajada, " Mb/s")
print("La velocidad de subida de tu conexion es: ", subida," Mb/s")

# Grafica, para esto instalar matplotlib e importamos a continuacion
from matplotlib import pyplot as plt
graficas=['Descarga', 'Subida']
velocidad=[bajada,subida]
plt.bar(graficas,velocidad,color='green')
plt.title('Velocidad de internet')
plt.xlabel('Tipo de conexion')
plt.ylabel('Velocidades en mb/s')
plt.show()
