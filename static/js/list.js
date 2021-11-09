async function showValues(){
    const response = await fetch('http://192.168.0.23/list_api',{
        method: 'GET', //*GET,POST,PUT, DELETE,etc.
    })
    const myJson = await response.json();//extract JSON from the http response 
    console.log(myJson)
}

$("a").click ( showValues)