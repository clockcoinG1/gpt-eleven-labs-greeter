Element,Name,Code,Description,Type,Access,Cocoa Key
value-type,RGB color,cRGB,,WFColor,,,
value-type,TIFF image,TIFF,,NSImage,,,
class-extension,shortcut,,a shortcut in the Shortcuts application,,,
class-extension,folder,,a folder containing shortcuts,,,
class,shortcut,srct,a shortcut in the Shortcuts application,shortcuts,r,WFWorkflowReference
property,name,pnam,the name of the shortcut,text,r,scriptingName
property,subtitle,subt,the shortcut's subtitle,text,r,scriptingSubtitle
property,id,ID  ,the unique identifier of the shortcut,text,r,scriptingID
property,folder,fldr,the folder containing this shortcut,folder,rw,scriptingFolder
property,color,colr,the shortcut's color,RGB color,r,scriptingColor
property,icon,sico,the shortcut's icon,TIFF image,r,scriptingIcon
property,accepts input,anpt,indicates whether or not the shortcut accepts input data,boolean,r,scriptingAcceptsInput
property,action count,acnt,the number of actions in the shortcut,integer,r,scriptingActionCount
responds-to,run,,,,
class,folder,fldr,a folder containing shortcuts,folders,r,WFWorkflowCollection
property,name,pnam,the name of the folder,text,rw,scriptingName
property,id,ID  ,the unique identifier of the folder,text,r,scriptingID
command,run,srctrun ,Run a shortcut. To run a shortcut in the background, without opening the Shortcuts app, tell 'Shortcuts Events' instead of 'Shortcuts'.,,,
parameter,with input,inpt,the input to provide to the shortcut,any,yes,
result,,the result of the shortcut,any,
