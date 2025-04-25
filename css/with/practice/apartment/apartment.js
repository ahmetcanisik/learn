const windows = document.getElementById("windows");
const door = document.getElementById("door");

// Create door panels
for (let i = 0; i < 3; i++) {
    const panel = document.createElement("div");
    panel.className = "door-panel";
    door.appendChild(panel);
}

// Create windows
for (let i = 0; i < 6; i++) {    
    const window = document.createElement("div");
    window.className = "window";
    
    // Create 4 panes for each window
    for (let j = 0; j < 4; j++) {
        const pane = document.createElement("div");
        pane.className = "pane";
        window.appendChild(pane);
    }
    
    // Create window sill
    const sill = document.createElement("div");
    sill.className = "sill";
    window.appendChild(sill);
    
    windows.appendChild(window);
}