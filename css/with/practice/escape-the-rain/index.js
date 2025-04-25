// Game state
let gameState = {
    playing: false,
    score: 0,
    rainSpeed: 2,
    rainFrequency: 50, // Lower = more frequent
    raindrops: []
};

// Constants
const speed = 50;
const jumpHeight = 80;
const jumpDuration = 500;
const canvas = document.getElementById("canvas");
const scoreDisplay = document.getElementById("score");
const finalScoreDisplay = document.getElementById("final-score");
const startScreen = document.getElementById("start-screen");
const gameOverScreen = document.getElementById("game-over-screen");
const startButton = document.getElementById("start-button");
const restartButton = document.getElementById("restart-button");

// Character setup
const character = document.createElement("div");
character.className = "character";

// Character properties
let jumping = false;
let characterPosition = {
    left: 0,
    bottom: 0
};
let characterRect = { width: 48, height: 48 };

// Game loop variables
let gameLoop;
let scoreInterval;

// Initialize game
function initGame() {
    // Reset game state
    gameState = {
        playing: true,
        score: 0,
        rainSpeed: 2,
        rainFrequency: 50,
        raindrops: []
    };
    
    // Reset character
    characterPosition = { left: 0, bottom: 0 };
    jumping = false;
    
    // Clear existing raindrops
    document.querySelectorAll('.raindrop').forEach(drop => drop.remove());
    
    // Add character to the canvas
    character.style.left = '0px';
    character.style.bottom = '0px';
    character.className = "character";
    canvas.appendChild(character);
    
    // Update score display
    updateScore(0);
    
    // Start game loop
    gameLoop = setInterval(updateGame, 20);
    scoreInterval = setInterval(() => {
        if (gameState.playing) {
            updateScore(gameState.score + 1);
            
            // Increase difficulty as score increases
            if (gameState.score % 100 === 0) {
                gameState.rainFrequency = Math.max(10, gameState.rainFrequency - 5);
                gameState.rainSpeed += 0.2;
            }
        }
    }, 100);
}

// Update game state
function updateGame() {
    if (!gameState.playing) return;
    
    // Create new raindrops
    if (Math.random() * 100 < 100 / gameState.rainFrequency) {
        createRaindrop();
    }
    
    // Move existing raindrops
    moveRaindrops();
    
    // Check for collisions
    checkCollisions();
}

// Create raindrop
function createRaindrop() {
    const raindrop = document.createElement("div");
    raindrop.className = "raindrop";
    
    // Random position
    const leftPos = Math.random() * (canvas.offsetWidth - 8); // Updated width
    raindrop.style.left = leftPos + "px";
    raindrop.style.top = "-25px"; // Updated height
    
    // Random duration (speed)
    const duration = 2 + Math.random() * 2 - (gameState.rainSpeed * 0.3);
    raindrop.style.animationDuration = duration + "s";
    
    // Add to DOM and store in our array
    canvas.appendChild(raindrop);
    gameState.raindrops.push({
        element: raindrop,
        left: leftPos,
        top: -25,
        speed: gameState.rainSpeed + (Math.random() * 1)
    });
}

// Move raindrops
function moveRaindrops() {
    for (let i = gameState.raindrops.length - 1; i >= 0; i--) {
        const drop = gameState.raindrops[i];
        
        // Update position
        drop.top += drop.speed;
        drop.element.style.top = drop.top + "px";
        
        // Remove if off screen
        if (drop.top > canvas.offsetHeight) {
            drop.element.remove();
            gameState.raindrops.splice(i, 1);
        }
    }
}

