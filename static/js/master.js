var theBeds = document.getElementById("operate-pad").children[1];
var how_many = 10;
var theBeds_value = new Array(how_many);
for(var i = 0;i < how_many;i++) {
  theBeds_value[i] = new Array(5);
}
var myDate = new Date();

function getTime() {
  myDate = new Date();
  var mytime=myDate.toTimeString().split(' ')[0];
  document.getElementById("clock").innerHTML=mytime;

  for(var i = 0;i < theBeds_value.length;i++) {
    var test = myDate - theBeds_value[i][1];
    if(test>0) {
      document.getElementById("bed"+(i+1).toString()).style.background='red';
    }
  }

}
setInterval("getTime()",1000);
