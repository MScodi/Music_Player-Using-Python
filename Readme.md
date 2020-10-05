We are going to create a Snake Game Using Javascript and Html5 Canvas
The player controls a dot, square, or object on a bordered plane. As it moves forward, it leaves a trail behind, resembling a moving snake. In some games, the end of the trail is in a fixed position, so the snake continually gets longer as it moves. In another common scheme, the snake has a specific length, so there is a moving tail a fixed number of units away from the head. The player loses when the snake runs into the screen border, a trail or other obstacle, or itself
            
# javascript            
 Selecting canvas
const cvs= document.getElementById('canvas');
Gives method to o various functions
const ctx=cvs.getContext('2d'); ---> Methods   Properies

Loading Image
let imageName =new Image()
.src=then soure
imageName= new Audio()
.src=then soure 
$ to play Audio--->audio.play()
# To Draw Images
ctx.drawImage(imageName, X,Y,Width,Height);
# To Draw Rectangle
ctx.fillstyle="Colour";
ctx.fillRect=(X,Y,Width,Height);

# Unit
  let box=32
  @ a single entity in our game for which we take it as reference 
# Snake %% ground $$ food %%% source
let snake=[]
snake[0]={x: 9*box, y:10*box}
snake[1]
     function.draw(){
         ctx.drawing(ground,0,0);
         for(let i=0; i<snake.length; i++){
            ctx.fillstyle=(i==0)?"green":"white";
            [[[[]]]]
         }
     }
    let game=setInterval(draw,100)