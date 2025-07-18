# Experimental Branch
Changes in this verison might not work

<br>
<br>
<br>

# Illusion Engine

**Illusion Engine** is a project with a goal to make python game development easier.

## Downlaod
In order to download **Illusion** click ***CODE*** button and ***Download ZIP*** in the list

For more info click [here](https://github.com/a4aran/IllusionEngine/wiki)

# Logs
## Version 0.0.1su.1
Added ***Parallax*** and a way to make ***Custom Buttons***<br>
Also changed ***globals.py*** to ***engine_constants.py*** 
which led to requirement of ***window_size.py*** outside the engine
<br>
<br>
*window_size.py:*
```
width = [window widht specified by user]
height = [window height specified by user]
```
<br>
This version is semi-updatable, which means that to update engine's version in your project 
you need to copy the files in <i><b>Illusion</b></i> package

## Version 0.0.1su.1b
Small addition and some fixes.

Added **_create_ui_** method to scene so you don't need to manually append new UIs.
<br>
<br>
Fixed the **data** in UI so that it actually works, I deleted the field from UI so now only **data** field in UI is in GUI subclass. Also added methods that allow editing the data, **_data_** in UI which returns the data field from GUI and **_delete_var_from_data_** which allows easy deletion.
<br>
<br>
Made **_parallax_** 'responsive', as in you can change the speed and things like that.

