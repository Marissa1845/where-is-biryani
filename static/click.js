a = new Date()
function printMousePos(event) {
    verifySuccess(event.clientX, event.clientY)
    document.getElementById("test").textContent =
      "clientX: " + event.clientX +
      " - clientY: " + event.clientY;
  }
function verifySuccess(x, y) {
    if((x>=500 && x<=600) && (y>=500 && y<=600)){
        b = new Date()
        timeTaken = b.getTime()-a.getTime()
        document.body.textContent=timeTaken;
        sendData(timeTaken);
    }
}

function sendData(data) {
  name = prompt ("Enter Name: ")
    fetch("/score", {
  method: "POST",
  body: JSON.stringify({
    time: data,
    username: name
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});

}
document.addEventListener("click", printMousePos);


