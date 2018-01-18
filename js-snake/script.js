const fruitSize = 2;
const gridSize = 20;
const blockSize = 800/gridSize;
var canvas,ctx,snakeDir,snakeXs,snakeYs,currentFruitX,currentFruitY,fruitCooldown,timeOut,lose,snakeDelay,score;

window.onload = function() {
    canvas = document.getElementById("canvas");
    document.addEventListener("keypress",keyPressed,false);
    ctx = canvas.getContext("2d");
    ctx.textAlign = "right";
    ctx.font = "30px Arial";
    reset();
}

function reset() {
    lose = false;
    snakeDir = "RIGHT";
    snakeXs = [3,4,5];
    snakeYs = [3,3,3];
    currentFruitX = 5;
    currentFruitY = 5;
    fruitCooldown = 0;
    snakeDelay = 180;
    score = 0;
    timeOut = setTimeout(moveSnake,snakeDelay);
}

function moveSnake() {
    clearTimeout(timeOut);
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
        fruitCooldown = fruitSize;
        while(true) {
            var validSpot = true;
            currentFruitX = Math.floor(Math.random()*gridSize);
            currentFruitY = Math.floor(Math.random()*gridSize);
            for(var i = 0; i < snakeXs.length; i++) {
                if(snakeXs[i] == currentFruitX && snakeYs[i] == currentFruitY) {
                    validSpot = false;
                }
            } if (validSpot) {break;}
        }
        snakeDelay -= (snakeDelay/200)**4*20;
        score++;
    }
    if(fruitCooldown > 0) {
        fruitCooldown--;
        // todo: make sure fruit not on snake
    } else {
        snakeXs.splice(0,1);
        snakeYs.splice(0,1);
    }
    ctx.fillStyle = "white";
    ctx.fillRect(0,0,800,800);
    ctx.fillStyle = "red";
    for(var i = 0; i < snakeXs.length-1; i++) {
        ctx.fillRect(blockSize*snakeXs[i],blockSize*snakeYs[i],blockSize,blockSize);
    }
    ctx.fillStyle = "green";
    ctx.fillRect(currentFruitX*blockSize, currentFruitY*blockSize, blockSize, blockSize)
    ctx.fillStyle = "blue";
    ctx.fillRect(blockSize*nextX,blockSize*nextY,blockSize,blockSize);
    ctx.fillStyle = "black";
    ctx.fillText(score,790,30);
    for(var i = 0; i < snakeXs.length-3; i++) {
        if(snakeXs[i] == nextX && snakeYs[i] == nextY) {lose = true;}
    }
    if(lose) {
        return;
    }
    timeOut = setTimeout(moveSnake,snakeDelay);
}

function keyPressed(e) {
    if(e.key == "r") {
        reset();
    }
    if (!lose) {
        if(snakeDir == "RIGHT" || snakeDir == "LEFT") {
            if(e.key == 'w') {
                snakeDir = "UP";
            } else if(e.key == 's') {
                snakeDir = "DOWN";
            } else {return;}
        } else {
            if(e.key == 'a') {
                snakeDir = "LEFT";
            } else if(e.key == 'd') {
                snakeDir = "RIGHT";
            } else {return;}
        }
        moveSnake();
    }
}