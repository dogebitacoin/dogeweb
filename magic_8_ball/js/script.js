//alert("javascript works");
function magic8ball(){
    askAQuestion();
    shake();
    getAFortune();
}

function askAQuestion(){
    alert("Ask a yes/no question and receive a fortune")
}
function shake(){
    alert("Im shaking")
}
function getAFortune(){
    //alert("ask again later")
    var fortunes = ['yes','no','maybe']
    var num = randomNumber(fortunes.length)
    displayFortune(fortunes[num])
}
function displayFortune(fortune){
    document
    .getElementById("fortune")
    .innerHTML = fortune
}
function randomNumber(n){
    return Math.floor(Math.random() * n)
}