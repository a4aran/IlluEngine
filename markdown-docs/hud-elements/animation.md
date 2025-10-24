**Animation** pbjects are used for displaying animations (lists of `pygame.Surface` in order).
To create it you need to input in the creator method:
- name: `str` - used for identification
- center_pos: `tuple[float,float]` - central position of your animation
- sprites: `list[pygame.Surface]` - list of your all frames of your animation
- fps: `int` - controls the speed of your animation in frames per second
- play_amount: `int` - number of repetitions of your animation, deafults to 0, when it's 0 the animation will reapet indefinitevly
