var stats = document.getElementsByClassName('status');

for(var i=0;i < stats.length;i++){
    var orderStatus = stats[i].innerText
    if(orderStatus == "Status: Ready"){
        stats[i].parentElement.parentElement.style.backgroundColor = "#00BCD4"
    }
    else if(orderStatus == "Status: Processing"){
        stats[i].parentElement.parentElement.style.backgroundColor = '#FFEB3B'
    }
    else if(orderStatus == "Status: Delivered"){
        stats[i].parentElement.parentElement.style.backgroundColor = '#4CAF50'
    }
}