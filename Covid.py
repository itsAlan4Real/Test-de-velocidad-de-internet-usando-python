# importing tkinter
from tkinter import *
# initializando tkinter
root = Tk()
# Tamaño de ventana
root.geometry("350x350")
# Titulo de ventana
root.title("Estadisticas sobre el Covid-19")

# funcion para obtener los datos del Covid
def showdata():
    # importando matplotlib
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    # initializando libreria covid
    covid = Covid()
    # declarando vacios cada arreglo de datos
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:

        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        # For para obtener los datos de todos los países
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        # for para obtener los datos de un país
        for y in cases:
            confirmed.append(y["confirmed"])
            print(str(confirmed))
            active.append(y["active"])
            print(str(active))
            deaths.append(y["deaths"])
            print(str(deaths))
            recovered.append(y["recovered"])
        # Colores de la grafica
        confirmed_patch = mpatches.Patch(color='yellow', label='confirmados')
        recovered_patch = mpatches.Patch(color='red', label='recuperados')
        active_patch = mpatches.Patch(color='blue', label='activos')
        deaths_patch = mpatches.Patch(color='black', label='muertes')
        # Leyenda de la grafica
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='yellow')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='red')
                plt.bar(country_names[x], active[x], color='blue')
            else:
                plt.bar(country_names[x], active[x], color='blue')
                plt.bar(country_names[x], recovered[x], color='red')
            plt.bar(country_names[x], deaths[x], color='black')
        # Titulo de la grafica
        plt.title('Casos actuales de Covid')
        # Eje X
        plt.xlabel('País')
        # Eje Y
        plt.ylabel('Casos en millones')
        # Mostrar grafica
        plt.show()
    except Exception as e:
        data.set("Escribe bien el nombre del país en ingles")


Label(root, text="Escribe los paises\nde donde te interesan los datos sobre el\ncovid-19 ", font="Consolas 15 bold").pack()
Label(root, text="Escribe el país aquí:").pack()
data = StringVar()
data.set("País en Ingles")
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Get Data", command=showdata).pack()
root.mainloop()
