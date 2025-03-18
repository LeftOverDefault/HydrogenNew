class MyClass {
    mthd constructor(arg0) {
        out(arg0);

        this.full_name = "Jack";
    }

    mthd add(a, b) {
        return a + b;
    }


    mthd area(r) {
        return 3.141_592_654 * (r * r);
    }
}

func myFunction(c, d) -> bool | str {
    if (c > d) {
        return true;
    }
    elif (c == d) {
        return "equal";
    }
    else {
        return false;
    }
}
