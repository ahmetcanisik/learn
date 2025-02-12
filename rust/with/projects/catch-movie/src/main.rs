use clap::Parser;
use reqwest::Client;
use scraper::{Html, Selector};
use webbrowser;

/// Simple program to greet a person
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// Name of the person to greet
    #[arg()]
    url: String,

    #[arg(short, long, default_value_t = false)]
    view: bool,
}

async fn find_embed_url(url: &str) -> Result<Option<String>, reqwest::Error> {
    let client = Client::new();
    let res = client.get(url).send().await?.text().await?;

    let document = Html::parse_document(&res);

    // Define the CSS selector for iframe
    let iframe_selector = Selector::parse("iframe").unwrap();

    // Loop through each iframe element found
    for iframe in document.select(&iframe_selector) {
        // Return the first iframe's src attribute (if available)
        if let Some(src) = iframe.value().attr("data-src") {
            return Ok(Some(src.to_string())); // Return the src as an Option<String>
        }
    }

    // If no iframe is found, return None
    Ok(None)
}

#[tokio::main]
async fn main() {
    let args = Args::parse();
    if args.url.is_empty() { return; }
    let result = find_embed_url(&args.url).await;

    match result {
        Ok(Some(src)) => {
            if args.view {
                if webbrowser::open(&src).is_ok() {
                    println!("{}, opened in browser", src);
                }
            } else {
                println!("{}", src);
            }
        }, // Successfully found iframe src
        Ok(None) => println!("No iframe found on the page."),
        Err(e) => eprintln!("Error: {}", e), // Handle any errors
    }
}
