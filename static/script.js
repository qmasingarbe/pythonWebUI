// page code
button = document.getElementById('button');
button.onclick = function(){
    sendData({
        'function_name': 'testFunc',
        'kwargs': {'arg1': 'puppy', 'arg2': 'booh'},
        'return_function' : 'populateText'
    })
};
function populateText(text){
    document.getElementById("testField").value = text['arg1'];
}
