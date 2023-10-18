public class DaemonThread extends Thread{
    public void run(){
        if(Thread.currentThread().isDaemon()){
            System.out.println(getName()+" is Daemon!");
        }
        else{
            System.out.println(getName()+" is not Daemon!");
        }
    }

    public static void main(String[] args) {
        DaemonThread d1 = new DaemonThread();
        DaemonThread d2 = new DaemonThread();
        DaemonThread d3 = new DaemonThread();

        d1.setName("D1");
        d2.setName("D2");
        d3.setName("D3");

        d1.setDaemon(true);
        d3.setDaemon(true);
        d1.start();
        d2.start();
        d3.start();
    }
}