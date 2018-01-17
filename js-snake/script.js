
const snakeDelay = 100;
const gridSize = 20;
const blockSize = 800/gridSize;
var canvas,ctx,snakeDir,snakeXs,snakeYs,currentFruitX,currentFruitY;

window.onload = function() {
    canvas = document.getElementById("canvas");
    canvas.addEventListener("keypress",keyPressed,false);
    ctx = canvas.getContext("2d");
    snakeDir = "RIGHT";
    snakeXs = [3,4,5];
    snakeYs = [3,3,3];
    currentFruitX = 5;
    currentFruitY = 5;
    setTimeout(moveSnake,snakeDelay);
}

function moveSnake() {
    clearTimeout();
    var nextX,nextY;
    var lastX = snakeXs[snakeXs.length-1];
    var lastY = snakeYs[snakeYs.length-1];
    if(snakeDir == "RIGHT") {
        nextX = lastX+1;
        nextY = lastY;
        if (nextX == gridSize) {nextX = 0;}
    } else if (snakeDir == "LEFT") {
        nextX = lastX-1;
        nextY = lastY;
        if (nextX == -1) {nextX = gridSize-1;}
    } else if (snakeDir == "UP") {
        nextY = lastY-1;
        nextX = lastX;
        if (nextY == -1) {nextY = gridSize-1;}
    } else if (snakeDir == "DOWN") {
        nextX = lastX;
        nextY = lastY+1;
        if (nextY == gridSize) {nextY = 0;}
    }
    snakeXs.push(nextX);
    snakeYs.push(nextY);
    if(nextX == currentFruitX && nextY == currentFruitY) {
        currentFruitX = Math.floor(Math.random()*gridSize);
        currentFruitY = Math.floor(Math.random()*gridSize);
        // todo: make sure fruit not on snake
    } else {
        snakeXs.splice(0,1);
        snakeYs.splice(0,1);
    }
    ctx.fillStyle = "white";
    ctx.fillRect(0,0,800,800);
    ctx.fillStyle = "red";
    for(var i = 0; i < snakeXs.length; i++) {
        ctx.fillRect(blockSize*snakeXs[i],blockSize*snakeYs[i],blockSize,blockSize);
    }
    setTimeout(moveSnake,snakeDelay);
}

function keyPressed() {
    //set dir, check if dir is possible, run moveSnake
}