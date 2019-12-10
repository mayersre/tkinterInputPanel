'''
Created on 10.12.2019

Latest version of InputPanel, developed from an initial Version in the Coolprop GUI

@author: mayers

install tkinterInputPanel with pip before running this example

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
                'location'         :  'Last Holiday place',
                'distance'         :  'There and back with car',
                'success'          :  'It was asuccess',
                'budget'           :  'Money spent'
                },
            'values':{
                # KEY                 default value
                'location'         :  'Southern France', # this will become <class 'str'>
                'distance'         :  2155,         # this will become <class 'int'>
                'success'          :  True,        # this will become <class 'bool'>
                'budget'           :  1267.53          # this will become <class 'float'>
                },
            'units':{
                # KEY                 Unit of measure
                'location'         :  '   ',
                'distance'         :  'km',
                'success'          :  'yes/no',
                'budget'           :  '€',
                },
            'order':[],
            'callback_vars':{},
            }

        return testdata

if __name__ == '__main__':
    root = tk.Tk()
    app = _TestApp(master=root)
    app.mainloop()


