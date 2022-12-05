package PROGRAMAÇÂO_OO.aula06;

public class ControleRemoto implements Controlador{
    // Atributos
    private int volume;
    private boolean ligado;
    private boolean tocando; 
    //Metodos Especiais

    
    public ControleRemoto() {
        this.volume = 50;
        this.ligado = false;
        this.tocando = false;
    }


    private int getVolume() {
        return volume;
    }


    private void setVolume(int volume) {
        this.volume = volume;
    }


    private boolean getLigado() {
        return ligado;
    }


    private void setLigado(boolean ligado) {
        this.ligado = ligado;
    }


    private boolean getTocando() {
        return tocando;
    }


    private void setTocando(boolean tocando) {
        this.tocando = tocando;
    }


    @Override
    public void ligar() {
        setLigado(true);
        
    }


    @Override
    public void desligar() {
        setLigado(false);
        
    }


    @Override
    public void abrirMenu() {
        if(this.getLigado()){
            System.out.println("-----MENU-----");
            System.out.println("Está ligado? "+ this.getLigado());
            System.out.println("Está Tocando? " + this.getTocando());
            System.out.println("Volume: "+ this.getVolume());
            for(int i =0; i <= this.getVolume(); i+=5){
                System.out.print("||");
            }
        }
    }


    @Override
    public void fecharMenu() {
        if(this.getLigado()){
            System.out.println("Menu fechado...");
        }
    }


    @Override
    public void maisVolume() {
        if(this.getLigado()){
            if (this.getVolume() < 100){
                this.setVolume(this.getVolume()+1);
                if (this.getVolume() > 0){
                    this.setTocando(true);
                }
                
            }
        }
    }


    @Override
    public void menosVolume() {
        if(this.getLigado()){
            if (this.getVolume() > 0){
                this.setVolume(this.getVolume()-1);
                if (this.getVolume() == 0){
                    this.setTocando(false);
                }
            }
        }
    }


    @Override
    public void ligarMudo() {
        if(this.getLigado()){
            if(getTocando()){
                setVolume(0);
                setTocando(false);
            }
        }
    }


    @Override
    public void desligarMudo() {
        if(this.getLigado()){
            if(!getTocando()){
                setVolume(50);
                setTocando(true);
            }    
        }
    }


    @Override
    public void play() {
        if((getLigado()) && !(getTocando())){
            setTocando(true);

        }
        
    }


    @Override
    public void pause() {
        if((getLigado()) && (getTocando())){
            setTocando(false);
        }
        
    }
}
