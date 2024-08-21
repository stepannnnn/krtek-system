function clock() {
    let date = new Date();
    let day = date.getDate();
    let mounth = date.getMonth();
    let year = date.getFullYear()
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();

    hh = (hh<10)?"0"+hh:hh;
    mm = (mm<10)?"0"+mm:mm;
    ss = (ss<10)?"0"+ss:ss;

    let time = day + "." + mounth + "." + year + " - " + hh + ":" + mm + ":" + ss;
    document.getElementById('clock').innerText = time;
    var t = setTimeout(function(){ clock() }, 1000);
}

clock();