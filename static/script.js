window.onload=initall;
var saveAnsButton;
function initall(){
    saveAnsButton  = document.getElementById('save_ans');
    console.log(saveAnsButton)
    if (saveAnsButton) {
        saveAnsButton.onclick = saveans;
    } else {
        console.log("Element with ID 'save_as' not found.");
    }
}
function saveans(){
    var ans = $("input:radio[name=name]:checked").val();
    alert("answer is submited")

    var req = new XMLHttpRequest();

    var url = '/saveans?ans='+ans
    req.open("GET",url,true)
    req.send()
}
