#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")] // hide console window on Windows in release

use eframe::{egui, epi};
mod client_sim;

struct MyApp {
    filename: String,
    sim: client_sim::dag::DAG<client_sim::ClientNode>,
    last_path : Option<Vec<usize>>,
    last_rev : Option<f64>,
    debug_infos : Vec<bool>
}

impl Default for MyApp {
    fn default() -> Self {
        Self {
            filename: "data1.txt".to_owned(),
            sim: client_sim::dag::DAG::<client_sim::ClientNode>
            {
                vertices : Vec::new()
            },
            last_path : Option::default(),
            last_rev : Option::default(),
            debug_infos : vec![false;1]

        }
    }
}

impl epi::App for MyApp {
    fn name(&self) -> &str {
        "Project 2a -- Luke & Amit"
    }

    fn update(&mut self, ctx: &egui::Context, frame: &epi::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Project 2a -- Luke & Amit");
            ui.horizontal(|ui| {
                ui.label("Enter the file to read data: ");
                ui.text_edit_singleline(&mut self.filename);
            });
            if ui.button("Open File").clicked() {
                
                match std::fs::File::open(&mut self.filename) {
                    Ok(x) => {
                        self.sim = client_sim::client_dag_from_file(x).unwrap();
                        let (rev, path) = self.sim.find_biggest_path();
                        self.last_path = Option::from(path);
                        self.last_rev = Option::from(rev);
                    }
                    Err(x) if x.kind() == std::io::ErrorKind::NotFound => {
                        ui.label("File not found!");
                    }
                    Err(x) => {
                        panic!("{:?},{:?}",x,x.kind())
                    }
                }
            }
            match &self.last_path {
                Some(x) =>{
                    ui.label(format!("There are {} clients in this file",self.sim.vertices.len()) );
                    ui.label(format!("Optimal revenue earned is {}",self.last_rev.unwrap()) );
                    ui.label(format!("Clients contributing to this optimal revenue: {:?}",x));
                    ui.checkbox(&mut self.debug_infos[0],"show debug info -- vertices");
                    if self.debug_infos[0] {
                        for vertex_idx in 0..self.sim.vertices.len(){
                            ui.label(format!("{:} : {:?}",vertex_idx, self.sim.vertices[vertex_idx]));
                        }
                    }
                }
                None => {
                    ui.label("Waiting to read file...");
                }
            }
        });

        // Resize the native window to be just the size we need it to be:
        frame.set_window_size(ctx.used_size());
    }
}

fn main() {
    let options = eframe::NativeOptions::default();
    eframe::run_native(Box::new(MyApp::default()), options);
}