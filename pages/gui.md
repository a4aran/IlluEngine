Sub-class of [UI](ui.md)

Graphical User Interface (**GUI**)

In **Illu** GUI elements/objects are those that user can intereact with, like a button.

It also has a dict `data` that by deafult stores:
```
{
    "should_change_scene": False,
    "scene_to_change_to": 0
}
```
Which is used for changing scenes

GUI Elements:
- [Button](gui-elements/button.md)