#include <GL/glut.h>
#include <vector>

// Define polygon vertices
std::vector<std::pair<float, float>> polygonVertices = {
    {8, 4}, {2, 4}, {0, 8}, {3, 12}, {7, 12}, {10, 8}
};

// Function to check if a point is inside the polygon (Even-Odd Rule Algorithm)
bool isInsidePolygon(float x, float y) {
    int count = 0;
    int n = polygonVertices.size();
    for (int i = 0, j = n - 1; i < n; j = i++) {
        float xi = polygonVertices[i].first, yi = polygonVertices[i].second;
        float xj = polygonVertices[j].first, yj = polygonVertices[j].second;

        if ((yi > y) != (yj > y) &&
            (x < (xj - xi) * (y - yi) / (yj - yi) + xi)) {
            count++;
        }
    }
    return (count % 2 == 1);
}

// Function to fill the polygon with green asterisks
void fillPolygonWithAsterisks() {
    glColor3f(0.0, 0.8, 0.0); // Green color
    glRasterPos2f(0, 0);
    
    for (float y = 4; y <= 12; y += 0.5) {
        for (float x = 0; x <= 10; x += 0.5) {
            if (isInsidePolygon(x, y)) {
                glRasterPos2f(x, y);
                glutBitmapCharacter(GLUT_BITMAP_9_BY_15, '*');
            }
        }
    }
}

// Function to draw the polygon outline
void drawPolygon() {
    glColor3f(1.0, 0.0, 0.0); // Red color
    glBegin(GL_POLYGON);
    for (auto& v : polygonVertices) {
        glVertex2f(v.first, v.second);
    }
    glEnd();
}

// Function to draw the scaled polygon
void drawScaledPolygon() {
    glPushMatrix();
    glScalef(2.0, 2.0, 1.0); // Scale by a factor of 2
    drawPolygon();
    glPopMatrix();
}

// Display function
void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw original polygon with fill
    glPushMatrix();
    glTranslatef(-5, -5, 0); // Adjust position for visibility
    drawPolygon();
    fillPolygonWithAsterisks(); // Fill interior with green asterisks
    glPopMatrix();

    // Draw scaled polygon
    glPushMatrix();
    glTranslatef(15, 0, 0); // Move right for better view
    drawScaledPolygon();
    glPopMatrix();

    glFlush();
}

// Initialize OpenGL settings
void init() {
    glClearColor(1, 1, 1, 1); // White background
    gluOrtho2D(-20, 20, -20, 20); // Coordinate system
}

// Main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(800, 800);
    glutCreateWindow("Polygon Scaling and Filling in OpenGL");

    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
