package Q3;


public class Employee {

    String name;
    double grossSalary;
    double tax;




    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getGrossSalary() {
        return grossSalary;
    }

    public void setGrossSalary(double grossSalary) {
        this.grossSalary = grossSalary;
    }

    public double getTax() {
        return tax;
    }

    public void setTax(double tax) {
        this.tax = tax;
    }



    public double NetSalary() {
        return grossSalary - tax;
        
    }

    public void increaseSalary(double percentage) {
        grossSalary = grossSalary + (grossSalary * (percentage / 100));
        
    }
    

    @Override
    public String toString() {
        return name + ", "+"R$ " + NetSalary();
    }
}
