import random
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    
    
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.5    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        
    def infect(self):
        self.state="I"
        self.time=0 ##can I do that? CAN I??? CAN IIIIIIII AYAJUIWHFIUHUIHI>?!/!?!
   
    ##infected at time 0? Or time 1?
    def process(self, adjacent_cells): ##return immediately?? RETURN WHAT??
       if(self.state=="I"):
           self.time+=1
           
           if(self.time==recovery_time):##CHECK TO MAKE SURE THIS IS THE RIGHT ORDER BITCH!!!!!!!!!!!
               self.state="S"
           elif(random.random()<=pdeath(self.time, 3,1)): ##CAN DEAD CELLS INFECT OTHER CELLS
               self.state="R"
           else:
               for i in range(0,len(adjacent_cells)):
                   if adjacent_cells[i].state=="S":
                       if(random.random()<=virality):
                           adjacent_cells[i].infect()
                       
           
    """
    Map is going to be the main class that implements the simulator. 
    The Map has attributes for height and width, as well as a dictionary cells 
    that stores the actual cells on the map. The keys of this dictionary will be
    tuples of (x,y) coordinates, and the values will be Cell instances.
    
    
    
    Write the method adjacent_cells(self, x, y) that returns a list of cell 
    instances that are adjacent to coordinate (x,y). Adjacent means that the 
    cell could be to the north, east, south, or west. Diagonal cells do not 
    count as adjacent. Pay attention to the boundary of the map. There cannot 
    be any cells outside of the map area. 
    
    Modify the process(self) method. Use the random.random() function to obtain a
    random float between 0.0 and 1.0 and use it to decide if the cell dies or not.
    Note: The order in which each cell is processed matters. When a cell is processed,
    first decide if the cell recovers, then if it dies. Then, if it is still infected,
    proceed to infect adjacent cells, as described above.
    
    Is it also if <= then dies??

    """

class Map(object):
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell): 
        self.cells[(cell.x, cell.y)]=cell
       
    def display(self):  ##is it always 150x150??? Should we avoid try catches???
        
        image=[]
        
        for y in range (0,150):
            row=[]
            for x in range (0, 150):
                if (y,x) in self.cells: ##More efficient?? Still accurate  if((x,y) in cells.keys())  
                    state=self.cells[(y,x)].state        
                    if state=="S":
                        row.append((0.0, 1.0, 0.0))
                    elif state=='I':
                        row.append((1.0, 0.0, 0.0))
                    elif state=='R': ##necessary?????
                        row.append((0.5, 0.5, 0.5))
                else:
                    row.append((0.0, 0.0, 0.0))
            image.append(row)
        
        plt.imshow(image)
    
    def adjacent_cells(self, x,y):
        
        ##Edge checking doesn't work because you don't know shape or boundaries of map
        ##map is a weird blob
        
        ##Possbile cords (x+1,y)
       ## adjacents=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        
        ##DID WE LEARN DEL IN CLASS?????!??!?!?!?!?!
        toReturn=[]
        
        if (x-1,y) in self.cells:
            toReturn.append(self.cells[(x-1,y)])
      
        if (x+1,y) in self.cells:
            toReturn.append(self.cells[(x+1,y)])
        
        if (x,y-1) in self.cells:
            toReturn.append(self.cells[(x,y-1)])
            
        if (x,y+1) in self.cells:
            toReturn.append(self.cells[(x,y+1)])
            
        return toReturn
    
    def time_step(self):
        for v in self.cells.values():
            v.process(self.adjacent_cells(v.x, v.y))
        self.display()
            
        

"""
Write the function read_map(filename). 
This function should reads in x,y coordinates from a file, 
create a new Cell instance for each coordinate pair.
 The function should return a Map instance containing all the cells. 
 The file nyc_map.csvPreview the documentView in a new window contains
 the coordinates for each cell of the 150x150 New York City map 
 in comma separated value format.
 
"""          

def read_map(filename):
    
    m = Map()
    file=open(filename, 'r')
    
    for line in file: ##Try catch
        coord=line.split(',')  
        ##print(coord)
        m.add_cell(Cell(int(coord[0]),int(coord[1])))  ##DO WE CAST??
    
    file.close()
        
    # ... Write this function
    
    return m
