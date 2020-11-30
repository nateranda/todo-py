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
    console.log(task_id);
    console.log(element_id);
}