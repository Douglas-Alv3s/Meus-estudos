package PROGRAMAÇÂO_OO.aula04.EXercicioBanco;

public class ContaBanco {
    public int numconta;
    protected String tipo;
    private String dono;
    private float saldo;
    private boolean status;

    public ContaBanco(){
        setSaldo(0); 
        setStatus(false);
    }

    public int getNumconta() {
        return numconta;
    }

    public void setNumconta(int numconta) {
        this.numconta = numconta;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        if ((tipo.equals("cc"))||(tipo.equals("cp"))){
            if (tipo.equals("cc")){
                System.out.println("CONTA CORRENTE");
                setSaldo(50);
                this.tipo = tipo;

            }else{
                System.out.println("CONTA POUPANÇA");
                setSaldo(150);
                this.tipo = tipo;
            }
        }else{
            System.out.println("ERRO: TIPO DE CONTA INVALIDO");
        }
    }

    public String getDono() {
        return dono;
    }

    public void setDono(String dono) {
        this.dono = dono;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void abrirConta(int numeroconta, String tipoconta, String donoo){
        setNumconta(numeroconta);
        setTipo(tipoconta);
        setDono(donoo);

        if((this.numconta != 0) && (this.tipo != null) && (this.status ==false) && (this.dono != null)){
            setStatus(true);
            System.out.println("Conta Aberta");
        } else{
            System.out.println("ERRO");
        }
    }

    public void fecharConta(){
        if(this.saldo > 0){
            System.out.println("Conta com dinheiro");
        } else if (this.saldo<0){
            System.out.println("Conta em debito");
        }else{
            setStatus(false);
        }
    }

    public void depositar(float deposito){
        if (this.status==true){
            this.saldo += deposito;
        } else{
            System.out.println("Não existe conta aberta");
        }

    }

    public void sacar(float sacado){
        if(this.status == true){
            if(this.saldo >= sacado){
                System.out.println("\nSacado: "+sacado);
                this.saldo -= sacado;
            }else{
                System.out.println("Saldo Insuficiente");
            }
        }else{
            System.out.println("Não existe conta aberta");
        }

    }

    public void pagarMensal(){
        if (this.status==true){
            float juros;
            if (this.tipo.equals("cc")){
                juros = 12f;
                this.saldo -= juros;
                System.out.println("Juros mensal cobrado R$12.00");
            } else {
                juros = 20f;
                this.saldo -= juros;
                System.out.println("Juros mensal cobrado R$20.00");
                 
            }

        }else{
            System.out.println("Não existe conta aberta");
        }
    }

    public void estadoAtual(){
        System.out.println("----------------------------");
        System.out.println("Conta: " + this.getNumconta());
        System.out.println("Tipo: " + this.getTipo());
        System.out.println("Dono: " + this.getDono());
        System.out.println("Saldo: " + this.getSaldo());
        System.out.println("Status: " + this.isStatus());
    }
    
}
