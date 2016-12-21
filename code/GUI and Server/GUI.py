import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt

import Tkinter as tk
from Tkinter import *
import ttk
import datetime
from PIL import ImageTk, Image


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

# Initial values for hysteresis 
TEMP_U_THRESHOLD = -98
TEMP_L_THRESHOLD = -99
HUMID_U_THRESHOLD = 101
HUMID_L_THRESHOLD = 100
LIGHT_THRESHOLD = 2000

SOIL_0_THRESHOLD = 100
SOIL_1_THRESHOLD = 100
SOIL_2_THRESHOLD = 100
SOIL_3_THRESHOLD = 100

# Plots for temp, humidity, etc
f = Figure(figsize=(12,7), dpi=100)
f.subplots_adjust(hspace = .35, wspace = .35)

a = f.add_subplot(231)
b = f.add_subplot(234)
c = f.add_subplot(232)
d = f.add_subplot(233)
e = f.add_subplot(235)
fe = f.add_subplot(236)

# Control Variables
lightStr = "light:off"
heatStr = "heat:off"
fanStr = "fan:off"
w0Str = "w0:off"
w1Str = "w1:off"
w2Str = "w2:off"
w3Str = "w3:off"

# Manual Mode Flags
lightMFlag = False
heatMFlag = False
fanMFlag = False
w0MFlag = False
w1MFlag = False
w2MFlag = False
w3MFlag = False

# What's growing in each plot?
plot1 = "empty"
plot2 = "empty"
plot3 = "empty"
plot4 = "empty"

OPTIONS = [ # Add an accompanying CSV file with the same name to add new plant types
        "empty",
        "kale",
        "thyme",
        "tomato",
        "rosemary",
        "cabbage",
        "lettuce"
]

# Initial deadlines for scheduled maintenance tasks
lightStart = datetime.datetime(100,1,1,1,0,0)
lightDeadline = lightStart

w0Start = datetime.datetime(100,1,1,1,0,0)
w0Deadline = w0Start

w1Start = datetime.datetime(100,1,1,1,0,0)
w1Deadline = w1Start

w2Start = datetime.datetime(100,1,1,1,0,0)
w2Deadline = w2Start

w3Start = datetime.datetime(100,1,1,1,0,0)
w3Deadline = w3Start

img1 = 0
img2 = 0
img3 = 0
img4 = 0

