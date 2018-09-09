LED_OFF();

function LED_ON(number){
    console.log(number);
    let name = '/led'+number;
    console.log(name)
    let ros=new ROSLIB.Ros({url:'ws://'+location.hostname+':9090'});
    let led = new ROSLIB.Topic({
        ros:ros,
        name:name,
        messageType:'std_msgs/Int8'
    });
    let data = new ROSLIB.Message({data:1});
    led.publish(data);
}
function LED_OFF(){
    console.log("OFF");
    let name;
    let ros;
    let led;
    let data;
    for(let i=1; i < 5; i++){
        name = '/led'+ i ;
        console.log(name)
        ros=new ROSLIB.Ros({url:'ws://'+location.hostname+':9090'});
        led = new ROSLIB.Topic({
            ros:ros,
            name:name,
            messageType:'std_msgs/Int8'
        });
        data = new ROSLIB.Message({data:0});
        led.publish(data);
    }
}
