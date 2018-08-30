from datetime import datetime
import random
import string

nodeIdList = set()
def generateId():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))

class owner:
    id = 0
    def __init__(self, name, password):
        self.name = name
        self.id+=1
        self.password = hash(password)
    
    def __hash__(self):
        return hash((self.id, self.name))
    
    def getPasswordHash(self):
        return self.password

class owners:
    def __init__(self):
        self.ownersList = []
    
    def verifyOwnerWithCredentials(self, name, password):
        for own in self.ownersList:
            if own.name == name:
                if(own.getPasswordHash == hash(password)):
                    return True
        return False
    
    def getOwner(self, name, password):
        for own in self.ownersList:
            if own.name == name:
                if(own.getPasswordHash == hash(password)):
                    return own
        return self.addNewOwner(new owner(name, password), True)
    
    def addNewOwner(self, own, ret = False):
        self.owners.append(own)
        if(ret):
            return own
            
class nodeData:
    nodeNumber = 0
    isGenesisNode = False
    def __init__(self, owner, value, genesisNode = None, refrence = None):
        self.timestamp = datetime.now()
        self.nodeNumber+=1
        self.owner = owner
        self.data = hash(self.owner.name, self.owner.id, value)
        self.nodeId = self.generateId()
        self.refrenceNode = refrence
        self.childreferencenode = []
        if(genesisNode is None):
            self.genesisNode = self.nodeId
            self.isGenesisNode = True
        else:
            self.genesisNode = genesisNode
        
    def __hash__():
        return hash((self.timestamp, self.data, self.nodeNumber, self.nodeId, self.refrenceNode, self.genesisNode, self.childreferencenode))
    
    def __add__(self, newObj):
        if(self.owner == newObj.owner):
            for e in newObj.childreferencenode:
                self.childreferencenode.append(e)
            # assuming the the old value has been changed to the new value
            self.setValue(newObj.getValue())
        else:
            print("Error: You should be the owner of the node to be merged")
    
    def addChild(self, node):
        self.childreferencenode.append(node.getNodeId)
    
    def getId(self):
        return self.nodeId
    
    def generateId(self):
        global nodeIdList
        tmpId = generateId()
        while(tmpId in nodeIdList):
            tmpId = generateId()
        nodeIdList.add(tmpId)
        return tmpId
            
    def getChildLength(self):
        return len(self.childreferencenode)
    
    def setValue(self, value):
        self.value = value
        self.data = hash(self.owner.name, self.owner.id, self.value)
    
    def getValue(elf, value):
        return self.value
    
    def changeOwner(self, owner):
        if(self.verifyOwner()):
            self.owner = owner
            self.data = hash(self.owner.name, self.owner.id, self.value)
        else:
            print("Your not the owner of the node, hence cannot the ownership!!")
    
    def verifyOwner(self):
        print("To verify your ownership, enter your password:")
        password = hash(input().stip())
        if(password==self.owner.getPasswordHash):
            print("Verified")
            return True
        else:
            print("password didn't Match")
            return False

def getOwner(owners):
    global currentOwner
    print("Enter Your Name:")
    name = input().strip()
    print("Enter Your Password:")
    password = input().strip()
    if(owners.verifyOwnerWithCredentials(name, password)):
        currentOwner = owners.getOwner(name, password)
    else:
        owners.addNewOwner(new owner(name, password))
        currentOwner = owners.getOwner(name, password)
    return

if __name__=='__main__':
    global currentOwner
    ownerslist = new owners
    if(currentOwner is None):
        getOwner(ownerslist)
    # genesis Node
    genesis = new nodeData(currentOwner, input("Enter a value").strip(), True)
    child1 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), genesis.getNodeId())
    child2 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), genesis.getNodeId())
    child3 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), genesis.getNodeId())
    child11 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), child1.getNodeId())
    child21 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), child2.getNodeId())
    child22 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), child2.getNodeId())
    # Merging Example
    child22+=child21
    print("Value of the new is: ", child22.getValue())
    getOwner(ownerslist)
    child4 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), genesis.getNodeId())
    child41 = new nodeData(currentOwner, input("Enter a value").strip(), genesis.getNodeId(), child4.getNodeId())
    child41+=child21
    print("Value of the new is: ", child41.getValue())