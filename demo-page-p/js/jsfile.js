function checkme(message)
{
  x=document.getElementById('Home');
  x.style.display="none";
  x=document.getElementById('Experience');
  x.style.display="none";
  x=document.getElementById('SkillProject');
  x.style.display="none";
  x=document.getElementById('Contact');
  x.style.display="none";
  g=document.getElementById(message);
  unfade(g);
}





function unfade(element) {
    var op = 0.1;  // initial opacity
    element.style.display = 'block';
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.1;
    }, 10);
}
function fade(element) {
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 50);
}
