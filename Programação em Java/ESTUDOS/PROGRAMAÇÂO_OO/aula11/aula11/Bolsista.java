package aula11;

public final class Bolsista extends Aluno{
    private int bolsa;

    public Bolsista(int bolsa) {
        this.bolsa = bolsa;
    }

    public void renovarBolsa(){
        System.out.println("Bolsa de R$"+this.bolsa+" renovada");
    }

    @Override
    public void pagarMensalidade(){
        System.out.println("Pagamento Realizado via bolsista");
        
    }
    
}
