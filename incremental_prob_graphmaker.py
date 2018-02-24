#Author Jesse Erger
#Creates random graphs in Gephi format with a set edge probability between two nodes (prob_of_edge). Adjust the tunable parameters to your desired parameters. Graph files will be created in the directory this is ran. To run, simply open a command prompt and navigate to the directory of this file. Run the command python create_graph.py. Expect a run time of O(num_nodes^2*num_graphs). Feel free to write various stats about each graph with the stats_fp.write("") command.


from random import *
def create_nodes(num_nodes, file):
  for i in range (0,num_nodes):
    file.write("  node\n  [\n    id "+str(i)+"\n    label \""+str(i)+"\"\n  ]\n")
def create_edge(source,target,file,weight = 0,weighted = False):
  if(weighted):
    file.write("  edge\n  [\n    source "+str(source)+"\n    target "+str(target)+"\n    value "+str(weight)+"\n  ]\n")
  else:
    file.write("  edge\n  [\n    source "+str(source)+"\n    target "+str(target)+"\n  ]\n")
def check_if_edges(num_nodes,prob_edge,fp):
  precision_of_prob = len(str(float(prob_edge)).split('.')[1]) #precision needed is based on the number of decimals in the probability. 
  #iterate over all nodes except the last node
  for cur_node in range(0,num_nodes-1): 
   #check to see if all nodes after cur_node have an edge based on the given prob of an edge
   for node_after in range(cur_node+1, num_nodes): 
     #generate number from 1 to 10^(number of decimals in probability)
     ran_num = randint(1,pow(10,precision_of_prob)) 
     #if the random number/10^precision <= the probability of making an edge, create an edge.
     if((ran_num/pow(10,precision_of_prob))<=prob_edge): 
       create_edge(cur_node,node_after,fp) 

#Tunable parameters   
stats_fp = open("Graph_Results.txt",'w')
num_graphs = 10
base_prob_of_edge = 0
increment_amount = 0.0003
precision_of_prob = 4 #number of decimals desired for probability of creating an edge
num_nodes = 1589
self_loops = False
directed = 0
#Make graphs
prob_of_edge = 0
for i in range(0,num_graphs):
 prob_of_edge = increment_amount*i + increment_amount + base_prob_of_edge
 fp = open("Graph_prob_"+str(round(prob_of_edge,precision_of_prob)).split('.')[1]+".gml",'w')
 stats_fp.write("Graph " + str(i) + '\n')
 fp.write("Creator \"Jesse Erger, Edge Probability = "+str(round(prob_of_edge,precision_of_prob))+"\"\ngraph\n[\n  directed "+str(directed)+"\n")
 create_nodes(num_nodes,fp)
 
 #Checks if there is an edge between each node based on the probability, if there is create an edge in the output file fp 
 check_if_edges(num_nodes,prob_of_edge,fp)  
 fp.write("]") 
 fp.close()
stats_fp.close()
