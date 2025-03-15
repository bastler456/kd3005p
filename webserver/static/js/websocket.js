const socket = io();
socket.connect('http://127.0.0.1:8000');


socket.on("message", function(msg){
    console.log(msg)
    let data = JSON.parse(msg)
})
