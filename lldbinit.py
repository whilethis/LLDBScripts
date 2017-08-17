#!/usr/bin/python

import lldb
import os
import imp

def __lldb_init_module(debugger, dict):
  filePath = os.path.realpath(__file__)
  lldbHelperDir = os.path.dirname(filePath)
  
  loadCommandsInDirectory(lldbHelperDir)

def loadCommandsInDirectory(commandsDirectory):
  for file in os.listdir(commandsDirectory):
    fileName, fileExtension = os.path.splitext(file)
    
    if fileExtension == '.py' and fileName != "lldbinit":
      lldb.debugger.HandleCommand("command script import " + os.path.join(commandsDirectory, file))
            

