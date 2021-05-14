# Find GO terms in an XML file
#import interpreters needed
from xml.dom.minidom import parse
import xml.dom.minidom
import re
import matplotlib.pyplot as plt

#parse the file 'go_obo.xml'
DOMTree = xml.dom.minidom.parse("go_obo.xml")
obo = DOMTree.documentElement
terms = obo.getElementsByTagName("term")
#define a function to find term related to spectific macromolecule
bool = False
def FindRelatedTerm(terms,x):
    related_list = []   #Set an empty list
    for term in terms:
        defstr = term.getElementsByTagName('defstr')[0]
        a = re.search(x, defstr.childNodes[0].data)
        if a == None:
            bool = False
        else:
            bool = True
        if bool == True:
            related_list.append(term) #write terms related to spectific macromolecule in it
    return related_list

#try to build a tree including the connection of all nodes
#get all nodes
class Node(object):
    def __init__(self, name):
        self.id = name
        self.connectTo = []
    def connection(self, adjacent):
        self.connectTo.append(adjacent)  #get the childNodes connection of nodes
#get branches of nodes
class Branch(object):
    def __init__(self):
        self.Nodeslist = {}

    def addNodes(self, name):
        nextNodes = Node(name)
        self.Nodeslist[name] = nextNodes
        return nextNodes

    def getNodes(self, i):
        if i in self.Nodeslist:
            return self.Nodeslist[i]
        else:
            return None

    def addadjacent(self,a,b):
        if a not in self.Nodeslist:
            nextNodes = self.addNodes(a)
        if b not in self.Nodeslist:
            nextNodes = self.addNodes(b)
        return self.Nodeslist[b].connection(self.Nodeslist[a])
    def getroot(self):
        return self.Nodeslist.name()

#make the tree including the connection of all nodes
def Tree(terms):
    tree= Branch()
    for term in terms:
        id = term.getElementsByTagName('id')[0].childNodes[0].data

        is_a = [i.childNodes[0].data for i in term.getElementsByTagName("is_a")]
        for i in is_a:
            tree.addadjacent(id,i)
    return tree
tree = Tree(terms)     #output the tree

#set a function to find all childNodes of a term
def FindAllChildren(tree,nodes):
    children=[]
    for node in nodes:
        if node:
            if node.connectTo:
                child = [i for i in node.connectTo]
                children += child
                children += FindAllChildren(tree, child)
    return children

#calculate the number of childNodes associated with specific macromolecules
def childNodesCounter(tree, molecule_name):
    match_list = FindRelatedTerm(terms, molecule_name)
    #match_list_id = FindRelatedTermID(terms,molecule_name )
    NodesList = [tree.getNodes(term.getElementsByTagName("id")[0].childNodes[0].data) for term in match_list]
    RDNodesList=set(FindAllChildren(tree, NodesList))
    count = len(RDNodesList)
    return count

#get the childNodes associated with specific macromolecules
DNA=childNodesCounter(tree,'DNA')
RNA=childNodesCounter(tree,'RNA')
protein=childNodesCounter(tree,'protein')
carbohydrate=childNodesCounter(tree,'carbohydrate')


#out put the number of childNodes associated with specific macromolecules
print("the number of childNodes associated with ‘DNA’ is",DNA,'.')
print("the number of childNodes associated with ‘RNA’ is",RNA,'.')
print("the number of childNodes associated with ‘protein’ is",protein,'.')
print("the number of childNodes associated with ‘carbohydrate’ is",carbohydrate,'.')

#Set specific pie chart parameters
labels = ['DNA', 'RNA', 'protein', 'carbohydrate']
var = [DNA,RNA,protein,carbohydrate]
colors = ["blue","red","coral","green"]
explode = [0.1,0.1,0.1,0.1]
plt.title('The number of childNodes associated with each terms',fontsize=15,pad=25)
plt.pie(var, labels=labels,explode=explode,colors=colors,autopct='%1.1f%%',shadow=True, labeldistance=1.1,pctdistance=0.8,startangle=90,textprops={'fontsize':12,'color':'black'},wedgeprops = {'linewidth':1.5,'edgecolor':'green'})
plt.axis('equal') #Equal aspect ratio ensures that pie is drawn as a circle


plt.show()  # show the pie chart