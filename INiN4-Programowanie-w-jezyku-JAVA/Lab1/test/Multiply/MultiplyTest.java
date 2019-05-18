package test.lab_1.Multiply;

import junit.framework.Assert;
import junit.framework.TestCase;
import lab_1.Multiply.Multiply;
import org.junit.jupiter.api.Test;

class MultiplyTest extends TestCase {

    @Test
    void checkPositiveNumbers() {
        int a = 2;
        int b = 3;
        int test = a * b;
        int result = new Multiply(a, b);

        Assert.assertSame(test, result);
    }

    @Test
    void checkNegativeNumbers() {
        int a = 2;
        int b = -6;
        int test = a * b;
        int result = new Multiply(a, b);

        Assert.assertSame(test, result);
    }

}