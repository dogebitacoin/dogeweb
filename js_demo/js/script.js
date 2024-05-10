function askQuestion(){
    var q= prompt("wood chuck chuckin some wood but how much could it chuck?");
    if(q != null){
        document.getElementById('question').innerHTML ='yikes' + q + 'thats a lot of wood';
        
    }

}
function showImage(){
    var image=document.getElementById('suprise');
    image.src ="images/isochibi2.png";
}