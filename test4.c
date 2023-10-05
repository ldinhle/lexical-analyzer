bool isEven(int number) {
    if (number % 2 == 0) {
        return true;
    } else {
        return false;
    }
}

int main() {
    bool result = isEven(4);
    if (result) {
        print "Even";
    } else {
        print "Odd";
    }
    return 0;
}
