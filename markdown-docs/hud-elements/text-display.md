**Text Display** is an element of [**HUD**](?load=hud)

It allows easy displaying of text. It displays aligned to the center.

## Sections:
1. [Creating the **Text Display**](#creating-the-text-display)
2. [Customization and text](#customization-and-text)
   1. [Setting text, color and size](#setting-text-color-and-size)
   2. [Text modifying](#text-modifying)
   3. [Constant Y Pos](#constant-y-pos)
3. [Misc](#misc)

### Creating the **Text Display**

First, you got to create the object using a creator method of your UI. It accepts:
- name: `string`, used for identification
- text_renderer: [`TextRenderer`](?load=text-renderer), font it will use
- center_pos: `(float,float)`, the center of the surface that will be drawn[*](#constant-y-pos)
```
your_ui.new_text_display(self, name: str,text_renderer: TextRenderer, center_pos: tuple[float,float])
```

### Customization and text

Before you can do anything with the **Text Display**,
first you need to get it using `get_text_display` method of your UI.
It accepts a `string` will be the name of you **Text Display**.

#### Setting text, color and size
In order to customize your **Text Display** you'll have to call setter methods. 
1. `set_all` - allows setting all the properties:
   - color: `(0-255,0-255,0-255)`
   - size: `int`
   - text: `list[string]`, every element in the list will be a new line, remember to put it in brackets even if you have only one line because passing a string will resolve in each character being drawn in a new line
2. `set_color/size/text` - work the same as `set_all` but accepts only one variable
3. `set_pos` - allows you to change the center position of the **Text Display**

#### Text modifying
There are 3 methods:
1. `add_line` - adds line to the end of the **text** list, accepts `string`
2. `change_line` - allows modifying of a line, to do that you'll need to `index` (`int`) of the line inside the **text** list and pass the new `string` that the line will be changed to
3. `delete_line` - deletes the line from **text** list, accepts the `index` (`int`) of the line

#### Constant Y Pos
Sometimes center position doesn't pair well with vertical position as you would often need to guess how high will the **Text Display** be on the screen.
That's what **constant y pos** is for.

There are 2 methods for managing it:
1. `toggle_constant_y_pos` - toggles the use of the **constant y pos** which by default is _False_
2. `set_constant_y_pos` - accepts a `float`, the new **constant y pos**

### Misc

`get_text` - returns the **text** list of the **Text Display**

See also [Formatted Text Display](?load=hud-elements/formatted-text-display)
