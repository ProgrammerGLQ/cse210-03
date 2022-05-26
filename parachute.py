class parachute:
    def __init__(self):
        self.__parachute = ""
    
    def __get_parachute__(self, lifes):
        if lifes == 8:
            self.__parachute = """
    ___    
   /___\   
   \   /   
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 7:
            self.__parachute = """
                    
   /___\   
   \   /   
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 6:
            self.__parachute = """
                    
    ___\   
   \   /   
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 5:
            self.__parachute = """
                    
    ___   
   \   /   
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 4:
            self.__parachute = """
                    
           
   \   /   
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 3:
            self.__parachute = """
                    
            
       /   
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 2:
            self.__parachute = """
                    
             
           
    \ /    
     O     
    /|\    
    / \    
    """
        elif lifes == 1:
            self.__parachute = """
                    
            
           
    \       
     O     
    /|\    
    / \    
    """
        elif lifes == 0:
            self.__parachute = """
                    
               
           
            
     x     
    /|\    
    / \    
    """
        return self.__parachute


#           Testing
#director = parachute()
#print(director.__get_parachute__(3))
       

