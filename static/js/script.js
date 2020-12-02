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
        'task': task_id,
        'element': element_id,
    }
    
    $.ajax({
        url: window.location.href + "/move",
        type: 'POST',
        data: JSON.stringify(data),
    })
    .done(function(result){
        console.log(result)
    })
}