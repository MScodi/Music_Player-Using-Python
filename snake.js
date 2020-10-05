const cvs = document.getElementById("snake");
const ctx = cvs.getContext('2d');

// creating Unit
const box = 32;

// loading Images

const ground = new Image();
ground.src = "ground.png";
const foodImg = new Image();
foodImg.src = "food.png";

// Create the snake

let snake = [];
snake[0] = {
    x: 9 * box,
    y: 10 * box
}

// create Food
let food = {
        x: Math.floor(Math.random() * 17 + 1) * box,
        y: Math.floor(Math.random() * 15 + 3) * box
    }
    // Create Score Variable
let score = 0;
// control the snake
let d;
document.addEventListener("keydown", direction);

function direction(event) {
    if (event.keyCode == 37) {
        d = "LEFT";
    } else if (event.keyCode == 38) {
        d = "UP";
    } else if (event.keyCode == 39) {
        d = "RIGHT";
    } else if (event.keyCode == 40) {
        d = "DOWN";
    }
}

function draw() {
    ctx.drawImage(ground, 0, 0);
    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = (i == 0) ? "green" : "white";
        ctx.fillRect(snake[i].x, snake[i].y, box, box);

        ctx.strokeStyle = "red";
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);

    }
    ctx.drawImage(foodImg, food.x, food.y);
    // old head Position
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;
    // remobe the tail
    sanke.pop();
    // which Direction

    ctx.fillStyle = "White";
    ctx.font = "45px Changa one ";
    ctx.fillText(score, 2 * box, 1.6 * box);


}
// call draw Function every 100 ms
let game = setInterval(draw, 100);