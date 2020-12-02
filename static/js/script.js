var task_id;
var element_id;

function dragOver(event){
    event.preventDefault()
    element_id = event.target.id;
}

function dragStart(event){
    task_id = event.target.id;
}

function dragEnd(event){
    var data = {
        task: task_id,
        element: element_id,
    };
    
    fetch(`${window.location.href}/move`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        }),
    })
    .then(function(){
        window.location = window.location.href
    })
}