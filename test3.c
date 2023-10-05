float computeArea(float radius) {
    float pi = 3.14159;
    return pi * radius * radius;
}

int main() {
    float area = computeArea(10.5);
    print area;
    return 0;
}