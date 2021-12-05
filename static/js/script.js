document.getElementById("close").onclick = close;
document.getElementById("bout").onclick = show;

function close() {
  document.getElementById("home").style.display = 'none';
}


function show() {
    document.getElementById("home").style.display = 'block';
  }