# Update graphs
def animate(i):
    def addSecs(tm, secs):
        fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        fulldate = fulldate + datetime.timedelta(seconds=secs)
        return fulldate.time()
	
	# Care for global greenhouse conditions
    def careGreenhouse():
        print "Caring for greenhouse"
        print "TempU " + str(TEMP_U_THRESHOLD)
        print "TempL " + str(TEMP_L_THRESHOLD)
        print "HumidU " + str(HUMID_U_THRESHOLD)
        print "HumidL " + str(HUMID_L_THRESHOLD)
        print "Light " + str(LIGHT_THRESHOLD)

        global lightStr, heatStr, fanStr, lightStart, lightDeadline

        #handle light
        if(lightMFlag == False):
            if (plot1 == "empty" and plot2=="empty" and plot3 =="empty" and plot4 == "empty"):
                lightStr = "light:off"
            elif(lightStr == "light:on" and lightMFlag == False and addSecs(lightStart,0) >= addSecs(lightDeadline,0)):
                print "Light Done!"
                lightStr = "light:off"
            elif (lightStr == "light:off" and lightYList[-1] < LIGHT_THRESHOLD):
                lightDeadline = addSecs(lightStart, 60*30) # Turn on light in 30 minute intervals
                lightStr = "light:on"
        else:
            lightStr = "light:on"
        #handle heat
        if(heatMFlag == False):
            if (plot1 == "empty" and plot2=="empty" and plot3 =="empty" and plot4 == "empty"):
                heatStr = "heat:off"

            elif(heatStr == "heat:on" and tempYList[-1] > TEMP_U_THRESHOLD):
                print "Heat Off!"
                heatStr = "heat:off"
            elif (heatStr == "heat:off" and tempYList[-1] < TEMP_L_THRESHOLD):
                print "Heat On!"
                heatStr = "heat:on"
        else:
            heatStr = "heat:on"
        #handle humidity
        if(fanMFlag == False):
            if(fanStr == "fan:on" and humidYList[-1] < HUMID_L_THRESHOLD):
                print "Fan Off!"
                fanStr = "fan:off"
            elif (fanStr == "fan:off" and humidYList[-1] > HUMID_U_THRESHOLD):
                print "Fan On!"
                fanStr = "fan:on"
        else:
            fanStr = "fan:on"
            
    # Care for each plant individually 
    def carePlots():

        global w0Str, w1Str, w2Str, w3Str
        global w0Start, w0Deadline, w1Start, w1Deadline, w2Start, w2Deadline, w3Start, w3Deadline
        #handle Plot 1
        print "Caring for plot 1"
        if(w0MFlag == False):
            w0Start = datetime.datetime.now().time()
            if(w0Str == "w0:on" and w0MFlag == False and addSecs(w0Start,0) >= addSecs(w0Deadline,0)):
                print "Plot 1 Watering Done!"
                w0Str = "w0:off"
            elif (w0Str == "w0:off" and sm0YList[-1] < SOIL_0_THRESHOLD):
                w0Deadline = addSecs(w0Start, 60*10)
                w0Str = "w0:on"
        else:
            w0Str = "w0:on"
        #handle Plot 2
        print "Caring for plot 2"
        if(w1MFlag == False):
            w1Start = datetime.datetime.now().time()
            if(w1Str == "w1:on" and w1MFlag == False and addSecs(w1Start,0) >= addSecs(w1Deadline,0)):
                print "Plot 2 Watering Done!"
                w1Str = "w1:off"
            elif (w1Str == "w1:off" and sm1YList[-1] < SOIL_1_THRESHOLD):
                w1Deadline = addSecs(w1Start, 60*10)
                w1Str = "w1:on"
        else:
            w1Str = "w1:on"
        #handle Plot 3
        print "Caring for plot 3"
        if(w2MFlag == False):
            w2Start = datetime.datetime.now().time()
            if(w2Str == "w2:on" and w2MFlag == False and addSecs(w2Start,0) >= addSecs(w2Deadline,0)):
                print "Plot 3 Watering Done!"
                w2Str = "w2:off"
            elif (w2Str == "w2:off" and sm2YList[-1] < SOIL_2_THRESHOLD):
                w2Deadline = addSecs(w2Start, 60*10)
                w2Str = "w2:on"
        else:
            w2Str = "w2:on"
        #handle Plot 4
        print "Caring for plot 4"
        if(w3MFlag == False):
            w3Start = datetime.datetime.now().time()
            if(w2Str == "w2:on" and w3MFlag == False and w2MFlag == False  and addSecs(w3Start,0) >= addSecs(w3Deadline,0)):
                print "Plot 4 Watering Done!"
                w2Str = "w2:off"
            elif (w2Str == "w2:off" and sm3YList[-1] < SOIL_3_THRESHOLD):
                w3Deadline = addSecs(w3Start, 60*10)
                w2Str = "w2:on"
        else:
            w2Str = "w2:on"
	
	# Append graphs with new data from each CSV file
	#-----------------------------------------------
    pullData = open("temp.csv","r").read()
    dataList = pullData.split('\n')
    tempXList = []
    tempYList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            tempXList.append(int(x))
            tempYList.append(int(y))
    pullData = open("humid.csv","r").read()
    dataList = pullData.split('\n')
    humidXList = []
    humidYList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            humidXList.append(int(x))
            humidYList.append(int(y))
    pullData = open("light.csv","r").read()
    dataList = pullData.split('\n')
    lightXList = []
    lightYList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            lightXList.append(int(x))
            lightYList.append(int(y))
    pullData = open("sm0.csv","r").read()
    dataList = pullData.split('\n')
    sm0XList = []
    sm0YList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            sm0XList.append(int(x))
            sm0YList.append(int(y))
    pullData = open("sm1.csv","r").read()
    dataList = pullData.split('\n')
    sm1XList = []
    sm1YList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            sm1XList.append(int(x))
            sm1YList.append(int(y))

    pullData = open("sm2.csv","r").read()
    dataList = pullData.split('\n')
    sm2XList = []
    sm2YList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            sm2XList.append(int(x))
            sm2YList.append(int(y))
    pullData = open("sm3.csv","r").read()
    dataList = pullData.split('\n')
    sm3XList = []
    sm3YList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            sm3XList.append(int(x))
            sm3YList.append(int(y))

	
	# Update graphs with new data
	#----------------------------
    a.clear()
    a.set_title('Temperature')
    a.set_ylabel('Temperature (deg F)')
    a.set_xlabel('Time (sec)')
    a.plot(tempXList, tempYList)

    b.clear()
    b.set_title('Humidity')
    b.set_ylabel('Relative Humidity (%)')
    b.set_xlabel('Time (sec)')
    b.plot(humidXList, humidYList)

    c.clear()
    c.set_title('Soil Moisture 1')
    c.set_ylabel('Soil Moisture')
    c.set_xlabel('Time (sec)')
    c.plot(sm0XList, sm0YList)

    d.clear()
    d.set_title('Soil Moisture 2')
    d.set_ylabel('Soil Moisture')
    d.set_xlabel('Time (sec)')
    d.plot(sm1XList, sm1YList)

    e.clear()
    e.set_title('Soil Moisture 3')
    e.set_ylabel('Soil Moisture')
    e.set_xlabel('Time (sec)')
    e.plot(sm2XList, sm2YList)

    fe.clear()
    fe.set_title('Soil Moisture 4')
    fe.set_ylabel('Soil Moisture')
    fe.set_xlabel('Time (sec)')
    fe.plot(sm3XList, sm3YList)

    careGreenhouse()
    carePlots()
    fd = open('control.txt','w')
    fd.write(lightStr+","+heatStr+","+fanStr+","+w0Str + ","+w1Str + ","+w2Str + ","+w3Str)
    fd.close()







class GreenhouseApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, bitmap="clienticon.ico")
        tk.Tk.wm_title(self, "Greenhouse Client")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage,0)

    def show_frame(self, cont, i):

        frame = self.frames[cont]
        frame.tkraise()
        if(i==1):
            print "Hello"


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        def lightWrite():
            global lightMFlag
            if (light_text.get() == " Turn Light On  "):
                light_text.set("Turn Light Auto")
                lightMFlag = True

            elif(light_text.get() == "Turn Light Auto"):
                light_text.set(" Turn Light On  ")
                lightMFlag = False

        def heatWrite():
            global heatMFlag
            if (heat_text.get() == "Turn Heat On  "):
                heat_text.set("Turn Heat Auto")
                heatMFlag = True

            elif(heat_text.get() == "Turn Heat Auto"):
                heat_text.set("Turn Heat On  ")
                heatMFlag = False

        def fanWrite():
            global fanMFlag
            if (fan_text.get() == "Turn Fan On  "):
                fan_text.set("Turn Fan Auto")
                fanMFlag = True

            elif(fan_text.get() == "Turn Fan Auto"):
                fan_text.set("Turn Fan On  ")
                fanMFlag = False

        def w0Write():
            global w0MFlag
            if (w0_text.get() == "Water Plot 1 On"):
                w0_text.set("Water Plot 1 Auto")
                w0MFlag = True

            elif(w0_text.get() == "Water Plot 1 Auto"):
                w0_text.set("Water Plot 1 On")
                w0MFlag = False

        def w1Write():
            global w1MFlag
            if (w1_text.get() == "Water Plot 2 On"):
                w1_text.set("Water Plot 2 Auto")
                w1MFlag = True

            elif(w1_text.get() == "Water Plot 2 Auto"):
                w1_text.set("Water Plot 2 On")
                w1MFlag = False

        def w2Write():
            global w2MFlag
            if (w2_text.get() == "Water Plot 3 On"):
                w2_text.set("Water Plot 3 Auto")
                w2MFlag = True

            elif(w2_text.get() == "Water Plot 3 Auto"):
                w2_text.set("Water Plot 3 On")
                w2MFlag = False

        def w3Write():
            global w3MFlag
            if (w3_text.get() == "Water Plot 4 On"):
                w3_text.set("Water Plot 4 Auto")
                w3MFlag = True

            elif(w3_text.get() == "Water Plot 4 Auto"):
                w3_text.set("Water Plot 4 On")
                w3MFlag = False



        tk.Frame.__init__(self,parent)

        button2 = ttk.Button(self, text="Camera",
                            command=lambda: controller.show_frame(PageOne,0))
        button2.grid(row = 4, column = 0)

        light_text = StringVar()
        lightButton = ttk.Button(self, textvariable = light_text,
                                    command=lightWrite)
        light_text.set(" Turn Light On  ")
        lightButton.grid(row = 5, column = 0)

        fan_text = StringVar()
        fanButton = ttk.Button(self, textvariable = fan_text,
                                    command=fanWrite)
        fan_text.set("Turn Fan On  ")
        fanButton.grid(row = 6, column = 0)

        heat_text = StringVar()
        heatButton = ttk.Button(self, textvariable = heat_text,
                                    command=heatWrite)
        heat_text.set("Turn Heat On  ")
        heatButton.grid(row = 7, column = 0)

        variable1 = StringVar()
        variable1.set(OPTIONS[0]) # default value
        variable2 = StringVar()
        variable2.set(OPTIONS[0]) # default value
        variable3 = StringVar()
        variable3.set(OPTIONS[0]) # default value
        variable4 = StringVar()
        variable4.set(OPTIONS[0]) # default value


        label1 = tk.Label(self, text="Plot 1", font=LARGE_FONT)
        label1.grid(row = 0, column = 1)
        option1 = OptionMenu(self, variable1, *OPTIONS,command = self.switchPlot1)
        option1.grid(row = 1, column = 1)

        label2 = tk.Label(self, text="Plot 2", font=LARGE_FONT)
        label2.grid(row = 0, column = 2)
        option2 = OptionMenu(self, variable2, *OPTIONS,command = self.switchPlot2)
        option2.grid(row = 1, column = 2)

        label3 = tk.Label(self, text="Plot 3", font=LARGE_FONT)
        label3.grid(row = 2, column = 1)
        option3 = OptionMenu(self, variable3, *OPTIONS,command = self.switchPlot3)
        option3.grid(row = 3, column = 1)

        label4 = tk.Label(self, text="Plot 4", font=LARGE_FONT)
        label4.grid(row = 2, column = 2)
        option4 = OptionMenu(self, variable4, *OPTIONS,command = self.switchPlot4)
        option4.grid(row = 3, column = 2)

        w0_text = StringVar()
        w0Button = ttk.Button(self, textvariable = w0_text,
                                    command=w0Write)
        w0_text.set("Water Plot 1 On")
        w0Button.grid(row = 0, column = 3)

        w1_text = StringVar()
        w1Button = ttk.Button(self, textvariable = w1_text,
                                    command=w1Write)
        w1_text.set("Water Plot 2 On")
        w1Button.grid(row = 1, column = 3)

        w2_text = StringVar()
        w2Button = ttk.Button(self, textvariable = w2_text,
                                    command=w2Write)
        w2_text.set("Water Plot 3 On")
        w2Button.grid(row = 2, column = 3)

        w3_text = StringVar()
        w3Button = ttk.Button(self, textvariable = w3_text,
                                    command=w3Write)
        w3_text.set("Water Plot 4 On")
        w3Button.grid(row = 3, column = 3)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()

        canvas.get_tk_widget().grid(row = 4, column = 1, columnspan = 3, rowspan = 4)



    def switchPlot1(self,val):
        global plot1, TEMP_U_THRESHOLD, TEMP_L_THRESHOLD, HUMID_U_THRESHOLD
        global HUMID_L_THRESHOLD, LIGHT_THRESHOLD, SOIL_0_THRESHOLD
        plot1 = val
        fileName = plot1+".csv"

        with open(fileName, 'r') as f:
            conditions = f.readline()
            conditions = conditions.split(",")
            for c in range(0,11):
                if c%2==0:

                    if(conditions[c] == "TEMP_U_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_U_THRESHOLD:
                            TEMP_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "TEMP_L_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_L_THRESHOLD:
                            TEMP_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_U_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_U_THRESHOLD:
                            HUMID_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_L_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_L_THRESHOLD:
                            HUMID_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "LIGHT_THRESHOLD"):
                        if int(conditions[c+1]) > LIGHT_THRESHOLD:
                            LIGHT_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "SOIL_THRESHOLD"):
                        SOIL_0_THRESHOLD = int(conditions[c+1])


        print plot1
        print TEMP_U_THRESHOLD
        print TEMP_L_THRESHOLD
        print SOIL_0_THRESHOLD

    def switchPlot2(self,val):
        global plot2, TEMP_U_THRESHOLD, TEMP_L_THRESHOLD, HUMID_U_THRESHOLD
        global HUMID_L_THRESHOLD, LIGHT_THRESHOLD, SOIL_1_THRESHOLD
        plot2 = val
        fileName = plot2+".csv"

        with open(fileName, 'r') as f:
            conditions = f.readline()
            conditions = conditions.split(",")
            for c in range(0,11):
                if c%2==0:

                    if(conditions[c] == "TEMP_U_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_U_THRESHOLD:
                            TEMP_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "TEMP_L_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_L_THRESHOLD:
                            TEMP_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_U_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_U_THRESHOLD:
                            HUMID_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_L_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_L_THRESHOLD:
                            HUMID_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "LIGHT_THRESHOLD"):
                        if int(conditions[c+1]) < LIGHT_THRESHOLD:
                            LIGHT_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "SOIL_THRESHOLD"):
                        SOIL_1_THRESHOLD = int(conditions[c+1])

        print plot2
        print TEMP_U_THRESHOLD
        print TEMP_L_THRESHOLD
        print SOIL_1_THRESHOLD

    def switchPlot3(self,val):
        global plot3, TEMP_U_THRESHOLD, TEMP_L_THRESHOLD, HUMID_U_THRESHOLD
        global HUMID_L_THRESHOLD, LIGHT_THRESHOLD, SOIL_2_THRESHOLD
        plot3 = val
        fileName = plot3+".csv"

        with open(fileName, 'r') as f:
            conditions = f.readline()
            conditions = conditions.split(",")
            for c in range(0,11):
                if c%2==0:

                    if(conditions[c] == "TEMP_U_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_U_THRESHOLD:
                            TEMP_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "TEMP_L_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_L_THRESHOLD:
                            TEMP_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_U_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_U_THRESHOLD:
                            HUMID_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_L_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_L_THRESHOLD:
                            HUMID_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "LIGHT_THRESHOLD"):
                        if int(conditions[c+1]) < LIGHT_THRESHOLD:
                            LIGHT_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "SOIL_THRESHOLD"):
                        SOIL_2_THRESHOLD = int(conditions[c+1])


        print plot3
        print TEMP_U_THRESHOLD
        print TEMP_L_THRESHOLD
        print SOIL_2_THRESHOLD

    def switchPlot4(self,val):
        global plot4, TEMP_U_THRESHOLD, TEMP_L_THRESHOLD, HUMID_U_THRESHOLD
        global HUMID_L_THRESHOLD, LIGHT_THRESHOLD, SOIL_3_THRESHOLD
        plot4 = val
        fileName = plot4+".csv"

        with open(fileName, 'r') as f:
            conditions = f.readline()
            conditions = conditions.split(",")
            for c in range(0,11):
                if c%2==0:

                    if(conditions[c] == "TEMP_U_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_U_THRESHOLD:
                            TEMP_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "TEMP_L_THRESHOLD"):
                        if int(conditions[c+1]) > TEMP_L_THRESHOLD:
                            TEMP_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_U_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_U_THRESHOLD:
                            HUMID_U_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "HUMID_L_THRESHOLD"):
                        if int(conditions[c+1]) < HUMID_L_THRESHOLD:
                            HUMID_L_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "LIGHT_THRESHOLD"):
                        if int(conditions[c+1]) < LIGHT_THRESHOLD:
                            LIGHT_THRESHOLD = int(conditions[c+1])
                    elif(conditions[c] == "SOIL_THRESHOLD"):
                        SOIL_3_THRESHOLD = int(conditions[c+1])


        print plot4
        print TEMP_U_THRESHOLD
        print TEMP_L_THRESHOLD
        print SOIL_3_THRESHOLD


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        def action1():
            global img1,img2,img3,img4
            img1 = ImageTk.PhotoImage(file = "plot1.jpg")
            img2 = ImageTk.PhotoImage(file = "plot2.jpg")
            img3 = ImageTk.PhotoImage(file = "plot3.jpg")
            img4 = ImageTk.PhotoImage(file = "plot4.jpg")

            panel1 = tk.Label(self, image = img1)
            panel1.image = img1
            panel1.grid(row = 0, column = 1)

            panel2 = tk.Label(self, image = img2)
            panel2.image = img2
            panel2.grid(row = 0, column = 2)

            panel3 = tk.Label(self, image = img3)
            panel3.image = img3
            panel3.grid(row = 1, column = 1)

            panel4 = tk.Label(self, image = img4)
            panel4.image = img4
            panel4.grid(row =1, column = 2)

        tk.Frame.__init__(self, parent)
        global img1, img2, img3, img4
        img1 = ImageTk.PhotoImage(file = "plot1.jpg")
        img2 = ImageTk.PhotoImage(file = "plot2.jpg")
        img3 = ImageTk.PhotoImage(file = "plot3.jpg")
        img4 = ImageTk.PhotoImage(file = "plot4.jpg")


        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage,0))
        button1.grid(row = 0, column = 0)

        button2 = ttk.Button(self, text="Refresh",
                            command=action1)
        button2.grid(row = 1, column = 0)

        panel1 = tk.Label(self, image = img1)
        panel1.image = img1
        panel1.grid(row = 0, column = 1)

        panel2 = tk.Label(self, image = img2)
        panel2.image = img2
        panel2.grid(row = 0, column = 2)

        panel3 = tk.Label(self, image = img3)
        panel3.image = img3
        panel3.grid(row = 1, column = 1)

        panel4 = tk.Label(self, image = img4)
        panel4.image = img4
        panel4.grid(row =1, column = 2)







app = GreenhouseApp()

ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
