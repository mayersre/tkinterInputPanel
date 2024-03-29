'''
Created on 10.12.2019

Latest version of InputPanel, developed from an initial Version in the Coolprop GUI

@author: mayers
'''
import tkinter as tk
from tkinter import ttk

class InputPanel(tk.LabelFrame):
    '''
    This input frame creates Entries and selects for Variables
    contained in a Dictionary structure
    
    The dictionary structure (datadict) needs at least the three nested dicts and a list described below. 
    
    For each one key must be an entry in every dict!
    
    The list 'order' is used for processing, it defines the order of appearance from top to down.
    
    You can pass a list 'order' even with only one field e.g. to init
    and only this field will be processed
    
    From the initial values provided the datatype of the variables will be derived!
    
    a default value of appropriate type must be present in the dict 'values'
     
    <class 'bool'>, <class 'int'>, <class 'float'>, <class 'str'> and <class 'list'> are available.
    
    See the values in the simple.py example in this package
    
    datadict={
                'verbose_names':{},
                'values':{},
                'callback_vars':{},
                'order':[],
                }
    
    if a dict units is added to the datadict, the units will be displayed behind the entry widgets
    
    '''
    def __init__(self, master,cnf={}, title=None,datadict=None,order=None,frameborder=5, InputWidth=40,**kwargs):
        #
        super().__init__(master)
        #
        self.start_line=1
        #
        self.InputWidth=InputWidth
        if datadict :
            self.datadict=datadict
        else:
            self.datadict={
                'verbose_names':{},
                'values':{},
                'callback_vars':{},
                'order':[],
                }
        #
        if order :
            '''
            A processing order was provided by kwarg
            '''
            self.order=order
        else:
            '''
            The data comes alread with a processing order
            '''
            self.order=self.datadict['order']
        '''
        Assign callback vars to each value/label/unit set and create an order if there is none
        '''
        self.createCallbackVars()
        #
        if len(self.order) == 0 :
            '''
            No processing order given yet, so we take the default one from the variable creation
            '''
            self.order=self.datadict['order']
            #
        if title :
            '''
            We have a Title, so we use it
            '''
            self.InputFrame = tk.LabelFrame(master, 
                                             relief=tk.GROOVE, 
                                             text=title,
                                             bd=frameborder,
                                             font=("Arial", 10, "bold"))
            #
        else:
            '''
            We have NO Title, so we use "Input", we could just omit text= ...
            '''
            self.InputFrame = tk.LabelFrame(master, 
                                             relief=tk.GROOVE,
                                             text='Input',
                                             bd=frameborder,
                                             font=("Arial", 10, "bold"))
            #
        self.InputFrame.grid(row=1,column=1,padx=8,pady=5,sticky=tk.W)
        #
        self.InputPanelHeader(self.InputFrame)
        #
        self.InputPanel(self.InputFrame,start_line=self.start_line)
        #
        self.InputPanelFooter(self.InputFrame,start_line=self.start_line)

    def createCallbackVars(self):
        '''
        extends self.datadict with callback variables and a list 'order' for processing
        '''
        #
        for key in self.datadict['verbose_names'] :
            if type(self.datadict['values'][key]) == type(1):
                '''
                We have an integer
                '''
                self.datadict['callback_vars'][key]=tk.IntVar()
                #
            elif type(self.datadict['values'][key]) == type(1.0):
                '''
                Floating point input
                '''
                self.datadict['callback_vars'][key]=tk.DoubleVar()
            else :
                '''
                For Boolean types we misuse <str>
                In InputPanelUpdate it is only one line of code
                For Strings and Lists we use <str>
                '''
                self.datadict['callback_vars'][key]=tk.StringVar()
            self.datadict['order'].append(key)
            self.datadict['callback_vars'][key].set(self.datadict['values'][key])
            #
            # add a dictionary so we can modify the unit labels when they change
            #
            self.datadict['unit_labels']={}
        #
    def InputPanelHeader(self, PanelFrame, font=("Arial", 10, "bold") ):
        '''
        '''
        self.start_line = 1
        print('InputPanelHeader')
    
    def InputPanel(self, PanelFrame, font=("Arial", 10, "bold"),start_line=1):
        '''
        '''
        #
        order_number=start_line
        for Dkey in self.order :
            if self.datadict['verbose_names'][Dkey] :
                #
                self.datadict['callback_vars'][Dkey].trace("w", lambda name, index, mode,
                                                         var=self.datadict['callback_vars'][Dkey],
                                                         value=self.datadict['values'][Dkey],
                                                         key=Dkey: self.InputPanelUpdate(var, key, value)
                                                         )
                tk.Label(PanelFrame, 
                          text=self.datadict['verbose_names'][Dkey], 
                          font=font).grid(column=1, 
                                          row=order_number, 
                                          padx=8, 
                                          pady=5, 
                                          sticky=tk.W)
                #
                if type(self.datadict['values'][Dkey])==type(True):
                    '''
                    We have a boolean type content so we create a checkbutton
                    '''
                    tk.Checkbutton(PanelFrame, 
                                    width=self.InputWidth, 
                                    variable=self.datadict['callback_vars'][Dkey], 
                                    font=font).grid(column=2, 
                                                    row=order_number, 
                                                    padx=8, 
                                                    pady=5, 
                                                    sticky=tk.W)
                    #
                elif type(self.datadict['values'][Dkey])==type([1,2,'3']):
                    '''
                    We have a selection type content so we create a ttk combobox for a list
                    '''
                    cbox=ttk.Combobox(PanelFrame, 
                                      textvariable=self.datadict['callback_vars'][Dkey],
                                      width=self.InputWidth,
                                      font=font)
                    #
                    # ttk.Combobox returns a Combobox, grid does not
                    # so we have to split this up here
                    #
                    cbox.grid(row=order_number,
                              column=2,
                              padx=8,
                              sticky=tk.W,
                              pady=5)
                    # assign List to combobox
                    cbox['values'] = self.datadict['values'][Dkey]
                    # select first item in list
                    cbox.current(0) 
                    #
                else:
                    '''
                    We have a multi input type content so we create an entry 
                    '''
                    tk.Entry(PanelFrame, 
                              width=self.InputWidth, 
                              textvariable=self.datadict['callback_vars'][Dkey], 
                              font=font).grid(column=2, 
                                              row=order_number, 
                                              padx=8, 
                                              pady=5, 
                                              sticky=tk.W)
                try:
                    '''
                    If we have a unit assigned, we add the unit of measure
                    and we add the tk Label to a dict so we can modify it
                    '''
                    ltext  = self.datadict['units'][Dkey]
                    llabel = tk.Label(PanelFrame, text=ltext, font=font)
                    #
                    # tk.Label returns a Label, grid does not
                    # so we have to split this up here
                    #
                    llabel.grid(column=3, row=order_number, padx=8, pady=5, sticky=tk.W)
                    self.datadict['unit_labels'][Dkey]=llabel
                    #
                except KeyError :
                    '''
                    If we have no unit assigned, we create an empty label
                    '''
                    tk.Label(PanelFrame, 
                              text='       ',
                              font=font).grid(column=3, 
                                              row=order_number,
                                              padx=8,
                                              pady=5,
                                              sticky=tk.W)
            else :
                '''
                self.datadict['verbose_names'][Dkey] --> so we create an empty label only
                '''
                tk.Label(PanelFrame, 
                          text=' ', 
                          font=font).grid(column=1, 
                                          row=order_number, 
                                          padx=8, 
                                          pady=5, 
                                          sticky=tk.W)
            #
            order_number+=1
        #
        self.start_line=order_number

    def InputPanelFooter(self, PanelFrame, font=("Arial", 10, "bold"),start_line=1 ):
        '''
        '''
        #pass
        print('InputPanelFooter',start_line)


    def InputPanelUpdate(self, tkVar, key, value):
        '''
        This method keeps updating the variables in the data structure
        '''
        #print(tkVar, key, tkVar.get(),'#')
        #
        if type(self.datadict['values'][key])==type(True):
            # For booleans we misuse a string
            self.datadict['values'][key] = True if tkVar.get()=='1' else False
        elif type(self.datadict['values'][key])==type(1):
            # int
            self.datadict['values'][key] = int(tkVar.get())
        elif type(self.datadict['values'][key])==type(1.1):
            # float
            self.datadict['values'][key] = float(tkVar.get())
        else:
            # all the rest
            self.datadict['values'][key] = tkVar.get()
        #
        self.UpdateAction(tkVar, key, self.datadict['values'][key])
        

    def UpdateAction(self, tkVar, key, value):
        '''
        This method does extra action when the data changes
        '''
        print(tkVar, key,self.datadict['values'][key])


