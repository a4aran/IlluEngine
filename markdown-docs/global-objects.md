**Global Objects** class is designed to store [Text Renderers/fonts](#text-renderers-fonts), [UI](#shared-uis) objects as well as other objects that all scenes will share.
An instance of it is created inside [Game/Game Manager](?load=game-game-manager), and you aren't meant to create new instances as that would deminish the purpose of the object. It is meant for you to store things that will be accesable by every scene.

# Sections:
1. [Text Rendererers (Fonts)](#text-renderers-fonts)
2. [Shared UIs](#shared-uis)
3. [Custom Objects](custom-objects)

## Text Rendererers (Fonts)

It's the only intendet way to create [Text Renderer](?load=text-renderer) objects. It provides 3 methods that allow managing the sotrage of them.
Also it has a field called `font_prefix` that you can edit so that it points to a floder where you have your fonts.

add_font - creates a new [Text Renderer](?load=text-renderer), accepts:
- name: `str`, the name of the font in your program, will be later used to get the font
- file_name: `str`, name of your font file, the path to it. If you have sub-folder in the folder that your `font_prefix` points to, include that sub-folder in the file_name.

get_font - returns the object you've created, accepts one agrument - name: `str`. It's the `name` argument you've put when creating the object.

render_text - returns the surface with the text you want, accepts:
- font_name: `str`, the name of the font you want to use
- text: `str`, text you want to render
- size: `int`, size of the text
- color: `(0-255,0-255,0-255)`, color of the text
It allows you to render text independently of the [Text Displays](?load=text-display)


## Shared UIs

**Global objects** object allows you to store [UI](?load=ui)s, you want to reuse in different scenes, in a simple and accesible way.
It has methods to also manage that sotrage.

add_ui - method that allows adding [UI](?load=ui)s to the storage, accepts only one argument - ui: `[UI](?load=ui)`. It doesn't create a new object, instead you first gotta create a [UI](?load=ui) and after that pass it through the method. It automatically saves the [UI](?load=ui) under its `id` as a identifier in the storage.

get_ui - method that returns the [UI](?load=ui) from your storage, accepts: name: `str`. The name is the same as the `id` of the [UI](?load=ui).

delete_ui - method that deletes specified [UI](?load=ui) from your storage. Accepts: name: `str`.


## Custom Objects

**Global objects** has a specified storage for custom objects. What that means is, that sotrage was designed to store every other thing that's supposed to be accesible in the code and isn't an [UI](?load=ui) or [Text Renderer](?load=text-renderer) object.

add_custom_object - method that adds your object to the storage. Accepts:
- name: `str`, name that will be used to acces the object inside the sotrage
- c_object: `any`, your object

get_custom_object - accepts one argument - name: `str`. Returns your object.

delete_custom_object - accepts - name: `str`. Deletes your object from the storage.
