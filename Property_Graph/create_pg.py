from py2neo import Graph
import pandas as pd 
from relations import ParseRelationTypes




class GraphDataCreator:
    def __init__(self, pathToRelationData):
        self.pathToRelationData = pathToRelationData
        self.df = pd.read_csv(self.pathToRelationData, sep="\t")
        self.df.drop_duplicates() #investigate later 
    
    def create_graph(self): #in the future, this will be create nodes, and then we create the graph
        neo4j_graph = Graph(password="password")
        for _, row in self.df.iterrows():
            parsedRelationTypes = ParseRelationTypes(row.relation_type, row.subject, row.object, row.tablet_num)
            neo4j_graph.create(parsedRelationTypes.Relationship)
        
 

gdc = GraphDataCreator("~/Desktop/urr3-drehem-KG/Data_Pipeline_go/IE_Extractor/output/ie_data.tsv") #fix path
# gdc = GraphDataCreator("test_relation.tsv")
gdc.create_graph()