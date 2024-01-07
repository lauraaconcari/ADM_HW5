#!/bin/bash

# Q 4


# Q 4.1 Is there any node that acts as an important "connector" between the different parts of the graph?
# To do so we created in Python the betweenness_centrality.csv using NetworkX's betweenness_centrality function. This gave me a file that I sorted based on the second column (value of betweenneess centrality) and the returned the highest one

# Display the entry message
echo "Node with the highest betweenness centrality is:"; 
# Sort the CSV file, specify comma as the delimiter (-t,), sort based on column 2 (-k2), in numeric (-n) reverse (-r) order, then display the top result
sort -t, -k2 -nr betweenness_centrality.csv | head -1


# Q 4.2 How does the degree of citation vary among the graph nodes?
# To do so we created in Python the degree_of_citation.csv using the degree function. This gave me a file that I sorted based on the degree and the returned the highest and lowest one

# Display the entry message
echo "Node with the highest degree is:"; 
# Similar sorting as above for a different file
sort -t, -k2 -nr degree_of_citation.csv | head -1

# Display the entry message
echo "Node with the lowest degree is:"; 
# The first part of the function filters out the header and then returns the lowest value
grep -v "Node,Degree" degree_of_citation.csv | tail -1


# Q 4.3 What is the average length of the shortest path among nodes?
# To do so we created in Python the path_lengths.csv usingusing NetworkX's all_pairs_shortest_path_length function. This gave me a file with all the shortest paths among nodes that I used to calculate the average.

# Display the entry message
echo "The average length of the shortest path is:"; 
# This AWK command calculates the average of numbers in the first column of path_lengths.csv, where each line in the file represents a path length
awk '{ total += $1; count++ } END { print total/count }' path_lengths.csv