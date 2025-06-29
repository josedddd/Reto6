
from math import degrees,acos,sin,radians,atan2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (float, int)):
            raise TypeError("No pusiste enteros o flotantes") ### Si no se pusieron o enteros o flotantes, saca un type error.


class Line:
    def __init__(self, point_start: Point, point_end: Point):
        
        self.point_start = point_start
        self.point_end = point_end
        self.length = round(((point_end.x - point_start.x) ** 2 + (point_end.y - point_start.y) ** 2) ** 0.5)
        if self.length == 0:
            raise ValueError("Pusiste mal los valores de cada vertice >:")  ### Aca si no existe linea (dos puntos iguales, o muy muy cercanos), saca un value error
        self.slope = atan2((point_end.y - point_start.y),(point_end.x - point_start.x))
        self.slope_degrees = degrees(self.slope)


    def compute_length(self) -> float:
        return self.length
    
class Shape():
    def __init__(self):
        pass

    def set_is_regular(self, is_regular:bool):
        self._is_regular=is_regular

    def get_is_regular(self):
        return self._is_regular

    def set_vertices(self, vertices:list):
        self._vertices=vertices
       
    def get_vertices(self) -> list:
        return [(self._vertices[x].x, self._vertices[x].y) for x in range(len(self._vertices))]
    
    def compute_edges(self):
        pass

    def get_edges(self):
        pass

    def compute_inner_angles(self):
        pass        

    def compute_perimeter(self):
        pass

    def compute_area(self):
        pass

    def verify_type(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    
    def compute_edges(self):   
        #Estructura de vertices de un rectangulo: 
        #[point_left_up, point_right_up, point_right_down, point_left_dowm]
        self._edgeH_up = Line(self._vertices[0], self._vertices[1])
        self._edgeH_down = Line(self._vertices[3], self._vertices[2])
        self._edgeV_left = Line(self._vertices[0], self._vertices[3])
        self._edgeV_right = Line(self._vertices[1], self._vertices[2])
      
    def get_edges(self) -> list:
        self.compute_edges()
        return [
            {
                "name": "top edge",
                "start": (self._edgeH_up.point_start.x, self._edgeH_up.point_start.y),
                "end": (self._edgeH_up.point_end.x, self._edgeH_up.point_end.y),
                "length": self._edgeH_up.compute_length()
            },
            {
                "name": "bottom edge",
                "start": (self._edgeH_down.point_start.x, self._edgeH_down.point_start.y),
                "end": (self._edgeH_down.point_end.x, self._edgeH_down.point_end.y),
                "length": self._edgeH_down.compute_length()
            },
            {
                "name": "left edge",
                "start": (self._edgeV_left.point_start.x, self._edgeV_left.point_start.y),
                "end": (self._edgeV_left.point_end.x, self._edgeV_left.point_end.y),
                "length": self._edgeV_left.compute_length()
            },
            {
                "name": "right edge",
                "start": (self._edgeV_right.point_start.x, self._edgeV_right.point_start.y),
                "end": (self._edgeV_right.point_end.x, self._edgeV_right.point_end.y),
                "length": self._edgeV_right.compute_length()
            }
        ]

    def compute_area(self) -> float:
        self.compute_edges()
        return (self._edgeH_up.compute_length()*self._edgeV_right.compute_length() )
       
    def compute_perimeter(self) -> float:
        self.compute_edges()
        return 2*self._edgeH_up.compute_length()+2*self._edgeV_right.compute_length()
    
    def compute_inner_angles(self):
        return [90, 90, 90, 90]

class Square(Rectangle):
    def __init__(self):
        super().__init__()
    
  
class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def compute_edges(self): 
        ## Orden de colocar los vertices 
        # [Vertice superior, Vertice_inferior derecho, Vertice inferior izquierdo]
        
        self._edge1 = Line(self._vertices[0], self._vertices[1])
        self._edge2 = Line(self._vertices[1], self._vertices[2])
        self._edge3 = Line(self._vertices[2], self._vertices[0])
        self._leng_edge1= self._edge1.compute_length()
        self._leng_edge2= self._edge2.compute_length()
        self._leng_edge3= self._edge3.compute_length()


    def get_edges(self):
        self.compute_edges()
        return [
        {
            "name": "A",
            "start": (self._edge1.point_start.x, self._edge1.point_start.y),
            "end": (self._edge1.point_end.x, self._edge1.point_end.y),
            "length": self._leng_edge1
        },
        {
            "name": "B",  
            "start": (self._edge2.point_start.x, self._edge2.point_start.y),
            "end": (self._edge2.point_end.x, self._edge2.point_end.y),
            "length": self._leng_edge2
        },
        {
            "name":"C",
            "start": (self._edge3.point_start.x, self._edge3.point_start.y),
            "end": (self._edge3.point_end.x, self._edge3.point_end.y),
            "length": self._leng_edge3
        }
    ]

    def compute_inner_angles(self):
        self.compute_edges()
         #### El orden del calculo de los angulos es 
         # [Angulo opuesto al lado "A", Angulo opuesto al Lado B, Angulo opuesto al lado C]
        self.compute_edges()
        cos_angle_edge1= (self._leng_edge3**2 + self._leng_edge2**2 - self._leng_edge1**2) / (
            2 * self._leng_edge3* self._leng_edge2)
        self.angle_edge_1 = round(degrees(acos(cos_angle_edge1)))

        cos_angle_edge2 = (self._leng_edge3**2 + self._leng_edge1**2 - self._leng_edge2**2) / (
            2 * self._leng_edge3* self._leng_edge1)
        self.angle_edge_2 = round(degrees(acos(cos_angle_edge2)))
        
        cos_angle_edge3 = (self._leng_edge2**2 + self._leng_edge1**2 - self._leng_edge3**2) / (
            2 * self._leng_edge2* self._leng_edge1)
        self.angle_edge_3 = round(degrees(acos(cos_angle_edge3)))
       
        self.total_angles=[self.angle_edge_1, self.angle_edge_2, self.angle_edge_3]
        return self.total_angles
        
    def compute_area(self) -> float:
        self.compute_edges()
        self.compute_inner_angles()
        return (1/2*self._leng_edge1*self._leng_edge2*sin(radians(self.angle_edge_3)))
       
    def compute_perimeter(self) -> float:
        self.compute_edges()
        return (self._leng_edge1+self._leng_edge2 +self._leng_edge3)

    

### La implementacion de los errores se puede ver aca, donde hago una funcion que verifique el tipo de triangulo, si las
# vertices puestos no corresponden al tipo saca un Value error (una buena manera de avisarle al usario :V)
class EquilateralTriangle(Triangle):
    def __init__(self):
        super().__init__()
    
    def verify_type(self) -> bool:
        self.get_edges()
        if self._leng_edge1 != self._leng_edge2 or self._leng_edge1 != self._leng_edge3:
            raise ValueError("Los vertices que colocaste no corresponden a un triangulo equilatero")
        else:
            return True
        
class IsoscelesTriangle(Triangle) :
     def __init__(self):
        super().__init__()

     def verify_type(self) -> bool:
        self.get_edges()  
        if (self._leng_edge1 != self._leng_edge2 and self._leng_edge1 != self._leng_edge3
             and self._leng_edge2!=self._leng_edge3):
                raise ValueError("Los vertices que colocaste no corresponden a un triangulo equilatero")
        else:
            return True
        
class ScaleneTriangle(Triangle):
    def __init__(self):
        super().__init__()

    def verify_type(self) -> bool:
        self.get_edges()  
        if (self._leng_edge1 == self._leng_edge2 or self._leng_edge1 == self._leng_edge3
             or self._leng_edge2 == self._leng_edge3):
                raise ValueError("Los vertices que colocaste no corresponden a un triangulo escaleno")
        else:
            return True
        
class RightTriangle(Triangle):
    def __init__(self):
        super().__init__()

    def verify_type(self) -> bool:
        self.compute_inner_angles()  
        if 90 not in self.total_angles:
            raise ValueError("Los vertices que colocaste no corresponden a un triangulo rectangulo")
        else:
            return True


if __name__=="__main__":
    #Rectangle
    print("Rectangle")
    rect = Rectangle()
    rect.set_vertices([Point(0, 2), Point(4, 2), Point(4, 0), Point(0, 0)])
    print(rect.get_vertices())
    print(rect.get_edges())
    print(rect._edgeV_left.slope_degrees)

   

   
