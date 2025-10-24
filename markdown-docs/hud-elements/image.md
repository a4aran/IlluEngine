**Image** object are meant for display of static surfaces.
Creation of an **Image** requires you to input:
- name: `str` - used for identification of the object
- img: `pygame.SUrface` - the static surface that will be displayed
- center_pos: `tuple[float,float]` - central position of the image
To create an instance of **Image** in the your UI you'll need to call its `new_img` method which accepts the above arguments.

 To modify your existing **Image** you'll need to call `get_img` and input the `name` of your desired **Image**.

 Modification methods:
 `change_img` - accepts `pygame.Surfce`, changes the displayed image
 `change_pos` - accepts `tuple[float,float]`, changes the `center_pos` to the new position
