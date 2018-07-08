''' main gui - displays and updates list of runs'''
from __future__ import absolute_import, division
import psychopy
psychopy.useVersion('1.85.3')
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functionspart of the Dlg object has been deleted, attribute access no longer allowed.

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8') # if problems with umlauten etc. arise -> uncomment line 14-16


# import your run files by name
import tnac_run1
import tnac_run2
import tnac_run3
import tnac_run4

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title='questionaire')
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp



# defines layout of gui and updates status of runs after each run
def update(field1,field2,field3,field4):
    # creates starting gui
    myDlg = gui.Dlg(title=u'questionaires')
    myDlg.addText(u'status: o = noch ausstehend  x = erledigt\n')
    # prompts static text field showing the status of each run
    myDlg.addText(field1 + '\trun 1')
    myDlg.addText(field2 + '\trun 2')
    myDlg.addText(field3 + '\trun 3')
    myDlg.addText(field3 + '\trun 4')
    # create empty list to append to
    list_ = []
    # check status of each run and add still open runs to drop down menu
    if field1 == 'o':
        list_.append('run 1')
    if field2 == 'o':
        list_.append('run 2')
    if field3 == 'o':
        list_.append('run 3')
    if field3 == 'o':
        list_.append('run 4')

    # prompt message when all runs are done, else print basic prompt and create drop down menu
    if len(list_) == 0 :
        myDlg.addText(u'\n Danke, sie sind nun fertig.')
    else:
        myDlg.addText(u'\n   Waehlen Sie den gewuenschten run aus:')
        myDlg.addField(u'',choices=list_)
    myDlg.show()
    return myDlg

# main func - defines starting values of each run and feeds the run modules into the gui
def gui_func():
    # create status icons/values for each run
    field1 = 'o'
    field2 = 'o'
    field3 = 'o'
    field4 = 'o'
    # call update function and add runs to menu
    myDlg = update(field1,field2,field3,field4)

    # while loop allows updating the gui
    while not field1 == 'x' or not field2 == 'x' or not field3 == 'x' or not field4 == 'x':

        for i in myDlg.data:
            if 'run 1' in myDlg.data:
                # call function defined in run script with expInfo as parameter (to maximize comparability)
                tnac_run1.run1_func(expInfo)
                field1='x'
                myDlg = update(field1,field2,field3,field4)

            elif 'run 2' in myDlg.data:
                 tnac_run2.run2_func(expInfo)
                 field2= 'x'
                 myDlg = update(field1,field2,field3,field4)

            elif 'run 3' in myDlg.data:
                tnac_run3.run3_func(expInfo)
                field3= 'x'
                myDlg = update(field1,field2,field3,field4)
            elif 'run 4' in myDlg.data:
                tnac_run4.run4_func(expInfo)
                field4= 'x'
                myDlg = update(field1,field2,field3,field4)






#  call function

gui_func()
core.quit()
