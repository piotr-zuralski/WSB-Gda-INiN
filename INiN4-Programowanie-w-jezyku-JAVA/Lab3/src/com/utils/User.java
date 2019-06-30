package com.utils;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Pattern;

public class User {

    @NotEmpty(message = "Username cannot be empty")
    @Pattern(regexp = "^([a-z])$", message="Username must contain only lowercase letters")
    private String username;

    @Email(message = "E-mail should be valid")
    private String email;

    @Pattern(regexp = "^([0-9]){9}$", message="Phone must contain exactly 9 numbers")
    private String phone;

    public User(String username, String email, String phone) {
        this.setUsername(username);
        this.setEmail(email);
        this.setPhone(phone);
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}
