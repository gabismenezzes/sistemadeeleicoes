
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner ler = new Scanner(System.in);
        Retangulo Base = new Retangulo();
        Retangulo Altura = new Retangulo();
        Retangulo Calculo = new Retangulo();

        System.out.println("base: ");
        double ReceberBase = ler.nextDouble();
        Base.setbase(ReceberBase);

        System.out.println("altura:");
        double ReceberAltura = ler.nextDouble();
        Altura.setAltura(ReceberAltura);

        System.out.printf("O valor da área é: ", Calculo);
    }

}
