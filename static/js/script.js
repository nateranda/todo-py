var id;

function allowDrop(event){
    event.preventDefault();
}

function dragStart(event){
    id = event.target.id;
}

function dragEnd(event){
    event.target.append(document.getElementById(id))
}