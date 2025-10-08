There's a class **Helper** in Illu and the engine automatically creates an object of it called `c_helper`. You don't need to make another one as everything inside that class is static.

## Methods and classes

### Button Base
`button_base` method is used for creating new custom buttons. It is meant to be placed while creating new button class like:
```
class NewBTN(c_helper.button_base()):
  ...
```
For more info on custom buttons look into [Custom Button Tutorial](?load=tutorials/custom-button)

### Hoverable Class
`Hoverable` is a class of the `c_helper` which is meant to be used as a parent when creating object/classes that can be hovered.
After making a child with that class as a parent you'll need to set `hoverbox` which is a field that is created on `init`. You can do that by simple `self.hoverbox = pygame.Rect(...)` or using a method called `set_hoverbox` which also accepts `Pygame.Rect`.

After asiging all a `pygame.Rect` to your `hover_box` you'll want to make a methods that will run every frame like an `update` method, and inside that method you'll need to call `check_hovers` method of that comes with the `Hoverable` class. It accepts `FrameData` as that's where mouse position is stored (more about that inside [Frame Data](?load=frame-data)), so make sure your method that runs every frame accepts the `FrameData`.
`check_hovers` returns a `bool` based if the mouse position collides with its `hoverbox` so you might want to do something like `self.is_hovered = self.check_hovers()` or just use it inside a if statment.

### Timer Class
`Timer` class was made with intention to make object of its type. The way it works is, when you're creating the object you'll put a `float` that is time in seconds. After that you'll be able to call several methods on the timer.

#### `Timer` methods:
- `start` - starts the timer
- `stop` - stops the timer without resetting the progress/countdown
- `update` - accepts `float`, more specifically delta time which you can get using something like `frame_data.dt` (the object name can change depending on what you call it inside your methods/functions, what's important is that that object is an instance of [Frame Data](?load=frame-data).
- `is_counting_down` - returns a `bool` based on if the timer has been started and the countdown isn't finished, in simple terms when the timer is counting down
- `reset` -  force resets the countdown of the timer and and turns the timer off
- `change_time` - accpets a `float`, changes the amount of time in seconds needed for the timer to countdown to
- `change_countdown` - accepts a `float`, changes the countdown/progress of the timer in seconds
- `get_completion_percentage` - returns the comppletion percentage of the timer as a `float`, if the timer is turned off it will return `1`
- `get_time_left` - returns the time left to the desired time that the timer countdowns to

### String Formatting Method
This method accepts:
- color: `(0-255,0-255,0-255)`, RGB color value
- size: `int`
- font_name: `string`
- text: `string`, the text that will be then returned in formatted way
It is meant to be used for [Formatted Text Display](?load=hud-elements/formatted-text-display) objects when passing text to it. It makes it easier to format the text as you don't need to manually write the formatting.
