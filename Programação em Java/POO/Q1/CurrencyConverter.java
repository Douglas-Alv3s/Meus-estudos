package Q1;
public class CurrencyConverter {
    private double dollar;
    private double quantia;

    public double getDollar() {
        return this.dollar;
    } 

    public double getQuantia() {
        return this.quantia;
    }

    public double setDollar(double dollar) {
        return this.dollar = dollar;
    }

    public double setQuantia(double quantia) {
        return this.quantia = quantia;
    }

    public static double dollarToReal(double quantia, double dollar) {
        double resultado = quantia  * dollar;
        double IOF = resultado * 0.06;
        double result_finish = resultado + IOF;
        return result_finish;
    }
    
}
