# Logs

## [Current Verison](#version-002su1-bugfix)

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

## Version 0.0.1su.2
Added better system for music by implementing _**Music Manager**_

## Version 0.0.1su.2b _hotfix_
Added _**resync_volume**_ method so that the muting is applied correctly

## Version 0.0.2su
All files that are important for the engines work come inside the _**Illusion**_ package.<br>
Only exception are **_game.py_** and **_window_size.py_** as they are meant ot be edited by the user.

## Version 0.0.2su.1 _bugfix_
Added new class **_GlobalsObjects_** whose object is automatically created in _**GameManager**_ similarly to classes from _**importer.py**_.
<br>
<br>
Made _**UI**_ work better in scenes. Added method to _**scene**_ called **_get_data_from_uis_**, which changes the scene's _change scene_ related **data**.
<br>
<br>
Fixed a bug in _**SceneManager**_ where it would change the scene to _should_change_scene_ data of the scene instead of _scene_to_change_to_.
<br>
<br>
Fixed a bug/oversight where the **_Scene Change Button_** didn't have **rendered_text** in their constructor.
<br>
<br>
Added **current_track** field to the _**MusicManager**_
