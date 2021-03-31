package kr.or.ddit;

public class RamdaTesting {
	public static void main(String[] args) {
		Person
	}
}
@FunctionalInterface
interface Say{
	int someting(int a, int b);
}

class Person{
	public void hi(Say line) {
		int number = line.someting(3, 5);
		System.out.println("Number is " + number);
	}
}