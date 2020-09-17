
def solution(src,dest):
    N=8
    n=src
    if(n==0):
        knightpos = [1, 1]
    elif(n==1):
        knightpos = [1, 2]
    elif(n==2):
        knightpos = [1, 3]
    elif(n==3):
        knightpos = [1, 4]
    elif(n==4):
        knightpos = [1, 5]
    elif(n==5):
        knightpos = [1, 6]
    elif(n==6):
        knightpos = [1, 7]
    elif(n==7):
        knightpos = [1, 8]
               
    elif(n==8):
        knightpos = [2, 1]
    elif(n==9):
        knightpos = [2, 2]
    elif(n==10):
        knightpos = [2, 3]
    elif(n==11):
        knightpos = [2, 4]
    elif(n==12):
        knightpos = [2, 5]
    elif(n==13):
        knightpos = [2, 6]
    elif(n==14):
        knightpos = [2, 7]      
    elif(n==15):
        knightpos = [2, 8]   

    elif(n==16):
        knightpos = [3, 1]
    elif(n==17):
        knightpos = [3, 2]
    elif(n==18):
        knightpos = [3, 3]
    elif(n==19):
        knightpos = [3, 4]
    elif(n==20):
        knightpos = [3, 5]
    elif(n==21):
        knightpos = [3, 6]
    elif(n==22):
        knightpos = [3, 7]      
    elif(n==23):
        knightpos = [3, 8]

    elif(n==24):
        knightpos = [4, 1]
    elif(n==25):
        knightpos = [4, 2]
    elif(n==26):
        knightpos = [4, 3]
    elif(n==27):
        knightpos = [4, 4]
    elif(n==28):
        knightpos = [4, 5]
    elif(n==29):
        knightpos = [4, 6]
    elif(n==30):
        knightpos = [4, 7]      
    elif(n==31):
        knightpos = [4, 8]   

    elif(n==32):
        knightpos = [5, 1]
    elif(n==33):
        knightpos = [5, 2]
    elif(n==34):
        knightpos = [5, 3]
    elif(n==35):
        knightpos = [5, 4]
    elif(n==36):
        knightpos = [5, 5]
    elif(n==37):
        knightpos = [5, 6]
    elif(n==38):
        knightpos = [5, 7]      
    elif(n==39):
        knightpos = [5, 8]
        
    elif(n==40):
        knightpos = [6, 1]
    elif(n==41):
        knightpos = [6, 2]
    elif(n==42):
        knightpos = [6, 3]
    elif(n==43):
        knightpos = [6, 4]
    elif(n==44):
        knightpos = [6, 5]
    elif(n==45):
        knightpos = [6, 6]
    elif(n==46):
        knightpos = [6, 7]      
    elif(n==47):
        knightpos = [6, 8]   

    elif(n==48):
        knightpos = [7, 1]
    elif(n==49):
        knightpos = [7, 2]
    elif(n==50):
        knightpos = [7, 3]
    elif(n==51):
        knightpos = [7, 4]
    elif(n==52):
        knightpos = [7, 5]
    elif(n==53):
        knightpos = [7, 6]
    elif(n==54):
        knightpos = [7, 7]      
    elif(n==55):
        knightpos = [7, 8]

    elif(n==56):
        knightpos = [8, 1]
    elif(n==57):
        knightpos = [8, 2]
    elif(n==58):
        knightpos = [8, 3]
    elif(n==59):
        knightpos = [8, 4]
    elif(n==60):
        knightpos = [8, 5]
    elif(n==61):
        knightpos = [8, 6]
    elif(n==62):
        knightpos = [8, 7]      
    elif(n==63):
        knightpos = [8, 8]      

    t=dest
    if(t==0):
        targetpos = [1, 1]
    elif(t==1):
        targetpos = [1, 2]
    elif(t==2):
        targetpos = [1, 3]
    elif(t==3):
        targetpos = [1, 4]
    elif(t==4):
        targetpos = [1, 5]
    elif(t==5):
        targetpos = [1, 6]
    elif(t==6):
        targetpos = [1, 7]
    elif(t==7):
        targetpos = [1, 8]
               
    elif(t==8):
        targetpos = [2, 1]
    elif(t==9):
        targetpos = [2, 2]
    elif(t==10):
        targetpos = [2, 3]
    elif(t==11):
        targetpos = [2, 4]
    elif(t==12):
        targetpos = [2, 5]
    elif(t==13):
        targetpos = [2, 6]
    elif(t==14):
        targetpos = [2, 7]      
    elif(t==15):
        targetpos = [2, 8]   

    elif(t==16):
        targetpos = [3, 1]
    elif(t==17):
        targetpos = [3, 2]
    elif(t==18):
        targetpos = [3, 3]
    elif(t==19):
        targetpos = [3, 4]
    elif(t==20):
        targetpos = [3, 5]
    elif(t==21):
        targetpos = [3, 6]
    elif(t==22):
        targetpos = [3, 7]      
    elif(t==23):
        targetpos = [3, 8]

    elif(t==24):
        targetpos = [4, 1]
    elif(t==25):
        targetpos = [4, 2]
    elif(t==26):
        targetpos = [4, 3]
    elif(t==27):
        targetpos = [4, 4]
    elif(t==28):
        targetpos = [4, 5]
    elif(t==29):
        targetpos = [4, 6]
    elif(t==30):
        targetpos = [4, 7]      
    elif(t==31):
        targetpos = [4, 8]   

    elif(t==32):
        targetpos = [5, 1]
    elif(t==33):
        targetpos = [5, 2]
    elif(t==34):
        targetpos = [5, 3]
    elif(t==35):
        targetpos = [5, 4]
    elif(t==36):
        targetpos = [5, 5]
    elif(t==37):
        targetpos = [5, 6]
    elif(t==38):
        targetpos = [5, 7]      
    elif(t==39):
        targetpos = [5, 8]
        
    elif(t==40):
        targetpos = [6, 1]
    elif(t==41):
        targetpos = [6, 2]
    elif(t==42):
        targetpos = [6, 3]
    elif(t==43):
        targetpos = [6, 4]
    elif(t==44):
        targetpos = [6, 5]
    elif(t==45):
        targetpos = [6, 6]
    elif(t==46):
        targetpos = [6, 7]      
    elif(t==47):
        targetpos = [6, 8]   

    elif(t==48):
        targetpos = [7, 1]
    elif(t==49):
        targetpos = [7, 2]
    elif(t==50):
        targetpos = [7, 3]
    elif(t==51):
        targetpos = [7, 4]
    elif(t==52):
        targetpos = [7, 5]
    elif(t==53):
        targetpos = [7, 6]
    elif(t==54):
        targetpos = [7, 7]      
    elif(t==55):
        targetpos = [7, 8]

    elif(t==56):
        targetpos = [8, 1]
    elif(t==57):
        targetpos = [8, 2]
    elif(t==58):
        targetpos = [8, 3]
    elif(t==59):
        targetpos = [8, 4]
    elif(t==60):
        targetpos = [8, 5]
    elif(t==61):
        targetpos = [8, 6]
    elif(t==62):
        targetpos = [8, 7]      
    elif(t==63):
        targetpos = [8, 8]      


     
    return(minStepToReachTarget(knightpos, 
                               targetpos, N))


