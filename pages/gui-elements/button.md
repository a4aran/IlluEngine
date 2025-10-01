Button is an element of **GUI**.

It logic detects when user of **Illu Application** is hovering over its *collision box* and if the user is clicking while hovering.

There's no default button beside `ChnageScButton` (scene change button).
It accepts an int as id of a scene it should change to. It changes GUI's `data` dict when clicked.
`ChangeScButton` creator:
```
self.get_ui("default").new_scene_change_button(
    "id",
    (pos_x,pos_y),
    (collision_box_width,collision_box_height),
    sprites, #idealy list of 3 pygame.Surface objects
    scene_to_change,
    sound=[None,None],
    delay=None
)
```

In order to make a **custom** button you'll need to use `c_helper.button_base()` from `Helper.py` and make a new child with 
