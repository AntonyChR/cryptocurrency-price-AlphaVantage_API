from tkinter import Tk, Button, Frame, LEFT, IntVar, Spinbox
from tkinter.ttk import Combobox
from Modules.API_parameters_values import cryptocurrencies, time_series
from Modules.data import *


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

url="https://www.alphavantage.co/query?"
APIkey = "F8EZV5KIZ5A1IJDX"

path_curr            = "./assets/digital_currency_list.csv"
path_ph              = "./assets/physical_currency_list.csv"
name_curr, code_curr = cryptocurrencies(path_curr)
name_ph, code_ph     = cryptocurrencies(path_ph)


def plot():
    #------------- indice del elemento seleccionado
    get_info(url,
            time_series[time_intervals.get()],
            code_curr[time_intervals.current()],
            code_ph[crypto_list.current()],
            APIkey
            )
            #average.get(),

    # the figure that will contain the plot
    fig = Figure(figsize = (10, 6.5), dpi = 100)
    y = [i**2 for i in range(101)]
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    plot1.plot(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = plot_frame)  
    canvas.draw()
    # placing the canvas on the Tkinter plot_frame
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, plot_frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

#---------------------------------------------------------
# the main Tkinter window
window = Tk()

# setting the title 
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("700x550")

config_frame = Frame(window)
config_frame.pack(side = LEFT)

#list that displays cryptocurrencies
crypto_list = Combobox(config_frame, text = "Cryptocurrencies")
crypto_list.pack(padx = 10, pady = 10)
crypto_list["values"] = name_curr
crypto_list.set("Bitcoin")

#list price in physical currency
Physical_currency = Combobox(config_frame, text = "currencies")
Physical_currency.pack(padx = 10, pady = 10)
Physical_currency["values"] = name_ph
Physical_currency.set("Peruvian Nuevo Sol")

#time intervals
time_intervals = Combobox(config_frame, text = "time")
time_intervals.pack(padx = 10, pady = 10)
time_intervals["values"] = list(time_series.keys())
time_intervals.set("Intraday")
#average size
average = IntVar()
average.set(5)
size_average = Spinbox(config_frame, from_=5, increment=1,to = 20, width = 21, textvariable = str(average))
size_average.pack(padx = 10, pady = 10)

# button that displays the plot
plot_button = Button(master = config_frame, 
                    command = plot,
                    height = 2, 
                    width = 10,
                    text = "Plot")

plot_button.pack()

plot_frame = Frame(window)
plot_frame.pack()
window.mainloop()
