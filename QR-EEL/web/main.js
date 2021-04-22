// JAVA SCRIPT
function onClickedCreateQRC() {

  var qrd = document.getElementById("qrd").value
  eel.generate_qr(qrd)
}
function loadQRC(){
  var image= document.getElementById("pic");
  image.src=`qr.png#${new Date().getTime()}`;
}