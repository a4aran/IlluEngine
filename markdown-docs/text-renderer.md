**Text Renderer** is a class that stores fonts. Is used for displaying text.
It still is based on `pygame.font.Font` but it caches them using it size as the deafult object has a constant size.

In order to create it you'll need to use [Global Objects](?load=global-objects). All **Text Renderers** are supposed to be stored here.

### Global Objects Related

First what you'll want to check is if your font files (like .ttf) are in correct folder that `global_objects.font_prefix` points to. If you want to add it to a different directory than the deafult one just change the prefix. If you intend on putting sub-folders in your folder that sotres fonts you don't need to change the prefix to the exact sub-folder because that you can include when specifying path of your font while creating a new **Text Renderer**.

To add a **Text Renderer**/font you'll need to use `add_font` method. It accepts 
- name: `str`, it will be used to access the object inside your app
- font_file: `str`, the name/path of the file

To get a **Text Renderer** use `get_font` method. It accepts a string which is supposed to be the `name` you've put when creating the object.

### Pure Text Renderer

Sometimes you might want to use a deafult text rendering instead of the built in [Text Displays](?load=hud-elements/text-display). For that you can use a method of **Text Display** called `render`. It accepts
- text: `str`, the text that's gonna be rendered
- size: `int`, size of your text
- color: `(0-255,0-255,0-255)`, color of your text
- antialias: `bool`, allows for smoothening of your font, by deafult it's True
