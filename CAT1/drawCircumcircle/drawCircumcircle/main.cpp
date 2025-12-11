// ======================================================
// OpenGL Program: Draw a Triangle and Its Circumscribed Circle
// ======================================================

#include <GL/glut.h>
#include <cmath>
#include <iostream>

// Define constant PI for angle calculations
#define PI 3.14159265358979323846

// ---------------------------------------------------------------------
// A simple structure to represent a 2D point with x and y coordinates.
// ---------------------------------------------------------------------
struct Point {
    float x, y;
};

// ---------------------------------------------------------------------
// Define the triangle vertices as given:
// A(-1,6), B(2,0), and C(-4,9)
// ---------------------------------------------------------------------
Point A = { -1.0f, 6.0f };
Point B = {  2.0f, 0.0f };
Point C = { -4.0f, 9.0f };

// ---------------------------------------------------------------------
// Function: computeCircumcenter
// Purpose: Given three points (forming a triangle), this function
// computes the circumcenter (center of the circumscribed circle)
// using the perpendicular bisector method.
// 
// "Think Pause": We use the formula
//   D = 2 * [ A.x*(B.y - C.y) + B.x*(C.y - A.y) + C.x*(A.y - B.y) ]
//   center.x = ( (A.x²+A.y²)*(B.y-C.y) + (B.x²+B.y²)*(C.y-A.y) + (C.x²+C.y²)*(A.y-B.y) ) / D
//   center.y = ( (A.x²+A.y²)*(C.x-B.x) + (B.x²+B.y²)*(A.x-C.x) + (C.x²+C.y²)*(B.x-A.x) ) / D
// ---------------------------------------------------------------------
Point computeCircumcenter(Point A, Point B, Point C) {
    float D = 2 * ( A.x*(B.y - C.y) + B.x*(C.y - A.y) + C.x*(A.y - B.y) );
    Point center;
    center.x = ((A.x*A.x + A.y*A.y) * (B.y - C.y) +
                (B.x*B.x + B.y*B.y) * (C.y - A.y) +
                (C.x*C.x + C.y*C.y) * (A.y - B.y)) / D;
    center.y = ((A.x*A.x + A.y*A.y) * (C.x - B.x) +
                (B.x*B.x + B.y*B.y) * (A.x - C.x) +
                (C.x*C.x + C.y*C.y) * (B.x - A.x)) / D;
    return center;
}

// ---------------------------------------------------------------------
// Utility Function: renderBitmapString
// Purpose: Draws a string at a given (x,y) location using GLUT bitmap fonts.
// ---------------------------------------------------------------------
void renderBitmapString(float x, float y, void *font, const char* string) {
    glRasterPos2f(x, y);
    for (const char* c = string; *c != '\0'; c++) {
        glutBitmapCharacter(font, *c);
    }
}

// ---------------------------------------------------------------------
// Function: drawAxes
// Purpose: For visual context, we draw the X-axis (in green) and Y-axis (in blue)
// across a wide range. Axes help in understanding the coordinate system.
// ---------------------------------------------------------------------
void drawAxes() {
    // X-axis in green
    glColor3f(0.0f, 1.0f, 0.0f);
    glBegin(GL_LINES);
        glVertex2f(-35, 0);
        glVertex2f(5, 0);
    glEnd();
    
    // Y-axis in blue
    glColor3f(0.0f, 0.0f, 1.0f);
    glBegin(GL_LINES);
        glVertex2f(0, -25);
        glVertex2f(0, 15);
    glEnd();
    
    // Label the axes for clarity
    glColor3f(0.0f, 0.0f, 0.0f);
    renderBitmapString(5.0f, -1.0f, GLUT_BITMAP_HELVETICA_12, "X");
    renderBitmapString(0.5f, 15.0f, GLUT_BITMAP_HELVETICA_12, "Y");
}

