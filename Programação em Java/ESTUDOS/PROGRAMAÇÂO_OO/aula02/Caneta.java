package PROGRAMAÇÂO_OO.aula02;

public class Caneta {
    public String modelo;
    public String cor;
    private float ponta;
    protected int carga;
    protected boolean tampada;

    public void escrever(){
        System.out.println("Escrevendo\n");
    }

    public void rabiscar() {   
        if (this.tampada == true){
            System.out.println("Erro: Não posso rabiscar");
        } else{
            System.out.println("Estou rabiscando");
        }
    }

    public void status(){
        System.out.println("Cor da caneta: "+this.cor +
        "\nPonta da caneta: "+ this.ponta+
        "\nEstá tampada? "+this.tampada+
        "\nModelo: "+ this.modelo+
        "\nCarga: "+ this.carga);
    }

    public void tampar() {
        this.tampada = true;
        
    }

    public void destampar() {
        this.tampada = false;

    }
    
}
