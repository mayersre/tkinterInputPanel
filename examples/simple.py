'''
Created on 10.12.2019

Latest version of InputPanel, developed from an initial Version in the Coolprop GUI

@author: mayers

install tkinterInputPanel with pip install . in the directory where you find setup.py before running this example

'''
import tkinter as tk

from tkinterInputPanel.InputPanel import InputPanel

class _TestApp(tk.Frame):
    
    def __init__(self, master=None):
        '''
        create tk app as master
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        # create a frame for our panel
        frame=tk.Frame(self)
        # create panel from test data
        data=self.getTestData()
        _test=InputPanel(frame, datadict=data, title='tkinterInputPanel simple.py')
        # pack panel into frame
        frame.pack(fill="both", expand=True)
        # add exit button
        self.quit = tk.Button(self, 
                              text="QUIT", 
                              fg="red",
                              command=self.master.destroy
                              )
        # pack exit button
        self.quit.pack(side="bottom")
        
    def getTestData(self):
        '''
        Create test data as described in InputPanel
        '''
        testdata = {
            'verbose_names':{
                # KEY                 LABEL
                'variable_key_1'      :  'Last Holiday place',
                'variable_key_2'      :  'There and back with car',
                'variable_key_3'      :  'It was asuccess',
                'variable_key_4'      :  'Money spent',
                'variable_key_5'      :  'Choose best place for Holiday'
        
                },
            'values':{
                # KEY                 default value
                'variable_key_1'      :  'Southern France',         # this will become an [ENTRY]    for <class 'str'>
                'variable_key_2'      :  2155,                      # this will become an [ENTRY]    for <class 'int'>
                'variable_key_3'      :  True,                      # this will become a  [CHECKBOX] for <class 'bool'>
                'variable_key_4'      :  1267.53,                   # this will become an [ENTRY]    for <class 'float'>
                'variable_key_5'      :  ['France','Italy','Home'], # this will become a  [COMBBOX]  for <class 'list'>
                },
            'units':{
                # KEY                 Unit of measure
                'variable_key_1'      :  '   ',
                'variable_key_2'      :  'km',
                'variable_key_3'      :  'yes/no',
                'variable_key_4'      :  '€',
                'variable_key_5'      :  '   ',
                },
            'order':[],
            'callback_vars':{},
            }

        return testdata

if __name__ == '__main__':
    root = tk.Tk()
    app = _TestApp(master=root)
    app.mainloop()


