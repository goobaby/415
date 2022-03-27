
pub trait Node {
    fn get_outgoing(&self) -> &Vec<usize>;
    fn get_incoming(&self) -> &Vec<usize>;
    fn get_weight(&self) -> f64;
}

pub struct DAG<T> where T : Node{
    pub vertices : Vec<T>
}
impl<T> DAG<T> where T : Node{
    fn is_cyclic(&self) -> bool{
        //ref_count == amount of nodes incoming to node at idx
        //cur_roots == list of nodes that currently have no incoming nodes (where ref_count == 0)
        let mut ref_count = vec![0; self.vertices.len()];
        let mut cur_roots = Vec::<usize>::new();
        for node_idx in 0..self.vertices.len() { //Just initializing ref_count here
            ref_count[node_idx] = self.vertices[node_idx].get_incoming().len();
            if ref_count[node_idx] == 0 {
                cur_roots.push(node_idx);
            }
        }

        //acyclic_nodes == # of nodes that are confirmed to be acyclic
        let mut acyclic_nodes = 0;
        loop {
            //If there are no more roots, then stop. Otherwise, take one to 'eliminate' from the graph
            let root_idx = match cur_roots.pop(){
                Some(x) => x,
                None => {break}
            };
            //Given that we are eliminating a root, we've guaranteed an acyclic node
            acyclic_nodes += 1;

            //For all of the children of this node,
            let children = self.vertices[root_idx].get_outgoing();
            for child_idx_ref in children {
                let child_idx = *child_idx_ref;
                //Remove one incoming node
                ref_count[child_idx] -= 1;
                //And if they don't have any incoming nodes anymore,
                if ref_count[child_idx] == 0 {
                    //Add them to the roots!
                    cur_roots.push(child_idx);
                }
            }
        }
        //Finally, we just see if every node ended up being acyclic, or if there was an impenetrable cycle in there
        acyclic_nodes == self.vertices.len()
    }

    pub fn find_biggest_path(&self) -> (f64,Vec<usize>){
        let mut cur_leaves = Vec::<usize>::new();
        let mut ref_count = vec![0; self.vertices.len()];
        //Maximum value for node at idx
        let mut node_max = vec![0.0;self.vertices.len()];
        //Maximum child for node at idx
        let mut node_max_kid = vec![self.vertices.len()+1;self.vertices.len()];
        
        for node_idx in 0..self.vertices.len() { //Just initializing ref_count here
            ref_count[node_idx] = self.vertices[node_idx].get_outgoing().len();
            if ref_count[node_idx] == 0 {
                cur_leaves.push(node_idx);
                node_max[node_idx] = self.vertices[node_idx].get_weight();
            }
        }

        loop {
            let leaf_idx = match cur_leaves.pop(){
                Some(x) => x,
                None => {break}
            };
            let leaf_ref = &self.vertices[leaf_idx];
            let leaf_value = node_max[leaf_idx];
            for parent_idx_ref in leaf_ref.get_incoming() {
                let parent_idx = *parent_idx_ref;
                ref_count[parent_idx] -= 1;
                //If this is the final leaf connected to the parent node, that parent node is now functionally a leaf!
                if ref_count[parent_idx] == 0 {
                    cur_leaves.push(parent_idx);
                }
                //If the path offered by this leaf is better than what's currently written down, write this instead!
                if leaf_value + self.vertices[parent_idx].get_weight() > node_max[parent_idx]{
                    node_max[parent_idx] = leaf_value + self.vertices[parent_idx].get_weight();
                    node_max_kid[parent_idx] = leaf_idx;
                }
            }
        }
        let mut max_idx = 0;
        let mut max_value = 0.0;
        for node_idx in 0..self.vertices.len() {
            if node_max[node_idx] > max_value {
                max_value = node_max[node_idx];
                max_idx = node_idx;
            }
        }
        let mut path = vec![max_idx;1];
        while node_max_kid[max_idx] != self.vertices.len() + 1 { //While the next node in the path has a child
            max_idx = node_max_kid[max_idx];
            path.push(max_idx);
        }
        (max_value,path)
    }
    fn get_roots(&self) -> Vec<usize> {
        let mut roots = vec![0;0];
        for node_idx in 0..self.vertices.len() {
            let node = &self.vertices[node_idx];
            if node.get_incoming().len() == 0 {
                roots.push(node_idx);
            }
        }
        roots
    }
    fn get_leaves(&self) -> Vec<usize> {
        let mut leaves = vec![0;0];
        for node_idx in 0..self.vertices.len() {
            let node = &self.vertices[node_idx];
            if node.get_outgoing().len() == 0 {
                leaves.push(node_idx);
            }
        }
        leaves
    }
}
