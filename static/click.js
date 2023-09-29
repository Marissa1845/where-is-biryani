function printMousePos(event) {
    verifySuccess(event.clientX, event.clientY)
    console.log("clientX: " + event.clientX +
    " - clientY: " + event.clientY)
  }
function verifySuccess(x, y) {
    if((level==1)&&(x>=700 && x<=900) && (y>=600 && y<=700)){
        b = new Date()
        timeTaken1 = b.getTime()-a.getTime()
        console.log(timeTaken1)
        level=2;
        transGScore1();
        
    }else if((level==2)&&(x>=1040 && x<=1100) && (y>=500 && y<=650)){
        c = new Date()
        timeTaken2 = c.getTime()-a.getTime()
        level=3;
        transGScore2();

    }else if((level==3)&&(x>=440 && x<=620) && (y>=60 && y<=200)){
        d = new Date()
        timeTaken3 = d.getTime() - a.getTime()
        level=4
        transGScore3();

    }else if((level==4)&&(x>=1080 && x<=1150) && (y>=135 && y<=235)){
        e = new Date();
        timeTaken4 = e.getTime() - a.getTime()
        dispSuccess();
        sendData(PlayerName, timeTaken1, timeTaken2, timeTaken3, timeTaken4);
    }
}
level=1
function sendData(PlayerName, timeTaken1, timeTaken2, timeTaken3, timeTaken4) {
    fetch("/score", {
  method: "POST",
  body: JSON.stringify({
    time: timeTaken1+timeTaken2+timeTaken3+timeTaken4,
    username: PlayerName
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});

}
document.addEventListener("click", printMousePos);
biryani = document.getElementById('imgstart')
biryani.addEventListener('click', transGStart)

function transGStart(){
  startPage = document.getElementById('startPage')
  startPage.remove()
  takingNamejs=document.getElementById('takingName')
  takingNamejs.style.display='flex';
  nameInput = document.getElementById('name')
  nameInput.addEventListener('keydown', transGStart2)
}

function transGStart2(data){
  if (data.key == 'Enter'){
    PlayerName = nameInput.value;
    takingName.remove();
    gameWindow = document.getElementById('game');
    gameWindow.style.display="block";
    a = new Date()
    printMousePos();
  }
}

function transGScore1(){
  gameWindow = document.getElementById('game');
  gameWindow.remove()
  scoreWindow1 = document.getElementById('success1');
  scoreWindow1.style.display="block";
  timeText = document.getElementById('usertime1');
  timeText.textContent = 'You took '+ timeTaken1/1000 + ' seconds'
  herel2 = document.addEventListener('click', transGStart3)
}

function transGStart3(data){
    scoreWindow1.remove()
    gameWindow2 = document.getElementById('game2');
    gameWindow2.style.display="block";
    a = new Date()
    printMousePos();
}

function transGScore2(){
  gameWindow2 = document.getElementById('game2');
  gameWindow2.remove()
  scoreWindow2 = document.getElementById('success2');
  scoreWindow2.style.display="block";
  timeText = document.getElementById('usertime2');
  timeText.textContent = 'You took '+ timeTaken2/1000 + ' seconds'
  herel3 = document.addEventListener('click', transGStart4)
}

function transGStart4(data){
  scoreWindow2.remove()
  gameWindow3 = document.getElementById('game3');
  gameWindow3.style.display="block";
  a = new Date()
  printMousePos();
}

function transGScore3(){
  gameWindow3 = document.getElementById('game3');
  gameWindow3.remove()
  scoreWindow3 = document.getElementById('success3');
  scoreWindow3.style.display="block";
  timeText = document.getElementById('usertime3');
  timeText.textContent = 'You took '+ timeTaken3/1000 + ' seconds'
  herel4 = document.addEventListener('click', transGStart5)
}

function transGStart5(data){
  scoreWindow3.remove()
  gameWindow4 = document.getElementById('game4');
  gameWindow4.style.display="block";
  a = new Date();
  printMousePos();
}

function dispSuccess(){
  gameWindow = document.getElementById('game4');
  gameWindow.remove()
  success = document.getElementById('success')
  success.style.display='block'
  timeText = document.getElementById('usertime4');
  timeText.innerHTML = 'You took '+ timeTaken4/1000 +' seconds <br><br> Your total time is ' +  (timeTaken1 + timeTaken2 + timeTaken3 + timeTaken4)/1000 + ' seconds!' 
  snark = document.getElementById('watch')
  snark.addEventListener ('click',comping)
}

function comping(){
  success = document.getElementById('success')
  success.remove()
  progressing=document.getElementById('progressing')
  progressing.style.display='block'
  setTimeout(()=>{
  progressing.remove()
  comp = document.getElementById('comp')
  comp.style.display='flex';
  here1 = document.getElementById('here1')
  here1.addEventListener ('click',lbpage)
  }, 4000)
}

function lbpage(){
  comp = document.getElementById('comp')
  comp.remove();
  lb = document.getElementById('lb')
  lb.style.display='block'
  retrieve_csv()
}

function retrieve_csv(){
  fetch('/static/sortedleaderboard.csv')
  .then(function(response){
      return response.text();
  })
  .then(function(data){
      var table_container = document.getElementById('table-container');
      csv_string_to_table(data, table_container);
  });
}

function csv_string_to_table(csv_string, element_to_insert_table) {
  var rows = csv_string.trim().split(/\r?\n|\r/); // Regex to split/separate the CSV rows
  var table = '';
  var table_rows = '';
  var table_header = '';

  rows.forEach(function(row, row_index) {
      var table_columns = '';
      var columns = row.split(','); // split/separate the columns in a row
      columns.forEach(function(column, column_index) {
          table_columns += row_index == 0 ? '<th>' + column + '</th>' : '<td>' + column + '</td>';
      });
      if (row_index == 0) {
          table_header += '<tr>' + table_columns + '</tr>';
      } else {
          table_rows += '<tr>' + table_columns + '</tr>';
      }
  });

  table += '<table>';
      table += '<thead>';
          table += table_header;
      table += '</thead>';
      table += '<tbody>';
          table += table_rows;
      table += '</tbody>';
  table += '</table>';

  element_to_insert_table.innerHTML += table;
}

