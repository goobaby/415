mod client_sim;
use std::fs::File;
use std::io::prelude::*;
use std::io::{stdin,stdout};

fn trim_newline(s: &mut String) {
    if s.ends_with('\n') {
        s.pop();
        if s.ends_with('\r') {
            s.pop();
        }
    }
}
fn main() {
    print!("Enter the file to read data: ");
    stdout().flush().unwrap(); 
    let mut filename = String::new();
    stdin().read_line(&mut filename).unwrap();
    println!("");
    trim_newline(&mut filename);
    let mut file = File::open(&mut filename);
    
    while file.is_err() {
        println!("File {0} not found!\nEnter the file to read data: ",filename);
        
        stdin().read_line(&mut filename).unwrap();
        file = File::open(&mut filename);
    }
    let mut out_filename = &mut "out".to_owned();
    out_filename.push_str(&mut filename);
    let mut out_file = File::create(&mut out_filename).unwrap();
    let sim = client_sim::client_dag_from_file(file.unwrap()).unwrap();
    let mut output = String::new();
    output.push_str(&format!("There are {0} clients in this file\n\n", sim.vertices.len()));
    let (rev, path) = sim.find_biggest_path();
    let mut path_string = String::new();
    let last_idx = *path.last().unwrap();
    for index in path {
        path_string.push_str(&(index+1).to_string());
        if index != last_idx {
            path_string.push_str(", ");
        }
        
    }
    output.push_str(&format!("Optimal revenue earned is {0}\n",rev));
    output.push_str(&format!("Clients contributing to this optimal revenue: {0}", path_string));
    out_file.write_all(output.as_bytes()).expect("Unable to write to output file.");
    println!("{0}",output);
    //let sim: client_sim::dag::DAG<client_sim::ClientNode> = 
}