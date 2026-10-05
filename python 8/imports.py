#basic import
import printing_functions 
printing_functions.printing_functions("yellow","pen","small")
#import specific function
from printing_functions import printing_functions
printing_functions("yelloww","penn","smalll")
#import with alias for the function
from printing_functions import printing_functions as pf
printing_functions("mustard","pencil","large")
#import module with alias
import printing_functions as pf
pf.printing_functions("red","glass","medium")
#import everything from the module
from printing_functions import *
printing_functions("white","box",'large')