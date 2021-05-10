from tkinter import Tk, Button, Frame, LEFT, IntVar, Spinbox
from tkinter.ttk import Combobox

from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

from pandas import DataFrame
from datetime import datetime

from Modules.API_parameters_values import cryptocurrencies, time_series
from Modules.data import get_info, filter_data

url="https://www.alphavantage.co/query?"

APIkey,_ = open("key.txt","r").readline().split("\n")

path_curr            = "./assets/digital_currency_list.csv"
path_ph              = "./assets/physical_currency_list.csv"
name_curr, code_curr = cryptocurrencies(path_curr)
name_ph, code_ph     = cryptocurrencies(path_ph)

def plot():
    plot1.clear()
    ts = time_series[time_intervals.get()]
    cc =code_curr[crypto_list.current()]
    cp = code_ph[Physical_currency.current()]
    try:
        info = get_info(url, ts, cc, cp, APIkey)
        date, price = filter_data(info,time_intervals.get(),cp)
        df_price = DataFrame(price, columns = ["price"])
        df_price["average"] = df_price["price"].rolling(average.get()).mean()

        date = list(map(datetime.strptime, date, len(date)*['%Y-%m-%d']))
        title = f"{crypto_list.get()}({cc})"
    
        plot1.set_title(title)
        plot1.set_xlabel("Date")
        plot1.set_ylabel(f"{Physical_currency.get()}")
        plot1.plot(date, price,label= f"{cc}")
        plot1.plot(date, df_price["average"],label="Average")

        plot1.grid(True)
        plot1.legend(loc="best")

        fig.autofmt_xdate(rotation = 45)
        canvas.draw()
    except:
        pass
    
#---------------------------------------------------------
# the main Tkinter window
window = Tk()

# setting the title 
window.title('Plotting in Tkinter')

# dimensions of the main window
#window.geometry("700x550")
window.state("zoomed")

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
#time_intervals.set("Intraday")
time_intervals.set("Weekly")
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
#create canvas
# the figure that will contain the plot
fig = Figure(figsize = (12, 6.5), dpi = 100)
# adding the subplot
plot1 = fig.add_subplot()
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = plot_frame)  
canvas.draw()
# placing the canvas on the Tkinter plot_frame
canvas.get_tk_widget().pack()
# creating the Matplotlib toolbar
toolbar = NavigationToolbar2Tk(canvas, plot_frame)
toolbar.pack()
toolbar.update()

# placing the toolbar on the Tkinter window
canvas.get_tk_widget().pack()
    

window.mainloop()
