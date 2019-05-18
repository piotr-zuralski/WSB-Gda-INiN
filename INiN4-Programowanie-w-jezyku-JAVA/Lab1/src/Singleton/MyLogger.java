package lab_1.Singleton;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public final class MyLogger {

    private String path;

    private static final String DATETIME_FORMAT = "HH:mm:ss dd/MM/yyyy";

    private static MyLogger instance = null;

    public static MyLogger getInstance() {
        if (instance == null) {
            instance = new MyLogger();
        }
        return instance;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    private MyLogger() { }

    private MyLogger(String _path) {
        this.path = _path;
    }

    private void appendToFile(String content) throws IOException {
        FileWriter fileWriter = new FileWriter(this.path, true);
        PrintWriter printWriter = new PrintWriter(fileWriter);
        printWriter.println(content);
        printWriter.close();
    }

    private String formatDate()
    {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(DATETIME_FORMAT);
        return now.format(formatter);
    }

    void addReport(String reportContent) throws IOException {
        String content = formatDate() + " " + reportContent;
        appendToFile(content);
    }
}
