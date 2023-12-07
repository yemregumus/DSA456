class Graph:
    # This function creates a Graph object and initializes it to support number_of_verts vertices.
    def __init__(self, number_of_verts):
        # 1. Storing the total number of vertices of a graph.
        self.graph_vertices = number_of_verts

        # 2. Creating an adjacency matrix.
        self.adjacency_matrix = [[0] * number_of_verts for _ in range(number_of_verts)]

    # This function adds an additional vertex to the graph. (ie your graph now supports one more vertex than it had previously supported).
    def add_vertex(self):
        # 1. Increasing the number of graph vertices
        self.graph_vertices += 1

        # 2. Adding a new row and new column to the adjacency matrix

        # 2.1. Appending a new column: Adding an element at the end of each row of current adjacency matrix with the value 0.
        for row in self.adjacency_matrix:
            row.append(0)

        # 2.2. Appending a new row: Adding an array, of size of new graph vertices with value 0, at the end of the adjacency matrix.
        self.adjacency_matrix.append([0] * self.graph_vertices)

    # This function does nothing and returns False, if either of the vertices are invalid, or the edge already exists. Otherwise, this function will create a directed edge from the vertex from_idx to the vertex to_idx and return True
    def add_edge(self, from_idx, to_idx, weight=1):
        # 1. Making sure that the passed vertice values are valid.
        if self.validate_indexes(from_idx, to_idx):
            # 2. Making sure that there is no edge between the passed vertices.
            if self.adjacency_matrix[from_idx][to_idx] == 0:
                # 3. Adding the new edge at the passed vertices.
                self.adjacency_matrix[from_idx][to_idx] = weight

                # 4. Returning true since the new edge is now added.
                return True

        # Returning false in the case where either vertice values are invalid or the edge is already present.
        return False

    # This function returns the number of edges in the graph.
    def num_edges(self):
        # 1. Veriable for storing the number of edges present in the graph.
        count = 0

        # 2. Counting the total edges present in the graph.

        # 2.1 Iterating through all the rows in the adjacency matrix.
        for row in self.adjacency_matrix:
            # 2.2 Iterating through all the columns present in the row.
            for element in row:
                # 2.3 Increasing the count if the value of the element is not 0.
                if element != 0:
                    count += 1

        # 3 Returning the total number of edges present in the graph.
        return count

    # This function returns number of vertices in the grpah
    def num_verts(self):
        # Returning the total number of vertices of this graph.
        return self.graph_vertices

    # This function returns True if there is an edge from vertex from_idx to vertex to_idx, otherwise it returns False
    def has_edge(self, from_idx, to_idx):
        # Returning true if there is a weight at the passed verice indexes, false otherwise.
        return self.edge_weight(from_idx, to_idx) != None

    # This function returns the weight for the edge from vertex from_idx to vertex to_idx.
    def edge_weight(self, from_idx, to_idx):
        # 1. Making sure if the passed vertice indexes are valid or not.
        if self.validate_indexes(from_idx, to_idx):
            # 2. Checking the weight at the passed indexes.
            weight = self.adjacency_matrix[from_idx][to_idx]

            # 3. Returning the weight if present at the passed indexes, None otherwise.
            if weight != 0:
                return weight
            else:
                return None

        # Returning None in the case where either of the vertice values are invalid.
        return None

    # This function returns an array of tuples where the first value of the tuple is the index of the vertex and the second value is the weight of the edge to that vertex.
    def get_connected(self, vert):
        # 1. Making sure that the vert passed is valid.
        if 0 <= vert <= self.graph_vertices:
            # 2. Creating a veriable to store the list of vertices and their weights.
            vertices = []

            # 3. Iterating over all the cols of the passed vertice.
            for col in range(self.graph_vertices):
                # 4. Storing the weight at the particular column.
                weight = self.adjacency_matrix[vert][col]

                # 5. Adding the column to the list of vertices if it has any weight.
                if weight != 0:
                    vertices.append((col, weight))

            # 6. Returning the list of vertices along with the weights.
            return vertices

        # Returning None in the case where the vertice value is invalid.
        return None

    # Util Function/s.

    # This function will validate the passed vertice indexs.
    def validate_indexes(self, index1, index2):
        # Return true if both the indexs are valid and vise-versa.
        return 0 <= index1 < self.graph_vertices and 0 <= index2 < self.graph_vertices


class LabelGraph:
    # This function creates a LabelGraph object with an initial list of vertices named according to the values in vertex_list.
    def __init__(self, vertex_list):
        # Storing the vertex names in a list.
        self.vertex_list = [name for name in vertex_list]

        # Storing other related graph information in a graph object.
        self.graph = Graph(len(vertex_list))

    # This function adds an additional vertex to the graph with name vertex_name.
    def add_vertex(self, vertex_name):
        # Adding the new vertex label in the list.
        self.vertex_list.append(vertex_name)

        # Adding a new vertex in the graph.
        self.graph.add_vertex()

    # This function will create a directed edge from the vertex from_vertex to the vertex to_vertex and return True
    def add_edge(self, from_vertex, to_vertex, weight=1):
        ids = self.get_ids(from_vertex, to_vertex)

        if ids != None:
            return self.graph.add_edge(ids[0], ids[1], weight)
        else:
            return False

    # This function returns the number of edges in the graph.
    def num_edges(self):
        return self.graph.num_edges()

    # This function returns number of vertices in the graph.
    def num_verts(self):
        # Returning the number of total vertices in the graph.
        return len(self.vertex_list)

    # This function returns list of vertex names.
    def get_verts(self):
        # Returning the list of vertices name.
        return self.vertex_list

    # This function returns True if there is an edge from vertex from_vertex to vertex to_vertex, otherwise it returns False.
    def has_edge(self, from_vertex, to_vertex):
        ids = self.get_ids(from_vertex, to_vertex)

        # Making sure that the passed label of the vertices are valid.
        if ids != None:
            return self.graph.has_edge(ids[0], ids[1])
        else:
            return False

    # This function returns the weight for the edge from vertex from_vertex to vertex to_vertex.
    def edge_weight(self, from_vertex, to_vertex):
        ids = self.get_ids(from_vertex, to_vertex)

        # Making sure that the passed label of the vertices are valid.
        if ids != None:
            return self.graph.edge_weight(ids[0], ids[1])
        else:
            return None

    #  This function finds all the vertices that can be reached with a direct link starting at from_vertex. This function returns an array of tuples where the first value of the tuple is the name of the vertex connected to from_vertex and the second value is the weight of the edge to that vertex.
    def get_connected(self, from_vertex):
        connected_vertices = self.graph.get_connected(
            self.vertex_list.index(from_vertex)
        )

        # Returning the tuple of names and weight.
        return [
            (self.vertex_list[index], weight) for (index, weight) in connected_vertices
        ]

    # Util Function/s.

    # This function returns a tuple of ids
    def get_ids(self, from_vertex, to_vertex):
        # Initiating the variables for storing the ids for the passed label of the vertices.
        from_id = None
        to_id = None

        # Iterating through the list of lables to find the ids for the labels passed.
        for index in range(self.graph.graph_vertices):
            if self.vertex_list[index] == from_vertex:
                from_id = index

            if self.vertex_list[index] == to_vertex:
                to_id = index

        # Making sure both the labels are present in the list before returning the index.
        if from_id != None and to_id != None:
            return (from_id, to_id)
        return None
