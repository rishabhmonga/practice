package LambdaTry;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * Created by rism on 2/5/15.
 */
public class LambdaTry {
    private Collection<Person> gatherPersons() {
        List<Person> population = new ArrayList<Person>();
        for(int i=0; i<100;i++){
            population.add(new Person(i));
        }
        return population;
    }

    public static void main(String[] args) {

    }

    private void processPeople(){
        gatherPersons();
    }


}

interface Predicate<T> {
    Boolean test(T t);
}

class Person {
    public String name;
    public int age;
    public Gender sex;

    public Person(int age) {
        this.name = setName();
        this.age = age;
        this.sex = setGender();
    }

    public Gender getSex() {
        return sex;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    private String setName(){
        return Letter.randomLetter().toString() + Letter.randomLetter().toString();
    }

    private Gender setGender(){
        return Gender.randomGender();
    }
}

enum Gender {
    male, female;

    private static final List<Gender> VALUES = Collections.unmodifiableList(Arrays.asList(values()));
    private static final int SIZE = VALUES.size();
    private static final Random RANDOM = new Random();

    public static Gender randomGender() {
        return VALUES.get(RANDOM.nextInt(SIZE));
    }
}

enum Letter {
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, w, x, y, z;

    private static final List<Letter> VALUES = Collections.unmodifiableList(Arrays.asList(values()));
    private static final int SIZE = VALUES.size();
    private static final Random RANDOM = new Random();

    public static Letter randomLetter() {
        return VALUES.get(RANDOM.nextInt(SIZE));
    }
}