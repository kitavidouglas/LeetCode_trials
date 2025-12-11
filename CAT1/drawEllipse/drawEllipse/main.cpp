#include <GL/glut.h>
#include <cmath>
#include <stack>
#include <iostream>

const int windowWidth = 600, windowHeight = 600;
float leftCoord = -10.0f, rightCoord = 10.0f;
float bottomCoord = -10.0f, topCoord = 10.0f;

// **Function to draw coordinate axes**
void drawAxes() {
    glColor3f(0.0f, 1.0f, 0.0f);  // Green X-axis
    glBegin(GL_LINES);
    glVertex2f(leftCoord, 0.0f); glVertex2f(rightCoord, 0.0f);
    glEnd();
    
    glColor3f(0.0f, 0.0f, 1.0f);  // Blue Y-axis
    glBegin(GL_LINES);
    glVertex2f(0.0f, bottomCoord); glVertex2f(0.0f, topCoord);
    glEnd();
}

// **Function to draw an ellipse using the Midpoint Algorithm**
void drawEllipse() {
    int rx = 6, ry = 5;  
    int xc = 2, yc = -1; 

    int x = 0, y = ry;
    float d1 = ry * ry - rx * rx * ry + 0.25 * rx * rx;

    glColor3f(0.0f, 0.0f, 0.0f);  // Black ellipse border
    glBegin(GL_POINTS);

    while (2 * ry * ry * x <= 2 * rx * rx * y) {
        glVertex2i(xc + x, yc + y);
        glVertex2i(xc - x, yc + y);
        glVertex2i(xc + x, yc - y);
        glVertex2i(xc - x, yc - y);

        if (d1 < 0)
            d1 += 2 * ry * ry * (x + 1) + ry * ry;
        else {
            d1 += 2 * ry * ry * (x + 1) - 2 * rx * rx * (y - 1) + rx * rx;
            y--;
        }
        x++;
    }

    float d2 = (ry * ry) * (x + 0.5) * (x + 0.5) + (rx * rx) * (y - 1) * (y - 1) - (rx * rx * ry * ry);

    while (y >= 0) {
        glVertex2i(xc + x, yc + y);
        glVertex2i(xc - x, yc + y);
        glVertex2i(xc + x, yc - y);
        glVertex2i(xc - x, yc - y);

        if (d2 > 0)
            d2 += -2 * rx * rx * y + rx * rx;
        else {
            d2 += 2 * ry * ry * (x + 1) - 2 * rx * rx * y + rx * rx;
            x++;
        }
        y--;
    }

    glEnd();
}

// **Function to match colors with tolerance**
bool colorMatch(const float c1[3], const float c2[3]) {
    return (fabs(c1[0] - c2[0]) < 0.01f &&
            fabs(c1[1] - c2[1]) < 0.01f &&
            fabs(c1[2] - c2[2]) < 0.01f);
}

// **Iterative Flood-Fill Algorithm (Stack-based, 4-connected)**
void floodFill(int x, int y, const float fillColor[3], const float borderColor[3]) {
    std::stack<std::pair<int, int>> pixelStack;
    pixelStack.push({x, y});

    while (!pixelStack.empty()) {
        auto [px, py] = pixelStack.top();
        pixelStack.pop();

        if (px < 0 || px >= windowWidth || py < 0 || py >= windowHeight) continue;

        float currentColor[3];
        glReadPixels(px, py, 1, 1, GL_RGB, GL_FLOAT, currentColor);

        if (colorMatch(currentColor, borderColor) || colorMatch(currentColor, fillColor)) continue;

        glColor3fv(fillColor);
        glBegin(GL_POINTS);
        glVertex2i(px, py);
        glEnd();
        glFlush();

        pixelStack.push({px + 1, py});
        pixelStack.push({px - 1, py});
        pixelStack.push({px, py + 1});
        pixelStack.push({px, py - 1});
    }
}

// **Convert world coordinates to pixel coordinates**
int worldToWindowX(float x) {
    return (int)((x - leftCoord) * windowWidth / (rightCoord - leftCoord));
}

int worldToWindowY(float y) {
    return (int)((y - bottomCoord) * windowHeight / (topCoord - bottomCoord));
}

// **Display Function**
void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    drawAxes();
    drawEllipse();
    glFlush();

    // **Save Projection**
    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();
    gluOrtho2D(0, windowWidth, 0, windowHeight);

    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glLoadIdentity();

    float fillColor[3] = {1.0f, 0.647f, 0.0f};  // Orange (#FFA500)
    float borderColor[3] = {0.0f, 0.0f, 0.0f};  // Black

    int seedX = worldToWindowX(2.0f);
    int seedY = worldToWindowY(-1.0f);

    floodFill(seedX, seedY, fillColor, borderColor);

    // **Restore Projection**
    glMatrixMode(GL_PROJECTION);
    glPopMatrix();
    glMatrixMode(GL_MODELVIEW);
    glPopMatrix();

    glutSwapBuffers();
}

// **Reshape Function**
void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(leftCoord, rightCoord, bottomCoord, topCoord);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

// **Initialization Function**
void init() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);  // White background
    glPointSize(2.0f);  
}

// **Main Function**
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(windowWidth, windowHeight);
    glutCreateWindow("Midpoint Ellipse with Flood Fill");

    init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);

    glutMainLoop();
    return 0;
}
