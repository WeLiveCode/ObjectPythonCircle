import math


class Circle:

    def __init__(self,x_co,y_co,p_name,radius):
        self.x_co = x_co
        self.y_co = y_co
        self.p_name = p_name
        self.radius = radius

    def input_attributes(self):
        self.y_co = float(input("Faka isilungelelanisi sika Y"))
        self.x_co = float(input("Faka isilungelelanisi sika X"))
        self.p_name = input("Faka igama lendawo")
        self.radius = float(input("Faka iradiyasi"))

    def cal_peri(self):
        peri = 2 * 3.14 * self.radius
        return peri

    def cal_sur_area(self):
        s_area = 3.14 * self.radius ** 2
        return s_area

    def det_in_out(self):
        x_center = 0
        y_center = 0
        distance = math.sqrt((self.x_co - x_center) ** 2 + (self.y_co - y_center) ** 2)
        if distance > self.radius:
            whe_in_out = "ngaphandle kwesekile"
        else:
            whe_in_out = "ngaphakathi kwesekile"
        return whe_in_out

    def output(self, pe, sa, whet):
        print("Iperimitha yalesekile ngu  ", pe)
        print("Isafesi eriya yalesekile ngu  ", sa)
        print("Lendawo ingu", self.p_name, "(", self.x_co, ",", self.y_co, ")", "ifakwe ngumntu i", whet)


class TestClass:
    cir = Circle(0.0, 0.0, "", 0.0)
    cir.input_attributes()
    s_ar = cir.cal_sur_area()
    per = cir.cal_peri()
    whether = cir.det_in_out()
    cir.output(per, s_ar, whether)



