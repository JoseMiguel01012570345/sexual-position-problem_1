import os

def pleasure_by_cost( ci,pi):
    
    result=[]
    
    for index,item in enumerate(ci,start=0):

        result.append(( f"{index}" , ci[index], pi[index] ,pi[index]/ci[index] ) )
    
    result = sorted(result,key=lambda x:x[3])
    
    return result

def time( E0_j, cij , pij , p_roof_j , j):
        
    pleasure_cost_list=pleasure_by_cost(cij,pij)    
    
    # lets find out if there is any other option satisfacing restructions the give us more time
    for option in pleasure_cost_list:
        
        if option[3] * E0_j > p_roof_j:
            
            pleasure = option[3] * E0_j
            over_pleasure = pleasure - p_roof_j
            E_prime = (option[1] * over_pleasure)/option[2]

            best_time = (E0_j - E_prime)/option[1]
            
            return f"Time for person { j + 1 } is : { best_time  + (E_prime/option[1])} in {option[0]} "
    
        elif option[3] * E0_j == p_roof_j:

            return f"Time for person { j + 1 } is : {E0_j/option[1]} in {option[0]}"
    
    return f"no solution for person {j + 1}"

 
def my_solution(E0_j, cij , pij , p_roof_j):
    
    result=[]
    for j,element in enumerate(cij,start=0):
        
        result.append(time(E0_j[j],cij[j],pij[j],p_roof_j[j],j))
    
    return result
 
os.system("cls")

E0_j= [ 100 , 90 , 95 , 98 ] 

cij = [ 
       [ 10 , 15 , 11 , 12 ] ,
       [ 20 , 13 , 15 , 16 ] , 
       [ 15 , 14 , 17 , 18 ] , 
       [ 19 , 17 , 20 , 15 ] ,
      ]

pij =[
       [ 2 , 4 , 1 , 5 ] , 
       [ 6 , 3 , 4 , 5 ] , 
       [ 7 , 6 , 2 , 1 ] , 
       [ 4 , 3 , 1 , 7 ] ,
     ]

p_roof_j = [ 20 , 30 , 25 , 35 ]

result =  my_solution(E0_j=E0_j,cij=cij,pij=pij,p_roof_j=p_roof_j)

print(result)