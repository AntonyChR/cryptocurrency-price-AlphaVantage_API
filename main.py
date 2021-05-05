from tkinter import Tk, Button, Frame
from tkinter.ttk import Combobox
from Modules import API_parameters_values as param
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
path: str = "./assets/digital_currency_list.csv"
def plot():
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                    dpi = 100)
    # list of squares
    y = [i**2 for i in range(101)]
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    plot1.plot(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                                master = plot_frame)  
    canvas.draw()
    # placing the canvas on the Tkinter plot_frame
    canvas.get_tk_widget().grid(row = 0, column = 1)
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                    plot_frame)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().grid(row = 1, column = 1)

# the main Tkinter window
path = "./assets/digital_currency_list.csv"
name, code = param.cryptocurrencies(path)
window = Tk()

# setting the title 
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("700x500")

config_frame = Frame(window)
config_frame.grid(row = 0, column = 0)

#list that displays cryptocurrencies
crypto_list = Combobox(config_frame, text = "Cryptocurrenci")
crypto_list.grid(row = 0, column = 0)
crypto_list["values"] = name


# button that displays the plot
plot_button = Button(master = config_frame, 
                    command = plot,
                    height = 2, 
                    width = 10,
                    text = "Plot")

plot_button.grid(row = 1, column = 0)

plot_frame = Frame(window)
plot_frame.grid(row = 0, column = 1)
window.mainloop()
