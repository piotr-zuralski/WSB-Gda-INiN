package com.utils;

import com.google.gson.Gson;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import org.apache.hc.client5.http.ClientProtocolException;
import org.apache.hc.client5.http.classic.methods.HttpPost;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.io.entity.StringEntity;
import java.io.IOException;

public class Controller {

    @FXML()
    private TextField username;

    @FXML()
    private TextField email;

    @FXML()
    private TextField phone;

    private String INTEGRATION_URL = "https://jsonplaceholder.typicode.com/users";

    public void Clicked(ActionEvent event) throws ClientProtocolException, IOException {

        User user = new User(username.getText(), email.getText(), phone.getText());

        Gson gson = new Gson();
        String json = gson.toJson(user);

        CloseableHttpClient client = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost(INTEGRATION_URL);

        httpPost.setEntity(new StringEntity(json));
        httpPost.setHeader("Accept", "application/json");
        httpPost.setHeader("Content-type", "application/json");

        CloseableHttpResponse response = client.execute(httpPost);
        Integer httpStatus = response.getCode();
        client.close();
        Boolean isOK = (201 == httpStatus);

        System.out.println("isOK: " + isOK);
    }
}
