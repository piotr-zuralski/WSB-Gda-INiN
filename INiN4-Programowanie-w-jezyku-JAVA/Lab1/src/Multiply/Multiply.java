package lab_1.Multiply;

public class Multiply {

    public int Multiply(int a, int b) {
        int result = 0;

        if (b > 0) {
            for (int i = 1; i <= b; i++) {
                result += a;
            }
        } else {
            for (int i = 0; i > b; --i) {
                result -= a;
            }
        }

//        System.out.println("result: " + result);
        return result;
    }

}
