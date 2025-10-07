**Formatted Text Display** is an element of [HUD](?load=hud) based on [Text Display](?load=hud-elements/text-display)

It's creator requires:
- name: `string`, for identification
- fonts: `dict[[TextRenderer](?load=text-renderer)]`, used while formatting, the names of fonts/[Text Renderer](?load=text-renderer)s will be later used in formatting.
- center_pos: `(float,float)`, center position of of the displayed text

It only has `set_text` from methods that change its properities as styling is handeled inside the string.
Shares its `set_pos`.`toggle_constant_y_pos`,`set_constant_y_pos` and `get_text` methods with [Text Display](?load=hud-elements/text-display).
> Note: `get_text` will return the same list as the one passed, with formatting characters

## Formatting
In order to format your text you'll put `{...}` before the text that will be formatted.
### How formatting works:
Use letters:
- `c` - color
- `s` - size
- `f` - font
Advised in this order.
Each one will have to be followed by `:[value]`.
Expected types of values:
- color: `(0-255,0-255,0-255)`, rgb based color, it has to written like a normal tuple
- size: `int`
- font: `string`, name of the font/[Text Renderer](?load=text-renderer) in the dict you've passed when creating the object

Example string: `"{c:(255,0,0),s:40,f:font1}Example text"` → <span style="color: rgb(255,0,0), font-size:40px">Example text</span>

Empty `{}` will make it deafult to:
- color: `rgb(0,0,0)` - black
- size: `24`
- font: first font in the dict

There's also a method in [Helper/c_helper](?load=helper-c-helper) called `[to_format_string](?load=helper-c-helper#string-formatting-method)` which generates the formatting so you don't have to mannually write it.