// ---------------------------------------------------------------------
// Function: drawTriangle
// Purpose: Draws the triangle using the three vertices in a loop.
// "Think Pause": We choose GL_LINE_LOOP so the triangle is outlined.
// ---------------------------------------------------------------------
void drawTriangle() {
    // Set a distinct color (magenta) for the triangle outline
    glColor3f(1.0f, 0.0f, 1.0f);
    glBegin(GL_LINE_LOOP);
        glVertex2f(A.x, A.y);
        glVertex2f(B.x, B.y);
        glVertex2f(C.x, C.y);
    glEnd();
    
    // Label the vertices with their coordinates
    glColor3f(0.0f, 0.0f, 0.0f); // Black for text
    renderBitmapString(A.x, A.y, GLUT_BITMAP_HELVETICA_12, "A(-1,6)");
    renderBitmapString(B.x, B.y, GLUT_BITMAP_HELVETICA_12, "B(2,0)");
    renderBitmapString(C.x, C.y, GLUT_BITMAP_HELVETICA_12, "C(-4,9)");
}

// ---------------------------------------------------------------------
// Function: drawCircumcircle
// Purpose: Draws the circumcircle (circle passing through the triangle's vertices)
// using the computed center and radius.
// "Think Pause": We use GL_LINE_LOOP with many segments to approximate a smooth circle.
// ---------------------------------------------------------------------
void drawCircumcircle(Point center, float radius) {
    // Set the drawing color to red (RGB: 1.0, 0.0, 0.0)
    glColor3f(1.0f, 0.0f, 0.0f);
    int num_segments = 200;  // Increase for smoother appearance
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < num_segments; i++) {
        // Calculate the angle for this segment
        float theta = 2.0f * PI * float(i) / float(num_segments);
        // Compute (x,y) position on the circle's circumference
        float x = radius * cosf(theta);
        float y = radius * sinf(theta);
        // Specify the vertex (translated by the circle's center)
        glVertex2f(center.x + x, center.y + y);
    }
    glEnd();
    
    // Optionally, mark the circle's center with a label "O"
    glColor3f(0.0f, 0.0f, 0.0f);
    renderBitmapString(center.x, center.y, GLUT_BITMAP_HELVETICA_12, "O");
}

// ---------------------------------------------------------------------
// Function: display
// Purpose: The main display callback where we clear the window,
// draw axes, the triangle, compute the circumcenter, and draw the circumcircle.
// ---------------------------------------------------------------------
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    
    // 1. Draw coordinate axes for reference.
    drawAxes();
    
    // 2. Draw the triangle.
    drawTriangle();
    
    // 3. Compute the circumcenter (center of the circumscribed circle)
    // "Pause and Think": Use the computed formulas to determine the center.
    Point center = computeCircumcenter(A, B, C);
    
    // Compute the circle's radius as the distance from the center to any vertex (A in this case).
    float radius = sqrtf((center.x - A.x) * (center.x - A.x) +
                         (center.y - A.y) * (center.y - A.y));
    
    // 4. Draw the circumcircle in red.
    drawCircumcircle(center, radius);
    
    glFlush();
}

// ---------------------------------------------------------------------
// Function: reshape
// Purpose: Adjust the viewport and set up a logical coordinate system
// that is scaled to include the entire triangle and the circle.
// ---------------------------------------------------------------------
void reshape(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // Set an orthographic projection that covers all drawing elements.
    gluOrtho2D(-35, 5, -25, 15);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

// ---------------------------------------------------------------------
// Function: main
// Purpose: Standard GLUT initialization, creating the window, and
// registering the callback functions.
// ---------------------------------------------------------------------
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    // Use single buffering and RGB color mode.
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(800, 600);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Triangle and Its Circumcircle");
    
    // Set the background to white.
    glClearColor(1.0, 1.0, 1.0, 1.0);
    
    // Register the display and reshape callback functions.
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    
    // Enter the GLUT event loop.
    glutMainLoop();
    return 0;
}
