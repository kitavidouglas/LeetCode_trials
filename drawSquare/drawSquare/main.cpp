#include <GL/glut.h>
#include <cmath>
#include <sstream>
#include <string>

#define PI 3.14159265
#define DEG_TO_RAD(angle) ((angle) * PI / 180.0)

// Function to render text at given coordinates
void renderText(float x, float y, std::string text) {
    glRasterPos2f(x, y);
    for (char c : text) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, c);
    }
}

// Function to rotate a point (x, y) around a pivot (cx, cy) by angle theta
void rotatePoint(float x, float y, float cx, float cy, float theta, float &newX, float &newY) {
    float rad = DEG_TO_RAD(theta);
    float cosTheta = cos(rad);
    float sinTheta = sin(rad);

    // Translate point to origin, rotate, then translate back
    newX = cosTheta * (x - cx) - sinTheta * (y - cy) + cx;
    newY = sinTheta * (x - cx) + cosTheta * (y - cy) + cy;
}

// Function to draw a square and label its points
void drawSquare(float x1, float y1, float x2, float y2, 
                float x3, float y3, float x4, float y4, std::string label) {
    glBegin(GL_LINE_LOOP);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
        glVertex2f(x3, y3);
        glVertex2f(x4, y4);
    glEnd();

    // Label the coordinates
    renderText(x1, y1, label + "A(" + std::to_string((int)x1) + "," + std::to_string((int)y1) + ")");
    renderText(x2, y2, label + "B(" + std::to_string((int)x2) + "," + std::to_string((int)y2) + ")");
    renderText(x3, y3, label + "C(" + std::to_string((int)x3) + "," + std::to_string((int)y3) + ")");
    renderText(x4, y4, label + "D(" + std::to_string((int)x4) + "," + std::to_string((int)y4) + ")");
}

// Function to draw coordinate axes
void drawAxes() {
    glBegin(GL_LINES);
        glColor3f(0.0, 0.0, 0.0); // Black axes
        glVertex2f(-10, 0); glVertex2f(10, 0); // X-axis
        glVertex2f(0, -10); glVertex2f(0, 10); // Y-axis
    glEnd();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    drawAxes(); // Draw reference axes

    // Draw original square in red
    glColor3f(1.0, 0.0, 0.0);
    drawSquare(0, 4, 3, 4, 4, 0, 0, 0, "");

    // Draw translated square in blue
    glColor3f(0.0, 0.0, 1.0);
    drawSquare(2, 6, 5, 6, 6, 2, 2, 2, "T");

    // Rotate translated square by 55º
    float cx = 3.75, cy = 4;  // Center of translated square

    float x1, y1, x2, y2, x3, y3, x4, y4;
    rotatePoint(2, 6, cx, cy, 55, x1, y1);
    rotatePoint(5, 6, cx, cy, 55, x2, y2);
    rotatePoint(6, 2, cx, cy, 55, x3, y3);
    rotatePoint(2, 2, cx, cy, 55, x4, y4);

    // Draw rotated square in green
    glColor3f(0.0, 1.0, 0.0);
    drawSquare(x1, y1, x2, y2, x3, y3, x4, y4, "R");

    glFlush();
}

void init() {
    glClearColor(1, 1, 1, 1);
    gluOrtho2D(-10, 10, -10, 10); // Scale the coordinate system
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(600, 600);
    glutCreateWindow("OpenGL Square Rotation by 55°");

    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