// Check for collisions
function checkCollisions() {
    if (!gameState.playing) return;
    
    // Get character bounding rectangle directly from DOM
    const charRect = character.getBoundingClientRect();
    const canvasRect = canvas.getBoundingClientRect();
    
    // Adjust character rectangle relative to canvas
    const adjustedCharRect = {
        left: charRect.left - canvasRect.left,
        right: charRect.right - canvasRect.left,
        top: charRect.top - canvasRect.top,
        bottom: charRect.bottom - canvasRect.top,
        width: charRect.width,
        height: charRect.height
    };
    
    // Create a smaller hitbox for better gameplay feel (80% of character size)
    const hitboxPadding = {
        x: adjustedCharRect.width * 0.1,
        y: adjustedCharRect.height * 0.1
    };
    
    const charHitbox = {
        left: adjustedCharRect.left + hitboxPadding.x,
        right: adjustedCharRect.right - hitboxPadding.x,
        top: adjustedCharRect.top + hitboxPadding.y,
        bottom: adjustedCharRect.bottom - hitboxPadding.y
    };
    
    // Check each raindrop for collision
    for (const drop of gameState.raindrops) {
        // Get raindrop's DOM element rect for accurate collision
        const dropRect = drop.element.getBoundingClientRect();
        
        // Adjust raindrop rectangle relative to canvas
        const adjustedDropRect = {
            left: dropRect.left - canvasRect.left,
            right: dropRect.right - canvasRect.left,
            top: dropRect.top - canvasRect.top,
            bottom: dropRect.bottom - canvasRect.top
        };
        
        // Simple collision detection with more accurate rectangles
        if (charHitbox.left < adjustedDropRect.right && 
            charHitbox.right > adjustedDropRect.left && 
            charHitbox.top < adjustedDropRect.bottom && 
            charHitbox.bottom > adjustedDropRect.top) {
            gameOver();
            return;
        }
    }
}

// Game over
function gameOver() {
    gameState.playing = false;
    character.classList.add("dead");
    
    // Stop game loop
    clearInterval(gameLoop);
    clearInterval(scoreInterval);
    
    // Show game over screen
    finalScoreDisplay.textContent = gameState.score;
    gameOverScreen.style.display = "flex";
}

// Update score
function updateScore(newScore) {
    gameState.score = newScore;
    scoreDisplay.textContent = `Score: ${newScore}`;
}

// Character movement
function move(to) {
    if (!gameState.playing) return;
    
    // Reset classes but keep "character"
    character.className = "character moving";
    
    switch (to) {
        case 'jump':
            if (jumping) return;
            
            jumping = true;
            character.classList.add("top");
            
            // Jump animation using requestAnimationFrame for smoother motion
            const jumpStart = Date.now();
            const startBottom = characterPosition.bottom;
            
            function jumpAnimation() {
                if (!gameState.playing) {
                    jumping = false;
                    return;
                }
                
                const elapsed = Date.now() - jumpStart;
                const progress = Math.min(elapsed / jumpDuration, 1);
                
                // Parabolic jump curve - up and then down
                const jumpProgress = Math.sin(progress * Math.PI);
                characterPosition.bottom = startBottom + jumpProgress * jumpHeight;
                
                // Update character position
                character.style.bottom = characterPosition.bottom + 'px';
                
                if (progress < 1 && gameState.playing) {
                    requestAnimationFrame(jumpAnimation);
                } else {
                    // End of jump
                    jumping = false;
                    if (gameState.playing) {
                        character.classList.remove("top");
                    }
                }
            }
            
            requestAnimationFrame(jumpAnimation);
            break;
            
        case 'left':
            character.classList.add("left");
            characterPosition.left -= speed;
            break;
            
        case 'right':
            character.classList.add("right");
            characterPosition.left += speed;
            break;
            
        case 'down':
            character.classList.add("down");
            if (characterPosition.bottom > 0) {
                characterPosition.bottom -= speed;
            }
            break;
            
        default:
            break;
    }
    
    // Keep character within bounds
    characterPosition.left = Math.max(0, Math.min(canvas.clientWidth - characterRect.width, characterPosition.left));
    characterPosition.bottom = Math.max(0, characterPosition.bottom);
    
    // Update character position (except during jump animation)
    if (to !== 'jump') {
        character.style.left = characterPosition.left + 'px';
        character.style.bottom = characterPosition.bottom + 'px';
    } else {
        character.style.left = characterPosition.left + 'px';
    }
    
    // Remove animation classes after a delay (except during jump)
    if (to !== 'jump' && gameState.playing) {
        setTimeout(() => {
            if (gameState.playing) {
                character.className = "character";
            }
        }, 300);
    }
}

// Event listeners
document.addEventListener("keydown", (e) => {
    if (!gameState.playing) return;
    
    // left
    if (e.key === "ArrowLeft" || e.key === "a") {
        move('left');
    }

    // right
    if (e.key === "ArrowRight" || e.key === "d") {
        move('right');
    }

    // jump
    if (e.key === "ArrowUp" || e.key === "w" || e.key === " ") {
        move('jump');
    }

    // down
    if (e.key === "ArrowDown" || e.key === "s") {
        move('down');
    }
});

// Start button
startButton.addEventListener("click", () => {
    startScreen.style.display = "none";
    initGame();
});

// Restart button
restartButton.addEventListener("click", () => {
    gameOverScreen.style.display = "none";
    initGame();
});