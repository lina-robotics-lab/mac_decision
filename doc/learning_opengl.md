# OPENGL

Got an error saying
```
OpenGL.error.NullFunctionError: Attempt to call an undefined function glutInit,
```
Only need to run 
```bash
conda install -c conda-forge freeglut
```

## handling open gl error

```bash
conda install -c conda-forge libffi
```
from [this stackoverflow post](https://stackoverflow.com/a/76557173)

## OpenGL transformation
After doing the transformation by `glTranslatef` and `glScalef`, the screen frame directly change to real frame.