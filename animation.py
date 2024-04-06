import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_lowercase as alcL
from string import ascii_uppercase as alcU
import matplotlib.animation as ma

fig, ax = plt.subplots() #set up figure and axis for graph visual
g = nx.Graph() #create blank graph; will hold the bipartite graph
positions = {} #dictionary that holds the positions of each nodes in terms of (x,y)
traveledPath = [] #list that holds the sequence from animation 
nodeLabels = [] #list that holds the labels of the nodes within the graph
numberOfAnimationFrames = 0 #holds the total number of animation frames including the base graph, all edges traveled, and final matching nodes
matchingNodes = [] #list that holds the maximum matching solution

def matrixToGraph(matrix): #fix me: may need to be modified for more that 26 nodes
    #add left nodes to graph
    for i in range(len(matrix)): #increment i until it equals the number of rows 
        g.add_node(alcL[i]) #add node
        positions[alcL[i]] = [0, i] #make position on left by making its ordered pair start with 0 and its y value  its column number
        nodeLabels.append(alcL[i]) #add the node label to the list

    #add right nodes to graph
    for j in range(len(matrix[0])): #increment j until it equals the number of columns
        g.add_node(alcU[j]) #add node
        positions[alcU[j]] = [1, j] #make position on right by making its ordered pair start with its row number and its y value be 1   
        nodeLabels.append(alcU[j]) #add the node label to the list

    #add edges to graph
    for i in range(len(matrix)): #increment through the rows of the matrix
        for j in range(len(matrix[i])): #increment through the columns of the matrix
            if matrix[i][j] != 0: #if there is a edge between the nodes (which is when matrix entry is anything besides 0)
                g.add_edge(alcL[i], alcU[j]) #add edge to graph

def drawBaseGraph():

    nx.draw_networkx_edges(g, positions, ax=ax, edge_color="black")

    #Draw nodes for men(lef) and women (right)
    men_nodes = [node for node in g.nodes() if node in alcL]
    women_nodes = [node for node in g.nodes() if node in alcU]

    nx.draw_networkx_nodes(g, positions, nodelist=men_nodes, ax=ax, node_color="blue", label="Men")  # Draw men nodes in blue
    nx.draw_networkx_nodes(g, positions, nodelist=women_nodes, ax=ax, node_color="pink", label="Women")  # Draw women nodes in pink

      # Add labels to nodes
    nx.draw_networkx_labels(g, positions, labels=dict(zip(nodeLabels, nodeLabels)), ax=ax)  # Add labels to ax graph using global list of labels

      # Add title to graph
    ax.set_title("Stable Marriage Problem", fontweight="bold")  # Set the ax graph title to indicate the problem

     
def doAnimation():
    #draw starting graph to prevent the starting graph from being blank
    drawBaseGraph() #call function to draw base bipartite graph
    
    #animate
    ani = ma.FuncAnimation(fig, animation, frames = numberOfAnimationFrames, interval = 1500, repeat = True) #using the animation function, create a repeating animatiion consisting of the different drawn graphs

    #show animation
    plt.show() #causes animation to display

def animation(num):
    ax.clear()

    if(num == 0):
        drawBaseGraph()
        return