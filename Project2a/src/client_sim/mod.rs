use std::fs::File;
use std::io::prelude::*;

pub mod dag;


#[derive(Debug)]
pub struct ClientNode {
    price : f64,
    entry_time : usize,
    exit_time : usize,
    prior_clients : Vec<usize>,
    after_clients : Vec<usize>
}

impl Default for ClientNode {
    fn default() -> ClientNode {
        ClientNode {
            price : 0.0,
            entry_time : 0,
            exit_time : 0,
            prior_clients : Vec::new(),
            after_clients : Vec::new()
        }
    }
}

impl From<&str> for ClientNode {
    fn from(input : &str) -> ClientNode {
        let mut new_client = ClientNode::default();
        let mut split_str = input.split(' ');
        //assert_eq!(split_str.len(),3);
        new_client.entry_time = split_str.next().unwrap().parse::<usize>().unwrap();
        new_client.exit_time = split_str.next().unwrap().parse::<usize>().unwrap();
        new_client.price = split_str.next().unwrap().parse::<f64>().unwrap();
        new_client
    }
}
impl From<(usize,usize,f64)> for ClientNode {
    fn from((entry_time, exit_time, price) : (usize, usize, f64)) -> ClientNode{
        let mut new_client = ClientNode::default();
        new_client.price = price;
        new_client.entry_time = entry_time;
        new_client.exit_time = exit_time;
        new_client
    }
}

impl dag::Node for ClientNode {
    fn get_weight(&self) -> f64 {
        self.price
    }
    fn get_incoming(&self) -> &Vec<usize> {
        &self.prior_clients
    }
    fn get_outgoing(&self) -> &Vec<usize> {
        &self.after_clients
    }
}

pub fn client_dag_from_file(mut file : File) -> Result<dag::DAG<ClientNode>,std::io::Error> {
    //TODO : This assumes that lines are sorted by entry times. This is true for at least the example files
    let mut vertices : Vec<ClientNode> = Vec::new();
    let mut buf : String = String::new();
    match file.read_to_string(&mut buf){
        Ok(_) => {},
        Err(e) => {return Err(e)}
    }
    let mut lines = buf.split('\n');
    loop {
        let line = match lines.next() {
            Some(x) => {
                if x.len() < 3 {
                    break
                }else{
                    x
                }
            },
            None => {break}
        };
        vertices.push(ClientNode::from(line));
    }
    for vertex_idx in 0..vertices.len(){
        for comp_vertex_idx in (vertex_idx+1)..vertices.len(){
            if vertices[vertex_idx].entry_time < vertices[comp_vertex_idx].entry_time &&
                vertices[vertex_idx].exit_time <= vertices[comp_vertex_idx].entry_time {
                    vertices[vertex_idx].after_clients.push(comp_vertex_idx);
                    vertices[comp_vertex_idx].prior_clients.push(vertex_idx);
            } 
            else if vertices[comp_vertex_idx].entry_time < vertices[vertex_idx].entry_time &&
            vertices[comp_vertex_idx].exit_time <= vertices[vertex_idx].entry_time{
                vertices[vertex_idx].prior_clients.push(comp_vertex_idx);
                vertices[comp_vertex_idx].after_clients.push(vertex_idx);
            }
        }
    }

    Ok(dag::DAG::<ClientNode> {
        vertices : vertices
    })
}