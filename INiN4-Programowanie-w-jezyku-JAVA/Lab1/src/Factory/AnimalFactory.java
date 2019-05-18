package lab_1.Factory;

public class AnimalFactory {

    private static final String CROW = "Crow";
    private static final String LION = "Lion";
    private static final String WHALE = "Whale";

    public Animal AnimalFactory(String animalName) {
        Animal animal = null;

        switch (animalName) {
            case CROW:
                animal = new Crow();
                break;

            case LION:
                animal = new Lion();
                break;

            case WHALE:
                animal = new Whale();
                break;
        }

        return animal;

    }

}
