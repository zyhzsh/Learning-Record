function checkme(message)
{
  x=document.getElementById('Home');
  x.style.display="none";
  x=document.getElementById('Resume');
  x.style.display="none";
  x=document.getElementById('SkillProject');
  x.style.display="none";
  x=document.getElementById('Contact');
  x.style.display="none";
  g=document.getElementById(message);
  unfade(g);
  x=document.getElementById('Home');
    if(x.style.display=="none"){
      x=document.getElementsByTagName('body');
      x[0].style['align-items']="unset";
    }
    else {
      x=document.getElementsByTagName('body');
      x[0].style['align-items']="center";
    }
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
    }, 50);
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

var infoswitch=true;
function checkinfo (){
  switch(infoswitch){
    case true:showinfo();infoswitch=false;break;
    case false:eclipseinfo();infoswitch=true;break;
    default:break;
  }
}


function showinfo(){
  x=document.getElementById('info');
  unfade(x);
}

function eclipseinfo(){
  x=document.getElementById('info');
  fade(x);
}
