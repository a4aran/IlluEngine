**Game** is a class that is being changed during the development process. It is defined in `game.py` which, is outside the Illusion package. It is expected that it's a child of a **Game Manager Preset**.
Currently there are two **Game Manager presets**, stored inside `game_manager.py` inside Illusion package.
When downloading the engine the **Game** uses `IllusionBuiltInsPreset` which gives an animation when boting up the app which is imported as `b_logo`, as well as souns: `b_successful_select`, `b_denied`, `b_logo_sound`.
Other preset is called `GameManagerPreset` and it has no scenes, it's a plain game.

**Game** is expected to accept one argument: `hws`, and call super passing it. `hws` stands for **h**ard**w**are **s**ound, if the argument is artifically set to `True` app won't work on devices wihtout sound hardwere, while setting it artifically to `False` will result with the game being muted.

**Game Manager presets** create 5 objects on when their constructor is called. Those being:
 - [Scene Manager](?load=scene-manager)
 - [Importer](?load=importer)
 - [Assets](?load=assets)
 - [Music Manager](?load=music-manager)
 - [Global Objects](?global-objects)

It also defines deafult paths for importing assets:
- images (static images, no spritesheets, stores a single `pygame.Surface`): `./assets/textures/static/`
- animated sprite (animated, spritesheets, stores a list of `pygame.Surface`): `./assets/textures/animated/`
- sound effects: `./assets/sounds/effects/`
- music: `./assets/sounds/music/`
