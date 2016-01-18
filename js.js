
var responseBody = "\"[{\"system_resources\": {\"vcpu\": {\"available\": 100, \"total\": 100}, \"ram\": {\"available\": 512, \"total\": 512}, \"disk\": {\"available\": 10240, \"total\": 10240}}, \"user_instances\": [{\"233141231\": {\"external_ip\": \"\", \"ip\": \"192.0.0.1\", \"state\": \"live\"}}, {\"333141231\": {\"external_ip\": \"\", \"ip\": \"192.0.0.2\", \"state\": \"live\"}}, {\"45141231\": {\"external_ip\": \"\", \"ip\": \"192.0.0.3\", \"state\": \"live\"}}], \"system_services\": {\"Administration Service\": \"live\", \"Network Service\": \"live\", \"Compute Service\": \"live\", \"Storage Service\": \"live\"}, \"timestamp\": \"2015-12-01 10:10:10\", \"internet\": 1}]\""
responseBody = responseBody.toString()
//
//responseBody = JSON.parse(responseBody, function(key, value){
//    if (key == 'date') return new Date(value);
//    return value;
//});
var data = JSON.parse(responseBody);
console.log(data)


console.log( ">>>>>>>>>>>>>>>>")
//
//
//alert( schedule.events[1].date.getDate() ); // сработает!