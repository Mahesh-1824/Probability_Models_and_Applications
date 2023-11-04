#include <iostream>
#include <vector>
#include <queue>
#include <bits/stdc++.h>

using namespace std;

queue<pair<int,int>> path;

int bfs(int source, int sink, vector<int>& parent, vector<vector<int>>& residualGraph)
{
    fill(parent.begin(), parent.end(), -1);
    int V = residualGraph.size();
    parent[source] = -2;
    queue<pair<int, int>> q;
    q.push({source, INT_MAX});

    while (!q.empty())
    {
        int u = q.front().first;
        int capacity = q.front().second;
        path.push(q.front());
        q.pop();

        for (int av=0; av < V; av++)
        {
            if (u != av && parent[av] == -1 && residualGraph[u][av] != 0)
            {
                parent[av] = u;
                int min_cap = min(capacity, residualGraph[u][av]);
                if (av == sink)
                {
                    return min_cap;
                }
                q.push({av, min_cap});
            }
        }
    }
    return 0;
}

void printPair(pair<int, int> p)
{
    // Gives first element from queue pair
    int f = p.first;
 
    // Gives second element from queue pair
    int s = p.second;
 
    cout << "(" << f << ", " << s << ") ";
}

int ford_fulkerson(vector<vector<int>>& graph, int source, int sink)
{
    vector<int> parent(graph.size(), -1);
    vector<vector<int>> residualGraph = graph;
    int min_cap = 0, max_flow = 0;
    while (min_cap = bfs(source, sink, parent, residualGraph))
    {
        
        // while (!path.empty())
        // {
        //     printPair(path.front());
        //     path.pop();
        // }

        max_flow += min_cap;
        int u = sink;
        while (u != source) {
            int v = parent[u];
            residualGraph[u][v] += min_cap;
            residualGraph[v][u] -= min_cap;
            u = v;
            // cout<<residualGraph[u][v]<<"\n";
        }
        cout << "\n" << max_flow << "\n\n";
        // cout<<residualGraph[u][v]<<"\n";

        cout << "Residual Graph : " << endl;

        for( int i=0; i<10; i++ )
        {
            for( int j=0; j<10; j++ )
            {
                cout << residualGraph[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    return max_flow;
}

void addEdge(vector<vector<int>>& graph,int u, int v, int w)
{
    graph[u][v] = w;
}

int main()
{
    int V = 10;
    vector<vector<int>> graph(V, vector<int> (V, 0));
    
    addEdge(graph,1, 3, 3);
    addEdge(graph,1, 7, 26);
    addEdge(graph,3, 8, 18);
    addEdge(graph,3, 5, 18);
    addEdge(graph,3, 10, 30);
    addEdge(graph,3, 6, 7);
    addEdge(graph,2, 8, 7);
    addEdge(graph,2 ,4, 5);
    addEdge(graph,2, 7, 27);
    addEdge(graph,2, 6, 4);
    addEdge(graph,5, 1, 28);
    addEdge(graph,5, 8, 16);
    addEdge(graph,5, 2, 20);
    addEdge(graph,5, 10, 28);
    addEdge(graph,5, 7, 7);
    addEdge(graph,4 ,8, 27);
    addEdge(graph,4, 6, 23);
    addEdge(graph,7, 3, 1);
    addEdge(graph,6 ,1, 16);
    addEdge(graph,8, 1, 17);
    addEdge(graph,8, 10,3);
    addEdge(graph,8, 7, 20);
    addEdge(graph,8, 6, 7);
    addEdge(graph,9, 2, 2);
    addEdge(graph,9, 7, 14);
    addEdge(graph,9, 6, 8);
    cout << "Maximum Flow: " << ford_fulkerson(graph, 0, 9) << endl;
    return 0;
}