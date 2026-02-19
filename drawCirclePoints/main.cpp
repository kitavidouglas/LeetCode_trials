#include <GL/glut.h>
#include <iostream>
#include <cmath>

// Conversion factor: 1 centimeter = 0.1 OpenGL units.
const float CM_TO_GL = 0.1f;

// Circle parameters (in OpenGL coordinate units)
const float centerX = 1.0f;  // Circle center x-coordinate (starting point)
const float centerY = 1.0f;  // Circle center y-coordinate (starting point)
const float circleRadius = 4.0f * CM_TO_GL;  // 4 centimeters

// Utility: Draw a string using GLUT bitmap fonts at a given raster position.
void drawString(void *font, const char* str, float x, float y) {
    glRasterPos2f(x, y);
    for (const char* c = str; *c != '\0'; c++) {
        glutBitmapCharacter(font, *c);
    }
}

// Plot the unique symmetric points for the circle.
// 'x' and 'y' are in centimeter grid units; we convert them using CM_TO_GL.
// We avoid duplicates by checking for conditions when points coincide.
void plotCirclePoints(int x, int y) {
    // Case 1: When x == 0, only 4 unique points exist.
    if (x == 0) {
        glVertex2f(centerX, centerY + y * CM_TO_GL); // Top
        glVertex2f(centerX, centerY - y * CM_TO_GL); // Bottom
        glVertex2f(centerX + y * CM_TO_GL, centerY); // Right
        glVertex2f(centerX - y * CM_TO_GL, centerY); // Left
    }
    // Case 2: When x == y, points along the 45° line appear only once.
    else if (x == y) {
        glVertex2f(centerX + x * CM_TO_GL, centerY + y * CM_TO_GL);
        glVertex2f(centerX - x * CM_TO_GL, centerY + y * CM_TO_GL);
        glVertex2f(centerX + x * CM_TO_GL, centerY - y * CM_TO_GL);
        glVertex2f(centerX - x * CM_TO_GL, centerY - y * CM_TO_GL);
    }
    // Case 3: Otherwise, plot all eight distinct symmetric points.
    else {
        glVertex2f(centerX + x * CM_TO_GL, centerY + y * CM_TO_GL);
        glVertex2f(centerX - x * CM_TO_GL, centerY + y * CM_TO_GL);
        glVertex2f(centerX + x * CM_TO_GL, centerY - y * CM_TO_GL);
        glVertex2f(centerX - x * CM_TO_GL, centerY - y * CM_TO_GL);
        glVertex2f(centerX + y * CM_TO_GL, centerY + x * CM_TO_GL);
        glVertex2f(centerX - y * CM_TO_GL, centerY + x * CM_TO_GL);
        glVertex2f(centerX + y * CM_TO_GL, centerY - x * CM_TO_GL);
        glVertex2f(centerX - y * CM_TO_GL, centerY - x * CM_TO_GL);
    }
}


// Bresenham's circle drawing algorithm.
void drawCircle() {
    int x = 0;
    // Calculate the radius in integer “cm grid units” (should be 4).
    int y = static_cast<int>(circleRadius / CM_TO_GL);
    int d = 3 - 2 * y;  // Initial decision parameter

    glBegin(GL_POINTS);
    while (x <= y) {
        plotCirclePoints(x, y);
        if (d < 0) {
            d += 4 * x + 6;
        } else {
            d += 4 * (x - y) + 10;
            y--;
        }
        x++;
    }
    glEnd();
}

// ---------------------------------------------------------------------
// Draw a filled circle using a triangle fan.
// (This function approximates the filled circle and is used after applying the rotation.)
void drawFilledCircle() {
    const int numSegments = 100; // Increase for a smoother circle approximation
    glBegin(GL_TRIANGLE_FAN);
        // Center of circle
        glVertex2f(centerX, centerY);
        // Points on the circumference.
        for (int i = 0; i <= numSegments; i++) {
            float angle = 2.0f * 3.14159265f * i / numSegments;
            float x = centerX + circleRadius * cos(angle);
            float y = centerY + circleRadius * sin(angle);
            glVertex2f(x, y);
        }
    glEnd();
}

// ---------------------------------------------------------------------
// Draw coordinate axes with distinct colors and label them.
void drawAxes() {
    glLineWidth(1.5f);
    
    // Draw X-axis in blue.
    glColor3f(0.0f, 0.0f, 1.0f);  
    glBegin(GL_LINES);
        glVertex2f(-1.0f, 0.0f);
        glVertex2f(1.5f, 0.0f);
    glEnd();
    
    // Draw Y-axis in green.
    glColor3f(0.0f, 0.5f, 0.0f);  
    glBegin(GL_LINES);
        glVertex2f(0.0f, -1.0f);
        glVertex2f(0.0f, 1.5f);
    glEnd();

    // Label the axes with black text.
    glColor3f(0.0f, 0.0f, 0.0f);
    drawString(GLUT_BITMAP_HELVETICA_12, "X", 1.45f, 0.05f);
    drawString(GLUT_BITMAP_HELVETICA_12, "Y", 0.05f, 1.45f);
}

// ---------------------------------------------------------------------
// Mark and label the circle's center (starting point) for clarity.
void drawCenterLabel() {
    glPointSize(6.0f);
    glColor3f(0.5f, 0.0f, 0.5f);  // Purple color for the center
    glBegin(GL_POINTS);
        glVertex2f(centerX, centerY);
    glEnd();
    
    // Label the center with its coordinates.
    glColor3f(0.0f, 0.0f, 0.0f);  
    drawString(GLUT_BITMAP_HELVETICA_12, "(1,1)", centerX + 0.02f, centerY + 0.02f);
}

// ---------------------------------------------------------------------
// Display callback: clears the screen, draws the axes, and then renders two versions of the circle:
// 1. The original circle outline drawn using Bresenham's algorithm.
// 2. The rotated (60° clockwise) filled circle.
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    
    drawAxes();

    // -------------------------------
    // (A) Draw the original circle using Bresenham's algorithm (outline)
    glPointSize(3.0f);
    glColor3f(0.0f, 0.0f, 0.0f);  // Black outline for contrast
    drawCircle();
    
    // -------------------------------
    // (B) Draw the rotated and filled circle:
    // Use transformation functions to rotate the circle 60° clockwise about its center.
    glPushMatrix();
        // Translate so the circle's center becomes the origin.
        glTranslatef(centerX, centerY, 0.0f);
        // Rotate -60° (clockwise).
        glRotatef(-60.0f, 0.0f, 0.0f, 1.0f);
        // Translate back.
        glTranslatef(-centerX, -centerY, 0.0f);
        
        // Set the fill color to red (#ff0000).
        glColor3f(1.0f, 0.0f, 0.0f);
        drawFilledCircle();
    glPopMatrix();
    
    drawCenterLabel();
    
    glFlush();
}

// ---------------------------------------------------------------------
// OpenGL initialization: set the background color and coordinate system.
void init() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);  // White background
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // Adjust the orthographic projection to include the circle and axes.
    gluOrtho2D(-1.0, 1.5, -1.0, 1.5);
}

// ---------------------------------------------------------------------
// Main function: initialize GLUT, set up callbacks, and start the main loop.
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Bresenham Circle with Rotation and Fill");
    
    init();
    glutDisplayFunc(display);
    glutMainLoop();
    
    return 0;
}