# Python3 code to find minimum steps to reach  
# to specific cell in minimum moves by Knight  
class cell: 
      
    def __init__(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 
          
# checks whether given position is  
# inside the board 
def isInside(x, y, N): 
    if (x >= 1 and x <= N and 
        y >= 1 and y <= N):  
        return True
    return False
      
# Method returns minimum step to reach 
# target position  
def minStepToReachTarget(knightpos,  
                         targetpos, N): 
      
    #all possible movments for the knight 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    queue = [] 
      
    # push starting position of knight 
    # with 0 distance 
    queue.append(cell(knightpos[0], knightpos[1], 0)) 
      
    # make all cell unvisited  
    visited = [[False for i in range(N + 1)]  
                      for j in range(N + 1)] 
      
    # visit starting state 
    visited[knightpos[0]][knightpos[1]] = True
      
    # loop untill we have one element in queue  
    while(len(queue) > 0): 
          
        t = queue[0] 
        queue.pop(0) 
          
        # if current cell is equal to target  
        # cell, return its distance  
        if(t.x == targetpos[0] and 
           t.y == targetpos[1]): 
            return t.dist 
              
        # iterate for all reachable states  
        for i in range(8): 
              
            x = t.x + dx[i] 
            y = t.y + dy[i] 
              
            if(isInside(x, y, N) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1)) 
  
# Driver Code      

    

    
    
      
