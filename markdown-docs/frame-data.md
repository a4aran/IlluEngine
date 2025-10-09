**Frame Data** is a class in a file called `frame_data_f` in **Illusion** package.
It's purpose is to have all the data of the frame like delta time or mouseposition. Those are updated every frame inside the main loop.

It has no methods (beside `reset_mbtn` which is also called every frame so there's no need for you to use it), al you need is stored as fields.
- dt: `float`, delta time - time difference between current and the last frame, in seconds
- mouse_pos: `(float,float)`, the coordiantes of the mouse, origin point at the top left of the screen
- mouse_buttons: `(bool,bool,bool)`, registers if the mouse buttons are down
  - `0` - Left Mouse Button
  - `1` - Middle Mouse Button
  - `2` - Right Mouse Button
- mbtn_just_pressed: `(bool,bool,bool)`, works the same as the `mouse_buttons` but instead of just checking if the button is pressed it checks if it was changed using pygame events
- keys" list of all keys, uses [`pygame.keys.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed)
Those fields aren't meant to be edited
Only field that could be edited is `hovers`, which is changed inside the deeper levels by objects like [Button](?load=gui-elements/button) or [Hoverable](?load=helper-c-helper#hoverable-class).
Still prefered method of using the object is not to edit its fields so you should rather resort to making chlidren classes of [Hoverable](?load=helper-c-helper#hoverable-class) instead.
