Button is an element of **GUI**.

It logic detects when user of **Illu Application** is hovering over its *collision box* and if the user is clicking while hovering.

## Sections:
1. [Plain Button Class](#plain-button-class)
2. [Scene Change Button](#scene-change-button)
3. [Custom Buttons](#custom-buttons)
4. [Text on buttons](#text-on-buttons)

### Plain Button Class

Button class has methods:
1. `init` - creates the object
2. `update` - is called every frame updating the state of the button
3. `reset` - resetting the button after click
4. `on_click` - what happens after the button is clicked
5. `draw` - draws the object on screen

    And several methods used for adding and modifying text on the button.


`init` method needs/accepts parameters:
- identifier: `string`, used for when you want to get button from gui
- center_pos: `(float,float) | pygame.Vector2`, uses values like `(x pos, y pos)`, sets where the button will display aligned to the center of the collision box/button
- Size: `(float,float)`, uses values like `(width, height)`,width and height of button's collision box
- Sprites: _advised_ `[pygame.Surface,pygame.Surface,pygame.Surface]` also accepts a list with one `pygame.Surface`, used for different states a button can be in like:
  - 0 - `DEFAULT STATE`, neither hovered nor pressed
  - 1 - `HOVERED STATE`, displayed when button is hovered
  - 2 - `PRESSED STATE`, displayed when button is pressed

  A list with 1 `pygame.Surface` can be passed as the engine should autofill the list with copies of the sprite but, a list with 3 `pygame.Surface` objects will ensure it will work. If a list with more objects than 3 will be passed there won't be issues, objects after the third object will be ignored.
- Sound: `[pygame.mixer.Sound,pygame.mixer.Sound]` defaults to `[None,None]`, first sound will be played when button calls its `on_click` method, the second one will be played when the button can't be pressed, leave it like default and there won't be any sounds that button will make
- Delay: `float` default to `None`, delay from click and calling `on_click` method, while the delay is on the button is in `PRESSED STATE` and cannot be pressed again until the delay ends

While making an application in **Illu** you won't use the plain button class although knowledge of how the button functions will be useful for making custom buttons.

### Scene Change Button
There's no default button beside `ChnageScButton` (scene change button).
It accepts an int as id of a scene it should change to. It changes GUI's `data` dict when clicked.
`ChangeScButton` creator:
```
self.get_ui("default").new_scene_change_button(
    "id",
    (x_pos,y_pos),
    (collision_box_width,collision_box_height),
    sprites, #idealy list of 3 pygame.Surface objects
    scene_to_change,
    sound=[None,None],
    delay=None
)
```
The difference between `ChangeSceneButton` is that it needs one more argument, a number `id` of the scene it will change to when clicked

### Custom Buttons
In order to make a **custom** button you'll need to use `c_helper.button_base()` from `Helper.py` and make a new child with it
_Example_
```
class ExampleBTN(c_helper.button_base()):
    pass
```
In order to add a custom button to your UI you won't call creator method, instead you'll call method called `add_custom_button` and then pass the button object to it. This means that you'll need to create the object first using its constructor.

A button from this class will do nothing. In order to make custom button do what you want you can edit its methods like `on_click` or `init`. Changing other methods is not advised.
When you're editing the existing methods first call super and after that write your own code.
```
class ExampleBTN(c_helper.button_base()):

    def on_click(self, data:dict):
        super().on_click(data)
        print("click!")
```
Simple button printing "click!" in console when clicked.
You can do more complicated stuff using `data`. It changes [GUI](?load=gui) `data` dict and that change can be read by the scene.

### Text on buttons
In order to add text to your buttons you will have to call `add_text` method on the button.
This method needs:
- text_renderer: `TextRenderer`, the font you want to use
- text: `string`, the text you want your button to have
- size: `int`, size of your text
- color: `(0-255,0-255,0-255)`, RGB value for color of your text

The method will add the same text for every state, with the same coloring and size. If you want to change it you will have to use `modify_[STATE]_method`. Every state has its own method for modifying text. Those methods accept the same arguments as `add_text` method.