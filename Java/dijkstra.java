import java.io.*;
import java.util.*;

public class Main {

  static class Edge {

    int src; // One of the nodes
    int nbr; // The second node forming the edge
    int wt; // Weight of the edge

    Edge(int src, int nbr, int wt) {
      this.src = src;
      this.nbr = nbr;
      this.wt = wt;
    }
  }

  static class Pair implements Comparable<Pair> {

    int vtx; // The vertex
    String psf; // The path from source node
    int wsf; // THe weight of the path
    
    Pair(int vtx, String psf, int wsf) {
      this.vtx = vtx;
      this.psf = psf;
      this.wsf = wsf;
    }
    
    // To compare two paths/routes, just compare their weights
    public int compareTo(Pair o) {
      return this.wsf - o.wsf;
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    // Read the number of vertices.
    int vtces = Integer.parseInt(br.readLine());
    ArrayList<Edge>[] graph = new ArrayList[vtces + 1];
      
    for (int i = 0; i < vtces + 1; i++) {
      graph[i] = new ArrayList<>();
    }
    
    // Read the number of edges edges
    int edges = Integer.parseInt(br.readLine());
      
    // Read the details of each of the edge.
    for (int i = 0; i < edges; i++) {
      String[] parts = br.readLine().split(" ");
      int v1 = Integer.parseInt(parts[0]);
      int v2 = Integer.parseInt(parts[1]);
      int wt = Integer.parseInt(parts[2]);
      graph[v1].add(new Edge(v1, v2, wt));
      graph[v2].add(new Edge(v2, v1, wt));
    }
    
    // Input the source vertex
    int src = Integer.parseInt(br.readLine());
    boolean[] visited = new boolean[vtces + 1];
      
    // Priority Queue to hold the pairs.
    PriorityQueue<Pair> pq = new PriorityQueue<>();
    pq.add(new Pair(src, src + "", 0));
      
    // Iterate till the priority queue is not empty
    while (pq.size() > 0) {
        
      // Remove the top vertex or the lowest path end point
      Pair rem = pq.remove();
      if (visited[rem.vtx] == true) {
        continue;
      }
        
      // If the vertex is not visited, mark it visited as 
      // the shortest path to the vertex is found.
      visited[rem.vtx] = true;
      System.out.println(rem.vtx + " via " + rem.psf + " @ " + rem.wsf);

      // For each adjacent node of the vertex,
      // Relax the distance to the adjacent edge
      for (Edge e : graph[rem.vtx]) {
        if (visited[e.nbr] == false) {
          pq.add(new Pair(e.nbr, rem.psf + "->" + e.nbr, rem.wsf + e.wt));
        }
      }
    }
  }
}
