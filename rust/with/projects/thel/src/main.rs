use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "cli-tool")]
#[command(author = "Sizin Adınız")]
#[command(version = "1.0")]
#[command(about = "Basit bir CLI aracı", long_about = None)]
struct Cli {
    /// İsteğe bağlı bir flag
    #[arg(short, long)]
    verbose: bool,

    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Merhaba komutu
    Hello {
        /// Selamlanacak kişinin adı
        #[arg(short, long)]
        name: String,
    },
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Hello { name } => {
            println!("Merhaba {}!", name);
            if cli.verbose {
                println!("Verbose mod aktif!");
            }
        }
    }
}
