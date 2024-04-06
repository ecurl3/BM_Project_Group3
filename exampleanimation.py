import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_lowercase as alcL
from string import ascii_uppercase as alcU
import matplotlib.animation as ma

#need list of matrix; need to keep track of how many paths travel and what nodes where;need to know number of animation frames; need to know what the matching edges are

#global variable
fig, ax = plt.subplots() #set up figure and axis for graph visual
g = nx.Graph() #create blank graph; will hold the bipartite graph
positions = {} #dictionary that holds the positions of each nodes in terms of (x,y)
traveledPath = [] #list that holds the sequence from animation 
nodeLabels = [] #list that holds the labels of the nodes within the graph
numberOfAnimationFrames = 0 #holds the total number of animation frames including the base graph, all edges traveled, and final matching nodes
matchingNodes = [] #list that holds the maximum matching solution

#function that takes a list of lists as input that represents the augmented matrix for the bipartite graph
#the function fills the g global variable with the nodes and edges from the matrix
#the nodes on the left side of the bipartite graph are labeled with lowercase letters starting at 'a'
#the nodes on the right side of the bipartite graph are labeled with uppercase letters starting at 'A'
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


#this function takes a number that represents the animation frame as its input
#the function draws the graph dependent on the current frame, and path of nodes traveled
#if its the first animation frame, the base graph function is called to draw the base graph
#if its the last amination frame, the function that prints the solution is called to draw the solution graph where matches are in purple
#otherwise, the nodes not being traveled are drawn in gray and the nodes and their edge being traveled are drawn in pink 
def animation(num):
    #clear axis/graph that is drawing is going into
    ax.clear()

    #check if base graph needs to be outputed
    if (num == 0): #if first animation frame
        drawBaseGraph() #call function to draw base bipartite graph
        return #exit function
    
    #check if matching solution needs to be outputed
    if (num == numberOfAnimationFrames - 1): #if last animation frame
        drawFinalSolution() #call function to draw bipartite match
        return #exit function

    #set up path
    currentTravel = traveledPath[num - 1:num] #get the edge traveled from traveledPath corresponding to the animation frame
    path = [currentTravel[0][0], currentTravel[0][1]] #convert list pair of nodes into a single list fix me
    
    #draw edges and labels
    nx.draw_networkx_edges(g, positions, ax = ax, edge_color = "black") #draw all the edges in the graph using the positions in black to the ax graph
    nx.draw_networkx_labels(g, positions,  font_color = "black", ax = ax) #add all the labels of the nodes in the graph in black to the ax graph

    #draw nodes not being traveled
    nx.draw_networkx_nodes(g, positions, nodelist = set(g.nodes()) - set(path), node_color = "gray", ax = ax) #draw nodes from the graph that are not in the path set using the positions dictionary in gray on the ax graph

    #draw nodes being traveled and change edge color
    nx.draw_networkx_nodes(g, positions, nodelist = path, node_color = "pink", ax = ax) #draw nodes from the graph that are in the path in pink on the ax graph
    edgelist = [[path[0], path[1]]] #create a list of lists of the edge traveled
    nx.draw_networkx_edges(g, positions, edgelist = edgelist, width = 3, ax = ax, edge_color = "pink") #recolor the traveled node to be pink and to be a wider line
    
    #add title to graph
    ax.set_title("Traveling: " + " -> ".join(path), fontweight = "bold") #set the ax graph title to tell what is happening

#this function has no parameters
#the function draws the base bipartite graph
def drawBaseGraph():
    #draw edges, nodes, and labels
    nx.draw_networkx_edges(g, positions, ax = ax, edge_color = "black") #draw graph edges in black onto ax graph
    nx.draw_networkx_nodes(g, positions, ax = ax, node_color = "gray") #draw graph nodes in gray onto ax graph
    nx.draw_networkx_labels(g, positions, labels = dict(zip(nodeLabels, nodeLabels)), ax = ax) #add labels to ax graph using global list of labels

    #add title to graph
    ax.set_title("Base Bipartite Graph", fontweight = "bold") #set the ax graph title to tell what is happening

#this function has no parameters
#this function uses the global matching nodes list to draw the graph 
#with the nonmatched nodes in gray and the matched nodes in purple
def drawFinalSolution():
    #convert list with lists to list   
    matches = [] #this list holds all the nodes that have a match
    for a in matchingNodes: #travel through all the list entries in the list of lists
        for b in a: #travel through all the values in the lists within the list
            matches.append(b) #add individual values to new list

    #draw edges and put labels on nodes
    nx.draw_networkx_edges(g, positions, ax = ax, edge_color = "black") #draw all the edges in the ax graph in black
    nx.draw_networkx_labels(g, positions,  font_color= "black", ax = ax) #add all the labels of the ndoes to the ax graph in black

    #draw nodes that do not have a match
    nx.draw_networkx_nodes(g, positions, nodelist = set(g.nodes()) - set(matches), ax = ax, node_color= "gray") #draw nodes from the graph that are not in the path set using the positions dictionary in gray on the ax graph

    #draw nodes that are a match
    nx.draw_networkx_nodes(g, positions, nodelist =  matches, ax = ax, node_color= "purple") #draw the nodes that have a match in purple into the ax graph
    edgelist = [matchingNodes[k] for k in range(len(matchingNodes))] #create the an edgelist to hold a list of lists of the node pairings that are matches
    nx.draw_networkx_edges(g, positions, edgelist = edgelist, width = 3, ax = ax, edge_color = "purple") #draw the matched edges in purple

    #add title to graph
    ax.set_title("Matching Solution: ", fontweight = "bold") #set the ax graph title to tell what is happening

#this function does not have any parameters
#this function implements the actual amination
#using the FuncAnimation, the animation function is called numberOfAnimation Frames times to create a short repeating animation
def doAnimation():
    #draw starting graph to prevent the starting graph from being blank
    drawBaseGraph() #call function to draw base bipartite graph
    
    #animate
    ani = ma.FuncAnimation(fig, animation, frames = numberOfAnimationFrames, interval = 1500, repeat = True) #using the animation function, create a repeating animatiion consisting of the different drawn graphs

    #show animation
    plt.show() #causes animation to display

#this function takes a parameter that is a list of lists that holds the edges being traveled
#using the parameter, the global list holding the edges traveled is updated
def setAnimationPath(edgesTraveled):
    for edge in range(len(edgesTraveled)): #travel through all the edges
        traveledPath.append([edge]) #add edge to global function

#this function takes a parameter that is the number of animation frames
#this function sets the global numberOfAnimationFrames to the parameter
#the number of animation frames includes the base graph, all the edges traveled, and the final solution 
def setNumberOfAnimationFrames(numFrames):
    global numberOfAnimationFrames #reference the global variable
    numberOfAnimationFrames = numFrames #update the global variable to hold the number of animation frames


#this function takes a paramater that is a list of lists that represents the edges that form the maximum matching set
#this function updates the global list of lists to hold these edges
def setSetofMatchingNodes(matches):
    for edges in matches: #travel through all the edges in the matching list
        matchingNodes.append(edges) #add the edge to the list
