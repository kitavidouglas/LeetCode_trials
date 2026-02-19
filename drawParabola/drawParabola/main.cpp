#include <GL/glut.h>
#include <cmath>
#include <iostream>

// Window settings
const int windowWidth = 600, windowHeight = 600;
float leftCoord = -10.0f, rightCoord = 10.0f;
float bottomCoord = -10.0f, topCoord = 10.0f;

// Function to render text at a given position
void drawText(const char* text, float x, float y) {
    glRasterPos2f(x, y);
    while (*text) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, *text);
        text++;
    }
}

// Function to draw axes with labels
void drawAxes() {
    glColor3f(0, 0, 0);  // Black color for axes
    glLineWidth(1.5);
    
    glBegin(GL_LINES);
        // X-axis
        glVertex2f(leftCoord, 0);
        glVertex2f(rightCoord, 0);
        
        // Y-axis
        glVertex2f(0, bottomCoord);
        glVertex2f(0, topCoord);
    glEnd();

    // Labels for axes
    drawText("+X", rightCoord - 1.0f, 0.5f);
    drawText("-X", leftCoord + 0.5f, 0.5f);
    drawText("+Y", 0.5f, topCoord - 1.0f);
    drawText("-Y", 0.5f, bottomCoord + 0.5f);
    drawText("0", -0.5f, -0.5f);
}

// Function to draw a smooth parabola x = y^2
void drawParabola() {
    glColor3f(1, 0, 0);  // Red color for the curve
    glLineWidth(2.0);

    glBegin(GL_LINE_STRIP);  // Using GL_LINE_STRIP for a smooth curve

    for (float y = -3.0f; y <= 3.0f; y += 0.05f) { // Smaller step for smoothness
        float x = y * y;
        glVertex2f(x, y);
    }

    glEnd();
}

// Display function
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    drawAxes();
    drawParabola();
    glFlush();
}

// Reshape function
void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(leftCoord, rightCoord, bottomCoord, topCoord);
    glMatrixMode(GL_MODELVIEW);
}

// Initialization
void init() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
}

// Main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(windowWidth, windowHeight);
    glutCreateWindow("Smooth Parabola - x = y^2");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}
