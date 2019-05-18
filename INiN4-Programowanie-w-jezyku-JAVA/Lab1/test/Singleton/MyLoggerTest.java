package test.lab_1.Singleton;

import junit.framework.TestCase;
import lab_1.Singleton.MyLogger;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.UUID;

class MyLoggerTest extends TestCase {

    private MyLogger logger = null;
    private String LoggerPath = "/srv/zuralski/WSB-Java/out/test.txt";

    @BeforeEach
    protected void setUp() {
        this.logger = MyLogger.getInstance();
    }

    @AfterEach
    protected void tearDown() {
        this.logger = null;
    }

    @Test
    void getInstance() {
        MyLogger logger1 = MyLogger.getInstance();
        logger1.setPath(this.LoggerPath);

        MyLogger logger2 = MyLogger.getInstance();
        assertSame(this.LoggerPath, logger2.getPath());
        assertSame(logger1, logger2);

        MyLogger logger3 = MyLogger.getInstance();
        assertSame(this.LoggerPath, logger3.getPath());
        assertSame(logger1, logger3);
    }

    @Test
    void getPath() {
        String path = "/sdfsdf/sdf/sf/sdfsd/fsf/sf/sd";
        logger.setPath(path);
        assertEquals(path, logger.getPath());
    }

    @Test
    void setPath() {
        String path = "/sdfsdf/sdf/sf/sdfsd/fsf/sf/sd";
        logger.setPath(path);
        assertEquals(path, logger.getPath());
    }

    @Test
    void addReport() throws IOException {
        logger.setPath(this.LoggerPath);
        String reportContent = UUID.randomUUID().toString();
        logger.addReport(reportContent);

        BufferedReader input = new BufferedReader(new FileReader(this.LoggerPath));
        String last = "";
        String line;

        while ((line = input.readLine()) != null) {
            last = line;
        }

        assertTrue(last.contains(reportContent));
    }
}