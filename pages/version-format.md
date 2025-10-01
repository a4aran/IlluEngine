Version Format looks like this: X.Y.Z.Q

- `X` - Release official version 
- `Y` - Pre-release version
- `Z` - Alpha-release / Update
- `Q` - Minor update

Versions below `0.1.0.0` have tags `su` or `up` which respectively mean _semi-updatable_ and _updatable_. If version below `0.1.0.0` does not have tag like that it means it's hard to update the engine to the next version.

`Q` part of the version can have letter at the end which mean they are really minor fixes. There's `a` at the end by default if there are no letters, this means that version `X.X.X.1` and `X.X.X.1b` have one minor/fix difference.
