package lab_1.Factory;

abstract class Animal {

    private String name = "";

    public void Animal(String name) {
        this.name = name;
    }

    abstract String makeSound();

}
