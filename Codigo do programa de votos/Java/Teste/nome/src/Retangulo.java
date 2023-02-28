import java.util.Scanner;

public class Retangulo {

    double base;
    double altura;
    double calculo;

    public Retangulo() {
        base = 0;
        altura = 0;
        calculo = 0;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double ler) {
        this.base = ler;
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public double getCalculo() {
        return base * altura;
    }

    public void setCalculo(double calculo) {
        this.calculo = calculo;
    }

    public double Calculo() {
        calculo = base * altura;
        return calculo;
    }

    public void setbase(double i) {
    }

}
