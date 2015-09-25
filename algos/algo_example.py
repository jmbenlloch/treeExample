
from ROOT import TFile, TTree
from Centella.AAlgo import AAlgo
from Centella.physical_constants import *

from array import *

class algo_example(AAlgo):

    def __init__(self,param=False,level = 1,label="",**kargs):

        """
        
        Deal here with your parameters in param and kargs.
        If param is an instace of ParamManager, parameters
        will be set as algorithm parameters by AAlgo.
            
        """
        
        # Branches variables must be declared as attributes of the class    
        self.name='algo_example'
        self.evtID = array('i',[0]) # Variables must be unidimensional arrays
        self.plane0 = array('f',10*[ 0. ]) # Arrays are arrays

        AAlgo.__init__(self,param,level,self.name,0,label,kargs)

        # your stuff here...


    def initialize(self):

        """

        You can use here:

            self.hman     -----> histoManager instance
            self.tman     -----> treeManager instance
            self.logman   -----> logManager instance
            self.autoDoc  -----> latex_gen instance
        
        """
        
        self.m.log(1,'+++Init method of algo_example algorithm+++')


        # Book the tree with key and name
        self.tman.book("petalo","petalo")
        # For branches with one variable dimension is not need (default=1)
        self.tman.addBranch("petalo","id",self.evtID)
        # For branches with an array dimension must be set
        self.tman.addBranch("petalo","plane0",self.plane0,10)

        return

    def execute(self,event=""):

        """
        
        You can also use here:

            self.event ----> current event from the input data 
            
        """

        # Give values reminding that variables are unidimensional arrays
        self.evtID[0] = event.GetID()
          
        # Arrays can not be reinitilized, values must be given one by one
        # or the reference would be lost and root will not save anything
        for i in range(0,10):
            self.plane0[i] = i

        # Fill tree
        self.tman.fill("petalo");
                 
        return True

    def finalize(self):


        self.m.log(1,'+++End method of algo_example algorithm+++')

        return

    
