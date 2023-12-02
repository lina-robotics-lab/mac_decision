import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to get the inverse of a matrix
def inverse_matrix(matrix):
    matrix = np.array(matrix).T
    return np.linalg.inv(matrix)

def transform_point(point, matrix):
    # Transform the point using the matrix
    return np.dot(matrix, point)

def display():
    glLoadIdentity()
    glTranslatef(1.0, 2.0, 0.0)  # Apply translation
    glScalef(2.0, 2.0, 1.0)

    # Get the current modelview matrix
    matrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    # Calculate the inverse translation matrix
    inverse_transformation = inverse_matrix(matrix)
    print(inverse_transformation)

    # Real-world homogeneous coordinate you want to render (replace with your desired value)
    real_world_homogeneous_coord = np.array([2., 3., 1., 1.])  # Replace x, y, z, w with desired values

    # Transform the real-world coordinate to local space
    local_coord = transform_point(real_world_homogeneous_coord, inverse_transformation)
    print(local_coord)
    # Render the point at the transformed coordinate (local space)
    glBegin(GL_POINTS)
    glVertex4f(local_coord[0], local_coord[1], local_coord[2], local_coord[3])
    glEnd()

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Render Point in Real-world Coordinate")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
