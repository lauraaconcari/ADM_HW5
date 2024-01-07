import pandas as pd
import networkx as nx
import csv

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('output.csv')

# Sort the DataFrame based on the number of citations in descending order
df_sorted = df.sort_values(by='n_citation', ascending=False)

# Select the top 10,000 documents
top_10000_documents = df_sorted.head(10000)

# Drop NaN values in the 'id' column
df_sorted = top_10000_documents.dropna(subset=['id'])

# Sort the DataFrame based on the number of citations in descending order
df_sorted = df.sort_values(by='n_citation', ascending=False)

# Select the top 10,000 documents
top_10000_documents = df_sorted.head(10000)

# Drop NaN values in the 'id' column
df_sorted = top_10000_documents.dropna(subset=['id'])

def fill_nodes_citation(data, G):
    for _, row in data.iterrows():
        paper_id = row['id']
        references_str = row['references']

        # Convert the references string to a list of integers
        references = [int(ref) for ref in str(references_str).split(';') if ref.isdigit()]

        # Add edges to the graph if the reference exists in the dataset
        for ref in references:
            if ref in data['id'].values:
                G.add_edge(paper_id, ref)


# Create an empty directed graph
citation_graph = nx.DiGraph()

# Call the function to fill nodes and edges in the citation graph
fill_nodes_citation(df_sorted, citation_graph)

pos = nx.spring_layout(citation_graph)
nx.draw(citation_graph, pos, with_labels=False, node_size=5)

# Started a variable called betweenness_centrality that calculates betweenness centrality using NetworkX
betweenness_centrality = nx.betweenness_centrality(citation_graph)

# Export to CSV betweenness_centrality.csv
with open('betweenness_centrality.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Node", "BetweennessCentrality"])
    for node, centrality in betweenness_centrality.items():
        writer.writerow([node, centrality])



# Started a variable called degrees that calculates degreess from our citation_grpah
degrees = citation_graph.degree()

# Export to CSV degree_of_citation.csv
with open('degree_of_citation.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Node', 'Degree'])
    for node, degree in degrees:
        writer.writerow([node, degree])


# Generate the shortest path lengths using NetworkX function all_pairs_shortest_path_length
path_lengths = nx.all_pairs_shortest_path_length(citation_graph)

# Export to CSV path_lengths.csv
with open('path_lengths.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Since in the question we only need the lengths to find the average, no headers are needed
    for source, lengths_dict in path_lengths:
        for target, length in lengths_dict.items():
            if source != target:  # Avoid self-loops if not interested in zero-length paths
                writer.writerow([length])

