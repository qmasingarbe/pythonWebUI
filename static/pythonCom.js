// send data
function sendData(data){
    // encode js object to json
    jsonData = JSON.stringify(data)
    // create request
    var url = "";
    var xhr = new XMLHttpRequest();
    // handle response
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200 && 'return_function' in data) {
            var json = JSON.parse(xhr.responseText);
            func = eval(data['return_function']);
            func(json)
        }
    }
    // send request
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(jsonData);
};
// close page
function sendClose(){
    var xhr = new XMLHttpRequest();
    var url = "/quit";
    xhr.open("GET", url, true);
    xhr.send();
};
window.onbeforeunload = function(){
    sendClose();
    return "Stop";
};
window.onunload = function(){
    sendClose();
    return "Stop";
};