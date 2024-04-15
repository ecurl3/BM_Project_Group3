import networkx as nx
import matplotlib.pyplot as plt
from string import ascii_lowercase as alcL
from string import ascii_uppercase as alcU
from Gale_Shapley import stepwise
import matplotlib.animation as ma

fig, ax = plt.subplots() #set up figure and axis for graph visual
g = nx.Graph() #create blank graph; will hold the bipartite graph
positions = {} #dictionary that holds the positions of each nodes in terms of (x,y)
traveledPath = [] #list that holds the sequence from animation 
nodeLabels = [] #list that holds the labels of the nodes within the graph
numberOfAnimationFrames = 0 #holds the total number of animation frames including the base graph, all edges traveled, and final matching nodes
matchingNodes = [] #list that holds the maximum matching solution

def matrixToGraph(matrix): #fix me: may need to be modified for more that 26 nodes
    num_nodes = len(matrix)
    half_nodes = num_nodes // 2
    
    #add left nodes to graph
    for i in range(half_nodes): #increment i until it equals the number of rows 
        g.add_node(alcL[i]) #add node
        positions[alcL[i]] = [0, i] #make position on left by making its ordered pair start with 0 and its y value  its column number
        nodeLabels.append(alcL[i]) #add the node label to the list

    #add right nodes to graph
    for i in range(half_nodes, num_nodes): #increment j until it equals the number of columns
        g.add_node(alcU[i]) #add node
        positions[alcU[i]] = [1, i - half_nodes] #make position on right by making its ordered pair start with its row number and its y value be 1   
        nodeLabels.append(alcU[i]) #add the node label to the list

    #add edges to graph
    for i in range(half_nodes): #increment through the rows of the matrix
        for j in range(half_nodes, num_nodes): #increment through the columns of the matrix
                g.add_edge(alcL[i], alcU[j]) #add edge to graph


def assign_edge_colors(g, preferences):
    edge_colors = []
    color_map = plt.cm.get_cmap('Blues')
    
    for edge in g.edges():
        node1, node2 = edge
        
        # Determine the indices of the nodes in the preference list
        node1_index = alcL.index(node1) if node1 in alcL else alcU.index(node1)
        node2_index = alcL.index(node2) if node2 in alcL else alcU.index(node2)
        
        # Calculate preference scores for both nodes
        preference_score1 = abs(node1_index - node2_index)
        preference_score2 = abs(node2_index - node1_index)
        
        # Calculate the maximum preference score
        max_preference = len(g.nodes()) // 2 - 1
        
        # Calculate color values for both nodes
        color_value1 = 1 - (preference_score1 / max_preference)
        color_value2 = 1 - (preference_score2 / max_preference)
        
        # Assign color to the edge based on the average color value of both nodes
        edge_color = color_map(((color_value1 + color_value2) / 2) + 1)
        
        edge_colors.append(edge_color)

    return edge_colors

def drawBaseGraph(preferences):
    edge_colors = assign_edge_colors(g, preferences)

    nx.draw_networkx_edges(g, positions, ax=ax, edge_color=edge_colors)

    #Draw nodes for men(lef) and women (right)
    men_nodes = [node for node in g.nodes() if node in alcL]
    women_nodes = [node for node in g.nodes() if node in alcU]

    nx.draw_networkx_nodes(g, positions, nodelist=men_nodes, ax=ax, node_color="blue", label="Men")  # Draw men nodes in blue
    nx.draw_networkx_nodes(g, positions, nodelist=women_nodes, ax=ax, node_color="pink", label="Women")  # Draw women nodes in pink

      # Add labels to nodes
    nx.draw_networkx_labels(g, positions, labels=dict(zip(nodeLabels, nodeLabels)), ax=ax)  # Add labels to ax graph using global list of labels

      # Add title to graph
    ax.set_title("Stable Marriage Problem", fontweight="bold")  # Set the ax graph title to indicate the problem

#TODO: Change implementation to show Gale_Shapley algorithim
def update(frame, preferences):
    #TODO: Fix logic so that every n??? frames the outer loop goes is performed, and every frame the inner loop is updated
    current_step_outer = frame  
    current_step_inner = 0
    
    #clear current plot
    plt.clf()

    if frame == 0:
        drawBaseGraph(preferences)
    
    # TODO: Call the Gale-Shapley algorithm (stepwise) for each frame
    # Input will require preference list + the current step of the inner loop 
    # + current step of outer loop and obtain the matching pairs or other relevant 
    # information
    prefW, freeM, proposals, engagements, current_step_inner = stepwise(preferences, current_step_outer, current_step_inner)

    for woman, man in engagements.items():
        matchingNodes.append([woman, man])

    if frame == numberOfAnimationFrames - 1:
        drawFinalSolution()

    # TODO: Update the graph visualization based on the matching pairs
    # For example, you can highlight the matched edges

    for woman, man in engagements.items():
        edge_color = "green"  # color for matched edges
        nx.draw_networkx_edges(g, positions, edgelist=[(man, woman)], ax=ax, edge_color=edge_color)

#TODO: Fix final graph / Might be able to just implement this logic in update
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

def doAnimation(preferences):
    #draw starting graph to prevent the starting graph from being blank
    drawBaseGraph(preferences) #call function to draw base bipartite graph
    
    #animate
    ani = ma.FuncAnimation(fig, update, frames = numberOfAnimationFrames, interval = 1500, fargs=(preferences,), repeat = True) #using the animation function, create a repeating animatiion consisting of the different drawn graphs

    #show animation
    plt.show() #causes animation to display