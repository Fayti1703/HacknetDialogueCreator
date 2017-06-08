#!/usr/bin/python3
InputFileName = input("Insert path to input file: ")
OutputFileName = InputFileName[:InputFileName.find(".txt")] + ".xml"

try:
    InputFile = open(InputFileName, "r")
except IOError:
    print("Could not open file")
    exit()
InputStr = InputFile.read()
InputFile.close()

OutputStr = "<ConditionalActions>" + '\n'

targetComp = ""
k=0

temp = InputStr.find('\n')
if(temp<0): exit()
targetComp = InputStr[0:temp]
k = temp+1

delay = ""
Name = ""
while k<len(InputStr):
    temp = InputStr[k:].find(' ')
    if(temp<0):
        break
    delay = InputStr[k:(temp+k)]
    
    k = temp + k + 1
    
    temp = InputStr[k:].find(':')
    if(temp<0):
        break
    Name = InputStr[k:(temp+k)]
    
    k = temp+k+1
    
    temp = InputStr[k:].find('\n')
    if(temp<0):
        OutputStr += "<AddIRCMessage Author=\"{}\" TargetComp=\"{}\" Delay=\"{}\">".format(Name, targetComp, delay) + InputStr[k:len(InputStr)] + "</AddIRCMessage>" + '\n'
        break
    OutputStr += "<AddIRCMessage Author=\"{}\" TargetComp=\"{}\" Delay=\"{}\">".format(Name, targetComp, delay) + InputStr[k:temp+k] + "</AddIRCMessage>" + '\n'
    k = temp+k+1
    
OutputStr += "</ConditionalActions>"

OutputFile = open(OutputFileName, "w")
OutputFile.write(OutputStr)
OutputFile.close()
