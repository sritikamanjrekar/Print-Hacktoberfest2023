import java.util.concurrent.ArrayBlockingQueue;

class Main {
    public static void main(String[] args) {
        ArrayBlockingQueue<String> animals = new ArrayBlockingQueue<>(5);

        animals.add("Dog");
        animals.add("Cat");
        animals.add("Horse");
        System.out.println("ArrayBlockingQueue: " + animals);

        // Using remove()
        String element1 = animals.remove();
        System.out.println("Removed Element:");
        System.out.println("Using remove(): " + element1);

        // Using poll()
        String element2 = animals.poll();
        System.out.println("Using poll(): " + element2);

        // Using clear()
        animals.clear();
        System.out.println("Updated ArrayBlockingQueue: " + animals);
    }
}
