# Foundation
After *installation* there are two python files outside **Illu**/**Illusion** folder, those files being **window_size.py** and **game.py**.

The first file is supposed to contain two variables: **width** and **height** that control the size of the game window. By default they're set to 600.

The second file contains a class called **Game** which should use one of the [**Game Manager presets**](to-do). By default it uses **IllusionBuiltInsPreset** which creates an intro scene that is played when starting the game.

# Custom Scenes and Objects

### Scenes

In order to make a custom Scene you'll need to create a new class that is a child of [**Scene**](to-do) then edit **constructor**,**update** or **draw** methods. All of them should use super because otherwise the **Scene** won't work.
After making the scene you'll need to add it to [**Scene Manager**](to-do) inside the game class by using its **add_scene** method.



