User Interface (**UI**)

In base **Illu** everything that is can be shown on screen is made using UI elements.
It's a good way to make a quick display with minimal logic.

UI is a class that combines 2 sub-classes [GUI*](gui.md) and [HUD](#).

Each UI has an `id` which is used in `Scenes` to get them.
UIs can have thier visibility changed by changing thier `should_show` field. It is supposed to have `bool` type object and putting any other type might result in a crash.
[GUI*](gui.md) and [HUD](#) are privatted so the only way to create objects of thier sub-classes is to use **creator methods** (they start with `new`).
If you want to edit an element or call a method of it you need to use `get` method of the UI.

Examples:
```
# creating new Text Display Object
self.get_ui("default").new_text_display(
    "text_display_name",
    text_renderer,
    (300,300)
)
```
```
# getting the Text Display Object
self.get_ui("default").get_text_display(
    "text_display_name"
)
```

*There's a method to get GUI