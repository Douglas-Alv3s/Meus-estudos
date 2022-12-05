package CLIENTES;

public class VisualizadorCLiente {

    public static void main(String[] args) {
        
        Cliente[] c = new Cliente[3];

        for (int i=0; i<c.length; i++){
            int codigo = (int) (1 + Math.random() * 1000-1);
            c[i] = new Cliente("Douglas", codigo, 500);
        }

        for (int i=0; i<c.length; i++){
            System.out.println(c[i].imprimir());
        }
    }

    
}
