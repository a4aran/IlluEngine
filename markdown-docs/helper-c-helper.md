There's a class **Helper** in Illu and the engine automatically creates an object of it called `c_helper`. You don't need to make another one as everything inside that class is static.

## Methods and classes

### Button Base
`button_base` method is used for creating new custom buttons. It is meant to be placed while creating new button class like:
```
class NewBTN(c_helper.button_base()):
  ...
```
