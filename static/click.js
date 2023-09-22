function printMousePos(event) {
    document.getElementById("test").textContent =
      "clientX: " + event.clientX +
      " - clientY: " + event.clientY;
  }
  
  document.addEventListener("click", printMousePos);

  