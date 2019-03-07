function main() {
  promptUser(showText);
}

function promptUser(showText) {
  var t = prompt("Provide time in seconds.", "0");
  showText(t);
}

function showText(t) {
  var mil = t * 1000;
  var text = document.createTextNode("TEXTBOOK");
  var Div = document.getElementById("textbook");
  window.setTimeout(function () { Div.appendChild(text); }, mil);
}
